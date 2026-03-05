Coloque aqui os CSVs de entrada do fluxo Structure D. Formatos esperados:

## Hz.csv
colunas: z, Hz, sigma

## fsigma8.csv
colunas: z, fs8, sigma

Você pode gerar dados exemplo rodando:
`python -m data.pipelines.structure_d.make_example_data`

A geração de exemplos também cria `mock_data_contract.json` com:
- `seed` utilizado;
- `generated_at_utc` (timestamp ISO-8601 UTC);
- ranges de `z` e `sigma` usados para `Hz.csv` e `fsigma8.csv`.

## Configuração por corrida (datasets ativos)
Arquivo: `data/pipelines/structure_d/datasets_config.json`

Campos principais:
- `default_profile`: profile usado por padrão.
- `profiles`: perfis de corrida com `run_name` e `active_datasets`.
- `datasets`: catálogo com path, observável, tipo de erro e metadados.

Profiles incluídos:
- `structure_d_default` (ativos: `hz`, `fsigma8`).
- `structure_d_real_validation` (ativos: `real_hz`, `real_bao`, `real_cmb_shift`).

Execução por profile:
- padrão: `python -m data.pipelines.structure_d.run_all`
- profile explícito: `STRUCTURE_D_PROFILE=structure_d_real_validation python -m data.pipelines.structure_d.run_all`
- validação real completa (Hz + BAO + CMB): `python -m data.pipelines.structure_d.run_all_real`

Esquema comum por observável (camada de dados em `data/pipelines/structure_d/`):
- `values`;
- `errors` **ou** `covariance`;
- `metadata` com `survey`, `redshift_range`, `reference`.

Restrições numéricas aplicadas no pipeline:
- `sigma` (em `Hz.csv` e `fsigma8.csv`) deve ser finito e estritamente positivo (`sigma > 0`).
- `covariance` (quando usada) deve ser matriz quadrada finita, diagonal estritamente positiva e dimensão consistente.
- `width` usado em `gaussian_window(...)` (módulo `data/pipelines/structure_d/feedback_agn.py`) deve ser finito e estritamente positivo (`width > 0`).

Observação: o pipeline aceita covariância cheia por bloco (SNe, BAO, fσ8, lentes). Quando não houver `C`, usa fallback diagonal com `sigma`.
