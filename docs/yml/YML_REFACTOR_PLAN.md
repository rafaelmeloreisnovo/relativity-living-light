# YML REFACTOR PLAN

Gerado em: `2026-07-03T16:02:54Z`  
Commit auditado: `929807336098e7edb7cfa2194dc2986fb6458deb`

| prioridade | classe | item | evidência | ação segura |
|---:|---|---|---|---|
| 1 | FATO_VERIFICADO | Todos os `110` YAML/YML parsearam com PyYAML. | comando `YAML parser validation` exit 0 | manter gate `.github/workflows/yml-syntax-validation.yml` |
| 2 | FATO_VERIFICADO | Workflows com `permissions` explícito são registrados no ledger. | leitura direta dos workflows | manter `contents: read` por padrão; justificar exceções `contents: write` |
| 3 | MITIGADO | Workflows com `contents: write` devem alterar repositório somente por input explícito. | workflows de commit usam `commit_*` default false quando há push/commit back | manter revisão de permissões por workflow |
| 4 | RISCO | `dha-fisher-ci.yml` materializa `results/dha/mock_catalog.csv` em CI. | mapa de execução registra script inline de mock | manter rotulado como mock; nunca promover para `real_validated` |
| 5 | LACUNA | Data-config YAML não tem consumidor único inferido nesta auditoria. | ledger registra `TOKEN_VAZIO` em scripts chamados | próximo PR: adicionar `consumed_by` documental sem alterar dados científicos |
| 6 | ACAO_RECOMENDADA | Checksums devem acompanhar outputs científicos. | workflows reais geram checksum em parte dos caminhos; não universal | próximo PR: padronizar checksum para todos os upload-artifacts |

## Status científico permitido

`metadata_ready` para YAML parseados e inventariados. `real_validated` fica BLOQUEADO quando faltar fonte externa, hash, execução registrada, métrica, baseline externo, covariância/erro quando aplicável, artefato final e claim boundary.
