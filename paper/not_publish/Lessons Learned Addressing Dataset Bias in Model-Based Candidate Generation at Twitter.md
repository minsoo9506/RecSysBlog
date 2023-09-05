- rank를 내기전에 ranker에 넣을 아이템 후보군을 만드는 과정에 있어서 bias를 다루는 논문
- 근데 해결책을 딱 제시하는 것은 아니고 insight, practical suggestion 정도

## Problem

- 논문에서는 후보군을 3가지로 구분
  - relevant and engaging candidate
  - relevant but not engaging candidate
  - extremely irrelevant cadidate
- 그리고 candidate generation task는 2가지로 이루어져 있다고 할 수 있다.
  - extremely irrelevant cadidate가 포함되는 것을 피하기
  - 최대한 relevant and engaging candidate가 포함되도록 하기

### Sampled Negatives

- explicit feedback sample을 positive로 하고 random sample을 negative로 해서 모델을 훈련시키면 relevant content와 completely irrelevant content는 잘 구분하지만 더 engaging한 아이템은 잘 구분하기 어렵다. 이런 문제가 심해지수록 ranker 모델이 더 잘 만들어져야한다.

### Demonstration of Bias on MovieLens

- Movielens 데이터를 통해서 추천모델을 만들고 rank가 높은 데이터를 이용하여 다음 추천모델을 만들어서 성능 평가를 진행했다.
- bias가 심해질수록 (상위 rank를 사용할수록) full unbiased dataset에서의 성능이 떨어졌다. 즉, 성능적으로도 filter bubble이라는 문제가 발생하는 것이다.

## Experimental Setup

### Two Tower Networks

- candidate generation 모델에 대한 설명

## Techniques

### Sampling ratio

- negative sample의 수와 비례해서 성능이 좋아졌다고 한다.

### Deep Triplet Loss

- cross-entropy보다 성능이 좋았다고 한다.

### Popularity Correction

- negative sample을 뽑을 때, uniformly 뽑으면 unpopular한 content가 많이 뽑힌다. 그리고 mostly popular content는 positive한 경우가 많다.
- 따라서 추천모델이 너무 popular content만 생성할 수도 있다.
- 따라서 가중치를 통해서 적절하게 popular content도 negative sample에 뽑히도록 한다. 이것도 너무 심해지면 irrelevant하거나 unpopular한 content가 뽑히게 되서 문제가 될 수 있다.
