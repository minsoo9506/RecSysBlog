https://matheusfacure.github.io/python-causality-handbook/02-Randomised-Experiments.html

association과 causation을 동일하게 만들기 위한 방법 중 하나는 Randomised experiments(or Randomised Controlled Trials)이다. RCT는 treatment와 potential outcome이 독립이 되게 만든다. 결국에 이는 treat, control group들이 comparable하다는 것을 의미한다.

$$(Y_0, Y_1) \perp\!\!\!\perp T$$

그래서 이전에 생겼던 bias가 사라지게 할 수 있다. 그래서 chap01에서의 bias가 사라지고 아래처럼 ATE를 구할 수 있다.

$$E[Y|T=1] - E[Y|T=0] = E[Y_1 - Y_0]=ATE$$

하지만 RCT도 너무 적은 수라면 comparable하지 않은 경우가 발생할 수도 있다. 그리고 비용적이거나 윤리적인 문제로 인해 RCT를 하지 못하는 경우도 발생한다.