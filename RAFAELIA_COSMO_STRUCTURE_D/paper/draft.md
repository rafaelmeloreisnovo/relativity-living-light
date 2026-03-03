# Draft (paper skeleton)

## Abstract
(…)

## Introduction
- ΛCDM successes
- H0/S8 tensions (context)
- Role of baryonic/AGN feedback
- Proposed effective extension (RLL_like + AGN)

## Methods
- H(z), fσ8 datasets
- Likelihood, χ², AIC, BIC
- Parameter counting

## Results
- Table: χ²/AIC/BIC
- Sensitivity to α, z_peak, width

### External validation

- **Objetivo:** validar o modelo em dois níveis explícitos e não intercambiáveis:
  1) **convergência qualitativa** (mesma direção física);
  2) **suporte quantitativo** (compatibilidade estatística com métricas comparáveis).
- **Ponte quantitativa com DESI/CPL:** incluir mapeamento explícito \(w_{RLL}(a)\rightarrow(w_0,w_a)\) usando expansão local em \(a=1\):
  - \(w_0=-f_0\)
  - \(w_a=-\left.dw/da\right|_{a=1}=-f_0(1-f_0)/w_t\)
- **Métricas comparáveis obrigatórias:** \(\chi^2_{\min}\), \(\Delta\)AIC, \(\Delta\)BIC, PPC e distância em sigma para \((w_0,w_a)\).
- **Critérios de rejeição objetivos (falsificação):**
  - \(\Delta\)AIC>10 e \(\Delta\)BIC>10;
  - p-valor global do ajuste < 0.01;
  - inconsistência >3σ no plano \((w_0,w_a)\) contra contornos externos;
  - viés residual \(|\langle r/\sigma\rangle|>2\) em ≥2 observáveis independentes.
- **Tabela de previsões falsificáveis:** incluir tabela por observável/dataset futuro (DESI DR3, Euclid, Roman, SKA, CMB-S4) com coluna “critério de falha”.
- **Referência de apoio:** alinhar esta subseção com `docs/COMPARACAO_DESI_2025.md` (seção “External validation”).

## Discussion
- Interpretation
- Degeneracies / priors / parameter reduction
- Next datasets: SN, lensing, CMB full

## Conclusion
(…)
