# Applied Changes — RLL Evidence Scan Layer — 2026-06-17

## Objetivo

Responder operacionalmente à pergunta:

> O que pode ser calculado com certeza para dizer se o RLL faz bem aos dados?

## Arquivos aplicados

| Arquivo | Função |
|---|---|
| `tools/scan_rll_model_evidence.py` | Scanner calculável de evidência: ranking, deltas, H0, Os0, k/dof e claim status. |
| `docs/RLL_CALCULABLE_EVIDENCE_SCAN_PROTOCOL.md` | Protocolo do que pode/não pode ser calculado do CSV. |
| `docs/RLL_CERTAINTY_CALCULATION_BOUNDARY.md` | Fronteira epistemológica: certeza operacional vs TOKEN_VAZIO. |
| `docs/RLL_DATA_FIT_DECISION_TREE.md` | Árvore de decisão para responder “faz bem meus dados?”. |
| `.github/workflows/academic-parameter-governance.yml` | CI atualizado para rodar registry validator + evidence scanner. |

## Issues abertas

| Issue | Função |
|---|---|
| #422 | Conectar outputs do scanner aos relatórios e claim gates. |
| #423 | Rodar ablação H0/r_d porque a tabela atual mostra H0 igual em todos os modelos. |

## Resultado esperado da tabela atual

```text
best_by_AICc = CPL_w0waCDM_joint_real
best_by_BIC  = CPL_w0waCDM_joint_real
H0_all_equal = True
RLL Os0      = 0.0
claim_status = CLAIM_BLOCKED
```

## Claim seguro

> Nesta rodada, RLL não faz melhor que CPL/w0waCDM nos dados usados. O claim autoral fica bloqueado porque `Os0` colapsa para zero e a tabela mostra `H0` igual em todos os modelos, exigindo ablação H0/r_d.

## Claim proibido

> RLL está provado.
> RLL vence CPL.
> RLL faz bem aos dados sem qualificação.

## Próximo passo

Rodar:

```bash
python3 tools/scan_rll_model_evidence.py
```

Depois integrar `results/audit/rll_model_evidence_scan.json` aos relatórios acadêmicos.
