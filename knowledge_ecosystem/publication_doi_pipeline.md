# Pipeline de Publicação, Release e DOI

**Status:** `pipeline_v0.1`  
**Objetivo:** transformar insight em publicação rastreável sem perder origem, autoria ou limite.

---

## 1. Tese

Não é necessário que todo trabalho tenha cálculo complexo. Um material pode ser forte por:

- organizar conceitos;
- mapear referências;
- separar domínios;
- preservar autoria;
- criar protocolo;
- reunir bibliografia;
- mostrar lacunas;
- propor método de validação.

Em muitos materiais acadêmicos, a força vem da ligação cuidadosa entre referências e argumento.

---

## 2. Fluxo canônico

```text
INSIGHT
→ RAW_RECORD
→ CURATION
→ DOMAIN_SPLIT
→ REFERENCE_MAP
→ CLAIM_LEDGER
→ DRAFT
→ REVIEW
→ VERSION_TAG
→ RELEASE
→ DOI
→ CITABLE_ARTIFACT
```

---

## 3. Artefatos mínimos por publicação

| Artefato | Função |
|---|---|
| `draft.md` | texto principal |
| `references.md` | fontes bibliográficas e internas |
| `data_manifest.md` | origem de dados e materiais |
| `claim_state_ledger.md` | claims permitidos/bloqueados |
| `reproducibility.md` | comandos, ambiente, hashes ou política de não execução |
| `CHANGELOG.md` | mudanças por versão |
| `CITATION.cff` | citação padronizada quando aplicável |

---

## 4. Regra de DOI

Um DOI só deve ser gerado para um pacote que tenha:

```text
versão + autoria + data + escopo + origem + limite + referência
```

Estados:

| Estado | DOI? |
|---|---:|
| `RAW_ORAL` | não |
| `CURATED_NOTE` | talvez, como registro bruto curado |
| `DRAFT` | não ideal, exceto preprint claro |
| `REVIEW_READY` | sim, se fechado por versão |
| `RELEASED` | sim |
| `CLAIM_ALLOWED` | sim, com escopo |

---

## 5. Registro de autoria

Cada bloco deve responder:

```text
Quem percebeu?
Quem registrou?
Quem curou?
Quem testou?
Quem revisou?
Quem publicou?
```

A autoria não deve ser apagada quando uma informação muda de forma.

---

## 6. Publicação sem plágio

Antes de publicar:

1. buscar origem possível;
2. citar técnica anterior;
3. marcar se origem é incerta;
4. diferenciar contribuição própria de contribuição herdada;
5. marcar `ORIGIN_UNCLEAR` quando histórico for disputado;
6. não chamar de próprio o que é continuidade de técnica existente.

---

## 7. R3

```text
F_ok   = pipeline de publicação e DOI definido.
F_gap  = falta automatizar geração de CITATION.cff e release notes.
F_next = criar template de pacote publicável por trilha PapersPub.
```
