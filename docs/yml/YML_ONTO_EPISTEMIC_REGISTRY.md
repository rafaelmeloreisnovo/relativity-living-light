# YML Onto-Epistemic Registry

## Status

`metadata_ready / governance_record / claim_boundary`

## Finalidade

Este documento define a classificação ontológica e epistemológica dos arquivos `.yml` e `.yaml` do repositório.

A regra central é:

> YAML parseável não é, por si só, validação científica.

Todo YAML deve ser classificado em duas dimensões:

1. **Ontológica** — o que o arquivo é no sistema.
2. **Epistemológica** — que tipo de conhecimento ele autoriza.

---

## 1. Rastreabilidade ontológica

A rastreabilidade ontológica responde:

```text
Este artefato é o quê?
Qual função ele cumpre?
Onde ele pertence?
Quem o consome?
O que ele produz?
```

### Estados ontológicos permitidos

| Estado | Significado |
|---|---|
| `workflow_executable` | GitHub Actions executável em `.github/workflows/` |
| `data_contract` | Contrato estrutural de dados |
| `source_manifest` | Manifesto de fontes externas ou internas |
| `validation_registry` | Registro de caminhos de validação |
| `result_manifest` | Manifesto de resultados ou artefatos produzidos |
| `pipeline_config` | Configuração operacional de pipeline |
| `schema_contract` | Contrato de schema ou validação estrutural |
| `example_fixture` | Exemplo, fixture, mock ou arquivo de teste |
| `legacy_mirror` | Cópia histórica ou espelho não canônico |
| `raw_authorial` | Material autoral bruto ainda não classificado cientificamente |
| `governance_record` | Documento de governança, auditoria ou política |

---

## 2. Rastreabilidade epistemológica

A rastreabilidade epistemológica responde:

```text
Como sabemos?
Qual evidência sustenta?
O que está verificado?
O que é declaração?
O que ainda é TOKEN_VAZIO?
O que não pode ser promovido a claim?
```

### Estados epistemológicos permitidos

| Estado | Significado |
|---|---|
| `VERIFIED` | Evidência localizada em arquivo, commit, tag, release, resultado, manifesto ou execução auditável |
| `DECLARED_BY_AUTHOR` | Declarado pelo autor, mas ainda sem prova independente suficiente no repo |
| `TOKEN_VAZIO` | Evidência necessária ainda não localizada |
| `CONTRADICTION` | Evidência localizada contradiz a alegação |
| `METADATA_READY` | YAML parseia, está catalogado e tem função identificada, mas não valida claim científico |
| `REAL_VALIDATED_BLOCKED` | Bloqueado para validação real até completar fonte, hash, execução, métrica, baseline e claim boundary |
| `SYNTHETIC_ONLY` | Artefato sintético, mock, exemplo ou demo; não pode ser promovido a dado real |
| `CLAIM_BLOCKED` | Claim explicitamente bloqueado por falta de evidência, métrica, baseline ou fronteira de escopo |
| `AUDIT_PENDING` | Aguarda auditoria de caminho, consumidor, fonte, execução ou hash |

---

## 3. Regra de promoção

A promoção de estado deve ser evidencial, não estética.

Fluxo mínimo recomendado:

```text
TOKEN_VAZIO
→ DECLARED_BY_AUTHOR
→ METADATA_READY
→ VERIFIED
```

`METADATA_READY` não vira `REAL_VALIDATED` automaticamente.

Para promoção a validação real, exigir:

1. fonte externa rastreável;
2. URL, DOI ou referência pública quando aplicável;
3. data de acesso;
4. hash/checksum ou artefato commitado;
5. comando executado;
6. ambiente, script ou workflow identificado;
7. artefato produzido;
8. métrica gerada;
9. baseline ou adversário definido;
10. covariância/erro quando aplicável;
11. fronteira explícita de claim;
12. registro em manifesto, índice ou nota de auditoria.

---

## 4. Regras contra inflação

Proibido:

```text
YAML parseou → teoria validada
workflow rodou → modelo venceu
mock funcionou → dado real confirmado
documento existe → claim científico provado
```

Permitido:

```text
YAML parseou → METADATA_READY
workflow rodou → EXECUTION_EVIDENCE
mock funcionou → SYNTHETIC_ONLY
documento existe → governance_record ou declared_by_author
```

---

## 5. Claim boundary obrigatório

Todo YAML que toca dados, validação, resultados ou rotas científicas deve conter ou apontar para uma fronteira de claim.

Modelo mínimo:

```yaml
claim_boundary: >
  Este arquivo organiza metadados, caminhos, fontes, contratos ou rotas.
  Ele não prova superioridade científica, nem valida fisicamente o modelo.
  Claims científicos exigem fonte, execução, métrica, baseline,
  erro/covariância quando aplicável e rastreabilidade completa.
```

---

## 6. Estados por localização

| Local | Estado ontológico provável | Observação |
|---|---|---|
| `.github/workflows/*.yml` | `workflow_executable` | Deve ter `permissions`; preferir `timeout-minutes` e `concurrency` |
| `data/**/*.yml` | `data_contract` ou `source_manifest` | Deve declarar fonte, schema, consumidor e claim boundary |
| `docs/pipelines/**/*.yml` | `validation_registry` ou `pipeline_config` | Deve declarar canonicidade e consumidores |
| `validacao_real/**/*.yml` | `source_manifest` ou `data_contract` | Deve bloquear claim sem execução real |
| `docs/yml/*.md` | `governance_record` | Documenta auditoria; não prova claim físico |
| raiz `*.yml` | `legacy_mirror` ou `pipeline_config` | Deve ser justificado, migrado ou marcado como não canônico |

---

## 7. Registro mínimo por YAML relevante

```yaml
artifact:
  path: TOKEN_VAZIO
  ontology_class: TOKEN_VAZIO
  epistemic_state: TOKEN_VAZIO
  canonical: false
  duplicate_of: TOKEN_VAZIO
  consumed_by:
    - TOKEN_VAZIO
  produced_by:
    - TOKEN_VAZIO
  claim_allowed:
    - TOKEN_VAZIO
  claim_blocked:
    - TOKEN_VAZIO
  evidence_required:
    - TOKEN_VAZIO
  next_action: TOKEN_VAZIO
```

---

## 8. Relação com auditoria

Mudanças em YAML devem ser registradas de forma consultável quando alterarem regime, canonicidade, validação, fonte, contrato, workflow ou fronteira de claim.

Diretórios relacionados:

```text
docs/audits/
docs/yml/
docs/governance/
data/real/
.github/workflows/
```

---

## 9. Fronteira final

Este registro organiza linguagem, estados e regras para YAML.

Ele não:

- valida RLL;
- refuta RLL;
- escolhe modelo cosmológico;
- altera outputs;
- promove mock ou sintético;
- substitui fonte, execução, métrica, baseline, covariância ou falsificador.

## Critério final

Um YAML bem classificado deve responder:

```text
O que sou?
Onde pertenço?
Quem me consome?
O que produzo?
Qual evidência me sustenta?
Qual estado epistemológico carrego?
Qual claim permito?
Qual claim bloqueio?
Qual próximo passo me promove ou me refuta?
```
