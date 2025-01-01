# Credit Card Fraud Detection
- Anonymized credit card transactions labeled as fraudulent or genuine
- [Kaggle Link](https://www.kaggle.com/mlg-ulb/creditcardfraud)

## Validation Result

|method|precision|recall|F1|ROCAUC|PRAUC(average precision socre)|
|------|---|---|---|---|---|
|Baseline(LogisticReg)|0.83|0.65|0.73|0.96|0.74|
|smote+LogisticReg|0.68|0.84|0.75|0.96|0.74|
|simple PCA version|0.27|0.27|.|.|.|

- smote
  - smote를 train data에 적용을 하니까 precision은 떨어졌다. 즉, minority라고 예측했지만 실제로는 majority에 속하는 observation의 수가 늘어났다는 것이다.
  - 위의 결과는 394개였던 minority를 5000개로 oversampling한 결과이다.
  - oversampling의 갯수도 결과에 상당한 영향을 미치는 것 같다.
- simple PCA version
  - label을 사용하지 않아서 성능은 많이 떨어진다.

## Related Paper
- Calibrating Probability with Undersampling for Unbalanced Classification (2015)
  - [`Paper Link`](https://www.researchgate.net/publication/283349138_Calibrating_Probability_with_Undersampling_for_Unbalanced_Classification) | `My summary` | `My code`
- Learned lessons in credit card fraud detection from a practitioner perspective (2014)
  - [`Paper Link`](https://www.researchgate.net/publication/260837261_Learned_lessons_in_credit_card_fraud_detection_from_a_practitioner_perspective) | `My summary` | `My code`