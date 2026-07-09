# Executive Summary — RLL audit gate 2026-07-01

Status consolidado: **NÃO APROVADO / FALSEAMENTO OPERACIONAL NESTA RODADA**.

## Resultado principal

O gate prioritário solicitado foi executado antes da microfísica e da estabilidade. Com dados reais materializados no repositório, o comparativo retornou:

- ΛCDM: χ² = `216.5765289143`, AIC = `220.5765289143`, BIC = `224.0989291457`.
- RLL: χ² = `238.4928708818`, AIC = `248.4928708818`, BIC = `257.2988714603`.
- ΔAIC (`RLL - ΛCDM`) = `+27.9163419675`.
- ΔBIC (`RLL - ΛCDM`) = `+33.1999423146`.

Como os deltas são positivos, o RLL perde no gate atual. A instrução de parada foi aplicada: não foram fabricadas chains MCMC, corner plots, curvas `V(phi)` nem provas globais de estabilidade.

## Não-conformidades tratadas sem mascarar erro

1. **Evidência numérica final:** documentada como resultado negativo no apêndice estatístico.
2. **Microfísica:** contrato algébrico preservado, mas não promovido por falta de suporte estatístico.
3. **Perturbações:** contrato de estabilidade preservado, mas não promovido sem domínio posterior aceito.
4. **Proveniência:** hashes e URLs disponíveis foram consolidados; lacunas ficam marcadas como `[VAZIO]`.

## Decisão editorial

Não submeter como “aprovado com louvor” a PRD/JCAP. O caminho correto é preparar uma nota de resultado negativo/limite superior ou repetir o ajuste com DESI DR2, Pantheon+ e Planck completos, covariâncias oficiais e baseline w0waCDM/CPL estritamente pareado.
