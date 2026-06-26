# YML NEXT ACTIONS

Gerado em: `2026-06-26T20:26:23Z`  
Commit auditado: `3a48ed3fb4e86daf43b471337bfcdf9bdbb85fea`

| ordem | ação | classe | escopo | rollback |
|---:|---|---|---|---|
| 1 | Manter mapa YAML -> SH/PY com gate de sintaxe e rollback por consumidor | FATO_IMPLEMENTADO | docs/yml/YML_PIPELINE_EXECUTION_READINESS.md | reverter artefato documental |
| 2 | Adicionar campo documental `consumed_by` aos manifests YAML sem alterar dados | FATO_IMPLEMENTADO | data_config metadata-only | revert do commit documental |
| 3 | Padronizar checksum para artifacts de workflows de escrita auditados | FATO_IMPLEMENTADO | workflows com commit back | revert do workflow específico |
| 4 | Tornar commits automáticos opt-in com input explícito | FATO_IMPLEMENTADO | workflows com commit back | reverter input/condição |
| 5 | Executar workflow real em GitHub Actions e anexar run_id/logs | ACAO_RECOMENDADA | validação real | nenhuma alteração de dados sem PR separado |
| 6 | Criar auditoria semântica por schema para cada família YAML | ACAO_RECOMENDADA | tools + docs | desativar via workflow_dispatch mode |

## Próximo PR mínimo seguro

`ci: keep write workflows opt-in and checksum-bearing` limitado a workflows que já usam `contents: write`, sem alterar dados científicos.
