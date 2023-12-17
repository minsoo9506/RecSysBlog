---
title: "[industry] How Instagram suggests new content, 2020"
date: "2023-12-17"
author: "SongMinsoo"
category: "Industry"
tag: ["Meta", "Suggest contents", "Instagram"]
---

- [How Instagram suggests new content, 2020](https://engineering.fb.com/2020/12/10/web/how-instagram-suggests-new-content/)

## background
- 홈피드 랭킹 시스템은 follow하는 포스트들을 engagement, relevance, freshness를 기준을 랭킹을 진행합니다.
- 탐색피드 랭킹 시스템은 유저와 관련있는 공개포스트들을 랭킹하여 제공합니다.
- 이들의 중간격인 suggested post를 홈피드에서 제공하려고 합니다.
- 이때 중요한 점은 "Feels Like Home" 입니다. (design principle of ML system)

## system overview
- information retrieval system은 two step으로 이루어져있습니다.
  - candidate generation + candidate selection
- 아래 그림처럼 홈피드는 connected recommendation이라고 할 수 있고 suggested post 시스템은 unconnected recommendation 이라고 할 수 있습니다.

![img](../../image/image_industry/meta(facebook)/meta_1.png)

## candidate generation
- 가장 많이 하는 접근법중 하나는 결국 KNN입니다. seed가 주어지면 그와 가까운 것들이 후보군으로 뽑힙니다.
  - embedding based similarity
  - co-occurrence based similarity

![img](../../image/image_industry/meta(facebook)/meta_2.png)

## cold start problem
- engagement가 비교적 적은 유저의 경우 다른 방법으로 해결합니다.
- Fallback graph exploration
  - 유저 A가 팔로우한 경우가 거의 없는 경우, A가 팔로우한 유저가 like한 게시물을 고려합니다.
  - 즉, 한단계 건너뛰어서 seed를 구하는 접근입니다.
- Popular media:
  - 완전 새로운 유저는 인기 게시글을 추천합니다.

## candidate selection
- like, comment, save 등 다양한 engagement들에 대한 확률값을 아래와 예시처럼 섞어서 사용합니다.
  - `Value(Post) = (probability_like)^weight_like * (1- probability_not_interested)^weight_see_less`
  - 이때 weight는 offine replay user session, online bayesian optimization을 사용합니다.
- 모델은 point-wise classification model, list-wise session based model을 사용합니다.
  - point-wise classification model: MTML(Multi Task Multi Label Sparse Neural Nets), GBDT
  - list-wise session based model: LambdaRank
- 이 과정에서 사용한 feature들은 다음과 같습니다.
  - Engagement features
  - Author-Viewer Interaction based features
  - Counters or trend based features for author and media
  - Content quality based features
  - Image or video understanding based features
  - Knowledge based features
  - Derived functional features
  - Content understanding based features
  - User embeddings
  - Content aggregation embeddings
  - Content taxonomy based features

## feels like home
- 먼저 home피드와 비슷하게 하기 위해 다양한 candidate들중에서 home피드에서 구한 것들이 우선수위가 높도록 합니다.
- candidate selection에서 모델링을 진행할때 전체적인 분포가 home피드 source들과 너무 멀어지지 않도록 합니다.
- home피드와 비슷하게 freshness, time sensitivity를 고려합니다.
- 추천되는 media의 종류도 home피드와 비슷하게 합니다.
- 마지막으로 user survey와 UX 전문가들의 도움을 받아서 qualitative한 guidance를 만들어가고 전략을 계속 수정합니다.