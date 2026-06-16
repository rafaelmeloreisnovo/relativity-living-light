# Protocolo de Origem e Referência

**Status:** `protocol_v0.1`  
**Objetivo:** impedir telefone sem fio, perda de autoria, overclaim e publicação sem fonte.

---

## 1. Princípio

```text
Informação sem origem pode ser insight.
Informação com origem pode virar conhecimento.
Informação com origem + método + revisão pode virar publicação.
```

A origem não precisa ser socialmente prestigiosa. Pode ser criança, professor, agricultor, técnico, tradição, arquivo, sensor, código, experimento, livro, artigo ou fala oral. O que importa é preservar:

```text
quem / quando / onde / como / em qual contexto / com qual limite
```

---

## 2. Unidade mínima: Primo de Informação

```text
primo_de_informacao = menor unidade rastreável que preserva autoria, contexto e função
```

Campos mínimos:

| Campo | Função |
|---|---|
| `id` | identificador único |
| `origin_type` | fala, artigo, livro, código, dado, observação, tradição, experimento |
| `origin_person_or_source` | pessoa, instituição, obra ou arquivo |
| `timestamp_or_date` | data conhecida ou `TOKEN_VAZIO_DATE` |
| `domain` | teologia, filosofia, física, biologia, matemática, computação, pedagogia, direito |
| `claim_state` | estado do claim |
| `evidence` | link, DOI, hash, commit, citação, log ou `TOKEN_VAZIO_EVIDENCE` |
| `limit` | o que ainda não pode ser afirmado |
| `next_step` | referenciar, testar, publicar, revisar, descartar |

---

## 3. Cadeia de origem

```text
RAW_ORAL
→ RAW_NOTE
→ CURATED_NOTE
→ DOMAIN_CLASSIFIED
→ REFERENCE_LINKED
→ CLAIM_TESTED
→ VERSIONED_ARTIFACT
→ RELEASE
→ DOI
```

Nenhuma etapa deve apagar a anterior.

---

## 4. Política de referência

Uma informação deve receber uma destas marcas:

| Marca | Significado |
|---|---|
| `SOURCE_PRIMARY` | fonte primária encontrada |
| `SOURCE_SECONDARY` | fonte secundária encontrada |
| `REF_REQUIRED` | precisa referência |
| `ORIGIN_UNCLEAR` | origem histórica disputada ou incompleta |
| `TOKEN_VAZIO_REFERENCE` | referência ausente no momento |
| `CLAIM_BLOCKED` | não pode virar afirmação forte |

---

## 5. Exemplo de registro

```json
{
  "id": "INFO_PRIME_000001",
  "origin_type": "oral_insight",
  "origin_person_or_source": "Rafael Melo Reis",
  "timestamp_or_date": "2026-06-16",
  "domain": ["epistemologia", "computação", "pedagogia"],
  "claim_state": "CURATED_NOTE",
  "content": "Toda informação pode surgir em qualquer ponto do grafo humano, mas só vira conhecimento forte com origem e teste.",
  "evidence": "GitHub commit / transcript / file path",
  "limit": "A frase é princípio metodológico; não é claim empírico isolado.",
  "next_step": "Vincular a paper e pipeline de DOI."
}
```

---

## 6. Anti-telefone-sem-fio

Proibido:

```text
ouvi dizer → claim forte
```

Permitido:

```text
ouvi dizer → RAW_ORAL → REF_REQUIRED → busca de fonte → claim condicionado
```

---

## 7. R3

```text
F_ok   = origem virou estrutura rastreável.
F_gap  = faltam automações para capturar fala, hash e DOI automaticamente.
F_next = implementar ledger JSONL de primos de informação.
```
