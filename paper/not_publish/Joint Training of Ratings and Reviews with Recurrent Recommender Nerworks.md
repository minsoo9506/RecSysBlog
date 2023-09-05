- ratings, reviews, temporal patterns 를 이용하여 모델링

# 모델

[논문 Figure 1](https://openreview.net/pdf?id=Bkv9FyHYx)에서 그림으로 모델을 한눈에 파악할 수 있다.

## Dynamic User and Movie State

- user(item)-state RNN에서 각 step 마다 $y_t = W_{embed}[x_t, 1_{new}, \tau_t, \tau_{t-1}]$를 input으로 받는다.
  - $x_t$: rating vector, $j$ th element는 user가 time $t$에 $j$ item에게 준 rating이고 나머지는 0
  - $1_{new}$: indicator for new users(items)
  - $\tau_t$: wall-clock time
- 그리고 state는 $u_t = LSTM(u_{t-1}, y_t)$로 update한다.

## Rating Emissions

- time-varying vector $u_{it},m_{jt}$를 보완하기 위해 staionary한 $u_i, m_j$를 사용한다.
  - 이는 유저의 long-term preference, item의 카테고리 등이다
- rating은:

$$r_{ij} = f(u_{it},m_{jt},u_i,m_j) =  \langle \tilde{u}_{it}, \tilde{m}_{jt} \rangle + \langle u_i,m_j \rangle$$

$$\tilde{u}_{it} = W_{user} u_{it} + b_{user},\;\; \tilde{m}_{jt} = W_{item} m_{jt} + b_{item}$$

## Review Text Model

- character-level LSTM 모델을 사용했다.
- rating model에서늬 latent state를 사용한다. (joint)

$$x_{joint, ij} = \phi (W_{joint} [u_{it}, m_{jt}, u_i, m_j] + b_{joint})$$
$$\tilde{x}_{ij,k} = [x_{O_{ij,k}}, x_{joint, ij}]$$

- $O_{ij,k}$: character at position $k$ for the review given by user $i$ to item $j$ -> $x_{O_{ij,k}}$: embedding of the character
- 따라서 character index $k=1,2,...$ 마다

$$h_{ij,k} = LSTM(h_{ij,k-1}, \tilde{x}_{ij,k}),\;\; \hat{o}_{ij,k}=softmax(W_{out} h_{ij,k} + b_{out})$$
