# [Dacon] 신용카드 연체 예측
- 3 classes, imbalance를 경험할 수 있는 competition
- 순위, 수상이 목적이 아니기 때문에 FE은 진행하지 않았다.
- 논문, 방법론을 실제 데이터에 적용해보는 것을 목표로 했다.

### Baseline (Logistic regression)
- 3 class에서 1개의 class가 다수를 차지하기 때문에 다른 class를 분류하는데 어려움이 있다.

### OVO + Oversampling
- `logistic`을 사용하여 OVO하면서 `SMOTE`를 사용하였다.
- 그러면 test data 하나당 확률이 두 class씩 묶어서 각각 2개씩 존재
- 이를 평균내었더니 오히려 더 logloss가 커졌다.
- 아마 major data라고 예측하는 경우가 더 적어져서 그런 것 같다 + 확률를 합산하는 과정에서 문제
- `RF`의 경우 `logistic`보다 성능이 더 떨어졌다.
- 추후 보완 방법
  - OVO와 단일 model의 Eensemble
  - `SMOTE`이외의 sampling 기법 적용

### OVO + Predict Probability Calibration
- `lgb` with sampling weight
  - imbalance하기 때문에 `lgb`에 내장된 기능인 sample weight를 이용하였다.
  - cost-sensitive하게 model을 학습시키는 것이다.
  - 이 때, weight를 어떻게 할지는 hyperparameter이다.
- probability calibration
  - Tree model의 경우 0,1과 멀어지게 확률을 예측하는 경향이 있다고 한다. 이를 calibration해보았다.
  - `sklearn`에 있는 `isotonic regression`을 이용했다.
  - `isotonic regression`을 fit, predict 할 때 주의 : target을 (0,1)로 바꾸고 input, output에 해당하는 확률값은 target=1 

### MetaCost
- `MetaCost` 방법론 적용
- 적용하는 방향에 따라 결과가 천차만별이기 때문에 (relabelling하니까) 주의
- 기존의 data와 어떤 부분에서 달라졌는지 post-analysis가 필요해 보인다.