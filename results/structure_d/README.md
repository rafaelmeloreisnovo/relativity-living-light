Outputs (CSVs, tabelas e plots) do fluxo Structure D aparecem aqui após rodar:
`python -m data.pipelines.structure_d.run_all`

## Comando de reprodução (CLI)
```bash
python -m data.pipelines.structure_d.run_all
```

## Ordem lógica de geração dos artefatos
1. Posteriores (`posterior_LCDM.csv`, `posterior_RLL_like_AGN.csv`)
2. Evidências (`bayes_evidence.csv`)
3. Fator de Bayes (`bayes_factor_summary.csv`)
4. Interpretação (`bayes_factor_interpretation.csv`)

## Arquivos relevantes de saída
- `model_comparison.csv`: comparação de χ²/AIC/BIC entre modelos.
- `covariance_usage.csv`: resumo versionável por corrida indicando, por modelo e por bloco (SNe, BAO, fσ8, lentes, etc.), se a covariância usada foi cheia (`full`) ou fallback diagonal (`diagonal_fallback`).
- `posterior_LCDM.csv`: amostras da posterior para o modelo ΛCDM.
- `posterior_RLL_like_AGN.csv`: amostras da posterior para o modelo RLL-like-AGN.
- `bayes_evidence.csv`: evidências Bayesianas (log-evidence) por modelo, derivadas das amostras posteriores.
- `bayes_factor_summary.csv`: resumo do fator de Bayes entre os modelos comparados.
- `bayes_factor_interpretation.csv`: interpretação textual/categórica do fator de Bayes com base em escala de evidência.

## Esquema de colunas esperado

### `posterior_LCDM.csv`
Colunas esperadas:
- `sample_id`: identificador inteiro da amostra.
- `weight`: peso da amostra (quando aplicável).
- `log_posterior`: valor de log-posterior da amostra.
- `log_likelihood`: valor de log-verossimilhança da amostra.
- `log_prior`: valor de log-prior da amostra.
- `parameter_*`: uma coluna por parâmetro inferido do ΛCDM (prefixo `parameter_`).

### `posterior_RLL_like_AGN.csv`
Colunas esperadas:
- `sample_id`: identificador inteiro da amostra.
- `weight`: peso da amostra (quando aplicável).
- `log_posterior`: valor de log-posterior da amostra.
- `log_likelihood`: valor de log-verossimilhança da amostra.
- `log_prior`: valor de log-prior da amostra.
- `parameter_*`: uma coluna por parâmetro inferido do RLL-like-AGN (prefixo `parameter_`).

### `bayes_evidence.csv`
Colunas esperadas:
- `model`: nome do modelo.
- `log_evidence`: log da evidência Bayesiana estimada.
- `log_evidence_std`: incerteza/desvio padrão associado à estimativa de log-evidence.
- `n_samples`: número de amostras efetivamente usadas no cálculo.

### `bayes_factor_summary.csv`
Colunas esperadas:
- `model_numerator`: modelo no numerador do fator de Bayes.
- `model_denominator`: modelo no denominador do fator de Bayes.
- `log_bayes_factor`: log do fator de Bayes (`log B_ij`).
- `bayes_factor`: fator de Bayes em escala linear (`B_ij`).

### `bayes_factor_interpretation.csv`
Colunas esperadas:
- `model_numerator`: modelo no numerador do fator de Bayes.
- `model_denominator`: modelo no denominador do fator de Bayes.
- `log_bayes_factor`: log do fator de Bayes utilizado na interpretação.
- `evidence_strength`: classificação categórica da evidência (ex.: inconclusiva, moderada, forte).
- `interpretation`: texto curto com a interpretação do resultado.
## Índice canônico de artefatos textuais
A referência oficial para **todos os artefatos textuais** de `results/` (incluindo este subdiretório) é:
- `results/OUTPUTS_TEXTUAIS_INDEX.md`
- manifesto de máquina correspondente: `results/manifest.json`

## Saídas textuais específicas do Structure D
- `model_comparison.csv`: comparação de χ²/AIC/BIC entre modelos.
- `covariance_usage.csv`: resumo versionável por corrida indicando, por modelo e por bloco (SNe, BAO, fσ8, lentes, etc.), se a covariância usada foi cheia (`full`) ou fallback diagonal (`diagonal_fallback`).

- `bayes_factor_interpretation.csv`: tabela canônica estática (Jeffreys/Trotta) com faixas de lnB e classificação textual de evidência.


## Artefatos de regimes em redshift (novos)
- `rll_regime_summary.csv`: resumo por bin de redshift com estatísticas de `R(z)` (`R_mean`, `R_median`, `R_std`), rótulo de regime e campo `notes` para auditoria de configuração.
- `rll_regime_metadata.csv`: metadado auxiliar (1 linha por corrida) repetindo limiares, estratégia de binning e `SENSITIVITY_EPS` para rastreabilidade.
- `rll_regime_overview.png`: visão global de `R(z)` vs. `z` com faixas de classificação.
- `rll_regime_by_bin.png`: evolução do regime médio por bin de redshift.

## Significado físico de `R(z)`
Neste pipeline, `R(z)` é tratado como um **indicador adimensional de dominância relativa** entre o setor efetivo RLL-like e a referência ΛCDM ao longo do redshift. A interpretação operacional é:
- `R(z) > 0`: tendência de dominância do setor RLL-like.
- `R(z) < 0`: tendência de dominância do setor ΛCDM.
- `|R(z)|` pequeno: regime de equilíbrio efetivo (mistura/balanço).

## Convenção de classificação
A convenção está explicitada em `data/pipelines/structure_d/reporting.py` e serializada em `notes`:
- limiar principal: `DOMINANCE_THRESHOLD = 0.10`;
- fronteiras do balanceado: `-0.10 <= R(z) <= 0.10`;
- classes:
  - `lcdm_dominant` para `R(z) < -0.10`;
  - `balanced` para `-0.10 <= R(z) <= 0.10`;
  - `rll_dominant` para `R(z) > 0.10`.

## Estratégia de binning e sensibilidade numérica
- Binning em redshift padrão: `fixed_n_bins` com `n_bins = 8` (há suporte alternativo para bins manuais).
- Passo de derivada numérica central: `SENSITIVITY_EPS = 1e-4`.
- Todos esses parâmetros são registrados em `rll_regime_summary.csv` (campo `notes`) e em `rll_regime_metadata.csv`.
