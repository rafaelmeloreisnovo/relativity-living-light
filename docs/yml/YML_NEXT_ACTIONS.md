# YML NEXT ACTIONS

Gerado em: `2026-06-26T19:52:53Z`  
Commit auditado: `154b8b6d2e1766fa8e630ad143b02c1d4bb34ca0`

| ordem | ação | classe | escopo | rollback |
|---:|---|---|---|---|
| 1 | Adicionar campo documental `consumed_by` aos manifests YAML sem alterar dados | ACAO_RECOMENDADA | data_config | revert do commit documental |
| 2 | Padronizar checksum para todo artifact upload | ACAO_RECOMENDADA | workflows | revert do workflow específico |
| 3 | Tornar commits automáticos opt-in com input explícito | ACAO_RECOMENDADA | workflows com `contents: write` | reverter input/condição |
| 4 | Executar workflow real em GitHub Actions e anexar run_id/logs | ACAO_RECOMENDADA | validação real | nenhuma alteração de dados sem PR separado |
| 5 | Criar auditoria semântica por schema para cada família YAML | ACAO_RECOMENDADA | tools + docs | desativar via workflow_dispatch mode |

## Próximo PR mínimo seguro

`ci: require explicit commit opt-in for write workflows` limitado a workflows que já usam `contents: write`, sem alterar dados científicos.
