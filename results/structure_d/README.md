Outputs (CSVs e plots) do fluxo Structure D aparecem aqui após rodar:
`python -m data.pipelines.structure_d.run_all`

## Perfil padrão
- Perfil: `structure_d_default`
- Datasets ativos: `hz`, `fsigma8`

## Artefatos canônicos (obrigatórios por execução)
Estes arquivos são obrigatórios e o pipeline valida que todos existem ao final da execução:
- `model_comparison.csv`
- `covariance_usage.csv`
- `error_mode_usage.csv`
- `rll_regime_summary.csv`
- `reproduction_contract.json`

## Blocos opcionais
- Bloco Bayesiano (`--bayes`):
  - `bayes_evidence.csv`
  - `bayes_factor_interpretation.csv`
- Motivo da opcionalidade: é um resumo complementar, não necessário para o perfil padrão clássico. O status de produção é registrado em `reproduction_contract.json`.

## Artefatos efetivamente produzidos no perfil padrão
Além dos 5 obrigatórios, o pipeline padrão também gera artefatos auxiliares de reporting.
Versionados no repositório (textuais):
- `sensitivity_long.csv`
- `dominance_by_z.csv`
- `degeneracy_corr_bin_*.csv`

Artefatos binários (`results/structure_d/figs/*.png`) podem ser gerados localmente na execução, mas não são necessários para o contrato canônico e não são versionados.

## Reproduction contract
Comando (perfil padrão):
```bash
python -m data.pipelines.structure_d.run_all --profile structure_d_default
```

Contrato de reprodução:
- Perfil esperado: `structure_d_default`
- Política de covariância padrão: `prefer_full` (ou a definida no config/CLI)
- Arquivos esperados (sempre):
  - `model_comparison.csv`
  - `covariance_usage.csv`
  - `error_mode_usage.csv`
  - `rll_regime_summary.csv`
  - `reproduction_contract.json`
- Arquivos opcionais (somente com `--bayes`):
  - `bayes_evidence.csv`
  - `bayes_factor_interpretation.csv`

O arquivo `reproduction_contract.json` registra, em formato de máquina, o comando, perfil, política de covariância e o status de cada artefato opcional.
