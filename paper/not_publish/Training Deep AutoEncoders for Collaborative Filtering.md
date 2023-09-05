- AE를 통해서 rating이 없는 부분을 채우는 것
- input data는 $x\in R^n$이고 $n$는 item의 수이다. 상당히 sparse하고 AE를 거지면 missing value들이 채워진다.

# 모델

## Loss function

- $m_i$: mask function s.t. $m_i=1$ if $r_i \neq 0$ else $m_i=0$

$$MMSE = \frac{m_i \cdot (ri - y_i)^2}{\sum_{i=0}^{i=n}m_i}$$

즉, rating이 있는 것만 이용하여 모델을 업데이트 하는 것이다.

## Dense re-feeding

optimization iteration동안 아래의 과정을 반복한다. (3,4번은 한번의 iteration동안 여러번 실행할 수도 있다)

1. sparse $x$으로 $f(x)$와 loss를 계산하다. (forward)
2. gradients를 계산하고 weight update를 진행한다. (backward)
3. $f(x)$를 새로운 input data로 취급하여 $f(f(x))$를 계산한다. (second forward)
4. gradients를 계산하고 weight update를 진행한다. (second backward)

# 실험결과

- hidden layer가 너무 크면 train set에 overfitting 발생한다.
- 그래서 dropout으로 성능 향상을 이뤄냈다.
- dense re-feeding해보니 성능이 더 좋았다.
