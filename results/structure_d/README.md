Outputs (CSVs, tabelas e plots) do fluxo Structure D aparecem aqui após rodar:
`python -m data.pipelines.structure_d.run_all`

Arquivos relevantes de saída:
- `model_comparison.csv`: comparação de χ²/AIC/BIC entre modelos.
- `covariance_usage.csv`: resumo versionável por corrida indicando, por modelo e por bloco (SNe, BAO, fσ8, lentes, etc.), se a covariância usada foi cheia (`full`) ou fallback diagonal (`diagonal_fallback`).
