# Claim State Ledger

**Status:** `ledger_policy_v0.1`  
**Objetivo:** separar fala, metáfora, hipótese, referência, evidência e claim forte.

---

## 1. Estados possíveis

| Estado | Significado | Pode publicar? | Pode afirmar forte? |
|---|---|---:|---:|
| `RAW_ORAL` | fala bruta ou insight oral | sim, como origem | não |
| `RAW_NOTE` | nota inicial | sim, como registro | não |
| `METAFORA` | imagem conceitual | sim, marcada | não |
| `PARABOLA_DIDATICA` | metáfora com função pedagógica | sim, marcada | não |
| `HIPOTESE` | proposta testável | sim | não, até teste |
| `REF_REQUIRED` | precisa referência externa | sim, como pendência | não |
| `TOKEN_VAZIO` | lacuna honesta | sim, como lacuna | não |
| `SOURCE_LINKED` | possui referência | sim | depende |
| `METHOD_DEFINED` | possui método/protocolo | sim | depende |
| `EVIDENCE_LINKED` | evidência anexada | sim | talvez |
| `RESULT_REPRODUCED` | resultado reproduzido | sim | talvez |
| `PEER_OR_REVIEW_READY` | pronto para revisão | sim | condicionado |
| `CLAIM_ALLOWED` | gates passaram | sim | sim, no escopo |
| `CLAIM_BLOCKED` | gate bloqueia | sim, como limite | não |

---

## 2. Regra de promoção

```text
RAW_ORAL não vira CLAIM_ALLOWED diretamente.
```

Fluxo mínimo:

```text
RAW_ORAL → CURATED_NOTE → DOMAIN_CLASSIFIED → REF_REQUIRED/SOURCE_LINKED → METHOD_DEFINED → EVIDENCE_LINKED → REVIEW → CLAIM_ALLOWED
```

---

## 3. Claims por domínio

| Domínio | Exige |
|---|---|
| Teologia | tradição, fonte textual, interpretação, limite de fé |
| Filosofia | definição, argumento, distinção conceitual, objeção |
| Física | modelo, medição, referência, unidade, escala, incerteza |
| Biologia | organismo, mecanismo, referência, observação, contexto evolutivo |
| Matemática | definição, prova, exemplo, contraexemplo |
| Computação | código, versão, log, teste, hash, ambiente |
| Medicina/saúde | fonte clínica confiável, escopo, risco, não prescrição indevida |
| Segurança pública | fonte primária, risco, população afetada, plano logístico |
| História | fonte primária/secundária, disputa de origem, cronologia |

---

## 4. Linguagem permitida por estado

| Estado | Linguagem segura |
|---|---|
| `RAW_ORAL` | “foi levantada a hipótese/observação...” |
| `REF_REQUIRED` | “exemplo citado, ainda pendente de referência” |
| `TOKEN_VAZIO` | “não há evidência suficiente registrada neste momento” |
| `SOURCE_LINKED` | “há referência associada, ainda precisa avaliação” |
| `EVIDENCE_LINKED` | “há evidência registrada no escopo X” |
| `CLAIM_ALLOWED` | “o claim é permitido no escopo definido” |

---

## 5. Estados proibidos de mistura

Proibido confundir:

```text
metáfora = prova
tradição = medição
estatística = verdade total
referência = reprodução
origem nobre = claim automático
origem humilde = claim fraco
TOKEN_VAZIO = confirmação
```

---

## 6. R3

```text
F_ok   = estados de claim definidos.
F_gap  = falta automatizar validação de transição entre estados.
F_next = criar arquivo JSONL real de ledger de claims.
```
