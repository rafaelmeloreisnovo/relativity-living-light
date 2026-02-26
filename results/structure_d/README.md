Outputs (CSVs, tabelas e plots) do fluxo Structure D aparecem aqui após rodar:
`python -m data.pipelines.structure_d.run_all`

## Índice canônico de artefatos textuais
A referência oficial para **todos os artefatos textuais** de `results/` (incluindo este subdiretório) é:
- `results/OUTPUTS_TEXTUAIS_INDEX.md`
- manifesto de máquina correspondente: `results/manifest.json`

## Saídas textuais específicas do Structure D
- `model_comparison.csv`: comparação de χ²/AIC/BIC entre modelos.
- `covariance_usage.csv`: resumo versionável por corrida indicando, por modelo e por bloco (SNe, BAO, fσ8, lentes, etc.), se a covariância usada foi cheia (`full`) ou fallback diagonal (`diagonal_fallback`).

- `rll_sensitivity_derivatives.csv`: derivadas por diferença finita central por redshift para cada parâmetro RLL, incluindo elasticidade, escore normalizado por incerteza observacional e flag de estabilidade numérica.
