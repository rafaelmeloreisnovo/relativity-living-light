# Plano Operacional de HOTFIX — Governança, Referências e Claim Gates

**Status:** `hotfix_plan_v0.1`  
**Data:** `2026-06-16`  
**Objetivo:** corrigir a estrutura para que o conhecimento cresça sem incoerência, sem overclaim e sem perda de cadeia de custódia.

---

## 1. Princípio

```text
HOTFIX não é remendo apressado.
HOTFIX é cirurgia mínima para impedir propagação de erro estrutural.
```

A documentação deve impedir que uma lacuna vire afirmação, que uma metáfora vire prova, que uma teoria vire resultado, ou que uma referência ausente vire autoridade.

---

## 2. Classes de HOTFIX

| Classe | Prazo | Definição | Exemplo |
|---|---|---|---|
| `P0_CRITICAL` | imediato | risco de claim falso, dado sem origem, referência inventada | afirmação científica sem fonte |
| `P1_STRUCTURAL` | curto prazo | organização incompleta, ausência de schema, índice quebrado | falta de registry de fórmulas |
| `P2_EXPANSION` | médio prazo | melhoria de documentação, DOI, visualização, grafo | mapa de referências |
| `P3_REFINEMENT` | contínuo | estilo, clareza, redução de redundância | melhorar texto |

---

## 3. HOTFIX P0 obrigatório

### P0.1 — afirmações sem fonte

```text
Se claim empírico não tem fonte:
status = REF_REQUIRED ou TOKEN_VAZIO_REFERENCE
```

### P0.2 — claims científicos fortes

```text
Se não há dado + método + métrica + referência + limite:
status = CLAIM_BLOCKED
```

### P0.3 — fórmulas sem domínio

```text
Se fórmula não tem definição de símbolos/domínio:
status = FORMULA_UNBOUNDED
```

### P0.4 — autoria e IA

```text
IA_ASSISTED = declarado
AI_AS_AUTHOR = proibido
HUMAN_RESPONSIBILITY = obrigatório
```

### P0.5 — dados sem cadeia

```text
Dado sem origem/hash/comando = DATA_CUSTODY_GAP
```

---

## 4. HOTFIX P1 estrutural

Criar ou consolidar:

```text
knowledge_ecosystem/thesis_theory_formula_registry.md
knowledge_ecosystem/source_search_queue.yml
knowledge_ecosystem/reference_seed_sources.yml
knowledge_ecosystem/claim_to_reference_matrix.md
knowledge_ecosystem/templates/publication_package_template.md
```

---

## 5. HOTFIX P2 expansão

- Criar grafo visual de claims ↔ referências.
- Criar release por trilha PapersPub madura.
- Gerar `CITATION.cff` com DOI/release quando houver metadados completos.
- Validar `InfoPrime` com JSON Schema.
- Criar scripts para listar `REF_REQUIRED` e `TOKEN_VAZIO`.

---

## 6. Regra de revisão

Todo PR documental deve responder:

```text
1. Qual origem foi preservada?
2. Qual domínio foi separado?
3. Qual referência foi adicionada?
4. Qual claim foi promovido ou bloqueado?
5. Qual TOKEN_VAZIO permaneceu?
6. Qual próximo passo ficou executável?
```

---

## 7. Critério de saída do HOTFIX

Um hotfix está completo quando:

```text
erro identificado + arquivo corrigido + claim boundary atualizado + referência/ lacuna marcada + R3 final
```

---

## 8. R3

```text
F_ok   = plano HOTFIX classifica risco e correção por P0/P1/P2/P3.
F_gap  = faltam scripts automáticos para detectar claims sem referência.
F_next = criar queue YAML e registry de teses/fórmulas.
```
