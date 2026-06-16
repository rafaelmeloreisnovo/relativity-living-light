# Cadeia Estrutural de Referências Bibliográficas

**Status:** `reference_chain_v0.1`  
**Data:** `2026-06-16`  
**Objetivo:** criar uma estrutura de busca, curadoria e promoção bibliográfica para teses, teorias, teoremas, paradoxos, conceitos e fórmulas.

---

## 1. Princípio

```text
referência não é enfeite
referência é cadeia de custódia do conhecimento
```

A bibliografia não serve apenas para “encher páginas”. Ela serve para mostrar:

- origem;
- tradição;
- continuidade;
- divergência;
- limite;
- método;
- autoridade contextual;
- caminho de revisão.

---

## 2. Tipos de referência

| Tipo | Função | Peso inicial |
|---|---|---:|
| `PRIMARY_SOURCE` | fonte original, artigo, livro, documento, dado bruto | 5 |
| `METHOD_SOURCE` | fonte de método, protocolo ou padrão | 5 |
| `STANDARD_SOURCE` | norma, recomendação, schema, guideline | 5 |
| `REVIEW_SOURCE` | revisão, survey, meta-análise | 4 |
| `HISTORICAL_SOURCE` | origem histórica, tradição, cronologia | 3 |
| `SECONDARY_SOURCE` | explicação derivada confiável | 2 |
| `ORAL_SOURCE` | fala, aula, relato, tradição oral | 1 |
| `UNVERIFIED_LEAD` | pista ainda sem fonte | 0 |

Peso não é verdade. Peso é prioridade de curadoria.

---

## 3. Estados da referência

```text
UNVERIFIED_LEAD
→ REF_REQUIRED
→ SOURCE_FOUND
→ SOURCE_CLASSIFIED
→ SOURCE_SUMMARIZED
→ SOURCE_LINKED_TO_CLAIM
→ SOURCE_REVIEWED
→ SOURCE_CANONICAL
```

Nenhuma referência vira canônica sem classificação e vínculo a claim.

---

## 4. Campos mínimos de uma referência

```yaml
id: REF_000001
type: STANDARD_SOURCE
title: "..."
author_or_org: "..."
year: "..."
url_or_doi: "..."
accessed: "2026-06-16"
domain:
  - computacao
  - governanca
supports:
  - CLAIM_000001
claim_state: SOURCE_FOUND
notes: "Resumo curto sem copiar extensamente."
```

---

## 5. Referências estruturantes iniciais

| ID | Referência | Domínio | Uso interno | Estado |
|---|---|---|---|---|
| `REF_STD_001` | FAIR Principles — GO FAIR | governança de dados | metadados, proveniência, reuso, vocabulários, referência qualificada | `SOURCE_FOUND` |
| `REF_STD_002` | DataCite Metadata Schema | DOI/metadados | identificação, citação e recuperação de recursos | `SOURCE_FOUND` |
| `REF_STD_003` | Citation File Format / CITATION.cff | citação de software/dados | metadados de citação legíveis por humano e máquina | `SOURCE_FOUND` |
| `REF_STD_004` | CRediT Contributor Role Taxonomy | autoria/contribuição | papéis de contribuição e integridade | `SOURCE_FOUND` |
| `REF_STD_005` | ICMJE authors/contributors recommendations | autoria/IA/responsabilidade | autoria humana, contribuição, declaração de IA | `SOURCE_FOUND` |

---

## 6. Como vincular referência a tese

Cada tese deve possuir pelo menos:

```text
1 referência de origem/conceito
1 referência de método
1 referência de oposição ou limite
1 referência de padrão/editorial quando houver publicação
```

Formato:

```yaml
claim_id: CLAIM_000001
claim_text: "..."
claim_domain: [filosofia, computacao]
status_before_reference: HIPOTESE
references_required:
  - PRIMARY_SOURCE
  - METHOD_SOURCE
  - REVIEW_SOURCE
references_found:
  - REF_STD_001
status_after_reference: SOURCE_LINKED
remaining_gap: "Falta fonte primária histórica."
```

---

## 7. Busca bibliográfica por fila

Cada busca deve virar tarefa rastreável:

```yaml
search_id: SEARCH_000001
question: "Qual é a origem histórica documentada da técnica X?"
domain: historia_da_medicina
query_terms:
  - "..."
  - "..."
preferred_sources:
  - books
  - review articles
  - primary historical sources
status: PENDING
result: TOKEN_VAZIO_RESULT
next_step: "buscar em bases acadêmicas e registrar referência"
```

---

## 8. Promoção e bloqueio

Uma tese pode ser promovida quando:

```text
SOURCE_LINKED + METHOD_DEFINED + LIMIT_DECLARED + REVIEWED
```

Uma tese deve ser bloqueada quando:

```text
REF_REQUIRED ou TOKEN_VAZIO_EVIDENCE ou CLAIM_CONTRADICTION
```

---

## 9. Bibliografia como grafo

```text
G_ref = (Claims, References, Domains, Methods, Evidence)
```

Arestas possíveis:

| Aresta | Significado |
|---|---|
| `supports` | referência sustenta claim |
| `limits` | referência limita claim |
| `contradicts` | referência contradiz claim |
| `originates` | referência é origem histórica |
| `method_for` | referência define método |
| `standard_for` | referência define padrão |
| `analogy_for` | referência serve apenas como analogia |

---

## 10. R3

```text
F_ok   = cadeia bibliográfica estrutural criada.
F_gap  = faltam buscas reais por EX_REF_ID e CLAIM_ID.
F_next = criar source_search_queue.yml e começar a preencher referências por prioridade P0.
```
