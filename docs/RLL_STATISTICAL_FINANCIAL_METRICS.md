# RLL Statistical and Financial Metrics

## Métricas de retorno

\[
r_t = \ln\left(\frac{P_t}{P_{t-1}}\right)
\]

\[
R_t = \frac{P_t-P_{t-1}}{P_{t-1}}
\]

## Estatística descritiva e dependência

\[
\bar{x} = \frac{1}{n}\sum_{i=1}^{n}x_i
\]

\[
\sigma^2 = \frac{1}{n-1}\sum_{i=1}^{n}(x_i-\bar{x})^2
\]

\[
\sigma = \sqrt{\sigma^2}
\]

\[
\operatorname{cov}(X,Y)=\frac{1}{n-1}\sum_{i=1}^{n}(x_i-\bar{x})(y_i-\bar{y})
\]

\[
\rho_{X,Y}=\frac{\operatorname{cov}(X,Y)}{\sigma_X\sigma_Y}
\]

\[
\rho_k = \frac{\sum_{t=k+1}^{n}(x_t-\bar{x})(x_{t-k}-\bar{x})}{\sum_{t=1}^{n}(x_t-\bar{x})^2}
\]

## Suavização

\[
SMA_t = \frac{1}{w}\sum_{i=0}^{w-1}P_{t-i}
\]

\[
EMA_t = \alpha P_t + (1-\alpha)EMA_{t-1}
\]

## Métricas de desempenho ajustado ao risco

\[
Sharpe = \frac{E[R_p-R_f]}{\sigma_p}
\]

\[
Sortino = \frac{E[R_p-R_f]}{\sigma_d}
\]

\[
Treynor = \frac{E[R_p-R_f]}{\beta_p}
\]

\[
Calmar = \frac{R_{\text{anual}}}{|MDD|}
\]

## Exposição ao mercado

\[
\beta = \frac{\operatorname{cov}(R_p,R_m)}{\operatorname{var}(R_m)}
\]

\[
\alpha_p = R_p - [R_f + \beta_p(R_m-R_f)]
\]

\[
R^2 = 1 - \frac{SS_{res}}{SS_{tot}}
\]

## Risco de perda e resultado líquido

\[
MDD = \max_t \left(\frac{P_{\text{peak},t}-P_t}{P_{\text{peak},t}}\right)
\]

\[
PNL_{\text{gross}} = \sum_{t=1}^{n} q_t(P_{sell,t}-P_{buy,t})
\]

\[
PNL_{\text{net}} = PNL_{\text{gross}} - fees - taxes - slippage
\]

## Claim boundary

Essas métricas podem avaliar risco, retorno, estabilidade e desempenho histórico. Não garantem previsão de mercado nem recomendação financeira.
