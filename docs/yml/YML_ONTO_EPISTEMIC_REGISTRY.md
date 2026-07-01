# YML Onto-Epistemic Registry

## Status

`metadata_ready`

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

```text
TOKEN_VAZIO
→ DECLARED_BY_AUTHOR
→ METADATA_READY
→ VERIFIED
```

`METADATA_READY` não vira `REAL_VALIDATED` automaticamente.

Para promoção, exigir:

1. fonte externa rastreável;
2. URL, DOI ou referência pública quando aplicável;
3. data de acesso;
4. hash/checksum ou artefato commitado;
5. comando executado;
6. ambiente ou workflow identificado;
7. artefato produzido;
8. métrica gerada;
9. baseline ou adversário definido;
10. covariância/erro quando aplicável;
11. fronteira explícita de claim;
12. registro no mapa de rastreabilidade.

---

## 4. Claim boundary obrigatório

```yaml
claim_boundary: >
  Este arquivo organiza metadados, caminhos ou contratos.
  Ele não prova superioridade científica, nem valida fisicamente o modelo.
  Claims científicos exigem fonte, execução, métrica, baseline, erro/covariância
  quando aplicável e rastreabilidade completa.
```

---

## 5. Cabeçalho recomendado para YAML de dados/configuração

```yaml
ontology:
  artifact_kind: validation_registry
  system_role: epistemic_router
  canonical_path: docs/pipelines/validation_paths/CAMINHOS_VALIDACAO_NOVOS.yml
  lifecycle: active
  owner_layer: docs/pipelines
  consumed_by:
    - tools/generate_yml_audit_docs.py
    - tools/docs_inventory.py
    - .github/workflows/START_MANUAL_HERE.yml

epistemics:
  default_state: DECLARED_BY_AUTHOR
  allowed_states:
    - VERIFIED
    - DECLARED_BY_AUTHOR
    - TOKEN_VAZIO
    - CONTRADICTION
    - METADATA_READY
    - REAL_VALIDATED_BLOCKED
  promotion_rule: >
    A rota só passa a VERIFIED quando houver fonte pública rastreável,
    DOI/URL quando aplicável, data de acesso, hash ou artefato commitado,
    comando executado, métrica produzida, baseline/adversário e claim_boundary.
  claim_boundary: >
    Metadata-ready YAML não implica validação científica.
```

---

## 6. Regras para mock, synthetic, demo e placeholder

Qualquer arquivo ou step contendo `mock`, `synthetic`, `example`, `demo`, `placeholder`, `sample` ou `fake` deve ser classificado como:

```text
SYNTHETIC_ONLY
```

ou, no mínimo:

```text
METADATA_READY / CLAIM_BLOCKED
```

Nunca como:

```text
REAL_VALIDATED
```

sem prova contrária explícita.

---

## 7. Critério final

Um YAML está bem organizado quando responde:

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
