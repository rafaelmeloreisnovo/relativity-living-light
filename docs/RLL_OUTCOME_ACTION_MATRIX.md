# RLL Outcome Action Matrix

> Escopo: para cada possível resultado do scanner/governança, definir ação técnica, linguagem permitida, linguagem proibida e política de release.

---

## Matriz compacta

| status | significado | release_policy |
|---|---|---|
| `CLAIM_BLOCKED` | A tabela atual não sustenta claim positivo ou algum gate falhou. | Não publicar como descoberta; permitir apenas relatório diagnóstico/auditoria. |
| `PASS_LIMITED` | RLL não é pior que CPL pelos critérios escaneados, mas faltam gates fortes. | Permitir wording metodológico limitado; bloquear linguagem de descoberta. |
| `PARTIAL` | Há cálculo, mas covariância/baseline/dataset/benchmark está incompleto. | Relatório interno ou publicação com limitações front-page. |
| `TOKEN_VAZIO` | Evidência insuficiente para responder sem inventar. | Sem claim científico; apenas gap ledger. |
| `AUDIT_FAIL` | Falhou registry, schema, N-k-dof, JSON, CI ou linguagem. | Bloquear release/claim até auditoria passar. |
| `RUNTIME_PENDING` | A rota existe, mas o fit/ablação ainda não foi executado. | Roadmap/status apenas; bloquear interpretação de resultado. |

---

## CLAIM_BLOCKED

**Linguagem permitida**

> Nesta rodada, o claim positivo do RLL está bloqueado; o relatório deve explicar o motivo, comparar com CPL e registrar TOKEN_VAZIO/PENDING onde aplicável.

**Ações obrigatórias**

- Manter bloqueio de wording de superioridade.
- Publicar apenas interpretação negativa/diagnóstica.
- Rodar ou agendar ablação H0/r_d se `H0_all_equal=True`.
- Reportar `Delta AICc/BIC` contra CPL.
- Reportar `Os0`, `zt`, `wt` e colapso de `Os0`.
- Marcar covariância, Pantheon, CMB ou growth ausentes como TOKEN_VAZIO/PENDING.

---

## PASS_LIMITED

**Linguagem permitida**

> RLL não é pior que CPL nesta tabela pelos critérios escaneados; o resultado é limitado e ainda depende de covariância, ablação, MCMC e benchmark físico.

**Ações obrigatórias**

- Rotular como `PASS_LIMITED`, não confirmado.
- Rodar H0/r_d ablation e rescan de cada CSV.
- Materializar política de covariância antes de claim forte.
- Rodar MCMC/nested sampling antes de inferência publicável.
- Rodar CLASS/CAMB ou manter growth claim bloqueado.

---

## PARTIAL

**Linguagem permitida**

> Resultado parcial: há cálculo, mas a interpretação fica limitada por lacunas explícitas de covariância, baseline, dataset ou benchmark.

**Ações obrigatórias**

- Declarar cada bloco ausente.
- Separar calculado de TOKEN_VAZIO.
- Evitar ranking claims se CPL ou covariância faltar.
- Adicionar manifests de dataset/covariância antes de rerun.

---

## TOKEN_VAZIO

**Linguagem permitida**

> TOKEN_VAZIO: não há evidência computacional suficiente para responder sem inventar resultado.

**Ações obrigatórias**

- Parar geração de claim.
- Identificar arquivo, dataset, covariância, baseline ou run ausente.
- Criar tarefa de reprodutibilidade antes de interpretar.

---

## AUDIT_FAIL

**Linguagem permitida**

> A auditoria falhou; nenhum claim científico deve ser emitido até correção do gate.

**Ações obrigatórias**

- Corrigir gate falho.
- Rodar registry validator e evidence scanner novamente.
- Registrar comando falho e erro exato.

---

## RUNTIME_PENDING

**Linguagem permitida**

> PENDING: a matriz/rota existe, mas o fit cosmológico ainda não foi executado para esta política.

**Ações obrigatórias**

- Executar a ablação ou marcar como pending.
- Não sobrescrever evidência anterior sem `run_id`.
- Escanear cada CSV gerado independentemente.

---

## Comando

```bash
python3 tools/apply_rll_outcome_protocol.py
```

Com matriz:

```bash
python3 tools/apply_rll_outcome_protocol.py --write-matrix
```

Saídas:

```text
results/audit/rll_outcome_action_plan.json
results/audit/rll_outcome_action_plan.md
data/inputs/cosmology_joint/rll_outcome_action_matrix.json
docs/RLL_OUTCOME_ACTION_MATRIX.md
```
