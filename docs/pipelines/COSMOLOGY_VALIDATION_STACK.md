# COSMOLOGY VALIDATION STACK (RLL)

Status: **Parcial real em preparação** (até validação cruzada completa).

## Objetivo
Comparar RLL com \(\Lambda\)CDM e \(w_0w_a\)CDM usando blocos observacionais de expansão e crescimento.

## Conjuntos de dados
- DESI DR2 BAO.
- Pantheon+ SNe Ia.
- Planck 2018 chains.
- H(z) cosmic chronometers.
- fσ8 / crescimento de estrutura.

## Pipeline operacional
1. Ingestão padronizada e versionada dos datasets.
2. Construção de likelihoods com covariâncias consistentes.
3. Definição dos modelos: \(\Lambda\)CDM, \(w_0w_a\)CDM e RLL.
4. Ajuste por \(\chi^2\) e comparação por AIC/BIC.
5. Rodar MCMC quando possível (posteriors e degenerescências).
6. Testar estabilidade por subconjunto de dados e validação cruzada.
7. Consolidar relatório com limites, tensão entre probes e robustez.

## Métricas mínimas
- \(\chi^2\) global e por bloco (BAO, SNe, CMB, H(z), fσ8).
- AIC e BIC para comparação de modelos com penalidade de complexidade.
- Intervalos de credibilidade dos parâmetros centrais.
- Diagnóstico de convergência MCMC (quando aplicável).

## Governança de status
- Status permanece **Parcial real** até validação cruzada completa e auditoria reproduzível.
- Não declarar “validação definitiva” sem execução integral e rastreável.
- Registrar cadeia de custódia e limitações em `data/real/cosmology/README.md`.
