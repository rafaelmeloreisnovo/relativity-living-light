# YML NEXT ACTIONS

Gerado em: `2026-06-26T20:06:17Z`  
Commit auditado: `623c7be20f0952cd5769615032f8d2d68a1a23e8`

| ordem | ação | classe | escopo | rollback |
|---:|---|---|---|---|
| 1 | Manter mapa YAML -> SH/PY com gate de sintaxe e rollback por consumidor | FATO_IMPLEMENTADO | docs/yml/YML_PIPELINE_EXECUTION_READINESS.md | reverter artefato documental |
| 2 | Adicionar campo documental `consumed_by` aos manifests YAML sem alterar dados | ACAO_RECOMENDADA | data_config | revert do commit documental |
| 3 | Padronizar checksum para todo artifact upload | ACAO_RECOMENDADA | workflows | revert do workflow específico |
| 4 | Tornar commits automáticos opt-in com input explícito | ACAO_RECOMENDADA | workflows com `contents: write` | reverter input/condição |
| 5 | Executar workflow real em GitHub Actions e anexar run_id/logs | ACAO_RECOMENDADA | validação real | nenhuma alteração de dados sem PR separado |
| 6 | Criar auditoria semântica por schema para cada família YAML | ACAO_RECOMENDADA | tools + docs | desativar via workflow_dispatch mode |

## Próximo PR mínimo seguro

`ci: require explicit commit opt-in for write workflows` limitado a workflows que já usam `contents: write`, sem alterar dados científicos.
