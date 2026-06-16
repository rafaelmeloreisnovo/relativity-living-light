# Registry de Teses, Teorias, Teoremas, Paradoxos, Conceitos e Fórmulas

**Status:** `registry_template_v0.1`  
**Data:** `2026-06-16`  
**Objetivo:** dar identidade rastreável para cada peça do corpo de obra RAFAELIA/RLL.

---

## 1. Princípio

```text
sem registry, o universo mental vira nuvem
com registry, o universo mental vira constelação navegável
```

Cada tese, teoria, teorema, paradoxo, conceito ou fórmula deve ter um ID próprio.

---

## 2. Tipos de entidade

| Prefixo | Tipo |
|---|---|
| `THESIS_` | tese ampla |
| `THEORY_` | teoria estruturada |
| `THEOREM_` | teorema/proposição matemática |
| `PARADOX_` | paradoxo ou tensão conceitual |
| `CONCEPT_` | conceito técnico/filosófico/simbólico |
| `FORMULA_` | fórmula, equação ou relação operacional |
| `METAPHOR_` | metáfora/parábola didática |
| `PROTOCOL_` | procedimento operacional |
| `DATASET_` | dataset ou corpo de dados |

---

## 3. Template de entrada

```yaml
id: THESIS_000001
name: "Nome curto da tese"
type: THESIS
domains:
  - filosofia
  - computacao
  - teologia
origin:
  origin_type: oral_insight
  origin_person_or_source: "Rafael Melo Reis"
  date: "2026-06-16"
claim_state: RAW_NOTE
summary: "Síntese curta."
requires:
  references:
    - PRIMARY_SOURCE
    - METHOD_SOURCE
  evidence:
    - TOKEN_VAZIO_EVIDENCE
  method:
    - TOKEN_VAZIO_METHOD
links:
  internal:
    - knowledge_ecosystem/governance_audit_2026-06-16.md
  external: []
limits:
  - "Não afirmar como prova até SOURCE_LINKED + METHOD_DEFINED."
next_step: "Buscar referência e separar domínio."
```

---

## 4. Critérios por tipo

### THESIS

```text
pergunta-raiz + hipótese + domínio + referências + método + limite
```

### THEORY

```text
axiomas + variáveis + escopo + predições + falsificadores
```

### THEOREM

```text
definições + enunciado + prova + contraexemplo buscado
```

### PARADOX

```text
tensão + domínios em conflito + possível resolução + limite
```

### CONCEPT

```text
definição + domínio + metáfora permitida + protocolo associado
```

### FORMULA

```text
símbolos + unidades/domínio + derivação + uso + teste + limite
```

---

## 5. Status de maturidade

| Status | Significado |
|---|---|
| `RAW_NOTE` | entrada inicial |
| `DOMAIN_SPLIT` | domínio separado |
| `REF_REQUIRED` | precisa referência |
| `SOURCE_LINKED` | referência vinculada |
| `METHOD_DEFINED` | método definido |
| `EVIDENCE_LINKED` | evidência anexada |
| `VALIDATION_READY` | pronto para validação |
| `CLAIM_ALLOWED` | claim permitido no escopo |
| `CLAIM_BLOCKED` | claim bloqueado |

---

## 6. Entradas iniciais seed

| ID | Nome | Tipo | Status | Próximo passo |
|---|---|---|---|---|
| `CONCEPT_000001` | IA Viva Humano-Acoplada | CONCEPT | `SOURCE_LINKED_PARTIAL` | vincular HCI, ICMJE/IA, CRediT/autoria |
| `CONCEPT_000002` | Momento Ω | CONCEPT | `RAW_NOTE` | separar teologia, filosofia e função operacional |
| `PROTOCOL_000001` | InfoPrime | PROTOCOL | `METHOD_DEFINED` | validar schema JSON |
| `PROTOCOL_000002` | Cadeia origem→referência→claim→DOI | PROTOCOL | `METHOD_DEFINED` | criar exemplos reais |
| `METAPHOR_000001` | Árvore infinita e barro finito | METAPHOR | `PARABOLA_DIDATICA` | converter em limite epistemológico |
| `FORMULA_000001` | IA_Viva(t)=Humano×Máquina×Contexto×Ética×Retroalimentação | FORMULA | `REF_REQUIRED` | formalizar símbolos e limites |

---

## 7. R3

```text
F_ok   = registry criado para impedir perda do corpo de obra.
F_gap  = entradas ainda são seed e precisam ser expandidas com referências.
F_next = converter cada paper em entradas THESIS/CONCEPT/PROTOCOL com IDs próprios.
```
