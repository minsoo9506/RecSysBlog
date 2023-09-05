- personalized ranking
  - user에게 ranked list of items를 추천하는 것
- implicit feedback
  - 주로 positive feedback이다
  - non-observed item = real negative feedback + missing values

### Problem setting

- 전체 데이터를 pairwise perference $i >_u j$로 나타낸다.
- 각 user별로 item-item matrix를 만들고 implicit feedback을 통해서 어떤 item을 더 선호하는지 +, - 를 표시한다. 둘 다 feedback이 없거나 있는 경우는 빈칸으로 남긴다.
  - 따라서 학습셋 $D_s$ 은 positive, negetive, missing value로 이루어짐

### BPR

- bayesian 접근

$$p(\theta | >_u) \propto p(>_u|\theta)p(\theta)$$

- likelihood

$$\prod_{u \in U}p(>_u|\theta) = \prod_{(u,i,j) \in U\cdot I \cdot J}p(i>_uj|\theta)^{\delta((u,i,j)\in D_s)}(1-p(i>_uj|\theta))^{\delta((u,j,i)\notin D_s)}\\=\prod_{(u,i,j)\in D_s}p(i >_u j | \theta)$$

- 따라서 $p(i >_u j | \theta)$를 어떤 모델를 통해 예측하면 된다.

$$p(i >_u j | \theta) = \sigma(\hat{x_{uij}(\theta)})$$

- 사전분포는 $p(\theta)\sim N(0, \Sigma_{\theta})$으로 한다.

그래서 완성된 optimization criterion은

$$BPR-OPT = \log p(\theta| >_u)\\=\log p(>_u\|\theta)p(\theta)\\=\log \prod \sigma(\hat{x}_{uij})p(\theta)\\=\sum \log \sigma (\hat{x}_{uij}) - \lambda_{\theta} ||\theta||^2$$

### BPR learning algorithm

- 위에서 구한 BPR-OPT를 gradient descent로 optimization한다.
- stochastic gradient-descent based on bootstrap sampling of training triples
  - 데이터 전수가 아닌 bootstrap sampling해서 데이터를 사용한다.
  - 수렴속도도 빠르다.
  - 훈련데이터의 skewness때문에 잘 수렴하지 않을 수 있는데 이를 방지한다.

$$\frac{\partial BPR-OPT}{\partial \theta} \propto \sum \frac{-e^{-\hat{x}_{uij}}}{1+e^{-\hat{x}_{uij}}} \cdot \frac{\partial}{\partial \theta} \hat{x}_{uij} - \lambda_\theta \theta $$

$$\theta \leftarrow \theta - \alpha \frac{\partial BPR-OPT}{\partial \theta}$$

- 위의 식에서 알 수 있듯이 추정치 $\hat{x}$가 differential하면 된다.
