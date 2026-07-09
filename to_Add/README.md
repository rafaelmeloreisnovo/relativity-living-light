# to_Add — Histórico de Ingestão

Status: legado controlado  
Claim: `claim_allowed=false`

Este diretório é apenas histórico/legado.
Não participa da execução científica canônica.

Fluxo operacional oficial:

```text
docs/ + data/ + results/
```

## Migração Structure D

O bundle histórico `to_Add/RAFAELIA_COSMO_STRUCTURE_D.zip` foi promovido para os locais canônicos:

```text
data/pipelines/structure_d/      # código Python autoritativo
data/inputs/structure_d/         # entradas e configs
results/structure_d/             # saídas
docs/science/structure_d/        # documentação científica lapidada
RAFAELIA_COSMO_STRUCTURE_D/       # wrappers de compatibilidade
```

Ledger:

```text
docs/yml/TO_ADD_MIGRATION_LEDGER.yml
```

Validação:

```bash
python3 tools/validate_to_add_migration.py
```

Outputs esperados:

```text
data/results/to_add_migration_validation.json
docs/TO_ADD_MIGRATION_STATUS.md
```

## Regra

```text
[OK] manter histórico rastreável.
[OK] usar data/pipelines/structure_d para execução.
[BLOQUEADO] adicionar lógica nova dentro de to_Add/.
[BLOQUEADO] usar to_Add/ como evidência científica canônica.
```
