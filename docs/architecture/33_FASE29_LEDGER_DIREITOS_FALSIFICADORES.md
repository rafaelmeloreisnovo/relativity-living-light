# FASE 29 — Ledger Temporal (D5), Direitos de Dataset (D6) e Bundle de Falsificadores (D7)

> **Estado:** gaps D5/D6/D7 da FASE 28 materializados  
> **Claim boundary:** `claim_allowed=false`  
> **Data:** 2026-07-20

---

## 1. Contexto

A FASE 28 construiu o mapa de rotas vetoriais Ω e a floresta de conhecimento, identificando três gaps TOKEN_VAZIO prioritários no blueprint:

| Gap | Direção | Nó | Status antes |
|-----|---------|----|-------------|
| N-TEMPORAL-MEMORY-GAP | D5 | Ledger append-only de estados | TOKEN_VAZIO |
| N-DATA-RIGHTS-GAP | D6 | Manifesto de direitos de datasets | TOKEN_VAZIO |
| N-HOLDOUT-GAP + N-FALSIFIER-GAP | D7 | Bundle de falsificadores + holdout | TOKEN_VAZIO |

O `next_gate` declarado no blueprint:

```text
Materialize historical route events, close rights and holdout gates,
then evaluate baseline ML readiness without enabling training.
```

Esta fase materializa os três artefatos. Não fecha o holdout (requer decisão de splits — P1 pendente), mas documenta o gap explicitamente.

---

## 2. D5 — Ledger de Transições de Estado

**Arquivo:** `results/state_transition_ledger.jsonl`

Ledger append-only com 17 eventos cobrindo todas as transições epistêmicas de FASE 1 a FASE 29:

| Evento | Transição | Nó | Fase |
|--------|-----------|-----|------|
| EVT-001 | ABSENT → AUTHORED | RLL v1.0.0 | — (2025-09-19) |
| EVT-002 | ABSENT → INGESTED | DESI DR2 BAO | — (2026-07-02) |
| EVT-003 | TOKEN_VAZIO → PIPELINE_READY | Pipeline CI P0 | FASE 7 |
| EVT-004 | TOKEN_VAZIO → VERIFIED_AT_SOURCE | F-COS-01 PASS | FASE 4 |
| EVT-005 | TOKEN_VAZIO → VERIFIED_AT_SOURCE | F-COS-02 PASS | FASE 4 |
| EVT-006 | TOKEN_VAZIO → CLOSED_FAIL | F-COS-03 FAIL [E] | FASE 20 |
| EVT-007 | TOKEN_VAZIO → CLOSED_FAIL | F-COS-04 FAIL [E] | FASE 20 |
| EVT-008 | TOKEN_VAZIO → VERIFIED_AT_SOURCE | F-COS-05 PASS | FASE 13 |
| EVT-009 | TOKEN_VAZIO → CLOSED_RESOLVED | G1 MCMC joint | FASE 20 |
| EVT-010 | TOKEN_VAZIO → CLOSED_RESOLVED | G2 rd calibrado | FASE 19 |
| EVT-011 | TOKEN_VAZIO → CLOSED_RESOLVED | G3 Bayes Factor | FASE 20 |
| EVT-012 | TOKEN_VAZIO → CLOSED_RESOLVED | G4 bias E&H | FASE 22 |
| EVT-013 | PARTIAL → READY_FOR_TEST | Pipeline Linear FASE 24 | FASE 24 |
| EVT-014 | ABSENT → STRUCTURED | Campo Entrópico TOKEN_VAZIO | FASE 26 |
| EVT-015 | ABSENT → OPERATIONAL | Ω7 Operational | FASE 27 |
| EVT-016 | ABSENT → BLUEPRINT | Route Forest FASE 28 | FASE 28 |
| EVT-017 | TOKEN_VAZIO → OPENED | N-TEMPORAL-MEMORY-GAP | FASE 29 |

**Invariante do ledger:** cada evento tem `timestamp`, `transition`, `region`, `direction`, `refs` e `claim_allowed`. Nenhum evento pode ser apagado — apenas novos eventos são adicionados.

**Formato:** JSONL (uma linha por evento) — compatível com `artifacts/EVOLUTION_TRAIL.jsonl` e com o schema `schemas/information_evolution_trace.schema.json`.

---

## 3. D6 — Manifesto de Direitos de Datasets

**Arquivo:** `data/contracts/dataset_rights_manifest.json`

Documenta 5 datasets com licença, privacidade, autoria e gates ML explícitos:

| Dataset | Licença verificada | training_allowed | rights_complete |
|---------|-------------------|--------------------|-----------------|
| Pantheon+SH0ES | ✅ Public domain | ❌ | ✅ |
| DESI DR2 BAO | ✅ CC-BY 4.0 | ❌ | ✅ |
| Moresco H(z) | ⚠️ Não verificado | ❌ | ❌ |
| Planck 2018 | ✅ ESA public | ❌ | ✅ |
| Dense Features | ✅ Interno | ❌ | ✅ |

**training_allowed = false para todos** — bloqueado até 3 gaps fechados:

- G-RIGHTS-01: licença Moresco H(z) não verificada [P2]
- G-RIGHTS-02: holdout split não definido [P1]
- G-RIGHTS-03: model-card template inexistente [P2]

---

## 4. D7 — Bundle de Falsificadores

**Arquivo:** `data/contracts/rll_falsifier_bundle.json`

Integra todos os F-COS-01..05 em formato estruturado com resultado, threshold, método, fonte e status:

| Falsificador | Threshold | Resultado | Status |
|-------------|-----------|-----------|--------|
| F-COS-01: ΔAIC | < 10 | 3.805 | ✅ PASS [E] |
| F-COS-02: χ²_red | < 1.05 | 0.4387 | ✅ PASS [E] |
| F-COS-03: z_t ∈ [0.5,1.5] | intervalo | 0.30 | ❌ FAIL [E] |
| F-COS-04: ln(B₁₀) > −5 | > −5 | −6.190±0.691 | ❌ FAIL [E] |
| F-COS-05: χ²_nom < 150 | < 150 | 93.806 | ✅ PASS [E] |

**Comparação baseline:**

```
ΛCDM:  χ²_Pantheon=710.808; dof=3; ln_evidence=0 (referência)
RLL:   χ²_Pantheon=710.613; dof=6; ln_B₁₀=−6.190±0.691
```

**Conclusão:** `claim_allowed=false`. F-COS-03 e F-COS-04 FAIL [E]. Resultado empírico negativo — ΛCDM fortemente preferido pelos dados disponíveis. Não é TOKEN_VAZIO.

---

## 5. Atualização do Blueprint da Floresta

O nó `N-TEMPORAL-MEMORY-GAP` foi aberto formalmente (EVT-017). O nó `N-FALSIFIER-GAP` tem agora o bundle em `data/contracts/rll_falsifier_bundle.json`. O nó `N-DATA-RIGHTS-GAP` tem agora o manifesto em `data/contracts/dataset_rights_manifest.json`.

Nenhum dos três nodes muda para `VERIFIED` nesta fase — eles passam de `TOKEN_VAZIO` para `PARTIAL` (documentação existe, holdout e model-card ainda abertos).

---

## 6. Correção de Dependência

`jsonschema>=4.0` adicionado a `requirements.txt` — ausência causava falha em todos os testes de FASES 26-28 no ambiente de desenvolvimento.

---

## 7. Gaps Remanescentes (não fechados nesta fase)

| Gap | Prioridade | Resolução |
|-----|-----------|-----------|
| G-RIGHTS-02: holdout split | P1 | Criar `data/contracts/holdout_split_manifest.json` |
| G-RIGHTS-03: model-card | P2 | Criar `docs/ml/MODEL_CARD_TEMPLATE.md` |
| G-RIGHTS-01: licença Moresco | P2 | Verificar com repositório/journal |
| N-DIMENSIONAL-GAP (D3) | P2 | Registro completo de invariantes dimensionais |

---

## 8. Retroalimentação R3

```text
F_ok   = D5 (ledger 17 eventos), D6 (manifesto 5 datasets), D7 (bundle F-COS-01..05) materializados
F_gap  = holdout split e model-card ausentes; licença Moresco não verificada; D3 dimensional ainda incompleto
F_next = criar holdout_split_manifest.json; fechar D3; consolidar D5+D6+D7 no blueprint atualizado da floresta
```
