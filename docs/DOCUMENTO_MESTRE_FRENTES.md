# Documento Mestre de Frentes — Structure D

## Área 1 — Expansão de fundo H(z)
- **Hipótese:** A parametrização RLL-like em `H(z)` reduz discrepâncias de expansão em relação ao cenário base em parte da faixa observacional.
- **Observável:** Curva `H_obs` vs `H_model` e resíduos `delta_H` por redshift.
- **Métrica:** χ² global de expansão e residual médio absoluto `mean(|delta_H|)` em `0.07 ≤ z ≤ 2.34`.
- **Status:** em validação
- **Ponte com código:** `RAFAELIA_COSMO_STRUCTURE_D/rll_pipeline/cosmo.py` (`H_of_z` reexportado), `data/pipelines/structure_d/cosmo.py` (`H_of_z`, `E_LCDM`), `data/pipelines/structure_d/models.py` (`model_LCDM_Hz`, `model_RLL_like_Hz`).
- **Ponte com resultados:** `results/two_radiation_model_preview.csv` (colunas `H_obs`, `H_model`, `delta_H`), `results/RLL_chi2_results.csv` (χ²/AIC/BIC por modelo).

## Área 2 — Crescimento estrutural fσ8(z)
- **Hipótese:** O termo de supressão por feedback melhora a coerência de `fσ8` em altos redshifts sem degradar excessivamente o ajuste global.
- **Observável:** Diferença entre `fs8_baseline` e `fs8_feedback` com `delta_fs8_pct` ao longo de z.
- **Métrica:** Erro relativo percentual médio em `delta_fs8_pct` e faixa de z com variação controlada (`|delta_fs8_pct| < 3%`).
- **Status:** em validação
- **Ponte com código:** `RAFAELIA_COSMO_STRUCTURE_D/rll_pipeline/growth.py` (`f_sigma8_proxy` reexportado), `data/pipelines/structure_d/growth.py` (`f_sigma8_proxy`), `data/pipelines/structure_d/models.py` (`model_LCDM_fs8`, `model_RLL_like_fs8`).
- **Ponte com resultados:** `results/two_radiation_model_preview.csv` (colunas `fs8_baseline`, `fs8_feedback`, `delta_fs8_pct`), `results/structure_d/README.md` (descrição de artefatos do pipeline).

## Área 3 — Seleção de modelo estatístico
- **Hipótese:** Mesmo com Δχ² pequeno, penalização de complexidade (AIC/BIC) pode indicar regime em que ΛCDM permanece preferível.
- **Observável:** Tabela comparativa `Model`, `chi2`, `AIC`, `BIC`, `chi2_dof`, `verdict`.
- **Métrica:** Δχ², ΔAIC e ΔBIC entre linhas `RLL` e `LCDM` (com rastreio explícito do sinal de vantagem).
- **Status:** validada
- **Ponte com código:** `RAFAELIA_COSMO_STRUCTURE_D/rll_pipeline/likelihood.py` (`chi2`, `aic`, `bic` reexportados), `data/pipelines/structure_d/likelihood.py` (`chi2`, `aic`, `bic`, `evaluate_model`), `data/pipelines/structure_d/models.py` (funções de predição usadas na avaliação).
- **Ponte com resultados:** `results/RLL_chi2_results.csv` (comparação objetiva entre modelos), `results/structure_d/README.md` (referência ao `model_comparison.csv`).

## Área 4 — Robustez com covariância completa
- **Hipótese:** Uso de covariância cheia, quando disponível, muda a superfície de likelihood de forma mensurável frente ao fallback diagonal.
- **Observável:** Modo de covariância por bloco observacional (`full` vs `diagonal_fallback`).
- **Métrica:** Fração de blocos com covariância cheia e variação de χ² ao alternar estratégia de matriz de covariância.
- **Status:** em validação
- **Ponte com código:** `data/pipelines/structure_d/likelihood.py` (`chi2_with_covariance`, `_validated_covariance_matrix`), `RAFAELIA_COSMO_STRUCTURE_D/rll_pipeline/likelihood.py` (reexport), `data/pipelines/structure_d/models.py` (vetores previstos comparados na likelihood).
- **Ponte com resultados:** `results/structure_d/covariance_usage.csv`, `results/structure_d/README.md` (documenta `covariance_usage.csv`).

## Área 5 — Consistência de parâmetros cosmológicos
- **Hipótese:** Pequenas variações em `H0`, `Om`, `Ol` e termos extras (`Os0`, `zt`, `wt`) preservam estabilidade numérica no intervalo observado.
- **Observável:** Diferença paramétrica entre linhas de modelos e impacto em `chi2_dof`.
- **Métrica:** Desvio relativo dos parâmetros-chave (`|Δp|/p_LCDM`) e limiar de estabilidade de `chi2_dof`.
- **Status:** planejada
- **Ponte com código:** `data/pipelines/structure_d/models.py` (`model_LCDM_Hz`, `model_RLL_like_Hz`, `model_LCDM_fs8`, `model_RLL_like_fs8`), `data/pipelines/structure_d/cosmo.py` (`Omega_m_z`), `RAFAELIA_COSMO_STRUCTURE_D/rll_pipeline/cosmo.py` (ponte de compatibilidade).
- **Ponte com resultados:** `results/RLL_chi2_results.csv` (parâmetros + `chi2_dof`), `results/two_radiation_model_preview.csv` (sensibilidade em z).

## Área 6 — Janela de redshift e cobertura observacional
- **Hipótese:** O desempenho relativo entre modelos depende da janela em z, com comportamento distinto em baixo e alto redshift.
- **Observável:** Séries por z para `delta_H` e `delta_fs8_pct`.
- **Métrica:** Estatísticas segmentadas por faixa (`z<0.5`, `0.5≤z<1.5`, `z≥1.5`) com residual médio e erro relativo médio.
- **Status:** planejada
- **Ponte com código:** `data/pipelines/structure_d/cosmo.py` (`H_of_z`), `data/pipelines/structure_d/growth.py` (`f_sigma8_proxy`), `RAFAELIA_COSMO_STRUCTURE_D/rll_pipeline/growth.py` (reexport), `data/pipelines/structure_d/models.py` (geração de séries comparáveis).
- **Ponte com resultados:** `results/two_radiation_model_preview.csv` (amostragem em z de 0.07 a 2.34), `results/RLL_chi2_results.csv` (`N_obs` para rastreio da cobertura).

## Área 7 — Qualidade de dados e validações de entrada
- **Hipótese:** Validações de finitude/positividade em incertezas e covariâncias reduzem risco de inferência espúria.
- **Observável:** Erros explícitos de validação para `sigma` e matriz de covariância fora do padrão.
- **Métrica:** Taxa de execução sem exceção em rodadas de pipeline e número de falhas de validação por lote.
- **Status:** validada
- **Ponte com código:** `data/pipelines/structure_d/likelihood.py` (`_validated_sigma_array`, `_validated_covariance_matrix`, `load_csv`), `RAFAELIA_COSMO_STRUCTURE_D/rll_pipeline/likelihood.py` (reexport), `data/pipelines/structure_d/models.py` (consumo de entradas validadas).
- **Ponte com resultados:** `results/structure_d/README.md` (saídas esperadas por corrida), `results/structure_d/covariance_usage.csv` (evidência de estratégia de covariância aplicada).

## Área 8 — Reprodutibilidade de pipeline e comparação de corridas
- **Hipótese:** Saídas versionáveis por CSV permitem rastrear evolução de ajustes sem ambiguidade de interpretação.
- **Observável:** Conjunto fixo de artefatos (`RLL_chi2_results.csv`, `two_radiation_model_preview.csv`, `covariance_usage.csv`) por execução.
- **Métrica:** Presença dos artefatos obrigatórios e consistência de colunas-chave entre corridas.
- **Status:** em validação
- **Ponte com código:** `data/pipelines/structure_d/likelihood.py` (`evaluate_model`), `data/pipelines/structure_d/run_all.py` (orquestração), `RAFAELIA_COSMO_STRUCTURE_D/rll_pipeline/likelihood.py` (ponte), `data/pipelines/structure_d/models.py` (fornece predições usadas nas tabelas).
- **Ponte com resultados:** `results/RLL_chi2_results.csv`, `results/two_radiation_model_preview.csv`, `results/structure_d/covariance_usage.csv`, `results/structure_d/README.md`.

## Rastreabilidade

| Área | Módulo(s) | Resultado(s) | Status |
|---|---|---|---|
| Expansão de fundo H(z) | `rll_pipeline/cosmo.py`; `structure_d/cosmo.py`; `structure_d/models.py` | `results/two_radiation_model_preview.csv`; `results/RLL_chi2_results.csv` | em validação |
| Crescimento estrutural fσ8(z) | `rll_pipeline/growth.py`; `structure_d/growth.py`; `structure_d/models.py` | `results/two_radiation_model_preview.csv`; `results/structure_d/README.md` | em validação |
| Seleção de modelo estatístico | `rll_pipeline/likelihood.py`; `structure_d/likelihood.py`; `structure_d/models.py` | `results/RLL_chi2_results.csv`; `results/structure_d/README.md` | validada |
| Robustez com covariância completa | `structure_d/likelihood.py`; `rll_pipeline/likelihood.py`; `structure_d/models.py` | `results/structure_d/covariance_usage.csv`; `results/structure_d/README.md` | em validação |
| Consistência de parâmetros cosmológicos | `structure_d/models.py`; `structure_d/cosmo.py`; `rll_pipeline/cosmo.py` | `results/RLL_chi2_results.csv`; `results/two_radiation_model_preview.csv` | planejada |
| Janela de redshift e cobertura observacional | `structure_d/cosmo.py`; `structure_d/growth.py`; `rll_pipeline/growth.py`; `structure_d/models.py` | `results/two_radiation_model_preview.csv`; `results/RLL_chi2_results.csv` | planejada |
| Qualidade de dados e validações de entrada | `structure_d/likelihood.py`; `rll_pipeline/likelihood.py`; `structure_d/models.py` | `results/structure_d/README.md`; `results/structure_d/covariance_usage.csv` | validada |
| Reprodutibilidade de pipeline e comparação de corridas | `structure_d/likelihood.py`; `structure_d/run_all.py`; `rll_pipeline/likelihood.py`; `structure_d/models.py` | `results/RLL_chi2_results.csv`; `results/two_radiation_model_preview.csv`; `results/structure_d/covariance_usage.csv`; `results/structure_d/README.md` | em validação |
