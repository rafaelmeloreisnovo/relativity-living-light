# Equações (esqueleto)

## 1) Expansão
Modelo base (ΛCDM + termo efetivo de feedback):
\[
H^2(z)=H_0^2\Big[\Omega_m(1+z)^3+\Omega_r(1+z)^4+\Omega_\Lambda+\Omega_f(z)\Big]
\]

Onde \(\Omega_f(z)\) representa um termo efetivo associado a processos energéticos (ex.: feedback AGN) ou parametrizações fenomenológicas.

## 2) Crescimento estrutural (forma prática)
Para crescimento linear, uma forma útil é integrar a equação para o fator de crescimento \(D(a)\) ou aproximar:
\[
f(z) \equiv \frac{d\ln D}{d\ln a} \approx \Omega_m(z)^\gamma
\]
e então construir \(f\sigma_8(z)\).

No pipeline aqui:
- você pode escolher ΛCDM puro (\(\Omega_f=0\))
- ou ligar um termo de supressão via `feedback_agn.py` que afeta \(\sigma_8\) efetivo (fenomenológico)

## 3) Estatística
\[
\chi^2 = \sum_i \left(\frac{x_i^{obs}-x_i^{mod}}{\sigma_i}\right)^2
\]
\[
AIC = \chi^2 + 2k
\quad\quad
BIC = \chi^2 + k\ln N
\]

## Índice canônico de fórmulas
- Referência oficial: [`docs/FORMULAS_CANONICAS_INDEX.md`](../FORMULAS_CANONICAS_INDEX.md).
