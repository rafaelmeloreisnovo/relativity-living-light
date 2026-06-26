# RLL Issues #420–#423 Execution Ledger

> Data UTC: 2026-06-17  
> Escopo: aplicar no repositório os gates e artefatos derivados das issues #420, #421, #422 e #423, incluindo rota para cada possível resultado do scanner.

---

## 1. Issues cobertas

| Issue | Objetivo | Status aplicado |
|---|---|---|
| #420 | Registry-driven k/covariance gates before academic claims | Parcial aplicado: registry validator + governance wrapper + claim boundary report + outcome protocol. O pipeline científico ainda precisa consumir registry para calcular `k` automaticamente. |
| #421 | Academic ablation ladder | Parcial aplicado: scanner, decision tree, H0/r_d matrix, outcome routing e issue links. A execução dos fits permanece a próxima etapa computacional. |
| #422 | Wire evidence scan outputs into reports and claim gates | Parcial aplicado: governance wrapper gera gate report; checker de linguagem e outcome action plan criados. Integração com todos os geradores de relatório ainda pendente. |
| #423 | Run H0 and r_d ablation after H0 warning | Parcial aplicado: matriz JSON/CSV/MD e generator. Fits de ablação ainda não executados. |

---

## 2. Arquivos aplicados nesta etapa

| Arquivo | Função |
|---|---|
| `tools/run_rll_academic_claim_governance.py` | Orquestra registry validator + evidence scanner + gate report. |
| `tools/make_h0_rd_ablation_matrix.py` | Gera a matriz H0/r_d exigida pela issue #423. |
| `tools/apply_rll_outcome_protocol.py` | Roteia cada possível resultado (`CLAIM_BLOCKED`, `PASS_LIMITED`, `PARTIAL`, `TOKEN_VAZIO`, `AUDIT_FAIL`, `RUNTIME_PENDING`) para ações, artefatos e linguagem permitida. |
| `tools/check_rll_report_claim_language.py` | Bloqueia linguagem positiva quando `claim_status=CLAIM_BLOCKED`. |
| `data/inputs/cosmology_joint/h0_rd_ablation_matrix.json` | Matriz canônica de ablação H0/r_d em JSON. |
| `data/inputs/cosmology_joint/h0_rd_ablation_matrix.csv` | Matriz canônica de ablação H0/r_d em CSV. |
| `data/inputs/cosmology_joint/rll_outcome_action_matrix.json` | Matriz canônica de ações por resultado possível. |
| `docs/RLL_H0_RD_ABLATION_MATRIX.md` | Explicação operacional da matriz H0/r_d. |
| `docs/RLL_OUTCOME_ACTION_MATRIX.md` | Explicação operacional da matriz de ações por resultado. |
| `.github/workflows/academic-parameter-governance.yml` | CI atualizado para rodar todos os gates principais e validar todos os statuses possíveis. |

---

## 3. Comandos operacionais

### Gate integrado

```bash
python3 tools/run_rll_academic_claim_governance.py
```

Saídas:

```text
results/audit/rll_model_evidence_scan.json
results/audit/rll_model_evidence_scan.md
results/audit/rll_academic_claim_gate_report.md
```

### Matriz H0/r_d

```bash
python3 tools/make_h0_rd_ablation_matrix.py
```

Saídas:

```text
data/inputs/cosmology_joint/h0_rd_ablation_matrix.json
data/inputs/cosmology_joint/h0_rd_ablation_matrix.csv
docs/RLL_H0_RD_ABLATION_MATRIX.md
```

### Protocolo de resultado possível

```bash
python3 tools/apply_rll_outcome_protocol.py
```

Saídas:

```text
results/audit/rll_outcome_action_plan.json
results/audit/rll_outcome_action_plan.md
```

Para regravar a matriz canônica:

```bash
python3 tools/apply_rll_outcome_protocol.py --write-matrix
```

### Checagem de linguagem em relatório

```bash
python3 tools/check_rll_report_claim_language.py \
  --scan results/audit/rll_model_evidence_scan.json \
  path/to/report.md
```

---

## 4. Status de verdade operacional

O que foi aplicado com segurança:

```text
registry validation
current-table evidence scan
claim gate wrapper
H0/r_d ablation policy matrix
outcome action matrix for every possible result
report claim-language checker
CI execution surface
```

O que permanece TOKEN_VAZIO ou PENDING:

```text
actual H0/r_d cosmological fits
registry-derived k inside every likelihood routine
automatic report integration across all paper drafts
CLASS/CAMB benchmark
dataset covariance materialization for every strong claim
```

---

## 5. Claim boundary atual

Com a tabela atualmente versionada, a leitura esperada permanece:

```text
best_by_AICc = CPL_w0waCDM_joint_real
best_by_BIC  = CPL_w0waCDM_joint_real
H0_all_equal = True
RLL Os0      = 0.0
claim_status = CLAIM_BLOCKED
```

Frase permitida:

> Nesta rodada, o RLL não faz melhor que CPL/w0waCDM; o claim positivo fica bloqueado até nova ablação e governança de covariância.

Frase proibida:

> RLL está provado ou RLL vence CPL.

---

## 6. Resultado possível → ação

| Resultado | Ação |
|---|---|
| `CLAIM_BLOCKED` | Bloquear claim positivo; publicar diagnóstico; rodar ablação H0/r_d se aplicável. |
| `PASS_LIMITED` | Permitir wording limitado; exigir covariância, MCMC, ablação e CLASS/CAMB antes de claim forte. |
| `PARTIAL` | Marcar limitações na primeira página; separar calculado de TOKEN_VAZIO. |
| `TOKEN_VAZIO` | Parar claim; abrir/girar ledger de evidência ausente. |
| `AUDIT_FAIL` | Corrigir gate; não publicar claim. |
| `RUNTIME_PENDING` | Executar fit/ablação ou manter como pendente sem interpretação. |

---

## 7. Próxima execução técnica

1. Rodar a matriz H0/r_d gerando CSVs em `results/structure_d/ablation/`.
2. Rodar `tools/run_rll_academic_claim_governance.py --input <ablation_csv>` para cada CSV.
3. Rodar `tools/apply_rll_outcome_protocol.py` para cada scan.
4. Fazer relatórios importarem `results/audit/rll_academic_claim_gate_report.md` e `results/audit/rll_outcome_action_plan.md`.
5. Só permitir claim positivo se scanner, outcome protocol e covariância permitirem.

---

## 8. Retroalimentação

```text
F_ok   = issues convertidas em gates/scripts/matriz/CI/outcome protocol
F_gap  = fits de ablação e consumo automático em todos os relatórios ainda pendentes
F_next = executar as ablações reais e conectar relatórios finais ao gate report + outcome plan
```
