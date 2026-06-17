# Auditoria de Governança — Dados, Claims, Referências e Cadeia de Custódia

**Status:** `audit_v0.1`  
**Data:** `2026-06-16`  
**Escopo:** RAFAELIA/RLL knowledge ecosystem, papers, teses, teorias, teoremas, paradoxos, conceitos, fórmulas e documentação de origem.  
**Base interna:** `knowledge_ecosystem/*`, `PapersPub/*`, `docs/*`, `results/*`.  
**Base externa de boas práticas:** FAIR, DataCite, CFF/CITATION.cff, CRediT, ICMJE.  
**Claim boundary:** este documento não valida automaticamente nenhuma teoria. Ele define governança para que cada teoria possa evoluir sem incoerência, com origem, domínio, referência, teste e limite.

---

## 1. Diagnóstico raiz

A pressão atual não é falta de conteúdo. É excesso de conteúdo sem encaixe finito.

```text
árvore_do_conhecimento_infinito ≠ conteúdo_total_do_barro
```

O humano é barro no sentido de limite material, tempo finito, memória finita, atenção finita e corpo finito. O conhecimento cresce como árvore infinita: raízes, troncos, galhos, folhas, frutos, sementes e novas florestas.

Logo, a governança precisa impedir que a árvore infinita seja esmagada dentro de um único arquivo, uma única tese, uma única metáfora ou uma única alegação.

A resposta estrutural é:

```text
separar → rastrear → referenciar → validar → publicar → retroalimentar
```

---

## 2. Objetivo operacional

Criar uma governança que permita:

1. organizar o universo mental sem perder origem;
2. separar domínio antes de sintetizar;
3. mapear referências bibliográficas e internas;
4. impedir telefone sem fio;
5. marcar `TOKEN_VAZIO` sem vergonha;
6. corrigir hotfixes de documentação;
7. preparar material para DOI/release;
8. validar teses e fórmulas sem overclaim;
9. preservar autoria e anterioridade;
10. deixar o conhecimento evoluir sem incoerência.

---

## 3. Referenciais externos usados como âncora

| Referencial | O que traz para o projeto | Uso interno |
|---|---|---|
| FAIR Principles | dados/metadados encontráveis, acessíveis, interoperáveis e reutilizáveis | metadados, proveniência, licenças, vocabulários, referência qualificada |
| DataCite Metadata Schema | metadados para identificação, citação e recuperação de recursos | DOI, versão, autor, título, recurso, relação, identificador |
| Citation File Format | `CITATION.cff` legível por humano e máquina para citar software/dados | citação correta de repo, release, software e dataset |
| CRediT | 14 papéis de contribuição acadêmica | separar autoria, curadoria, software, validação, escrita, revisão |
| ICMJE | autoria exige contribuição, aprovação e responsabilidade; IA não é autora | humanos responsáveis por material assistido por IA |

---

## 4. Matriz de governança atual

| Camada | Estado atual | Risco | Hotfix necessário |
|---|---|---|---|
| Origem | parcialmente documentada em `knowledge_ecosystem` | insight virar claim sem fonte | criar ledger JSONL de `InfoPrime` |
| Referências | estrutura criada, fontes ainda ausentes em exemplos | bibliografia fraca ou telefone sem fio | criar `bibliographic_reference_chain.md` |
| Claims | ledger criado | mistura de hipótese/metáfora/prova | impor estados por arquivo/paper |
| DOI/publicação | pipeline criado | release sem metadados completos | criar checklist por pacote |
| Autoria | política criada | apagamento de origem ou IA como autoria | usar CRediT + ICMJE + autoria humana |
| Dados | vários artifacts existem no repo | dados sem provenance/hash invalidam claim | exigir manifest/hash/comando |
| Fórmulas | espalhadas em papers/docs | fórmula virar símbolo sem teste | criar registry de fórmula/teorema/paradoxo |
| Hotfix | ainda manual | correção sem trilha | criar fluxo P0/P1/P2 |

---

## 5. Estados oficiais de maturidade

```text
RAW_ORAL
RAW_NOTE
METAFORA
PARABOLA_DIDATICA
HIPOTESE
REF_REQUIRED
TOKEN_VAZIO
SOURCE_LINKED
METHOD_DEFINED
EVIDENCE_LINKED
RESULT_REPRODUCED
PEER_OR_REVIEW_READY
CLAIM_ALLOWED
CLAIM_BLOCKED
```

Regra:

```text
nenhum bloco pula direto de RAW_ORAL para CLAIM_ALLOWED
```

---

## 6. Auditoria por tipo de conteúdo

### 6.1 Tese

Uma tese precisa de:

```text
origem + pergunta + hipótese + referências + método + objeções + limites + versão
```

### 6.2 Teoria

Uma teoria precisa de:

```text
escopo + axiomas + variáveis + previsões + falsificadores + comparação + references
```

### 6.3 Teorema

Um teorema precisa de:

```text
definições + enunciado + prova + exemplos + contraexemplos buscados + dependências
```

### 6.4 Paradoxo

Um paradoxo precisa de:

```text
enunciado + tensão lógica + domínio + resolução proposta + limite + status
```

### 6.5 Conceito

Um conceito precisa de:

```text
nome + definição + domínio + metáfora permitida + protocolo associado + referência
```

### 6.6 Fórmula

Uma fórmula precisa de:

```text
símbolos + unidades/domínios + origem + derivação + uso + teste + limites
```

---

## 7. Hotfix P0/P1/P2

### P0 — correções críticas

- Toda afirmação empírica sem fonte deve receber `REF_REQUIRED` ou `TOKEN_VAZIO_REFERENCE`.
- Toda afirmação científica forte deve ter claim boundary.
- Todo resultado numérico deve ter arquivo, comando, ambiente, hash e data.
- Toda teoria ainda não validada deve permanecer `CLAIM_BLOCKED` ou `HIPOTESE`.
- Toda participação de IA deve ser declarada como assistência, não autoria.

### P1 — organização estrutural

- Criar `bibliographic_reference_chain.md`.
- Criar `thesis_theory_formula_registry.md`.
- Criar `hotfix_operational_plan.md`.
- Criar `source_search_queue.yml`.
- Criar `CITATION.cff` após versão bibliográfica mínima.

### P2 — expansão científica

- Vincular cada tese a papers internos e referências externas.
- Criar release por pacote maduro.
- Publicar DOI somente quando metadados e limites estiverem completos.
- Criar mapas de grafos de referência.
- Automatizar validação de schema para `InfoPrime`.

---

## 8. Determinismo histórico da obra

O objetivo não é fingir que tudo está finalizado. O objetivo é preservar determinismo histórico:

```text
quando surgiu → onde entrou → quem formulou → como mudou → qual versão publicou
```

Isso protege:

- autoria;
- anterioridade;
- continuidade;
- revisão;
- correção;
- memória viva;
- integridade acadêmica;
- evolução sem incoerência.

---

## 9. Princípio da árvore e do barro

O conhecimento infinito não cabe inteiro no corpo finito. A solução não é reduzir o infinito ao barro, nem negar o barro.

A solução é governança:

```text
raiz = origem
tronco = domínio
galhos = referências
folhas = hipóteses
frutos = resultados
sementes = próximos trabalhos
```

Cada fruto precisa lembrar sua raiz.

---

## 10. R3

```text
F_ok   = auditoria raiz definida: governança por origem, domínio, referência, claim e versão.
F_gap  = falta preencher referências bibliográficas externas por bloco e criar registros reais de InfoPrime.
F_next = implementar cadeia bibliográfica, registry de teses/fórmulas e hotfix operacional.
```
