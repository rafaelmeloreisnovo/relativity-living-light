Coloque aqui os CSVs de entrada do fluxo Structure D. Formatos esperados:

## Hz.csv
colunas: z, Hz, sigma

## fsigma8.csv
colunas: z, fs8, sigma

Você pode gerar dados exemplo rodando:
`python -m data.pipelines.structure_d.make_example_data`


Restrições numéricas aplicadas no pipeline:
- `sigma` (em `Hz.csv` e `fsigma8.csv`) deve ser finito e estritamente positivo (`sigma > 0`).
- `width` usado em `gaussian_window(...)` (módulo `data/pipelines/structure_d/feedback_agn.py`) deve ser finito e estritamente positivo (`width > 0`).
