# Documentação de Workflows — RLL

Diretório iniciado na **FASE 25** e endurecido na **FASE 25.1** com um **contrato executável** entre documentação e YAML real.

## Ordem de autoridade

1. [`.github/workflow-contract.yml`](../../.github/workflow-contract.yml) — invariantes legíveis por máquina;
2. [`.github/workflows/`](../../.github/workflows/) — implementação operacional;
3. [`tools/validate_workflow_docs.py`](../../tools/validate_workflow_docs.py) — validação determinística;
4. artefatos de validação em `artifacts/workflow-docs/`;
5. índices humanos deste diretório.

Os índices explicam o sistema; o contrato e os YAMLs determinam o estado executável.

## Documentos

| Arquivo | Propósito |
|---|---|
| [INDICE_CANONICO.md](INDICE_CANONICO.md) | Snapshot histórico; usar o contrato e o índice YML para o estado atual |
| [MAPA_ARTICULACOES.md](MAPA_ARTICULACOES.md) | Grafo de dependências, delegações e lacunas da rede |
| [INDICE_ARTEFATOS.md](INDICE_ARTEFATOS.md) | Rastreabilidade workflow → artefato → resultado científico |
| [FASE_25_1_CONTRATO_EXECUTAVEL.md](FASE_25_1_CONTRATO_EXECUTAVEL.md) | Correções de semântica, fronteira de evidência e precedência temporal |
| [RLL_RESEARCH_FRAGMENT_ROUTE_V1.md](RLL_RESEARCH_FRAGMENT_ROUTE_V1.md) | Intake bibliográfico, grafo de fragmentos, receipts e preview Jekyll claim-gated |

## Métrica canônica do pipeline

`.github/workflows/rll-pipeline-linear-completo.yml` contém:

- **44 etapas lógicas** executadas pelo orquestrador;
- **8 fases**, da FASE 0 à FASE 7;
- 6 steps físicos no job `deterministic-gate`.

Essas medidas descrevem camadas diferentes e não devem ser reduzidas à expressão ambígua “44 steps”.

## Checks documentados

`deterministic-gate` · `test` · `validate-yaml` · `check-conventions` · `build-formulas-artifacts` · `formulas-manifest`

A presença desses jobs é verificável no repositório. A configuração externa de branch protection permanece `branch_protection_verified=false` até auditoria específica da regra da branch.

## Sessões explícitas e capacidade

O catálogo não varre mais `.github/workflows/*.yml`. O perfil completo contém sete manifestos allowlisted, com orçamento máximo configurado de 260 minutos; o workflow `frontier` de 190 minutos fica isolado. O job pai usa 320 minutos para incluir até 60 minutos de margem.

| Perfil | Uso | Budget |
|---|---|---:|
| `quick_session` | gate de sintaxe YAML | 20 min |
| `real_data_session` | preflight e workflows real-data em modo controlado | 165 min |
| `science_session` | artefatos científicos e preview de fragmentos | 75 min |
| `literature_session` | valida pacote e aceita um arXiv opcional | 15 min |
| `pages_preview_session` | gera o preview Jekyll como artifact | 15 min |
| `frontier_session` | fronteira isolada | 190 min |
| `full_session` | catálogo allowlisted exceto frontier | 260 min |

A sessão continua single-flight e cada etapa aguarda a anterior. Para intake, passe o ID e a anotação de relação apenas quando houver um alvo revisável. O workflow baixa um registro público por chamada, preserva a resposta e gera um edge pendente; não executa polling nem publica em Pages.

## Snapshot histórico

`INDICE_CANONICO.md` ainda registra uma fotografia de julho de 2026 com 44 workflows. Ele foi mantido para rastreabilidade; use `.github/workflow-contract.yml`, `.github/workflow-orchestrator/session.yml` e `YML_WORKFLOWS_INDEX.md` para a rota e inventário atuais.

## Executar a validação

```bash
python3 tools/validate_workflow_docs.py --strict --write-report
pytest -q tests/test_validate_workflow_docs.py
```

## Navegação rápida

Consulte [`.github/GUIA_WORKFLOWS.md`](../../.github/GUIA_WORKFLOWS.md).
