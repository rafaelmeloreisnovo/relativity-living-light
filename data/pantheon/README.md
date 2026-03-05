# Pantheon+ inputs

Este diretório é o ponto canônico para os insumos Pantheon+ usados por `docs/panteon_likelihood.py`.

## Arquivos esperados

- `lcparam_full_long_zhel.txt` (obrigatório)
- `sys_full_long.txt` (opcional, recomendado para covariância sistemática)

## Como usar sem travar o pipeline principal

- O pipeline principal `data.pipelines.structure_d.run_all` não depende deste diretório.
- A validação Pantheon+ é rodada separadamente via `python docs/panteon_likelihood.py`.
- Se `sys_full_long.txt` não existir, o script roda com covariância estatística diagonal e registra aviso.

## Fonte

Data release oficial:
https://github.com/PantheonPlusSH0ES/DataRelease
