- conventional popularity bias
    - 추천시스템이 popular items를 loss popular items에 비해 높은 rating을 주는 것
- 이 논문은 이전 연구와 다르게 conditioned on user preferences한 상태에서 item popularity를 연구
- bias정도를 판단하기 위해 논문에서 2가지 metric을 제시
- 이론적으로 CF에서 bias가 있는지 증명 (skip함)
- 그렇다면 debiasing하는 방법? 2가지 제시
    - Popularity compensation (post processing)
        - predicted score, user & item 별 특징을 이용하여 re-scoring하는 방법
    - Regularization (in-processing)
        - 일반적인 loss function에 regularization term을 추가
        - 인기있는 item에 대한 predicted score가 높으면 패널티를 주는 방식
- 실제로 데이터셋에 효과가 있는 것을 보여줌 (MF, BPR 알고리즘)
- 추후에 딥러닝에도 적용하는 것이 계획이라고 함