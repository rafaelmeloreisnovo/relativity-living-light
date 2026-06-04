# Dark Matter / RLL — Mapa de Links Documentais

Este documento liga o arquivo de raiz [` darkmatter.md`](../%20darkmatter.md) aos pontos técnicos do repositório que precisam permanecer rastreáveis em `docs`, dados reais, workflows e pipelines.

## Arquivo-fonte

- [` darkmatter.md`](../%20darkmatter.md) — pacote de validação cosmológica real para RLL, contendo dados, fórmulas, DESI DR2 BAO, Planck, cronômetros cósmicos, fσ8, mapeamento logístico para `w_eff(a)` e critérios `chi2/AIC/BIC/Bayes`.

## Pontos-link principais

| Ponto | Significado | Link documental / técnico |
|---|---|---|
| `r_d` | Horizonte sonoro de arrasto, pivô BAO/CMB usado para converter distância em `D/rd`. | [` darkmatter.md`](../%20darkmatter.md#1-horizonte-sonoro-de-arrasto-r_d) |
| `DESI_DR2_BAO` | 13 observáveis BAO: BGS, LRG, ELG, QSO, Lyα; base para validação com dados reais. | [`darkmatter DESI`](../%20darkmatter.md#2-desi-dr2-bao--13-observ%C3%A1veis-e-correla%C3%A7%C3%B5es) · [`data/real/desi_dr2_bao_measurements.csv`](../data/real/desi_dr2_bao_measurements.csv) · [`data/real/desi_dr2_bao_covariance.csv`](../data/real/desi_dr2_bao_covariance.csv) |
| `w0_wa` | Linguagem acadêmica de energia escura dinâmica para comparação com DESI/CMB/SN. | [`darkmatter w0-wa`](../%20darkmatter.md#3-w0wa-desi-dr2-modelo-w0wacdm) |
| `H_z` | Cronômetros cósmicos; mede expansão cósmica sem supernovas. | [`darkmatter cronômetros`](../%20darkmatter.md#4-cron%C3%B4metros-c%C3%B3smicos-hz) |
| `CMB_DISTANCE_PRIORS` | Priors Planck 2018: `R`, `lA`, `obh2`, `ns`, `z*`. | [`darkmatter CMB`](../%20darkmatter.md#5-distance-priors-cmb-planck-2018) |
| `fsigma8` | Crescimento de estrutura, ligação observacional com matéria escura e gravitação efetiva. | [`darkmatter fσ8`](../%20darkmatter.md#6-f%CF%838-crescimento-de-estrutura) |
| `RLL_w_eff` | Tradução do setor logístico/superposição RLL para equação de estado efetiva. | [`darkmatter w_eff`](../%20darkmatter.md#7-tradu%C3%A7%C3%A3o-wz%E2%86%94cpl-e-mapeamento-log%C3%ADstico%E2%86%92w_eff) |
| `MODEL_COMPARISON` | Régua de prova: `chi2`, `AIC`, `AICc`, `BIC`, Bayes/Jeffreys. | [`darkmatter comparação`](../%20darkmatter.md#8-compara%C3%A7%C3%A3o-de-modelos) · [`data/results/desi_dr2_bao_model_comparison.json`](../data/results/desi_dr2_bao_model_comparison.json) |
| `DESI_ZML` | Saída ZML para leitura operacional dos pontos DESI e comparação. | [`data/results/desi_dr2_bao_zml.yml`](../data/results/desi_dr2_bao_zml.yml) · [`scripts/compute_desi_dr2_bao_zml.py`](../scripts/compute_desi_dr2_bao_zml.py) |
| `REAL_ORCHESTRATOR_IML` | Amarra IML, Doc Inventory, Real Data Complete, Structure-D, Pantheon e DESI. | [`data/real_sources/rll_real_orchestrator_inventory.iml.yml`](../data/real_sources/rll_real_orchestrator_inventory.iml.yml) |
| `PANTHEON_IML` | Contrato IML de validação Pantheon+ / SH0ES. | [`data/real_sources/rll_pantheon_real_validation.iml.yml`](../data/real_sources/rll_pantheon_real_validation.iml.yml) |
| `DOC_INVENTORY` | Inventário documental e numérico do repositório. | [`docs/DOCUMENTATION_FULL_INVENTORY.md`](DOCUMENTATION_FULL_INVENTORY.md) · [`docs/REAL_NUMBERS_REPORT.md`](REAL_NUMBERS_REPORT.md) · [`docs/YML_WORKFLOWS_INDEX.md`](YML_WORKFLOWS_INDEX.md) |
| `WORKFLOW_MANUAL` | Orquestrador manual de rotas RLL/IML/real_validation/validation_paths. | [`START_MANUAL_HERE.yml`](../.github/workflows/START_MANUAL_HERE.yml) |
| `REAL_DATA_COMPLETE` | Workflow completo para materializar, auditar e validar dados reais. | [`real-data-complete-execution.yml`](../.github/workflows/real-data-complete-execution.yml) |
| `IML_ARTIFACT` | Workflow IML para gerar artefato operacional a partir de `data/iml/daise_input.json`. | [`iml_artifact.yml`](../.github/workflows/iml_artifact.yml) · [`data/iml/daise_input.json`](../data/iml/daise_input.json) |

## Sete direções de ligação documental

1. **Cosmologia teórica** — `RLL_w_eff`, `w0_wa`, `r_d`.
2. **Observação cosmológica** — `DESI_DR2_BAO`, `H_z`, `CMB_DISTANCE_PRIORS`, `fsigma8`.
3. **Matéria escura / crescimento de estrutura** — `fsigma8`, BAO, CMB e crescimento.
4. **Engenharia de validação** — `MODEL_COMPARISON`, `DESI_ZML`, `Structure-D` e `Real Data Complete`.
5. **Reprodutibilidade GitHub** — workflows, checksums, inventário e artifacts.
6. **Autoria / anterioridade** — separar fórmulas antigas, hash/timestamp e observação posterior em dossiê próprio.
7. **Mercado / aplicação** — software científico, pipeline de auditoria, educação técnica e proposta de P&D.

## Próximo artefato recomendado

Criar `docs/PRIOR_PREDICTIONS_VS_DESI.md` e `data/results/prior_predictions_vs_observations.json` para registrar:

- fórmula original;
- arquivo/commit/timestamp anterior;
- valor previsto;
- observação DESI/Pantheon posterior;
- erro absoluto;
- erro relativo;
- pull em sigma;
- conclusão sem fake-fill.

## Regra de ligação

Todo ponto técnico novo deve ter pelo menos três links:

1. link para o arquivo conceitual em `docs`;
2. link para dado real em `data/real` ou resultado em `data/results`;
3. link para workflow/script que reproduz ou valida o ponto.
