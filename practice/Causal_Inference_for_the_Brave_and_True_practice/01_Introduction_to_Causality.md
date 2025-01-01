- $T_i$: the treatment for unit $i$

$$T_i=\begin{cases}
1 \ \text{if unit i received the treatment}\\
0 \ \text{otherwise}\\
\end{cases}$$

- $Y_i$: the observed outcome variable for unit $i$

- fundamental problem of causal inference is
  - that **we can never observe the same unit with and without treatment**

- potential outcome:
  - what would have happened in the case some treatment was taken
  - We sometimes call the potential outcome that happened, *factual*, and the one that didn’t happen, *counterfactual*

- $Y_{1i} - Y_{0i}$: individual treatment effect
  - we can never know the individual treatment effect because we only observe one of the potential outcomes

- $ATE=E[Y_1 - Y_0]$: average treatment effect
- $ATT=E[Y_1 - Y_0 | T=1]$: average treatment effect on the treated

# Bias
- Association
$$\begin{align}
E[Y|T=1] - E[Y|T=0] &= E[Y_1|T=1] - E[Y_0|T=0]\\
&= E[Y_1|T=1] - E[Y_0|T=0] + E[Y_0|T=1] - E[Y_0|T=1]\\
& = \underbrace{E[Y_1 - Y_0|T=1]}_{ATT} + \underbrace{\{ E[Y_0|T=1] - E[Y_0|T=0] \}}_{BIAS}
\end{align}$$

treatment , control group이 comparable (treatment이외에 다른 부분에서 동등) 하다면? association이 causation이 될 수도 있다. comparable하면 bias가 0이 된다.

$$E[Y|T=1] - E[Y|T=0] = E[Y_1 - Y_0|T=1] = ATT$$

$$\begin{align}
E[Y_1 - Y_0|T=1] &= E[Y_1|T=1] - E[Y_0|T=1] \\
&= E[Y_1|T=1] - E[Y_0|T=0] \\
&= E[Y|T=1] - E[Y|T=0] = ATE
\end{align}$$