# This training script is a duplicate of the Training.ipynb notebook but can be invoked from the terminal

import os
print(os.getcwd())
os.environ["PATH"]="/usr/local/cuda-11.7/bin:"+os.getenv("PATH")

os.system('pip uninstall -y torch')
os.system('pip uninstall -y einops')
os.system('pip uninstall -y transformers')
os.system('pip uninstall -y sentence_transformers')
os.system('pip uninstall -y datasets')
os.system('pip uninstall -y sagemaker')
os.system('pip uninstall -y smart_open')
os.system('pip uninstall -y pynvml')

os.system('pip install -r lodestone-reqs.txt')

os.system('pip install -e ./sentence-transformers')

os.system('pip uninstall -y triton')
os.system('pip install --no-deps triton==2.0.0.dev20221202')

#####

from pynvml import *
import math
from sentence_transformers import models, losses
from sentence_transformers import LoggingHandler, SentenceTransformer, util, InputExample
import logging
import os
import json
import torch
import boto3
from smart_open import open
import random
import time
import gc

os.environ["PATH"]="/usr/local/cuda-11.7/bin:"+os.getenv("PATH")
os.environ["TOKENIZERS_PARALLELISM"] = "false"

#####


def print_gpu_utilization():
    "This helper function outputs the current GPU memory usage."
    nvmlInit()
    handle = nvmlDeviceGetHandleByIndex(0)
    info = nvmlDeviceGetMemoryInfo(handle)
    return f"GPU memory occupied: {info.used/1024**3} GB."

#####


class MultiDatasetDataLoader:
    """
    This custom dataloader class consumes a list of datasets and a batch size and produces batches randomly sampled 
    from the datasets provided where each batch consists of records from a single dataset and datasets are chosen 
    for batches in proportion to their total number of records.
    """
    def __init__(self, datasets, batch_size_pairs, batch_size_triplets=None, dataset_size_temp=-1, allow_swap=True):
        self.allow_swap = allow_swap
        self.batch_size_pairs = batch_size_pairs
        self.batch_size_triplets = batch_size_pairs if batch_size_triplets is None else batch_size_triplets

        # Compute dataset weights
        self.dataset_lengths = list(map(len, datasets))
        self.dataset_lengths_sum = sum(self.dataset_lengths)

        weights = []
        # if dataset_size_temp > 0:  # Scale probability with dataset size
        #     for dataset in datasets:
        #         prob = len(dataset) / self.dataset_lengths_sum
        #         weights.append(max(1, int(math.pow(prob, 1 / dataset_size_temp) * 1000)))
        # else:  # Equal weighting of all datasets
        #     weights = [100] * len(datasets)
        for dataset in datasets:
            weights.append(len(dataset))

        # logging.info("Dataset lengths and weights: {}".format(list(zip(self.dataset_lengths, weights))))

        self.dataset_idx = []
        self.dataset_idx_pointer = 0

        for idx, weight in enumerate(weights):
            self.dataset_idx.extend([idx] * weight)
        random.shuffle(self.dataset_idx)

        self.datasets = []
        for dataset in datasets:
            random.shuffle(dataset)
            self.datasets.append({
                'elements': dataset,
                'pointer': 0,
            })

    def __iter__(self):
        for _ in range(int(self.__len__())):
            # Select dataset
            if self.dataset_idx_pointer >= len(self.dataset_idx):
                self.dataset_idx_pointer = 0
                random.shuffle(self.dataset_idx)

            dataset_idx = self.dataset_idx[self.dataset_idx_pointer]
            self.dataset_idx_pointer += 1

            # Select batch from this dataset
            dataset = self.datasets[dataset_idx]
            batch_size = self.batch_size_pairs if len(dataset['elements'][0].texts) == 2 else self.batch_size_triplets

            batch = []
            texts_in_batch = set()
            guid_in_batch = set()
            while len(batch) < batch_size:
                example = dataset['elements'][dataset['pointer']]

                valid_example = True
                # First check if one of the texts in already in the batch
                for text in example.texts:
                    text_norm = text.strip().lower()
                    if text_norm in texts_in_batch:
                        valid_example = False

                    texts_in_batch.add(text_norm)

                # If the example has a label, check if label is in batch
                if example.guid is not None:
                    valid_example = valid_example and example.guid not in guid_in_batch
                    guid_in_batch.add(example.guid)

                if valid_example:
                    if self.allow_swap and random.random() > 0.5:
                        example.texts[0], example.texts[1] = example.texts[1], example.texts[0]

                    batch.append(example)

                dataset['pointer'] += 1
                if dataset['pointer'] >= len(dataset['elements']):
                    dataset['pointer'] = 0
                    random.shuffle(dataset['elements'])

            yield self.collate_fn(batch) if self.collate_fn is not None else batch

    def __len__(self):
        return int(self.dataset_lengths_sum / self.batch_size_pairs)

#####


# These four classes of custom generators parse the raw data from the files in S3 and format it into InputExamples which can be properly interpreted by a SentenceTransformer model.

class RedditTitleBodyDataset:
    def __init__(self, source_uri, max_seq_length):
        self.source_uri = source_uri
        self.s3_client = boto3.client("s3")
        self.max_seq_length = max_seq_length

    def __iter__(self):
        while True:
            for json_line in open(self.source_uri, transport_params={"client": self.s3_client}):
                data_line = json.loads(json_line.strip())

                if "title" in data_line and "body" in data_line:
                    data = {'guid': None, 'texts': [" ".join(data_line['title'].split(" ")[:self.max_seq_length]), " ".join(data_line['body'].split(" ")[:self.max_seq_length])]}
                    record = InputExample(guid=data.get('guid', None), texts=data['texts'])

                    yield record


class RedditYearDataset:
    def __init__(self, source_uri, max_seq_length):
        self.source_uri = source_uri
        self.s3_client = boto3.client("s3")
        self.max_seq_length = max_seq_length

    def __iter__(self):
        while True:
            for json_line in open(self.source_uri, transport_params={"client": self.s3_client}):
                data_line = json.loads(json_line.strip())

                if "response" in data_line and "context" in data_line:
                    data = {'guid': None, 'texts': [" ".join(data_line['response'].split(" ")[:self.max_seq_length]), " ".join(data_line['context'].split(" ")[:self.max_seq_length])]}
                    record = InputExample(guid=data.get('guid', None), texts=data['texts'])

                    yield record


class HuggingFaceQueryPosDataset:
    def __init__(self, source_uri, max_seq_length):
        self.source_uri = source_uri
        self.s3_client = boto3.client("s3")
        self.max_seq_length = max_seq_length

    def __iter__(self):
        while True:
            for json_line in open(self.source_uri, transport_params={"client": self.s3_client}):
                data_line = json.loads(json_line.strip())

                if "query" in data_line and "pos" in data_line:
                    for i in range(len(data_line['pos'])):
                        data = {'guid': None, 'texts': [" ".join(data_line['query'].split(" ")[:self.max_seq_length]), " ".join(data_line['pos'][i].split(" ")[:self.max_seq_length])]}
                        record = InputExample(guid=data.get('guid', None), texts=data['texts'])

                        yield record


class Dataset:
    def __init__(self, source_uri, max_seq_length):
        self.source_uri = source_uri
        self.s3_client = boto3.client("s3")
        self.max_seq_length = max_seq_length

    def __iter__(self):
        while True:
            for json_line in open(self.source_uri, transport_params={"client": self.s3_client}):
                data_line = json.loads(json_line.strip())

                if not isinstance(data_line, dict):
                    data = {'guid': None, 'texts': data_line}
                    for text_idx in range(len(data['texts'])):
                        data['texts'][text_idx] = " ".join(data['texts'][text_idx].split(" ")[:self.max_seq_length])
                    record = InputExample(guid=data.get('guid', None), texts=data['texts'])
                else:
                    for text_idx in range(len(data_line['texts'])):
                        data_line['texts'][text_idx] = " ".join(data_line['texts'][text_idx].split(" ")[:self.max_seq_length])
                    record = InputExample(guid=data_line.get('guid', None), texts=data_line['texts'])

                yield record

#####


def build_generators(data_records, max_seq_length=512, testing=False):
    """
    This function consumes the data_records dictionary and creates a new dictionary of data generators where each entry is 
    of the form {filename: data generator object}.
    """
    if testing:
        # filepaths = [file for file in list(data_records.keys()) if file.startswith('S2ORC') or file.startswith('reddit_')]
        filepaths = [file for file in list(data_records.keys())][:3]
    else:
        filepaths = list(data_records.keys())
    generators = {}
    for filepath in filepaths:
        filepath = filepath.strip()
        source_uri = 's3://lodestone-rnd/data/'+filepath
        if filepath in ['S2ORC_citations_abstracts.json.gz', 'amazon-qa.json.gz'] or 'reddit' in filepath:
            if "title" in filepath:
                generators[f'{filepath.split(".")[0]}'] = iter(RedditTitleBodyDataset(source_uri, max_seq_length))
            elif "reddit" in filepath:
                generators[f'{filepath.split(".")[0]}'] = iter(RedditYearDataset(source_uri, max_seq_length))
            else:
                generators[f'{filepath.split(".")[0]}'] = iter(HuggingFaceQueryPosDataset(source_uri, max_seq_length))
        else:
            generators[f'{filepath.split(".")[0]}'] = iter(Dataset(source_uri, max_seq_length))

    return generators

#####


def produce_data(data_records, num_chunks, generators, batch_size, failed_on=None, first_iter=False, testing=False, temp=-1):
    """
    This function consumes the data_records dictionary, the number of chunks to break the datasets into, the dictionary of 
    data generators, and a batch size and returns a MultiDatasetDataloader which can be fed into the .fit method of a 
    SentenceTransformer model.
    """
    if testing:
        # filepaths = [file for file in list(data_records.keys()) if file.startswith('S2ORC') or file.startswith('reddit_')]
        filepaths = [file for file in list(data_records.keys())][:3]
    else:
        filepaths = list(data_records.keys())
    datasets = []
    for file_idx, filepath in enumerate(filepaths):
        filepath = filepath.strip()
        dataset = []

        if failed_on is not None and failed_on != 1 and first_iter:
            for k in range((failed_on-1)*max(1, data_records[filepath]//num_chunks)):
                next(generators[f'{filepath.split(".")[0]}'])
            for m in range(max(1, data_records[filepath]//num_chunks)):
                dataset.append(next(generators[f'{filepath.split(".")[0]}']))
        else:
            for n in range(max(1, data_records[filepath]//num_chunks)):
                dataset.append(next(generators[f'{filepath.split(".")[0]}']))

        datasets.append(dataset)
        logging.info("{}. {}: {}".format(file_idx+1, filepath, len(dataset)))

    dataset_lengths_sum = sum(list(map(len, datasets)))

    batch_size_pairs = batch_size_triplets = batch_size
    # Special data loader to load from multiple datasets
    train_dataloader = MultiDatasetDataLoader(datasets=datasets,
                                              batch_size_pairs=batch_size_pairs,
                                              batch_size_triplets=batch_size_triplets,
                                              dataset_size_temp=temp)

    return train_dataloader, dataset_lengths_sum

#####


def construct_model(model_name, max_seq_length=512):
    """
    This function constructs a SentenceTransformer model from a HuggingFace transformer model name 
    or from a local path to a transformer model repository.
    """
    word_embedding_model = models.Transformer(model_name_or_path=model_name,
                                              max_seq_length=max_seq_length,
                                              tokenizer_name_or_path='bert-base-uncased',
                                              trust_remote_code=True,
                                              model_args={'torch_dtype': torch.bfloat16})
    pooling_model = models.Pooling(word_embedding_model.get_word_embedding_dimension())
    norm = models.Normalize()
    model = SentenceTransformer(modules=[word_embedding_model, pooling_model, norm], device='cuda')
    model[0].tokenizer.model_max_length = max_seq_length

    return model

#####


# Just some code to print debug information to stdout
logging.basicConfig(format='%(asctime)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.INFO,
                    handlers=[LoggingHandler()])
# /print debug information to stdout

#####


# Set Hyperparameters
model_name = 'mosaic-bert-base-seqlen-2048'
# model_name = 'hum-lodestone-v1'
batch_size = 16
batch_size_pairs = batch_size_triplets = batch_size
max_seq_length = 2048
use_amp = False

num_cycles = 2
num_chunks = 50
num_epochs = 2
steps_per_epoch = 10000
# Total training steps = num_cycles * num_chunks * num_epochs * steps_per_epoch = 2 * 50 * 2 * 10,000 = 2,000,000 steps
warmup_steps = 500

testing = False
temp = -1

#####


output_path = 'hum-lodestone-v1'
logging.info("Output: "+output_path)

# Instantiate SentenceTransformer Model
model = construct_model(model_name=model_name, max_seq_length=max_seq_length)

# Load File Names and Record Volumes
with open('data_records.json') as fIn:
    data_records = json.load(fIn)

total_pairs = sum(data_records.values())

logging.info("Total Training Pairs: {}".format(total_pairs))

# Initialize Data Generators
generators = build_generators(data_records=data_records,
                              max_seq_length=max_seq_length,
                              testing=testing)

logging.info("Data Generators Initialized")

# Define Training Loss Function
train_loss = losses.MultipleNegativesRankingLoss(model,
                                                 scale=20,
                                                 similarity_fct=util.dot_score)

logging.info(print_gpu_utilization())

#####


# Configure Training Cycles
failed_on = None  # chunk that the process failed on
random.seed(42)
steps = 0
first_iter = True
for cycle_num in range(num_cycles):
    logging.info("Starting Cycle {}".format(cycle_num+1))
    for chunk_num in range(num_chunks):
        if failed_on is not None and (chunk_num+1) < failed_on and (cycle_num+1) == 1:
            pass
        else:
            logging.info("Chunk {}/{}".format(chunk_num+1, num_chunks))
            logging.info("Loading {} Datasets".format(len([file for file in list(data_records.keys()) if file.startswith('S2ORC') or file.startswith('reddit_')]) if testing else len(data_records)))
            # t_dataload0 = time.time()
            # Create the training dataloader for the given chunk of data
            train_dataloader, dataset_lengths_sum = produce_data(data_records,
                                                                 num_chunks,
                                                                 generators,
                                                                 batch_size,
                                                                 failed_on=failed_on,
                                                                 first_iter=first_iter,
                                                                 testing=testing,
                                                                 temp=temp)
            first_iter = False
            # t_dataload1 = time.time()
            # print(t_dataload1-t_dataload0)

            logging.info(print_gpu_utilization())

            # steps_per_epoch = dataset_lengths_sum // batch_size_pairs

            for epoch_num in range(num_epochs):
                logging.info("Performing Cycle {}, Chunk {}, Epoch {}".format(cycle_num+1, chunk_num+1, epoch_num+1))
                try:
                    # t_fit0 = time.time()
                    # Train the model
                    model.fit(train_objectives=[(train_dataloader, train_loss)],
                              evaluator=None,
                              epochs=1,
                              warmup_steps=warmup_steps,
                              steps_per_epoch=steps_per_epoch,
                              use_amp=use_amp,
                              output_path=output_path)
                    # t_fit1 = time.time()
                    # print(t_fit1-t_fit0)

                    steps += steps_per_epoch

                    logging.info(print_gpu_utilization())
                    logging.info("Succeeded on Cycle {}, Chunk {}, Epoch {}".format(cycle_num+1, chunk_num+1, epoch_num+1))
                    logging.info("{} Steps Completed in Total".format(steps))

                    with open('train_logs.txt', 'a') as log:
                        log.write("Succeeded on Cycle {}, Chunk {}, Epoch {}: {} Steps Completed in Total\n".format(cycle_num+1, chunk_num+1, epoch_num+1, steps))

                except:
                    logging.info("Failed on Cycle {}, Chunk {}, Epoch {}".format(cycle_num+1, chunk_num+1, epoch_num+1))

                    with open('train_logs.txt', 'a') as log:
                        log.write("Failed on Cycle {}, Chunk {}, Epoch {}: {} Steps Completed in Total\n".format(cycle_num+1, chunk_num+1, epoch_num+1, steps))

                finally:
                    warmup_steps = 0

            # Clear GPU/CUDA memory cache between data chunks
            train_dataloader = None
            model = None
            train_loss = None

            gc.collect()
            torch.cuda.empty_cache()

            # Reload the model and reinitialize the loss function
            model = construct_model(model_name='hum-lodestone-v1', max_seq_length=max_seq_length)

            train_loss = losses.MultipleNegativesRankingLoss(model,
                                                             scale=20,
                                                             similarity_fct=util.dot_score)

            logging.info(print_gpu_utilization())