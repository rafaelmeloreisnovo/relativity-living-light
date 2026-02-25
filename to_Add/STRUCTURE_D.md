# D) Estrutura forte (documentação + execução)

## Pastas padrão
/paper  /theory  /code  /data  /results  /governance

## Artefatos obrigatórios
- FILE_MANIFEST.csv (sha256)
- LINK_GRAPH.json (links internos)
- requirements.txt / environment.yml
- seeds + logs reprodutíveis
- tabela: hipótese ↔ evidência ↔ teste ↔ status

## CI recomendado
- lint + unit tests (equações e integrais)
- pipeline reproduzível de figuras
- checagem de links quebrados
