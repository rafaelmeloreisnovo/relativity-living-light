Coloque aqui os CSVs de entrada do fluxo Structure D. Formatos esperados:

## Hz.csv
colunas: z, Hz, sigma

## fsigma8.csv
colunas: z, fs8, sigma

Você pode gerar dados exemplo rodando:
`python -m data.pipelines.structure_d.make_example_data`

## Configuração por corrida (datasets ativos)
Arquivo: `data/pipelines/structure_d/datasets_config.json`

Campos principais:
- `run_name`: identificador da corrida.
- `active_datasets`: datasets habilitados na execução.
- `datasets`: catálogo com path, observável, tipo de erro e metadados.

Exemplo padrão:
- ativos: `hz`, `fsigma8`.
- reais estruturados disponíveis: `real_hz`, `real_bao`, `real_cmb_shift`.

Esquema comum por observável (camada de dados em `data/pipelines/structure_d/`):
- `values`;
- `errors` **ou** `covariance`;
- `metadata` com `survey`, `redshift_range`, `reference`.

Restrições numéricas aplicadas no pipeline:
- `sigma` (em `Hz.csv` e `fsigma8.csv`) deve ser finito e estritamente positivo (`sigma > 0`).
- `covariance` (quando usada) deve ser matriz quadrada finita, diagonal estritamente positiva e dimensão consistente.
- `width` usado em `gaussian_window(...)` (módulo `data/pipelines/structure_d/feedback_agn.py`) deve ser finito e estritamente positivo (`width > 0`).
