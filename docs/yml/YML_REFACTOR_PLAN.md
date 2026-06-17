# YML REFACTOR PLAN

Gerado em: `2026-06-13T06:12:53Z`  
Commit auditado: `c8eb1047ada81ee2a1f6eb4c917ae707fdee8e4f`

| prioridade | classe | item | evidência | ação segura |
|---:|---|---|---|---|
| 1 | FATO_VERIFICADO | Todos os `35` YAML/YML parsearam com PyYAML. | comando `YAML parser validation` exit 0 | manter gate `.github/workflows/yml-syntax-validation.yml` |
| 2 | FATO_VERIFICADO | Workflows com `permissions` explícito são registrados no ledger. | leitura direta dos workflows | manter `contents: read` por padrão; justificar exceções `contents: write` |
| 3 | RISCO | Workflows com `contents: write` podem alterar repositório por automação. | ledger marca `RISCO_WRITE_PERMISSION_REQUER_JUSTIFICATIVA` | próximo PR: commit/push apenas por input explícito ou environment protegido |
| 4 | RISCO | `dha-fisher-ci.yml` materializa `results/dha/mock_catalog.csv` em CI. | mapa de execução registra script inline de mock | manter rotulado como mock; nunca promover para `real_validated` |
| 5 | LACUNA | Data-config YAML não tem consumidor único inferido nesta auditoria. | ledger registra `TOKEN_VAZIO` em scripts chamados | próximo PR: adicionar `consumed_by` documental sem alterar dados científicos |
| 6 | ACAO_RECOMENDADA | Checksums devem acompanhar outputs científicos. | workflows reais geram checksum em parte dos caminhos; não universal | próximo PR: padronizar checksum para todos os upload-artifacts |

## Status científico permitido

`metadata_ready` para YAML parseados e inventariados. `real_validated` fica BLOQUEADO quando faltar fonte externa, hash, execução registrada, métrica, baseline externo, covariância/erro quando aplicável, artefato final e claim boundary.
