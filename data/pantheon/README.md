# Pantheon+ inputs

Este diretório é reservado para os arquivos do Pantheon+ usados em `docs/panteon_likelihood.py`.

Arquivos esperados:
- `lcparam_full_long_zhel.txt` (obrigatório)
- `sys_full_long.txt` (opcional, recomendado)

Fonte oficial:
- https://github.com/PantheonPlusSH0ES/DataRelease

Modo offline:
- Se `sys_full_long.txt` não existir, o pipeline usa apenas covariância estatística (diagonal) e emite aviso explícito.
