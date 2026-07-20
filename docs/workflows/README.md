# Documentação de Workflows — RLL

Diretório de referência criado na **FASE 25** (2026-07-20). Substitui a navegação ad-hoc por um sistema estruturado com índices, mapas e rastreabilidade de artefatos.

## Documentos neste diretório

| Arquivo | Propósito |
|---------|-----------|
| [INDICE_CANONICO.md](INDICE_CANONICO.md) | Índice categorizado completo dos 44 workflows — camadas, triggers, scripts, status |
| [MAPA_ARTICULACOES.md](MAPA_ARTICULACOES.md) | Grafo de dependências, delegações, lacunas (TOKEN_VAZIO) da rede de workflows |
| [INDICE_ARTEFATOS.md](INDICE_ARTEFATOS.md) | Rastreabilidade workflow → artefato → resultado científico |

## Navegação Rápida

Para decisão rápida sobre qual workflow usar: [`.github/GUIA_WORKFLOWS.md`](../../.github/GUIA_WORKFLOWS.md)

## Pipeline Canônico

`.github/workflows/rll-pipeline-linear-completo.yml` — gate determinístico único (44 steps, 7 fases).

## Checks Obrigatórios (branch protection)

`rll` · `test` · `validate-yaml` · `check-conventions` · `build-formulas-artifacts` · `formulas-manifest`
