# RLL — Figure and Table Manifest

**Status:** manifesto de figuras e tabelas necessárias para paper, suplemento e leitura executiva.  
**Regra:** este arquivo não gera imagens nem altera resultados; ele define o que deve existir, de onde vem e qual gate bloqueia.

---

## 1. Objetivo

Transformar o repositório em narrativa científica visual sem overclaim.

Cada figura ou tabela deve indicar:

- fonte dos dados;
- script ou função geradora;
- status;
- claim permitido;
- lacuna bloqueante;
- próximo ato.

---

## 2. Figuras mínimas

| ID | Figura | Fonte | Script/função sugerida | Status | Gate |
|---|---|---|---|---|---|
| F1 | Pipeline claim-gated RLL | docs + results | diagrama manual/mermaid | pendente | nenhum dado novo |
| F2 | Transição logística RLL `f(z)` | `src/rll/cosmology_fairness.py` | `rll_transition` | pendente | parâmetros canônicos/fit |
| F3 | `E(z)` / `H(z)` comparando modelos | funções cosmológicas | `e2_lcdm`, `e2_wcdm`, `e2_cpl`, `e2_rll_logistic` | pendente | usar parâmetros do artefato |
| F4 | Residuals BAO por modelo | DESI + rows atuais | script novo | pendente | cuidado com covariância |
| F5 | `w_eff_RLL(z)` vs `w_CPL(z)` | funções cosmológicas | `w_eff_rll_density` + CPL | pendente | ablação A8 |
| F6 | Ranking por ICs no smoke atual | JSON/CSV atual | tabela/plot simples | pendente | rotular smoke |
| F7 | Frequência `Os0=0.0` por seed | robust fit | script robusto | TOKEN_VAZIO_ROBUST_FIT | output versionado |
| F8 | Mapa de ablações | matriz de ablação | diagrama | pendente | sem fit novo |
| F9 | Pantheon+ residuals | Pantheon+ | script futuro | TOKEN_VAZIO_DATASET | dataset/covariância |
| F10 | Growth externo | CLASS/CAMB | script futuro | TOKEN_VAZIO_BACKEND | backend externo |

---

## 3. Tabelas mínimas

| ID | Tabela | Fonte | Status | Gate |
|---|---|---|---|---|
| T1 | Resultados atuais paper-ready | `docs/RLL_CURRENT_RESULTS_PAPER_TABLE.md` | criada | smoke only |
| T2 | Parâmetros por modelo e k | JSON/CSV atual | criada dentro de T1 | smoke only |
| T3 | Decomposição chi2 por bloco | JSON/CSV atual | criada dentro de T1 | smoke only |
| T4 | Deltas contra LCDM | JSON atual | criada dentro de T1 | smoke only |
| T5 | Deltas contra CPL | robust/ablação | TOKEN_VAZIO_ROBUST_FIT | output versionado |
| T6 | Robust seeds 1..10 | robust fit | TOKEN_VAZIO_ROBUST_FIT | output versionado |
| T7 | Ablation matrix | `docs/RLL_ABLATION_MATRIX.md` | criada | execução pendente |
| T8 | Claim gate ledger | `docs/RLL_CLAIM_GATE_LEDGER.md` | criada | claims bloqueados |
| T9 | Dataset provenance | manifests/data | parcial | hashes e materialização |
| T10 | Missing calculations ledger | `docs/RLL_MISSING_CALCULATIONS_LEDGER.md` | existente | manter vivo |

---

## 4. Ordem de geração recomendada

### Etapa segura imediata

Pode ser feita sem alterar resultado canônico:

1. F1 pipeline claim-gated;
2. F6 ranking por ICs smoke;
3. F8 mapa de ablações;
4. T1/T2/T3/T4 já consolidadas;
5. T7/T8 já criadas.

### Etapa com scripts, mas sem novos datasets

Exige apenas cuidado de output:

1. F2 transição logística;
2. F3 `E(z)`/`H(z)`;
3. F5 `w_eff_RLL(z)` vs `w_CPL(z)`;
4. F4 BAO residuals se o script usar os mesmos inputs já materializados.

### Etapa bloqueada por robust fit/dados/backends

Não executar até fechar lacunas:

1. F7 frequência `Os0=0.0`;
2. T5/T6 robust seeds;
3. F9 Pantheon+;
4. F10 growth externo.

---

## 5. Legenda de status

| Status | Significado |
|---|---|
| criada | já existe no repositório |
| pendente | pode ser criado sem novo dado, mas ainda não foi |
| TOKEN_VAZIO_ROBUST_FIT | depende de bateria robusta |
| TOKEN_VAZIO_DATASET | depende de materialização de dado |
| TOKEN_VAZIO_COVARIANCE | depende de matriz/covariância completa |
| TOKEN_VAZIO_BACKEND | depende de backend externo |

---

## 6. Claim boundary visual

Toda figura/tabela de smoke deve carregar nota:

```text
Preliminary smoke/sanity run. Not a final cosmological fit. claim_allowed=false.
```

Toda figura/tabela robusta futura deve carregar:

```text
Robust fit artifact: seed/maxiter/output hash required.
```

Toda figura/tabela com dataset parcial deve carregar:

```text
Partial dataset/covariance. Strong claims blocked.
```

---

## 7. R3

```text
F_ok   = manifesto de figuras e tabelas criado; saídas paper/suplemento agora têm mapa.
F_gap  = figuras ainda não geradas; robust fit/datasets/backends pendentes.
F_next = criar índice de próximos atos seguros para ordenar execução sem perguntas repetidas.
```
