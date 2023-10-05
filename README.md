---
license: apache-2.0
pipeline_tag: sentence-similarity
inference: false
tags:
- sentence-transformers
- feature-extraction
- sentence-similarity
- mteb
language: en
datasets:
- s2orc
- flax-sentence-embeddings/stackexchange_title_body_jsonl
- flax-sentence-embeddings/stackexchange_titlebody_best_voted_answer_jsonl
- flax-sentence-embeddings/stackexchange_title_best_voted_answer_jsonl
- flax-sentence-embeddings/stackexchange_titlebody_best_and_down_voted_answer_jsonl
- sentence-transformers/reddit-title-body
- msmarco
- gooaq
- yahoo_answers_topics
- code_search_net
- search_qa
- eli5
- snli
- multi_nli
- wikihow
- natural_questions
- trivia_qa
- embedding-data/sentence-compression
- embedding-data/flickr30k-captions
- embedding-data/altlex
- embedding-data/simple-wiki
- embedding-data/QQP
- embedding-data/SPECTER
- embedding-data/PAQ_pairs
- embedding-data/WikiAnswers
- sentence-transformers/embedding-training-data
model-index:
- name: lodestone-base-4096-v1
  results:
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_counterfactual
      name: MTEB AmazonCounterfactualClassification (en)
      config: en
      split: test
      revision: e8379541af4e31359cca9fbcf4b00f2671dba205
    metrics:
    - type: accuracy
      value: 69.7313432835821
    - type: ap
      value: 31.618259511417733
    - type: f1
      value: 63.30313825394228
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_polarity
      name: MTEB AmazonPolarityClassification
      config: default
      split: test
      revision: e2d317d38cd51312af73b3d32a06d1a08b442046
    metrics:
    - type: accuracy
      value: 86.89837499999999
    - type: ap
      value: 82.39500885672128
    - type: f1
      value: 86.87317947399657
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_reviews_multi
      name: MTEB AmazonReviewsClassification (en)
      config: en
      split: test
      revision: 1399c76144fd37290681b995c656ef9b2e06e26d
    metrics:
    - type: accuracy
      value: 44.05
    - type: f1
      value: 42.67624383248947
  - task:
      type: Retrieval
    dataset:
      type: arguana
      name: MTEB ArguAna
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 26.173999999999996
    - type: map_at_10
      value: 40.976
    - type: map_at_100
      value: 42.067
    - type: map_at_1000
      value: 42.075
    - type: map_at_3
      value: 35.917
    - type: map_at_5
      value: 38.656
    - type: mrr_at_1
      value: 26.814
    - type: mrr_at_10
      value: 41.252
    - type: mrr_at_100
      value: 42.337
    - type: mrr_at_1000
      value: 42.345
    - type: mrr_at_3
      value: 36.226
    - type: mrr_at_5
      value: 38.914
    - type: ndcg_at_1
      value: 26.173999999999996
    - type: ndcg_at_10
      value: 49.819
    - type: ndcg_at_100
      value: 54.403999999999996
    - type: ndcg_at_1000
      value: 54.59
    - type: ndcg_at_3
      value: 39.231
    - type: ndcg_at_5
      value: 44.189
    - type: precision_at_1
      value: 26.173999999999996
    - type: precision_at_10
      value: 7.838000000000001
    - type: precision_at_100
      value: 0.9820000000000001
    - type: precision_at_1000
      value: 0.1
    - type: precision_at_3
      value: 16.287
    - type: precision_at_5
      value: 12.191
    - type: recall_at_1
      value: 26.173999999999996
    - type: recall_at_10
      value: 78.378
    - type: recall_at_100
      value: 98.222
    - type: recall_at_1000
      value: 99.644
    - type: recall_at_3
      value: 48.862
    - type: recall_at_5
      value: 60.953
  - task:
      type: Clustering
    dataset:
      type: mteb/arxiv-clustering-p2p
      name: MTEB ArxivClusteringP2P
      config: default
      split: test
      revision: a122ad7f3f0291bf49cc6f4d32aa80929df69d5d
    metrics:
    - type: v_measure
      value: 42.31689035788179
  - task:
      type: Clustering
    dataset:
      type: mteb/arxiv-clustering-s2s
      name: MTEB ArxivClusteringS2S
      config: default
      split: test
      revision: f910caf1a6075f7329cdf8c1a6135696f37dbd53
    metrics:
    - type: v_measure
      value: 31.280245136660984
  - task:
      type: Reranking
    dataset:
      type: mteb/askubuntudupquestions-reranking
      name: MTEB AskUbuntuDupQuestions
      config: default
      split: test
      revision: 2000358ca161889fa9c082cb41daa8dcfb161a54
    metrics:
    - type: map
      value: 58.79109720839415
    - type: mrr
      value: 71.79615705931495
  - task:
      type: STS
    dataset:
      type: mteb/biosses-sts
      name: MTEB BIOSSES
      config: default
      split: test
      revision: d3fb88f8f02e40887cd149695127462bbcf29b4a
    metrics:
    - type: cos_sim_pearson
      value: 76.44918756608115
    - type: cos_sim_spearman
      value: 70.86607256286257
    - type: euclidean_pearson
      value: 74.12154678100815
    - type: euclidean_spearman
      value: 70.86607256286257
    - type: manhattan_pearson
      value: 74.0078626964417
    - type: manhattan_spearman
      value: 70.68353828321327
  - task:
      type: Classification
    dataset:
      type: mteb/banking77
      name: MTEB Banking77Classification
      config: default
      split: test
      revision: 0fd18e25b25c072e09e0d92ab615fda904d66300
    metrics:
    - type: accuracy
      value: 75.40584415584415
    - type: f1
      value: 74.29514617572676
  - task:
      type: Clustering
    dataset:
      type: mteb/biorxiv-clustering-p2p
      name: MTEB BiorxivClusteringP2P
      config: default
      split: test
      revision: 65b79d1d13f80053f67aca9498d9402c2d9f1f40
    metrics:
    - type: v_measure
      value: 37.41860080664014
  - task:
      type: Clustering
    dataset:
      type: mteb/biorxiv-clustering-s2s
      name: MTEB BiorxivClusteringS2S
      config: default
      split: test
      revision: 258694dd0231531bc1fd9de6ceb52a0853c6d908
    metrics:
    - type: v_measure
      value: 29.319217023090705
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackAndroidRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 26.595000000000002
    - type: map_at_10
      value: 36.556
    - type: map_at_100
      value: 37.984
    - type: map_at_1000
      value: 38.134
    - type: map_at_3
      value: 33.417
    - type: map_at_5
      value: 35.160000000000004
    - type: mrr_at_1
      value: 32.761
    - type: mrr_at_10
      value: 41.799
    - type: mrr_at_100
      value: 42.526
    - type: mrr_at_1000
      value: 42.582
    - type: mrr_at_3
      value: 39.39
    - type: mrr_at_5
      value: 40.727000000000004
    - type: ndcg_at_1
      value: 32.761
    - type: ndcg_at_10
      value: 42.549
    - type: ndcg_at_100
      value: 47.915
    - type: ndcg_at_1000
      value: 50.475
    - type: ndcg_at_3
      value: 37.93
    - type: ndcg_at_5
      value: 39.939
    - type: precision_at_1
      value: 32.761
    - type: precision_at_10
      value: 8.312
    - type: precision_at_100
      value: 1.403
    - type: precision_at_1000
      value: 0.197
    - type: precision_at_3
      value: 18.741
    - type: precision_at_5
      value: 13.447999999999999
    - type: recall_at_1
      value: 26.595000000000002
    - type: recall_at_10
      value: 54.332
    - type: recall_at_100
      value: 76.936
    - type: recall_at_1000
      value: 93.914
    - type: recall_at_3
      value: 40.666000000000004
    - type: recall_at_5
      value: 46.513
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackEnglishRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 22.528000000000002
    - type: map_at_10
      value: 30.751
    - type: map_at_100
      value: 31.855
    - type: map_at_1000
      value: 31.972
    - type: map_at_3
      value: 28.465
    - type: map_at_5
      value: 29.738
    - type: mrr_at_1
      value: 28.662
    - type: mrr_at_10
      value: 35.912
    - type: mrr_at_100
      value: 36.726
    - type: mrr_at_1000
      value: 36.777
    - type: mrr_at_3
      value: 34.013
    - type: mrr_at_5
      value: 35.156
    - type: ndcg_at_1
      value: 28.662
    - type: ndcg_at_10
      value: 35.452
    - type: ndcg_at_100
      value: 40.1
    - type: ndcg_at_1000
      value: 42.323
    - type: ndcg_at_3
      value: 32.112
    - type: ndcg_at_5
      value: 33.638
    - type: precision_at_1
      value: 28.662
    - type: precision_at_10
      value: 6.688
    - type: precision_at_100
      value: 1.13
    - type: precision_at_1000
      value: 0.16
    - type: precision_at_3
      value: 15.562999999999999
    - type: precision_at_5
      value: 11.019
    - type: recall_at_1
      value: 22.528000000000002
    - type: recall_at_10
      value: 43.748
    - type: recall_at_100
      value: 64.235
    - type: recall_at_1000
      value: 78.609
    - type: recall_at_3
      value: 33.937
    - type: recall_at_5
      value: 38.234
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackGamingRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 33.117999999999995
    - type: map_at_10
      value: 44.339
    - type: map_at_100
      value: 45.367000000000004
    - type: map_at_1000
      value: 45.437
    - type: map_at_3
      value: 41.195
    - type: map_at_5
      value: 42.922
    - type: mrr_at_1
      value: 38.37
    - type: mrr_at_10
      value: 47.786
    - type: mrr_at_100
      value: 48.522
    - type: mrr_at_1000
      value: 48.567
    - type: mrr_at_3
      value: 45.371
    - type: mrr_at_5
      value: 46.857
    - type: ndcg_at_1
      value: 38.37
    - type: ndcg_at_10
      value: 50.019999999999996
    - type: ndcg_at_100
      value: 54.36299999999999
    - type: ndcg_at_1000
      value: 55.897
    - type: ndcg_at_3
      value: 44.733000000000004
    - type: ndcg_at_5
      value: 47.292
    - type: precision_at_1
      value: 38.37
    - type: precision_at_10
      value: 8.288
    - type: precision_at_100
      value: 1.139
    - type: precision_at_1000
      value: 0.132
    - type: precision_at_3
      value: 20.293
    - type: precision_at_5
      value: 14.107
    - type: recall_at_1
      value: 33.117999999999995
    - type: recall_at_10
      value: 63.451
    - type: recall_at_100
      value: 82.767
    - type: recall_at_1000
      value: 93.786
    - type: recall_at_3
      value: 48.964999999999996
    - type: recall_at_5
      value: 55.358
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackGisRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 16.028000000000002
    - type: map_at_10
      value: 23.186999999999998
    - type: map_at_100
      value: 24.236
    - type: map_at_1000
      value: 24.337
    - type: map_at_3
      value: 20.816000000000003
    - type: map_at_5
      value: 22.311
    - type: mrr_at_1
      value: 17.514
    - type: mrr_at_10
      value: 24.84
    - type: mrr_at_100
      value: 25.838
    - type: mrr_at_1000
      value: 25.924999999999997
    - type: mrr_at_3
      value: 22.542
    - type: mrr_at_5
      value: 24.04
    - type: ndcg_at_1
      value: 17.514
    - type: ndcg_at_10
      value: 27.391
    - type: ndcg_at_100
      value: 32.684999999999995
    - type: ndcg_at_1000
      value: 35.367
    - type: ndcg_at_3
      value: 22.820999999999998
    - type: ndcg_at_5
      value: 25.380999999999997
    - type: precision_at_1
      value: 17.514
    - type: precision_at_10
      value: 4.463
    - type: precision_at_100
      value: 0.745
    - type: precision_at_1000
      value: 0.101
    - type: precision_at_3
      value: 10.019
    - type: precision_at_5
      value: 7.457999999999999
    - type: recall_at_1
      value: 16.028000000000002
    - type: recall_at_10
      value: 38.81
    - type: recall_at_100
      value: 63.295
    - type: recall_at_1000
      value: 83.762
    - type: recall_at_3
      value: 26.604
    - type: recall_at_5
      value: 32.727000000000004
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackMathematicaRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 11.962
    - type: map_at_10
      value: 17.218
    - type: map_at_100
      value: 18.321
    - type: map_at_1000
      value: 18.455
    - type: map_at_3
      value: 15.287999999999998
    - type: map_at_5
      value: 16.417
    - type: mrr_at_1
      value: 14.677000000000001
    - type: mrr_at_10
      value: 20.381
    - type: mrr_at_100
      value: 21.471999999999998
    - type: mrr_at_1000
      value: 21.566
    - type: mrr_at_3
      value: 18.448999999999998
    - type: mrr_at_5
      value: 19.587
    - type: ndcg_at_1
      value: 14.677000000000001
    - type: ndcg_at_10
      value: 20.86
    - type: ndcg_at_100
      value: 26.519
    - type: ndcg_at_1000
      value: 30.020000000000003
    - type: ndcg_at_3
      value: 17.208000000000002
    - type: ndcg_at_5
      value: 19.037000000000003
    - type: precision_at_1
      value: 14.677000000000001
    - type: precision_at_10
      value: 3.856
    - type: precision_at_100
      value: 0.7889999999999999
    - type: precision_at_1000
      value: 0.124
    - type: precision_at_3
      value: 8.043
    - type: precision_at_5
      value: 6.069999999999999
    - type: recall_at_1
      value: 11.962
    - type: recall_at_10
      value: 28.994999999999997
    - type: recall_at_100
      value: 54.071999999999996
    - type: recall_at_1000
      value: 79.309
    - type: recall_at_3
      value: 19.134999999999998
    - type: recall_at_5
      value: 23.727999999999998
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackPhysicsRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 22.764
    - type: map_at_10
      value: 31.744
    - type: map_at_100
      value: 33.037
    - type: map_at_1000
      value: 33.156
    - type: map_at_3
      value: 29.015
    - type: map_at_5
      value: 30.434
    - type: mrr_at_1
      value: 28.296
    - type: mrr_at_10
      value: 37.03
    - type: mrr_at_100
      value: 37.902
    - type: mrr_at_1000
      value: 37.966
    - type: mrr_at_3
      value: 34.568
    - type: mrr_at_5
      value: 35.786
    - type: ndcg_at_1
      value: 28.296
    - type: ndcg_at_10
      value: 37.289
    - type: ndcg_at_100
      value: 42.787
    - type: ndcg_at_1000
      value: 45.382
    - type: ndcg_at_3
      value: 32.598
    - type: ndcg_at_5
      value: 34.521
    - type: precision_at_1
      value: 28.296
    - type: precision_at_10
      value: 6.901
    - type: precision_at_100
      value: 1.135
    - type: precision_at_1000
      value: 0.152
    - type: precision_at_3
      value: 15.367
    - type: precision_at_5
      value: 11.03
    - type: recall_at_1
      value: 22.764
    - type: recall_at_10
      value: 48.807
    - type: recall_at_100
      value: 71.859
    - type: recall_at_1000
      value: 89.606
    - type: recall_at_3
      value: 35.594
    - type: recall_at_5
      value: 40.541
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackProgrammersRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 19.742
    - type: map_at_10
      value: 27.741
    - type: map_at_100
      value: 29.323
    - type: map_at_1000
      value: 29.438
    - type: map_at_3
      value: 25.217
    - type: map_at_5
      value: 26.583000000000002
    - type: mrr_at_1
      value: 24.657999999999998
    - type: mrr_at_10
      value: 32.407000000000004
    - type: mrr_at_100
      value: 33.631
    - type: mrr_at_1000
      value: 33.686
    - type: mrr_at_3
      value: 30.194
    - type: mrr_at_5
      value: 31.444
    - type: ndcg_at_1
      value: 24.657999999999998
    - type: ndcg_at_10
      value: 32.614
    - type: ndcg_at_100
      value: 39.61
    - type: ndcg_at_1000
      value: 42.114000000000004
    - type: ndcg_at_3
      value: 28.516000000000002
    - type: ndcg_at_5
      value: 30.274
    - type: precision_at_1
      value: 24.657999999999998
    - type: precision_at_10
      value: 6.176
    - type: precision_at_100
      value: 1.1400000000000001
    - type: precision_at_1000
      value: 0.155
    - type: precision_at_3
      value: 13.927
    - type: precision_at_5
      value: 9.954
    - type: recall_at_1
      value: 19.742
    - type: recall_at_10
      value: 42.427
    - type: recall_at_100
      value: 72.687
    - type: recall_at_1000
      value: 89.89
    - type: recall_at_3
      value: 30.781
    - type: recall_at_5
      value: 35.606
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 19.72608333333333
    - type: map_at_10
      value: 27.165333333333336
    - type: map_at_100
      value: 28.292499999999997
    - type: map_at_1000
      value: 28.416333333333327
    - type: map_at_3
      value: 24.783833333333334
    - type: map_at_5
      value: 26.101750000000003
    - type: mrr_at_1
      value: 23.721500000000002
    - type: mrr_at_10
      value: 30.853333333333328
    - type: mrr_at_100
      value: 31.741750000000003
    - type: mrr_at_1000
      value: 31.812999999999995
    - type: mrr_at_3
      value: 28.732249999999997
    - type: mrr_at_5
      value: 29.945166666666665
    - type: ndcg_at_1
      value: 23.721500000000002
    - type: ndcg_at_10
      value: 31.74883333333333
    - type: ndcg_at_100
      value: 36.883583333333334
    - type: ndcg_at_1000
      value: 39.6145
    - type: ndcg_at_3
      value: 27.639583333333334
    - type: ndcg_at_5
      value: 29.543666666666667
    - type: precision_at_1
      value: 23.721500000000002
    - type: precision_at_10
      value: 5.709083333333333
    - type: precision_at_100
      value: 0.9859166666666666
    - type: precision_at_1000
      value: 0.1413333333333333
    - type: precision_at_3
      value: 12.85683333333333
    - type: precision_at_5
      value: 9.258166666666668
    - type: recall_at_1
      value: 19.72608333333333
    - type: recall_at_10
      value: 41.73583333333334
    - type: recall_at_100
      value: 64.66566666666668
    - type: recall_at_1000
      value: 84.09833333333336
    - type: recall_at_3
      value: 30.223083333333328
    - type: recall_at_5
      value: 35.153083333333335
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackStatsRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 17.582
    - type: map_at_10
      value: 22.803
    - type: map_at_100
      value: 23.503
    - type: map_at_1000
      value: 23.599999999999998
    - type: map_at_3
      value: 21.375
    - type: map_at_5
      value: 22.052
    - type: mrr_at_1
      value: 20.399
    - type: mrr_at_10
      value: 25.369999999999997
    - type: mrr_at_100
      value: 26.016000000000002
    - type: mrr_at_1000
      value: 26.090999999999998
    - type: mrr_at_3
      value: 23.952
    - type: mrr_at_5
      value: 24.619
    - type: ndcg_at_1
      value: 20.399
    - type: ndcg_at_10
      value: 25.964
    - type: ndcg_at_100
      value: 29.607
    - type: ndcg_at_1000
      value: 32.349
    - type: ndcg_at_3
      value: 23.177
    - type: ndcg_at_5
      value: 24.276
    - type: precision_at_1
      value: 20.399
    - type: precision_at_10
      value: 4.018
    - type: precision_at_100
      value: 0.629
    - type: precision_at_1000
      value: 0.093
    - type: precision_at_3
      value: 9.969
    - type: precision_at_5
      value: 6.748
    - type: recall_at_1
      value: 17.582
    - type: recall_at_10
      value: 33.35
    - type: recall_at_100
      value: 50.219
    - type: recall_at_1000
      value: 71.06099999999999
    - type: recall_at_3
      value: 25.619999999999997
    - type: recall_at_5
      value: 28.291
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackTexRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 11.071
    - type: map_at_10
      value: 16.201999999999998
    - type: map_at_100
      value: 17.112
    - type: map_at_1000
      value: 17.238
    - type: map_at_3
      value: 14.508
    - type: map_at_5
      value: 15.440999999999999
    - type: mrr_at_1
      value: 13.833
    - type: mrr_at_10
      value: 19.235
    - type: mrr_at_100
      value: 20.108999999999998
    - type: mrr_at_1000
      value: 20.196
    - type: mrr_at_3
      value: 17.515
    - type: mrr_at_5
      value: 18.505
    - type: ndcg_at_1
      value: 13.833
    - type: ndcg_at_10
      value: 19.643
    - type: ndcg_at_100
      value: 24.298000000000002
    - type: ndcg_at_1000
      value: 27.614
    - type: ndcg_at_3
      value: 16.528000000000002
    - type: ndcg_at_5
      value: 17.991
    - type: precision_at_1
      value: 13.833
    - type: precision_at_10
      value: 3.6990000000000003
    - type: precision_at_100
      value: 0.713
    - type: precision_at_1000
      value: 0.116
    - type: precision_at_3
      value: 7.9030000000000005
    - type: precision_at_5
      value: 5.891
    - type: recall_at_1
      value: 11.071
    - type: recall_at_10
      value: 27.019
    - type: recall_at_100
      value: 48.404
    - type: recall_at_1000
      value: 72.641
    - type: recall_at_3
      value: 18.336
    - type: recall_at_5
      value: 21.991
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackUnixRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 18.573
    - type: map_at_10
      value: 25.008999999999997
    - type: map_at_100
      value: 26.015
    - type: map_at_1000
      value: 26.137
    - type: map_at_3
      value: 22.798
    - type: map_at_5
      value: 24.092
    - type: mrr_at_1
      value: 22.108
    - type: mrr_at_10
      value: 28.646
    - type: mrr_at_100
      value: 29.477999999999998
    - type: mrr_at_1000
      value: 29.57
    - type: mrr_at_3
      value: 26.415
    - type: mrr_at_5
      value: 27.693
    - type: ndcg_at_1
      value: 22.108
    - type: ndcg_at_10
      value: 29.42
    - type: ndcg_at_100
      value: 34.385
    - type: ndcg_at_1000
      value: 37.572
    - type: ndcg_at_3
      value: 25.274
    - type: ndcg_at_5
      value: 27.315
    - type: precision_at_1
      value: 22.108
    - type: precision_at_10
      value: 5.093
    - type: precision_at_100
      value: 0.859
    - type: precision_at_1000
      value: 0.124
    - type: precision_at_3
      value: 11.474
    - type: precision_at_5
      value: 8.321000000000002
    - type: recall_at_1
      value: 18.573
    - type: recall_at_10
      value: 39.433
    - type: recall_at_100
      value: 61.597
    - type: recall_at_1000
      value: 84.69
    - type: recall_at_3
      value: 27.849
    - type: recall_at_5
      value: 33.202999999999996
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackWebmastersRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 22.807
    - type: map_at_10
      value: 30.014000000000003
    - type: map_at_100
      value: 31.422
    - type: map_at_1000
      value: 31.652
    - type: map_at_3
      value: 27.447
    - type: map_at_5
      value: 28.711
    - type: mrr_at_1
      value: 27.668
    - type: mrr_at_10
      value: 34.489
    - type: mrr_at_100
      value: 35.453
    - type: mrr_at_1000
      value: 35.526
    - type: mrr_at_3
      value: 32.477000000000004
    - type: mrr_at_5
      value: 33.603
    - type: ndcg_at_1
      value: 27.668
    - type: ndcg_at_10
      value: 34.983
    - type: ndcg_at_100
      value: 40.535
    - type: ndcg_at_1000
      value: 43.747
    - type: ndcg_at_3
      value: 31.026999999999997
    - type: ndcg_at_5
      value: 32.608
    - type: precision_at_1
      value: 27.668
    - type: precision_at_10
      value: 6.837999999999999
    - type: precision_at_100
      value: 1.411
    - type: precision_at_1000
      value: 0.23600000000000002
    - type: precision_at_3
      value: 14.295
    - type: precision_at_5
      value: 10.435
    - type: recall_at_1
      value: 22.807
    - type: recall_at_10
      value: 43.545
    - type: recall_at_100
      value: 69.39800000000001
    - type: recall_at_1000
      value: 90.706
    - type: recall_at_3
      value: 32.183
    - type: recall_at_5
      value: 36.563
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackWordpressRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 13.943
    - type: map_at_10
      value: 20.419999999999998
    - type: map_at_100
      value: 21.335
    - type: map_at_1000
      value: 21.44
    - type: map_at_3
      value: 17.865000000000002
    - type: map_at_5
      value: 19.36
    - type: mrr_at_1
      value: 15.712000000000002
    - type: mrr_at_10
      value: 22.345000000000002
    - type: mrr_at_100
      value: 23.227999999999998
    - type: mrr_at_1000
      value: 23.304
    - type: mrr_at_3
      value: 19.901
    - type: mrr_at_5
      value: 21.325
    - type: ndcg_at_1
      value: 15.712000000000002
    - type: ndcg_at_10
      value: 24.801000000000002
    - type: ndcg_at_100
      value: 29.799
    - type: ndcg_at_1000
      value: 32.513999999999996
    - type: ndcg_at_3
      value: 19.750999999999998
    - type: ndcg_at_5
      value: 22.252
    - type: precision_at_1
      value: 15.712000000000002
    - type: precision_at_10
      value: 4.1770000000000005
    - type: precision_at_100
      value: 0.738
    - type: precision_at_1000
      value: 0.106
    - type: precision_at_3
      value: 8.688
    - type: precision_at_5
      value: 6.617000000000001
    - type: recall_at_1
      value: 13.943
    - type: recall_at_10
      value: 36.913000000000004
    - type: recall_at_100
      value: 60.519
    - type: recall_at_1000
      value: 81.206
    - type: recall_at_3
      value: 23.006999999999998
    - type: recall_at_5
      value: 29.082
  - task:
      type: Retrieval
    dataset:
      type: climate-fever
      name: MTEB ClimateFEVER
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 9.468
    - type: map_at_10
      value: 16.029
    - type: map_at_100
      value: 17.693
    - type: map_at_1000
      value: 17.886
    - type: map_at_3
      value: 13.15
    - type: map_at_5
      value: 14.568
    - type: mrr_at_1
      value: 21.173000000000002
    - type: mrr_at_10
      value: 31.028
    - type: mrr_at_100
      value: 32.061
    - type: mrr_at_1000
      value: 32.119
    - type: mrr_at_3
      value: 27.534999999999997
    - type: mrr_at_5
      value: 29.431
    - type: ndcg_at_1
      value: 21.173000000000002
    - type: ndcg_at_10
      value: 23.224
    - type: ndcg_at_100
      value: 30.225
    - type: ndcg_at_1000
      value: 33.961000000000006
    - type: ndcg_at_3
      value: 18.174
    - type: ndcg_at_5
      value: 19.897000000000002
    - type: precision_at_1
      value: 21.173000000000002
    - type: precision_at_10
      value: 7.4719999999999995
    - type: precision_at_100
      value: 1.5010000000000001
    - type: precision_at_1000
      value: 0.219
    - type: precision_at_3
      value: 13.312
    - type: precision_at_5
      value: 10.619
    - type: recall_at_1
      value: 9.468
    - type: recall_at_10
      value: 28.823
    - type: recall_at_100
      value: 53.26499999999999
    - type: recall_at_1000
      value: 74.536
    - type: recall_at_3
      value: 16.672
    - type: recall_at_5
      value: 21.302
  - task:
      type: Retrieval
    dataset:
      type: dbpedia-entity
      name: MTEB DBPedia
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 6.343
    - type: map_at_10
      value: 12.717
    - type: map_at_100
      value: 16.48
    - type: map_at_1000
      value: 17.381
    - type: map_at_3
      value: 9.568999999999999
    - type: map_at_5
      value: 11.125
    - type: mrr_at_1
      value: 48.75
    - type: mrr_at_10
      value: 58.425000000000004
    - type: mrr_at_100
      value: 59.075
    - type: mrr_at_1000
      value: 59.095
    - type: mrr_at_3
      value: 56.291999999999994
    - type: mrr_at_5
      value: 57.679
    - type: ndcg_at_1
      value: 37.875
    - type: ndcg_at_10
      value: 27.77
    - type: ndcg_at_100
      value: 30.288999999999998
    - type: ndcg_at_1000
      value: 36.187999999999995
    - type: ndcg_at_3
      value: 31.385999999999996
    - type: ndcg_at_5
      value: 29.923
    - type: precision_at_1
      value: 48.75
    - type: precision_at_10
      value: 22.375
    - type: precision_at_100
      value: 6.3420000000000005
    - type: precision_at_1000
      value: 1.4489999999999998
    - type: precision_at_3
      value: 35.5
    - type: precision_at_5
      value: 30.55
    - type: recall_at_1
      value: 6.343
    - type: recall_at_10
      value: 16.936
    - type: recall_at_100
      value: 35.955999999999996
    - type: recall_at_1000
      value: 55.787
    - type: recall_at_3
      value: 10.771
    - type: recall_at_5
      value: 13.669999999999998
  - task:
      type: Classification
    dataset:
      type: mteb/emotion
      name: MTEB EmotionClassification
      config: default
      split: test
      revision: 4f58c6b202a23cf9a4da393831edf4f9183cad37
    metrics:
    - type: accuracy
      value: 41.99
    - type: f1
      value: 36.823402174564954
  - task:
      type: Retrieval
    dataset:
      type: fever
      name: MTEB FEVER
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 40.088
    - type: map_at_10
      value: 52.69200000000001
    - type: map_at_100
      value: 53.296
    - type: map_at_1000
      value: 53.325
    - type: map_at_3
      value: 49.905
    - type: map_at_5
      value: 51.617000000000004
    - type: mrr_at_1
      value: 43.009
    - type: mrr_at_10
      value: 56.203
    - type: mrr_at_100
      value: 56.75
    - type: mrr_at_1000
      value: 56.769000000000005
    - type: mrr_at_3
      value: 53.400000000000006
    - type: mrr_at_5
      value: 55.163
    - type: ndcg_at_1
      value: 43.009
    - type: ndcg_at_10
      value: 59.39
    - type: ndcg_at_100
      value: 62.129999999999995
    - type: ndcg_at_1000
      value: 62.793
    - type: ndcg_at_3
      value: 53.878
    - type: ndcg_at_5
      value: 56.887
    - type: precision_at_1
      value: 43.009
    - type: precision_at_10
      value: 8.366
    - type: precision_at_100
      value: 0.983
    - type: precision_at_1000
      value: 0.105
    - type: precision_at_3
      value: 22.377
    - type: precision_at_5
      value: 15.035000000000002
    - type: recall_at_1
      value: 40.088
    - type: recall_at_10
      value: 76.68700000000001
    - type: recall_at_100
      value: 88.91
    - type: recall_at_1000
      value: 93.782
    - type: recall_at_3
      value: 61.809999999999995
    - type: recall_at_5
      value: 69.131
  - task:
      type: Retrieval
    dataset:
      type: fiqa
      name: MTEB FiQA2018
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 10.817
    - type: map_at_10
      value: 18.9
    - type: map_at_100
      value: 20.448
    - type: map_at_1000
      value: 20.660999999999998
    - type: map_at_3
      value: 15.979
    - type: map_at_5
      value: 17.415
    - type: mrr_at_1
      value: 23.148
    - type: mrr_at_10
      value: 31.208000000000002
    - type: mrr_at_100
      value: 32.167
    - type: mrr_at_1000
      value: 32.242
    - type: mrr_at_3
      value: 28.498
    - type: mrr_at_5
      value: 29.964000000000002
    - type: ndcg_at_1
      value: 23.148
    - type: ndcg_at_10
      value: 25.325999999999997
    - type: ndcg_at_100
      value: 31.927
    - type: ndcg_at_1000
      value: 36.081
    - type: ndcg_at_3
      value: 21.647
    - type: ndcg_at_5
      value: 22.762999999999998
    - type: precision_at_1
      value: 23.148
    - type: precision_at_10
      value: 7.546
    - type: precision_at_100
      value: 1.415
    - type: precision_at_1000
      value: 0.216
    - type: precision_at_3
      value: 14.969
    - type: precision_at_5
      value: 11.327
    - type: recall_at_1
      value: 10.817
    - type: recall_at_10
      value: 32.164
    - type: recall_at_100
      value: 57.655
    - type: recall_at_1000
      value: 82.797
    - type: recall_at_3
      value: 19.709
    - type: recall_at_5
      value: 24.333
  - task:
      type: Retrieval
    dataset:
      type: hotpotqa
      name: MTEB HotpotQA
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 25.380999999999997
    - type: map_at_10
      value: 33.14
    - type: map_at_100
      value: 33.948
    - type: map_at_1000
      value: 34.028000000000006
    - type: map_at_3
      value: 31.019999999999996
    - type: map_at_5
      value: 32.23
    - type: mrr_at_1
      value: 50.763000000000005
    - type: mrr_at_10
      value: 57.899
    - type: mrr_at_100
      value: 58.426
    - type: mrr_at_1000
      value: 58.457
    - type: mrr_at_3
      value: 56.093
    - type: mrr_at_5
      value: 57.116
    - type: ndcg_at_1
      value: 50.763000000000005
    - type: ndcg_at_10
      value: 41.656
    - type: ndcg_at_100
      value: 45.079
    - type: ndcg_at_1000
      value: 46.916999999999994
    - type: ndcg_at_3
      value: 37.834
    - type: ndcg_at_5
      value: 39.732
    - type: precision_at_1
      value: 50.763000000000005
    - type: precision_at_10
      value: 8.648
    - type: precision_at_100
      value: 1.135
    - type: precision_at_1000
      value: 0.13799999999999998
    - type: precision_at_3
      value: 23.105999999999998
    - type: precision_at_5
      value: 15.363
    - type: recall_at_1
      value: 25.380999999999997
    - type: recall_at_10
      value: 43.241
    - type: recall_at_100
      value: 56.745000000000005
    - type: recall_at_1000
      value: 69.048
    - type: recall_at_3
      value: 34.659
    - type: recall_at_5
      value: 38.406
  - task:
      type: Classification
    dataset:
      type: mteb/imdb
      name: MTEB ImdbClassification
      config: default
      split: test
      revision: 3d86128a09e091d6018b6d26cad27f2739fc2db7
    metrics:
    - type: accuracy
      value: 79.544
    - type: ap
      value: 73.82920133396664
    - type: f1
      value: 79.51048124883265
  - task:
      type: Retrieval
    dataset:
      type: msmarco
      name: MTEB MSMARCO
      config: default
      split: dev
      revision: None
    metrics:
    - type: map_at_1
      value: 11.174000000000001
    - type: map_at_10
      value: 19.451999999999998
    - type: map_at_100
      value: 20.612
    - type: map_at_1000
      value: 20.703
    - type: map_at_3
      value: 16.444
    - type: map_at_5
      value: 18.083
    - type: mrr_at_1
      value: 11.447000000000001
    - type: mrr_at_10
      value: 19.808
    - type: mrr_at_100
      value: 20.958
    - type: mrr_at_1000
      value: 21.041999999999998
    - type: mrr_at_3
      value: 16.791
    - type: mrr_at_5
      value: 18.459
    - type: ndcg_at_1
      value: 11.447000000000001
    - type: ndcg_at_10
      value: 24.556
    - type: ndcg_at_100
      value: 30.637999999999998
    - type: ndcg_at_1000
      value: 33.14
    - type: ndcg_at_3
      value: 18.325
    - type: ndcg_at_5
      value: 21.278
    - type: precision_at_1
      value: 11.447000000000001
    - type: precision_at_10
      value: 4.215
    - type: precision_at_100
      value: 0.732
    - type: precision_at_1000
      value: 0.095
    - type: precision_at_3
      value: 8.052
    - type: precision_at_5
      value: 6.318
    - type: recall_at_1
      value: 11.174000000000001
    - type: recall_at_10
      value: 40.543
    - type: recall_at_100
      value: 69.699
    - type: recall_at_1000
      value: 89.403
    - type: recall_at_3
      value: 23.442
    - type: recall_at_5
      value: 30.536
  - task:
      type: Classification
    dataset:
      type: mteb/mtop_domain
      name: MTEB MTOPDomainClassification (en)
      config: en
      split: test
      revision: d80d48c1eb48d3562165c59d59d0034df9fff0bf
    metrics:
    - type: accuracy
      value: 89.6671226630187
    - type: f1
      value: 89.57660424361246
  - task:
      type: Classification
    dataset:
      type: mteb/mtop_intent
      name: MTEB MTOPIntentClassification (en)
      config: en
      split: test
      revision: ae001d0e6b1228650b7bd1c2c65fb50ad11a8aba
    metrics:
    - type: accuracy
      value: 60.284997720018254
    - type: f1
      value: 40.30637400152823
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (en)
      config: en
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 63.33557498318763
    - type: f1
      value: 60.24039910680179
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (en)
      config: en
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 72.37390719569603
    - type: f1
      value: 72.33097333477316
  - task:
      type: Clustering
    dataset:
      type: mteb/medrxiv-clustering-p2p
      name: MTEB MedrxivClusteringP2P
      config: default
      split: test
      revision: e7a26af6f3ae46b30dde8737f02c07b1505bcc73
    metrics:
    - type: v_measure
      value: 34.68158939060552
  - task:
      type: Clustering
    dataset:
      type: mteb/medrxiv-clustering-s2s
      name: MTEB MedrxivClusteringS2S
      config: default
      split: test
      revision: 35191c8c0dca72d8ff3efcd72aa802307d469663
    metrics:
    - type: v_measure
      value: 30.340061711905236
  - task:
      type: Reranking
    dataset:
      type: mteb/mind_small
      name: MTEB MindSmallReranking
      config: default
      split: test
      revision: 3bdac13927fdc888b903db93b2ffdbd90b295a69
    metrics:
    - type: map
      value: 32.01814326295803
    - type: mrr
      value: 33.20555240055367
  - task:
      type: Retrieval
    dataset:
      type: nfcorpus
      name: MTEB NFCorpus
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 3.3910000000000005
    - type: map_at_10
      value: 7.7219999999999995
    - type: map_at_100
      value: 10.286
    - type: map_at_1000
      value: 11.668000000000001
    - type: map_at_3
      value: 5.552
    - type: map_at_5
      value: 6.468
    - type: mrr_at_1
      value: 34.365
    - type: mrr_at_10
      value: 42.555
    - type: mrr_at_100
      value: 43.295
    - type: mrr_at_1000
      value: 43.357
    - type: mrr_at_3
      value: 40.299
    - type: mrr_at_5
      value: 41.182
    - type: ndcg_at_1
      value: 31.424000000000003
    - type: ndcg_at_10
      value: 24.758
    - type: ndcg_at_100
      value: 23.677999999999997
    - type: ndcg_at_1000
      value: 33.377
    - type: ndcg_at_3
      value: 28.302
    - type: ndcg_at_5
      value: 26.342
    - type: precision_at_1
      value: 33.437
    - type: precision_at_10
      value: 19.256999999999998
    - type: precision_at_100
      value: 6.662999999999999
    - type: precision_at_1000
      value: 1.9900000000000002
    - type: precision_at_3
      value: 27.761000000000003
    - type: precision_at_5
      value: 23.715
    - type: recall_at_1
      value: 3.3910000000000005
    - type: recall_at_10
      value: 11.068
    - type: recall_at_100
      value: 25.878
    - type: recall_at_1000
      value: 60.19
    - type: recall_at_3
      value: 6.1690000000000005
    - type: recall_at_5
      value: 7.767
  - task:
      type: Retrieval
    dataset:
      type: nq
      name: MTEB NQ
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 15.168000000000001
    - type: map_at_10
      value: 26.177
    - type: map_at_100
      value: 27.564
    - type: map_at_1000
      value: 27.628999999999998
    - type: map_at_3
      value: 22.03
    - type: map_at_5
      value: 24.276
    - type: mrr_at_1
      value: 17.439
    - type: mrr_at_10
      value: 28.205000000000002
    - type: mrr_at_100
      value: 29.357
    - type: mrr_at_1000
      value: 29.408
    - type: mrr_at_3
      value: 24.377
    - type: mrr_at_5
      value: 26.540000000000003
    - type: ndcg_at_1
      value: 17.41
    - type: ndcg_at_10
      value: 32.936
    - type: ndcg_at_100
      value: 39.196999999999996
    - type: ndcg_at_1000
      value: 40.892
    - type: ndcg_at_3
      value: 24.721
    - type: ndcg_at_5
      value: 28.615000000000002
    - type: precision_at_1
      value: 17.41
    - type: precision_at_10
      value: 6.199000000000001
    - type: precision_at_100
      value: 0.9690000000000001
    - type: precision_at_1000
      value: 0.11299999999999999
    - type: precision_at_3
      value: 11.790000000000001
    - type: precision_at_5
      value: 9.264
    - type: recall_at_1
      value: 15.168000000000001
    - type: recall_at_10
      value: 51.914
    - type: recall_at_100
      value: 79.804
    - type: recall_at_1000
      value: 92.75999999999999
    - type: recall_at_3
      value: 30.212
    - type: recall_at_5
      value: 39.204
  - task:
      type: Retrieval
    dataset:
      type: quora
      name: MTEB QuoraRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 67.306
    - type: map_at_10
      value: 80.634
    - type: map_at_100
      value: 81.349
    - type: map_at_1000
      value: 81.37299999999999
    - type: map_at_3
      value: 77.691
    - type: map_at_5
      value: 79.512
    - type: mrr_at_1
      value: 77.56
    - type: mrr_at_10
      value: 84.177
    - type: mrr_at_100
      value: 84.35000000000001
    - type: mrr_at_1000
      value: 84.353
    - type: mrr_at_3
      value: 83.003
    - type: mrr_at_5
      value: 83.799
    - type: ndcg_at_1
      value: 77.58
    - type: ndcg_at_10
      value: 84.782
    - type: ndcg_at_100
      value: 86.443
    - type: ndcg_at_1000
      value: 86.654
    - type: ndcg_at_3
      value: 81.67
    - type: ndcg_at_5
      value: 83.356
    - type: precision_at_1
      value: 77.58
    - type: precision_at_10
      value: 12.875
    - type: precision_at_100
      value: 1.503
    - type: precision_at_1000
      value: 0.156
    - type: precision_at_3
      value: 35.63
    - type: precision_at_5
      value: 23.483999999999998
    - type: recall_at_1
      value: 67.306
    - type: recall_at_10
      value: 92.64
    - type: recall_at_100
      value: 98.681
    - type: recall_at_1000
      value: 99.79
    - type: recall_at_3
      value: 83.682
    - type: recall_at_5
      value: 88.424
  - task:
      type: Clustering
    dataset:
      type: mteb/reddit-clustering
      name: MTEB RedditClustering
      config: default
      split: test
      revision: 24640382cdbf8abc73003fb0fa6d111a705499eb
    metrics:
    - type: v_measure
      value: 50.76319866126382
  - task:
      type: Clustering
    dataset:
      type: mteb/reddit-clustering-p2p
      name: MTEB RedditClusteringP2P
      config: default
      split: test
      revision: 282350215ef01743dc01b456c7f5241fa8937f16
    metrics:
    - type: v_measure
      value: 55.024711941648995
  - task:
      type: Retrieval
    dataset:
      type: scidocs
      name: MTEB SCIDOCS
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 3.9379999999999997
    - type: map_at_10
      value: 8.817
    - type: map_at_100
      value: 10.546999999999999
    - type: map_at_1000
      value: 10.852
    - type: map_at_3
      value: 6.351999999999999
    - type: map_at_5
      value: 7.453
    - type: mrr_at_1
      value: 19.400000000000002
    - type: mrr_at_10
      value: 27.371000000000002
    - type: mrr_at_100
      value: 28.671999999999997
    - type: mrr_at_1000
      value: 28.747
    - type: mrr_at_3
      value: 24.583
    - type: mrr_at_5
      value: 26.143
    - type: ndcg_at_1
      value: 19.400000000000002
    - type: ndcg_at_10
      value: 15.264
    - type: ndcg_at_100
      value: 22.63
    - type: ndcg_at_1000
      value: 28.559
    - type: ndcg_at_3
      value: 14.424999999999999
    - type: ndcg_at_5
      value: 12.520000000000001
    - type: precision_at_1
      value: 19.400000000000002
    - type: precision_at_10
      value: 7.8100000000000005
    - type: precision_at_100
      value: 1.854
    - type: precision_at_1000
      value: 0.329
    - type: precision_at_3
      value: 13.100000000000001
    - type: precision_at_5
      value: 10.68
    - type: recall_at_1
      value: 3.9379999999999997
    - type: recall_at_10
      value: 15.903
    - type: recall_at_100
      value: 37.645
    - type: recall_at_1000
      value: 66.86
    - type: recall_at_3
      value: 7.993
    - type: recall_at_5
      value: 10.885
  - task:
      type: STS
    dataset:
      type: mteb/sickr-sts
      name: MTEB SICK-R
      config: default
      split: test
      revision: a6ea5a8cab320b040a23452cc28066d9beae2cee
    metrics:
    - type: cos_sim_pearson
      value: 80.12689060151425
    - type: cos_sim_spearman
      value: 70.46515535094771
    - type: euclidean_pearson
      value: 77.17160003557223
    - type: euclidean_spearman
      value: 70.4651757047438
    - type: manhattan_pearson
      value: 77.18129609281937
    - type: manhattan_spearman
      value: 70.46610403752913
  - task:
      type: STS
    dataset:
      type: mteb/sts12-sts
      name: MTEB STS12
      config: default
      split: test
      revision: a0d554a64d88156834ff5ae9920b964011b16384
    metrics:
    - type: cos_sim_pearson
      value: 70.451157033355
    - type: cos_sim_spearman
      value: 63.99899601697852
    - type: euclidean_pearson
      value: 67.46985359967678
    - type: euclidean_spearman
      value: 64.00001637764805
    - type: manhattan_pearson
      value: 67.56534741780037
    - type: manhattan_spearman
      value: 64.06533893575366
  - task:
      type: STS
    dataset:
      type: mteb/sts13-sts
      name: MTEB STS13
      config: default
      split: test
      revision: 7e90230a92c190f1bf69ae9002b8cea547a64cca
    metrics:
    - type: cos_sim_pearson
      value: 77.65086614464292
    - type: cos_sim_spearman
      value: 78.20169706921848
    - type: euclidean_pearson
      value: 77.77758172155283
    - type: euclidean_spearman
      value: 78.20169706921848
    - type: manhattan_pearson
      value: 77.75077884860052
    - type: manhattan_spearman
      value: 78.16875216484164
  - task:
      type: STS
    dataset:
      type: mteb/sts14-sts
      name: MTEB STS14
      config: default
      split: test
      revision: 6031580fec1f6af667f0bd2da0a551cf4f0b2375
    metrics:
    - type: cos_sim_pearson
      value: 76.26381598259717
    - type: cos_sim_spearman
      value: 70.78377709313477
    - type: euclidean_pearson
      value: 74.82646556532096
    - type: euclidean_spearman
      value: 70.78377658155212
    - type: manhattan_pearson
      value: 74.81784766108225
    - type: manhattan_spearman
      value: 70.79351454692176
  - task:
      type: STS
    dataset:
      type: mteb/sts15-sts
      name: MTEB STS15
      config: default
      split: test
      revision: ae752c7c21bf194d8b67fd573edf7ae58183cbe3
    metrics:
    - type: cos_sim_pearson
      value: 79.00532026789739
    - type: cos_sim_spearman
      value: 80.02708383244838
    - type: euclidean_pearson
      value: 79.48345422610525
    - type: euclidean_spearman
      value: 80.02708383244838
    - type: manhattan_pearson
      value: 79.44519739854803
    - type: manhattan_spearman
      value: 79.98344094559687
  - task:
      type: STS
    dataset:
      type: mteb/sts16-sts
      name: MTEB STS16
      config: default
      split: test
      revision: 4d8694f8f0e0100860b497b999b3dbed754a0513
    metrics:
    - type: cos_sim_pearson
      value: 77.32783048164805
    - type: cos_sim_spearman
      value: 78.79729961288045
    - type: euclidean_pearson
      value: 78.72111945793154
    - type: euclidean_spearman
      value: 78.79729904606872
    - type: manhattan_pearson
      value: 78.72464311117116
    - type: manhattan_spearman
      value: 78.822591248334
  - task:
      type: STS
    dataset:
      type: mteb/sts17-crosslingual-sts
      name: MTEB STS17 (en-en)
      config: en-en
      split: test
      revision: af5e6fb845001ecf41f4c1e033ce921939a2a68d
    metrics:
    - type: cos_sim_pearson
      value: 82.04318630630854
    - type: cos_sim_spearman
      value: 83.87886389259836
    - type: euclidean_pearson
      value: 83.40385877895086
    - type: euclidean_spearman
      value: 83.87886389259836
    - type: manhattan_pearson
      value: 83.46337128901547
    - type: manhattan_spearman
      value: 83.9723106941644
  - task:
      type: STS
    dataset:
      type: mteb/sts22-crosslingual-sts
      name: MTEB STS22 (en)
      config: en
      split: test
      revision: 6d1ba47164174a496b7fa5d3569dae26a6813b80
    metrics:
    - type: cos_sim_pearson
      value: 63.003511169944595
    - type: cos_sim_spearman
      value: 64.39318805580227
    - type: euclidean_pearson
      value: 65.4797990735967
    - type: euclidean_spearman
      value: 64.39318805580227
    - type: manhattan_pearson
      value: 65.44604544280844
    - type: manhattan_spearman
      value: 64.38742899984233
  - task:
      type: STS
    dataset:
      type: mteb/stsbenchmark-sts
      name: MTEB STSBenchmark
      config: default
      split: test
      revision: b0fddb56ed78048fa8b90373c8a3cfc37b684831
    metrics:
    - type: cos_sim_pearson
      value: 76.63101237585029
    - type: cos_sim_spearman
      value: 75.57446967644269
    - type: euclidean_pearson
      value: 76.93491768734478
    - type: euclidean_spearman
      value: 75.57446967644269
    - type: manhattan_pearson
      value: 76.92187567800636
    - type: manhattan_spearman
      value: 75.57239337194585
  - task:
      type: Reranking
    dataset:
      type: mteb/scidocs-reranking
      name: MTEB SciDocsRR
      config: default
      split: test
      revision: d3c5e1fc0b855ab6097bf1cda04dd73947d7caab
    metrics:
    - type: map
      value: 78.5376604868993
    - type: mrr
      value: 92.94422897364073
  - task:
      type: Retrieval
    dataset:
      type: scifact
      name: MTEB SciFact
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 38.872
    - type: map_at_10
      value: 50.417
    - type: map_at_100
      value: 51.202000000000005
    - type: map_at_1000
      value: 51.25999999999999
    - type: map_at_3
      value: 47.02
    - type: map_at_5
      value: 49.326
    - type: mrr_at_1
      value: 41.0
    - type: mrr_at_10
      value: 51.674
    - type: mrr_at_100
      value: 52.32599999999999
    - type: mrr_at_1000
      value: 52.376999999999995
    - type: mrr_at_3
      value: 48.778
    - type: mrr_at_5
      value: 50.744
    - type: ndcg_at_1
      value: 41.0
    - type: ndcg_at_10
      value: 56.027
    - type: ndcg_at_100
      value: 59.362
    - type: ndcg_at_1000
      value: 60.839
    - type: ndcg_at_3
      value: 50.019999999999996
    - type: ndcg_at_5
      value: 53.644999999999996
    - type: precision_at_1
      value: 41.0
    - type: precision_at_10
      value: 8.1
    - type: precision_at_100
      value: 0.987
    - type: precision_at_1000
      value: 0.11100000000000002
    - type: precision_at_3
      value: 20.444000000000003
    - type: precision_at_5
      value: 14.466999999999999
    - type: recall_at_1
      value: 38.872
    - type: recall_at_10
      value: 71.906
    - type: recall_at_100
      value: 86.367
    - type: recall_at_1000
      value: 98.0
    - type: recall_at_3
      value: 56.206
    - type: recall_at_5
      value: 65.05
  - task:
      type: PairClassification
    dataset:
      type: mteb/sprintduplicatequestions-pairclassification
      name: MTEB SprintDuplicateQuestions
      config: default
      split: test
      revision: d66bd1f72af766a5cc4b0ca5e00c162f89e8cc46
    metrics:
    - type: cos_sim_accuracy
      value: 99.7039603960396
    - type: cos_sim_ap
      value: 90.40809844250262
    - type: cos_sim_f1
      value: 84.53181583031557
    - type: cos_sim_precision
      value: 87.56698821007502
    - type: cos_sim_recall
      value: 81.69999999999999
    - type: dot_accuracy
      value: 99.7039603960396
    - type: dot_ap
      value: 90.40809844250262
    - type: dot_f1
      value: 84.53181583031557
    - type: dot_precision
      value: 87.56698821007502
    - type: dot_recall
      value: 81.69999999999999
    - type: euclidean_accuracy
      value: 99.7039603960396
    - type: euclidean_ap
      value: 90.4080982863383
    - type: euclidean_f1
      value: 84.53181583031557
    - type: euclidean_precision
      value: 87.56698821007502
    - type: euclidean_recall
      value: 81.69999999999999
    - type: manhattan_accuracy
      value: 99.7
    - type: manhattan_ap
      value: 90.39771161966652
    - type: manhattan_f1
      value: 84.32989690721648
    - type: manhattan_precision
      value: 87.02127659574468
    - type: manhattan_recall
      value: 81.8
    - type: max_accuracy
      value: 99.7039603960396
    - type: max_ap
      value: 90.40809844250262
    - type: max_f1
      value: 84.53181583031557
  - task:
      type: Clustering
    dataset:
      type: mteb/stackexchange-clustering
      name: MTEB StackExchangeClustering
      config: default
      split: test
      revision: 6cbc1f7b2bc0622f2e39d2c77fa502909748c259
    metrics:
    - type: v_measure
      value: 59.663210666678715
  - task:
      type: Clustering
    dataset:
      type: mteb/stackexchange-clustering-p2p
      name: MTEB StackExchangeClusteringP2P
      config: default
      split: test
      revision: 815ca46b2622cec33ccafc3735d572c266efdb44
    metrics:
    - type: v_measure
      value: 32.107791216468776
  - task:
      type: Reranking
    dataset:
      type: mteb/stackoverflowdupquestions-reranking
      name: MTEB StackOverflowDupQuestions
      config: default
      split: test
      revision: e185fbe320c72810689fc5848eb6114e1ef5ec69
    metrics:
    - type: map
      value: 46.440691925067604
    - type: mrr
      value: 47.03390257618199
  - task:
      type: Summarization
    dataset:
      type: mteb/summeval
      name: MTEB SummEval
      config: default
      split: test
      revision: cda12ad7615edc362dbf25a00fdd61d3b1eaf93c
    metrics:
    - type: cos_sim_pearson
      value: 31.067177519784074
    - type: cos_sim_spearman
      value: 31.234728424648967
    - type: dot_pearson
      value: 31.06717083018107
    - type: dot_spearman
      value: 31.234728424648967
  - task:
      type: Retrieval
    dataset:
      type: trec-covid
      name: MTEB TRECCOVID
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 0.136
    - type: map_at_10
      value: 0.767
    - type: map_at_100
      value: 3.3689999999999998
    - type: map_at_1000
      value: 8.613999999999999
    - type: map_at_3
      value: 0.369
    - type: map_at_5
      value: 0.514
    - type: mrr_at_1
      value: 48.0
    - type: mrr_at_10
      value: 63.908
    - type: mrr_at_100
      value: 64.615
    - type: mrr_at_1000
      value: 64.615
    - type: mrr_at_3
      value: 62.0
    - type: mrr_at_5
      value: 63.4
    - type: ndcg_at_1
      value: 44.0
    - type: ndcg_at_10
      value: 38.579
    - type: ndcg_at_100
      value: 26.409
    - type: ndcg_at_1000
      value: 26.858999999999998
    - type: ndcg_at_3
      value: 47.134
    - type: ndcg_at_5
      value: 43.287
    - type: precision_at_1
      value: 48.0
    - type: precision_at_10
      value: 40.400000000000006
    - type: precision_at_100
      value: 26.640000000000004
    - type: precision_at_1000
      value: 12.04
    - type: precision_at_3
      value: 52.666999999999994
    - type: precision_at_5
      value: 46.800000000000004
    - type: recall_at_1
      value: 0.136
    - type: recall_at_10
      value: 1.0070000000000001
    - type: recall_at_100
      value: 6.318
    - type: recall_at_1000
      value: 26.522000000000002
    - type: recall_at_3
      value: 0.41700000000000004
    - type: recall_at_5
      value: 0.606
  - task:
      type: Retrieval
    dataset:
      type: webis-touche2020
      name: MTEB Touche2020
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 1.9949999999999999
    - type: map_at_10
      value: 8.304
    - type: map_at_100
      value: 13.644
    - type: map_at_1000
      value: 15.43
    - type: map_at_3
      value: 4.788
    - type: map_at_5
      value: 6.22
    - type: mrr_at_1
      value: 22.448999999999998
    - type: mrr_at_10
      value: 37.658
    - type: mrr_at_100
      value: 38.491
    - type: mrr_at_1000
      value: 38.503
    - type: mrr_at_3
      value: 32.312999999999995
    - type: mrr_at_5
      value: 35.68
    - type: ndcg_at_1
      value: 21.429000000000002
    - type: ndcg_at_10
      value: 18.995
    - type: ndcg_at_100
      value: 32.029999999999994
    - type: ndcg_at_1000
      value: 44.852
    - type: ndcg_at_3
      value: 19.464000000000002
    - type: ndcg_at_5
      value: 19.172
    - type: precision_at_1
      value: 22.448999999999998
    - type: precision_at_10
      value: 17.143
    - type: precision_at_100
      value: 6.877999999999999
    - type: precision_at_1000
      value: 1.524
    - type: precision_at_3
      value: 21.769
    - type: precision_at_5
      value: 20.0
    - type: recall_at_1
      value: 1.9949999999999999
    - type: recall_at_10
      value: 13.395999999999999
    - type: recall_at_100
      value: 44.348
    - type: recall_at_1000
      value: 82.622
    - type: recall_at_3
      value: 5.896
    - type: recall_at_5
      value: 8.554
  - task:
      type: Classification
    dataset:
      type: mteb/toxic_conversations_50k
      name: MTEB ToxicConversationsClassification
      config: default
      split: test
      revision: d7c0de2777da35d6aae2200a62c6e0e5af397c4c
    metrics:
    - type: accuracy
      value: 67.9394
    - type: ap
      value: 12.943337263423334
    - type: f1
      value: 52.28243093094156
  - task:
      type: Classification
    dataset:
      type: mteb/tweet_sentiment_extraction
      name: MTEB TweetSentimentExtractionClassification
      config: default
      split: test
      revision: d604517c81ca91fe16a244d1248fc021f9ecee7a
    metrics:
    - type: accuracy
      value: 56.414827391058296
    - type: f1
      value: 56.666412409573105
  - task:
      type: Clustering
    dataset:
      type: mteb/twentynewsgroups-clustering
      name: MTEB TwentyNewsgroupsClustering
      config: default
      split: test
      revision: 6125ec4e24fa026cec8a478383ee943acfbd5449
    metrics:
    - type: v_measure
      value: 47.009746255495465
  - task:
      type: PairClassification
    dataset:
      type: mteb/twittersemeval2015-pairclassification
      name: MTEB TwitterSemEval2015
      config: default
      split: test
      revision: 70970daeab8776df92f5ea462b6173c0b46fd2d1
    metrics:
    - type: cos_sim_accuracy
      value: 84.02574953805807
    - type: cos_sim_ap
      value: 67.66599910763128
    - type: cos_sim_f1
      value: 63.491277990844985
    - type: cos_sim_precision
      value: 59.77172140694154
    - type: cos_sim_recall
      value: 67.70448548812665
    - type: dot_accuracy
      value: 84.02574953805807
    - type: dot_ap
      value: 67.66600090945406
    - type: dot_f1
      value: 63.491277990844985
    - type: dot_precision
      value: 59.77172140694154
    - type: dot_recall
      value: 67.70448548812665
    - type: euclidean_accuracy
      value: 84.02574953805807
    - type: euclidean_ap
      value: 67.6659842364448
    - type: euclidean_f1
      value: 63.491277990844985
    - type: euclidean_precision
      value: 59.77172140694154
    - type: euclidean_recall
      value: 67.70448548812665
    - type: manhattan_accuracy
      value: 84.0317100792752
    - type: manhattan_ap
      value: 67.66351692448987
    - type: manhattan_f1
      value: 63.48610948306178
    - type: manhattan_precision
      value: 57.11875131828729
    - type: manhattan_recall
      value: 71.45118733509234
    - type: max_accuracy
      value: 84.0317100792752
    - type: max_ap
      value: 67.66600090945406
    - type: max_f1
      value: 63.491277990844985
  - task:
      type: PairClassification
    dataset:
      type: mteb/twitterurlcorpus-pairclassification
      name: MTEB TwitterURLCorpus
      config: default
      split: test
      revision: 8b6510b0b1fa4e4c4f879467980e9be563ec1cdf
    metrics:
    - type: cos_sim_accuracy
      value: 87.53832421314084
    - type: cos_sim_ap
      value: 83.11416594316626
    - type: cos_sim_f1
      value: 75.41118114347518
    - type: cos_sim_precision
      value: 73.12839059674504
    - type: cos_sim_recall
      value: 77.8410840776101
    - type: dot_accuracy
      value: 87.53832421314084
    - type: dot_ap
      value: 83.11416226342155
    - type: dot_f1
      value: 75.41118114347518
    - type: dot_precision
      value: 73.12839059674504
    - type: dot_recall
      value: 77.8410840776101
    - type: euclidean_accuracy
      value: 87.53832421314084
    - type: euclidean_ap
      value: 83.11416284455395
    - type: euclidean_f1
      value: 75.41118114347518
    - type: euclidean_precision
      value: 73.12839059674504
    - type: euclidean_recall
      value: 77.8410840776101
    - type: manhattan_accuracy
      value: 87.49369348391353
    - type: manhattan_ap
      value: 83.08066812574694
    - type: manhattan_f1
      value: 75.36561228603892
    - type: manhattan_precision
      value: 71.9202518363064
    - type: manhattan_recall
      value: 79.15768401601478
    - type: max_accuracy
      value: 87.53832421314084
    - type: max_ap
      value: 83.11416594316626
    - type: max_f1
      value: 75.41118114347518
---

# lodestone-base-4096-v1

[Hum-Works/lodestone-base-4096-v1](https://huggingface.co/Hum-Works/lodestone-base-4096-v1). [Griffin McCauley](https://huggingface.co/gmccaul1), [Will Fortin](https://huggingface.co/willathum), [Dylan DiGioia](https://huggingface.co/dylanAtHum) 2023

This new [sentence-transformers](https://www.SBERT.net) model from [Hum](https://www.hum.works/) maps long sentences & paragraphs to a 768 dimensional dense vector space and can be used for tasks like clustering or semantic search.

## Abstract

In the hopes of furthering Hum's overarching mission of increasing the accessibility and interconnectivity of human knowledge, this model was developed as part of a project intending to boost the maximum input sequence length of sentence embedding models by leveraging recent architectural advances in the design of transformer models such as the incorporation of FlashAttention, Attention with Linear Biases (ALiBi), and Gated Linear Units (GLU). These modifications and enhancements were implemented by the team at MosaicML who designed and constructed the pre-trained [`mosaic-bert-base-seqlen-2048`](https://huggingface.co/mosaicml/mosaic-bert-base-seqlen-2048) model, and more information regarding the details of their development and testing specifications can be found on the model card.

While the fine-tuning procedure followed during the course of this project loosely mirrors that of the of the original [Flax-sentence-embeddings](https://huggingface.co/flax-sentence-embeddings) team responsible for the creation of many other popular sentence-transformers models (e.g. [all-mpnet-base-v2](https://huggingface.co/sentence-transformers/all-mpnet-base-v2), [all-distilroberta-v1](https://huggingface.co/sentence-transformers/all-distilroberta-v1), and [all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2)), our methodology includes novel techniques for data loading, batch sampling, and model checkpointing intended to improve training efficiency with regards to memory allocation and data storage.

Through combining these well-established and proven fine-tuning practices with novel advances in transformer architectural elements, our `lodestone-base-4096-v1` model is able to achieve comparable performance metrics on standard text embedding evaluation benchmarks while also supporting a longer and more robust input sequence length of 4096 while retaining a smaller, more manageable size capable of being run on either a GPU or CPU. 

## Usage

Using this model becomes relatively easy when you have [sentence-transformers](https://www.SBERT.net) installed. 
*At the time of publishing, sentence-transformers does not support remote code which is required for flash-attention used by the model. A fork of the sentence-transformers repository that allows remote code execution is provided for convenience. It can be installed using the following command:*
```
pip install git+https://github.com/Hum-Works/sentence-transformers.git
pip install einops
```

Then you can use the model like this:
```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('Hum-Works/lodestone-base-4096-v1', trust_remote_code=True, revision='v1.0.0')
sentences = ["This is an example sentence", "Each sentence is converted"]
embeddings = model.encode(sentences)
print(embeddings)
```
*Note: The model will use the openAI/Triton implementation of FlashAttention if installed. This is more performant than the fallback, torch implementation. Some platforms and GPUs may not be supported by Triton - up to date compatibility can be found on [Triton’s github page](https://github.com/openai/triton#compatibility).*

------

## Background

The project aims to train sentence embedding models on very large sentence level datasets using a self-supervised contrastive learning objective. We used the pretrained [`mosaic-bert-base-seqlen-2048`](https://huggingface.co/mosaicml/mosaic-bert-base-seqlen-2048) model and fine-tuned it on a nearly 1.5B sentence pairs dataset. We use a contrastive learning objective: given a sentence from the pair, the model should predict which out of a set of randomly sampled other sentences, was actually paired with it in our dataset.

## Intended uses

Our model is intended to be used as a long sentence and paragraph encoder. Given an input text, it outputs a vector containing the semantic information. The sentence vector may be used for information retrieval, clustering, or sentence similarity tasks.

## Training procedure

### Pre-training 

We use the pretrained [`mosaic-bert-base-seqlen-2048`](https://huggingface.co/mosaicml/mosaic-bert-base-seqlen-2048). Please refer to the model card for more detailed information about the pre-training procedure.

### Fine-tuning 

We fine-tune the model using a contrastive objective. Formally, we compute the dot product of each possible sentence pairing in the batch. We then apply the cross entropy loss by comparing with true pairs.

#### Hyperparameters

We trained our model on an ml.g5.4xlarge EC2 instance with 1 NVIDIA A10G Tensor Core GPU. We train the model during 1.4 million steps using a batch size of 16. We use a learning rate warm up of 500. The sequence length during training was limited to 2048 tokens. We used the AdamW optimizer with a 2e-5 learning rate and weight decay of 0.01 (i.e. the default parameter values for SentenceTransformer.fit()). The full training script is accessible in this current repository: `Training.py`.

## Model Architecture
By incorporating FlashAttention, [Attention with Linear Biases (ALiBi)](https://arxiv.org/abs/2108.12409), and Gated Linear Units (GLU), this model is able to handle input sequences of 4096, 8x longer than that supported by most comparable sentence embedding models. 
The model was trained using a sequence length maximum of 2048, but the final model has a maximum sequence length of 4096. This is accomplished by taking advantage of ALiBi’s positional attention extrapolation which has been shown to allow sequence lengths of 2x the initial trained length.

## Full Model Architecture
```
SentenceTransformer(
  (0): Transformer({'max_seq_length': 4096, 'do_lower_case': False}) with Transformer model: BertModel 
  (1): Pooling({'word_embedding_dimension': 768, 'pooling_mode_cls_token': False, 'pooling_mode_mean_tokens': True, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False, 'pooling_mode_weightedmean_tokens': False, 'pooling_mode_lasttoken': False})
  (2): Normalize()
)
```

#### Training data

We use the concatenation from multiple datasets to fine-tune our model. The total number of sentence pairs is nearly 1.5 billion sentences. We sampled each dataset given a weighted probability proportional to its relative contribution to the entire dataset.
The breakdown of the dataset can be seen below, and the entire dataset can be publicly accessed and uploaded via the `Dataloading.ipynb` located within this repository.

| Dataset                                                  | Paper                                    | Number of training tuples  |
|--------------------------------------------------------|:----------------------------------------:|:--------------------------:|
| [Reddit comments (2015-2018)](https://github.com/PolyAI-LDN/conversational-datasets/tree/master/reddit) | [paper](https://arxiv.org/abs/1904.06472) | 726,484,430 |
| **[S2ORC](https://github.com/allenai/s2orc) Citation pairs (Abstracts)** | [paper](https://aclanthology.org/2020.acl-main.447/) | 252,102,397 |
| **[Reddit posts](https://huggingface.co/datasets/sentence-transformers/reddit-title-body) (Title, Body) pairs** | - | 127,445,911 |
| **[Amazon reviews (2018)](https://huggingface.co/datasets/sentence-transformers/embedding-training-data) (Title, Review) pairs** | - | 87,877,725 |
| [WikiAnswers](https://github.com/afader/oqa#wikianswers-corpus) Duplicate question pairs | [paper](https://doi.org/10.1145/2623330.2623677) | 77,427,422 |
| [PAQ](https://github.com/facebookresearch/PAQ) (Question, Answer) pairs | [paper](https://arxiv.org/abs/2102.07033) | 64,371,441 |
| [S2ORC](https://github.com/allenai/s2orc) Citation pairs (Titles) | [paper](https://aclanthology.org/2020.acl-main.447/) | 52,603,982 |
| [S2ORC](https://github.com/allenai/s2orc) (Title, Abstract) | [paper](https://aclanthology.org/2020.acl-main.447/) | 41,769,185 |
| [Stack Exchange](https://huggingface.co/datasets/flax-sentence-embeddings/stackexchange_title_body_jsonl) (Title, Body) pairs  | - | 25,368,423 |
| [MS MARCO](https://microsoft.github.io/msmarco/) triplets | [paper](https://doi.org/10.1145/3404835.3462804) | 9,144,553 |
| **[Stack Exchange](https://huggingface.co/datasets/flax-sentence-embeddings/stackexchange_title_best_voted_answer_jsonl) (Title, Most Upvoted Answer) pairs** | - | 4,784,250 |
| **[Stack Exchange](https://huggingface.co/datasets/flax-sentence-embeddings/stackexchange_titlebody_best_voted_answer_jsonl) (Title+Body, Most Upvoted Answer) pairs** | - | 4,551,660 |
| [GOOAQ: Open Question Answering with Diverse Answer Types](https://github.com/allenai/gooaq) | [paper](https://arxiv.org/pdf/2104.08727.pdf) | 3,012,496 |
| **[Amazon QA](https://huggingface.co/datasets/sentence-transformers/embedding-training-data)** | - | 2,507,114 |
| [Code Search](https://huggingface.co/datasets/code_search_net) | - | 1,375,067 |
| [Yahoo Answers](https://www.kaggle.com/soumikrakshit/yahoo-answers-dataset) (Title, Answer) | [paper](https://proceedings.neurips.cc/paper/2015/hash/250cf8b51c773f3f8dc8b4be867a9a02-Abstract.html) | 1,198,260 |
| **[AG News]((Title, Description) pairs of news articles from the AG News dataset)** | - | 1,157,745 |
| [COCO](https://cocodataset.org/#home) Image captions | [paper](https://link.springer.com/chapter/10.1007%2F978-3-319-10602-1_48) | 828,395|
| [SPECTER](https://github.com/allenai/specter) citation triplets | [paper](https://doi.org/10.18653/v1/2020.acl-main.207) | 684,100 |
| [Yahoo Answers](https://www.kaggle.com/soumikrakshit/yahoo-answers-dataset) (Question, Answer) | [paper](https://proceedings.neurips.cc/paper/2015/hash/250cf8b51c773f3f8dc8b4be867a9a02-Abstract.html) | 681,164 |
| [Yahoo Answers](https://www.kaggle.com/soumikrakshit/yahoo-answers-dataset) (Title, Question) | [paper](https://proceedings.neurips.cc/paper/2015/hash/250cf8b51c773f3f8dc8b4be867a9a02-Abstract.html) | 659,896 |
| **[CC News](https://huggingface.co/datasets/sentence-transformers/embedding-training-data) (Title, article) pairs** | - | 614,664 |
| **[NPR](https://huggingface.co/datasets/sentence-transformers/embedding-training-data) (Title, Body) pairs** | - | 594,384 |
| [SearchQA](https://huggingface.co/datasets/search_qa) | [paper](https://arxiv.org/abs/1704.05179) | 582,261 |
| **[MS Marco](https://microsoft.github.io/msmarco/) (Query, Answer Passage) pairs** | [paper](https://doi.org/10.1145/3404835.3462804) | 532,751 |
| [Stack Exchange](https://docs.google.com/spreadsheets/d/1vXJrIg38cEaKjOG5y4I4PQwAQFUmCkohbViJ9zj_Emg/edit#gid=0) (Title, Body) pairs | - | 364,000 |
| [Eli5](https://huggingface.co/datasets/eli5) | [paper](https://doi.org/10.18653/v1/p19-1346) | 325,475 |
| [Flickr 30k](https://shannon.cs.illinois.edu/DenotationGraph/) | [paper](https://transacl.org/ojs/index.php/tacl/article/view/229/33) | 317,695 |
| **[CNN & DailyMail](https://huggingface.co/datasets/sentence-transformers/embedding-training-data) (highlight sentences, article) pairs** | - | 311,971 |
| [Stack Exchange](https://docs.google.com/spreadsheets/d/1vXJrIg38cEaKjOG5y4I4PQwAQFUmCkohbViJ9zj_Emg/edit#gid=0) Duplicate questions (titles) | - | 304,524 |
| AllNLI ([SNLI](https://nlp.stanford.edu/projects/snli/) and [MultiNLI](https://cims.nyu.edu/~sbowman/multinli/) | [paper SNLI](https://doi.org/10.18653/v1/d15-1075), [paper MultiNLI](https://doi.org/10.18653/v1/n18-1101) | 277,230 | 
| [Stack Exchange](https://docs.google.com/spreadsheets/d/1vXJrIg38cEaKjOG5y4I4PQwAQFUmCkohbViJ9zj_Emg/edit#gid=0) Duplicate questions (bodies) | - | 250,518 |
| [Stack Exchange](https://docs.google.com/spreadsheets/d/1vXJrIg38cEaKjOG5y4I4PQwAQFUmCkohbViJ9zj_Emg/edit#gid=0) Duplicate questions (titles+bodies) | - | 250,459 |
| **[XSUM](https://huggingface.co/datasets/sentence-transformers/embedding-training-data) (Summary, News Article) pairs** | - | 226,711 |
| **[Stack Exchange](https://huggingface.co/datasets/flax-sentence-embeddings/stackexchange_titlebody_best_and_down_voted_answer_jsonl) (Title+Body, Most Upvoted Answer, Most Downvoted Answer) triplets** | - | 216,454 |
| [Sentence Compression](https://github.com/google-research-datasets/sentence-compression) | [paper](https://www.aclweb.org/anthology/D13-1155/) | 180,000 |
| **[FEVER](https://docs.google.com/spreadsheets/d/1vXJrIg38cEaKjOG5y4I4PQwAQFUmCkohbViJ9zj_Emg/edit#gid=0) training data** | - | 139,051 |
| [Wikihow](https://github.com/pvl/wikihow_pairs_dataset) | [paper](https://arxiv.org/abs/1810.09305) | 128,542 |
| **[SearchQA](https://huggingface.co/datasets/search_qa) (Question, Top-Snippet)** | [paper](https://arxiv.org/abs/1704.05179) | 117,384 |
| [Altlex](https://github.com/chridey/altlex/) | [paper](https://aclanthology.org/P16-1135.pdf) | 112,696 |
| **[Quora Question Duplicates](https://quoradata.quora.com/First-Quora-Dataset-Release-Question-Pairs)** | - | 103,663 |
| [Quora Question Triplets](https://quoradata.quora.com/First-Quora-Dataset-Release-Question-Pairs) | - | 103,663 |
| [Simple Wikipedia](https://cs.pomona.edu/~dkauchak/simplification/) | [paper](https://www.aclweb.org/anthology/P11-2117/) | 102,225 |
| [Natural Questions (NQ)](https://ai.google.com/research/NaturalQuestions) | [paper](https://transacl.org/ojs/index.php/tacl/article/view/1455) | 100,231 |
| [SQuAD2.0](https://rajpurkar.github.io/SQuAD-explorer/) | [paper](https://aclanthology.org/P18-2124.pdf) | 87,599 |
| [TriviaQA](https://huggingface.co/datasets/trivia_qa) | - | 73,346 |
| **Total** | | **1,492,453,113** |

#### Replication

The entire fine-tuning process for this model can be replicated by following the steps outlined in the `Replication.txt` file within this repository. This document explains how to modify the [sentence-transformers](https://www.SBERT.net) library, configure the pre-trained [`mosaic-bert-base-seqlen-2048`](https://huggingface.co/mosaicml/mosaic-bert-base-seqlen-2048) model, load all of the training data, and execute the training script.

#### Limitations

Due to technical constraints (e.g. limited GPU memory capacity), this model was trained with a smaller batch size of 16, making it so that each step during training was less well-informed than it would have been on a higher performance system. This smaller than ideal hyperparameter value will generally cause the model to be more likely to get stuck in a local minimum and for the parameter configuration to take a longer time to converge to the optimum. In order to counteract this potential risk, we trained the model for a larger number of steps than many of its contemporaries to ensure a greater chance of achieving strong performance, but this is an area which could be improved if further fine-tuning was performed.

It is also worth noting that, while this model is able to handle longer input sequences of up to 4096 word pieces, the training dataset used consists of sentence and paragraph pairs and triplets which do not necessarily reach that maximum sequence length. Since the data was not tailored specifically for this larger input size, further fine-tuning may be required to ensure highly accurate embeddings for longer texts of that magnitude.

Finally, as stated on https://huggingface.co/datasets/sentence-transformers/reddit-title-body, an additional reminder and warning regarding the Reddit posts data is that one should "Be aware that this dataset is not filtered for biases, hate-speech, spam, racial slurs etc. It depicts the content as it is posted on Reddit." Thus, while we believe this has not induced any pathological behaviors in the model's performance due to its relatively low prevalence of records in the whole dataset of nearly 1.5B sentence pairs and the fact that this model was trained to produce semantic embeddings rather than generative text outputs, it is always important to be aware of vulnerabilities to bias.

