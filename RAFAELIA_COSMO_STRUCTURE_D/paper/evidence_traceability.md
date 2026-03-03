# Evidence Traceability — Structure D

> Escopo: registrar rastreabilidade de evidência para cada claim principal do draft.
> Regra de governança: **nenhuma nova claim entra em `paper/draft.md` sem rastreabilidade registrada aqui (fonte → transformação → artefato em `results/structure_d/`).**

## Matriz de rastreabilidade de claims

| Claim principal | Fonte de dados (CSV/JSON) | Colunas/chaves usadas | Transformação aplicada | Figura/Tabela derivada (em `results/structure_d/`) | Status |
|---|---|---|---|---|---|
| C1. Comparação de ajuste entre ΛCDM e RLL-like-AGN por χ²/AIC/BIC. | `data/inputs/structure_d/Hz.csv`, `data/inputs/structure_d/fsigma8.csv` (profile default) **ou** `data/real/Hz_data_real.csv`, `data/real/BAO_data_real.csv`, `data/real/CMB_shift_real.json` (profile real validation). | `z`, `Hz`/`H_obs`, `fs8`/`DV_over_rs`, `sigma`/`sigma_H`, `R_obs`, `la_obs`, `R_sig`, `la_sig`. | Cálculo de likelihood por observável, agregação de χ² total, penalização por número de parâmetros para AIC/BIC, e exportação de comparação entre modelos. | `results/structure_d/model_comparison.csv` (tabela principal de resultados). | **Em validação** (arquivo não presente neste snapshot). |
| C2. Evidência Bayesiana relativa entre modelos (Bayes factor e interpretação). | Posteriores geradas pelo pipeline (`results/structure_d/posterior_LCDM.csv`, `results/structure_d/posterior_RLL_like_AGN.csv`). | `log_posterior`, `log_likelihood`, `log_prior`, `weight`, `parameter_*`. | Estimativa de log-evidence por modelo, cálculo de `log_bayes_factor`/`bayes_factor`, mapeamento categórico em escala Jeffreys/Trotta. | `results/structure_d/bayes_evidence.csv`, `results/structure_d/bayes_factor_summary.csv`, `results/structure_d/bayes_factor_interpretation.csv`. | **Hipótese** para comparação numérica (posteriores/evidências não presentes); **Suportado** apenas para tabela de interpretação estática (`bayes_factor_interpretation.csv`). |
| C3. Sensibilidade dos observáveis aos parâmetros efetivos (incl. α, `z_peak`, `width`). | `data/inputs/structure_d/Hz.csv`, `data/inputs/structure_d/fsigma8.csv` (ou datasets reais via profile dedicado). | `z`, valor observado (`Hz`/`fs8`), `sigma`; parâmetros nominais e passos de perturbação. | Derivadas numéricas centrais (`dO/dp`, `dlnO/dlnp`), escore normalizado por incerteza observacional e checagem de estabilidade do passo. | `results/structure_d/rll_sensitivity_derivatives.csv`. | **Em validação** (há evidência parcial no CSV atual; cobertura explícita de α/`z_peak`/`width` deve ser checada em cada corrida). |
| C4. Mudança de regime de dominância ao longo do redshift (ΛCDM ↔ RLL-like). | Saída do modelo efetivo em malha de redshift (gerada internamente no pipeline Structure D). | `z`, `R(z)` agregado por bin (`R_mean`, `R_median`, `R_std`). | Binning em redshift (`fixed_n_bins`), classificação por limiares (`lcdm_dominant`, `balanced`, `rll_dominant`), serialização de metadados de thresholds. | `results/structure_d/rll_regime_summary.csv`, `results/structure_d/rll_regime_metadata.csv`, `results/structure_d/rll_regime_overview.png`, `results/structure_d/rll_regime_by_bin.png`. | **Em validação** (CSVs disponíveis; figuras ausentes neste snapshot). |
| C5. Robustez do uso de covariância por bloco observacional. | Mesmos datasets ativos da corrida (`datasets_config.json` + entradas CSV/JSON correspondentes). | Flags por bloco: presença de `covariance` completa vs. fallback diagonal por `sigma`. | Auditoria por bloco/modelo no ato da montagem do likelihood; exportação de trilha de decisão de covariância. | `results/structure_d/covariance_usage.csv`. | **Em validação** (arquivo existe, porém sem linhas de corrida neste snapshot). |

## Regras para inclusão de novas claims no draft

1. **Pré-requisito obrigatório:** antes de inserir claim em `RAFAELIA_COSMO_STRUCTURE_D/paper/draft.md`, registrar uma linha nesta matriz com todos os campos preenchidos.
2. **Sem evidência rastreável = sem claim no draft:**
   - se não houver artefato em `results/structure_d/`, marcar como **Hipótese** e manter fora da seção de resultados conclusivos;
   - se artefato existir mas a cadeia fonte→transformação estiver incompleta, marcar como **Em validação**.
3. **Atualização acoplada:** qualquer PR que adicione/edite claim no draft deve atualizar este arquivo no mesmo commit/PR.
4. **Caminhos concretos obrigatórios:** referências devem usar paths explícitos (ex.: `results/structure_d/model_comparison.csv`), sem descrições genéricas.

## Checklist rápido (gate de revisão)

- [ ] Claim nova adicionada no draft possui linha correspondente nesta matriz.
- [ ] Fonte de dado (arquivo + colunas/chaves) foi identificada.
- [ ] Transformação foi descrita de forma reproduzível.
- [ ] Artefato derivado em `results/structure_d/` foi referenciado por path concreto.
- [ ] Status (`Suportado`, `Em validação`, `Hipótese`) está explícito.
