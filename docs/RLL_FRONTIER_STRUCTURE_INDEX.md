# RLL — Frontier Structure Index

**Status:** índice organizador da camada de fronteira, dinâmica efetiva e anomalias.  
**Escopo:** mapa documental; não altera dados, fórmulas, resultados ou claims.

---

## 1. Objetivo

Organizar os arquivos criados para transformar a investigação RLL em uma sequência operacional:

```text
estado atual → dinâmica efetiva → comparação funcional → ablação → robust fit → posterior → claim review
```

---

## 2. Núcleo documental

| Documento | Função |
|---|---|
| `docs/RLL_FRONTIER_DYNAMICS_AND_ANOMALY_LEDGER.md` | documento-mãe de fronteira e anomalias |
| `docs/RLL_EFFECTIVE_DYNAMICS_WORKPACKAGE.md` | pacote de trabalho para funções efetivas |
| `docs/RLL_CURRENT_RESULTS_PAPER_TABLE.md` | tabela canônica do smoke atual |
| `docs/RLL_ABLATION_MATRIX.md` | matriz de ablações necessárias |
| `docs/RLL_FIGURE_TABLE_MANIFEST.md` | manifesto de figuras e tabelas |
| `docs/RLL_CLAIM_GATE_LEDGER.md` | limites de claims permitidos/bloqueados |
| `docs/RLL_RISK_REGISTER.md` | riscos científicos e operacionais |
| `docs/RLL_OUTPUT_STEM_SAFE_WRAPPER.md` | rota segura para outputs versionados |

---

## 3. Núcleo computacional

| Script/teste | Função |
|---|---|
| `scripts/run_structure_d_joint_likelihood.py` | executa likelihood com output stem seguro |
| `scripts/analysis/structure_d_effective_dynamics.py` | deriva `E(z)`, `H(z)`, `w_eff(z)`, `q(z)`, `D_C(z)` |
| `tests/test_structure_d_output_stem_wrapper.py` | testa segurança do output stem |
| `tests/test_structure_d_effective_dynamics.py` | testa invariantes da camada dinâmica efetiva |

---

## 4. Diretórios de saída recomendados

```text
results/structure_d/
  joint_real_likelihood.json
  joint_real_likelihood.csv
  joint_real_likelihood_covariance_manifest.json

results/structure_d/effective_dynamics/
  joint_real_likelihood_effective_dynamics.csv
  joint_real_likelihood_effective_dynamics_manifest.json

results/structure_d/robust_fits/
  joint_real_likelihood_seed_1_maxiter_100.json
  joint_real_likelihood_seed_1_maxiter_100.csv
  ...

results/structure_d/figures/
  rll_vs_cpl_w_eff.csv
  rll_vs_cpl_q.csv
  rll_vs_cpl_distance_delta.csv
```

---

## 5. Ordem operacional segura

### Etapa 1 — confirmar testes

```bash
python -m pytest -q tests/test_structure_d_output_stem_wrapper.py tests/test_structure_d_effective_dynamics.py
```

### Etapa 2 — gerar dinâmica efetiva do smoke atual

```bash
python scripts/analysis/structure_d_effective_dynamics.py
```

### Etapa 3 — rodar robust fits versionados

```bash
for seed in 1 2 3 4 5 6 7 8 9 10; do
  STRUCTURE_D_JOINT_SEED=$seed \
  STRUCTURE_D_JOINT_MAXITER=100 \
  python scripts/run_structure_d_joint_likelihood.py \
    --output-stem "joint_real_likelihood_seed_${seed}_maxiter_100"
done
```

### Etapa 4 — derivar dinâmica efetiva para cada robust fit

```bash
for seed in 1 2 3 4 5 6 7 8 9 10; do
  python scripts/analysis/structure_d_effective_dynamics.py \
    --input-json "results/structure_d/joint_real_likelihood_seed_${seed}_maxiter_100.json" \
    --output-dir results/structure_d/effective_dynamics
 done
```

---

## 6. Claim boundary

Mesmo após gerar curvas efetivas:

```text
claim_allowed = false
```

até que:

```text
robust fits passem
CPL/GEDE sejam comparados
posterior seja produzido
ablações sejam estáveis
CMB/Pantheon+/growth gates sejam resolvidos
```

---

## 7. R3

```text
F_ok   = índice de estrutura criado; documentos, scripts, testes e saídas estão organizados.
F_gap  = falta executar scripts e gerar os artefatos derivados.
F_next = criar manifesto de outputs derivados e comparador funcional RLL vs CPL.
```
