### Learning from Implicit data

- user-item interaction matrix: 0,1로 user-item이 interaction이 있는지 여부를 표시
- interaction function을 정의해서 user-item간의 interaction이 있는지 확률을 예측하는 문제를 주로 푼다.
- 2가지 objective function이 가장 많이 사용된다.
  - Point-wise: 실제값과 예측값 차이를 최소화
  - Pair-wise: BPR에서 사용한 것처럼 1이 0보다 더 높은 순위를 갖도록 함

### Matrix Fatorization

기존 MF의 한계점을 지적한다. (0,1로 표현된 matrix를 이용할 때)

- MF estimates an interaction $y_{ui}$ as inner product

$$\hat{y}_{ui} = f(u,i|p_u, q_i) = p_u^Tq_i = \sum_{k=1}^K p_{uk}q_{ik}$$

- MF는 user, iterm을 동일한 latent space에 mapping한다. (inner product하니까)
- user-item의 관계를 low-dim으로 표현하면서 부정확한 유사관계를 만들 수 있다.
- 하지만 그렇다고 dim을 키우면 overfitting이 발생한다.

그렇다면 non-linear한 NN을 통해서 복잡한 관계(latent space)를 더 잘 표현해보자.

### NCF

- GMF + MLP
- Point-wise 방법, binary classificaion 이라고 할 수 있다.
- [논문](https://arxiv.org/pdf/1708.05031.pdf)에서 Figure3

$$\psi^{GMF} = p_u^G \odot q_i^G$$

$$\psi^{MLP} = a_L (W_L^T(a_{L-1}(...a_2(W_2^T\begin{bmatrix}p_u^M\\q_i^M\\ \end{bmatrix}+b_2)...) + b_{L-1}) + b_L)$$

$$\hat{y}_{ui} = \sigma(h^t \begin{bmatrix}\psi^{GMF}\\ \psi^{MLP} \\ \end{bmatrix})$$

#### Experiments

- 평가방법
  - 각 user마다 interaction을 leave-one-out 방법으로 train, test set을 만들어서 test set을 평가
  - 근데 시간이 너무 걸려서 아이템 100개만 선정
- MLP layer가 깊어질수록 성능이 올랐다 -> 딥모델이 효과있다
