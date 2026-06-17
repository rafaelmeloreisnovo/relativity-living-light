# RLL Calculable Evidence Scan Protocol

> Escopo: definir o que é seguro calcular a partir dos resultados existentes e o que ainda é TOKEN_VAZIO até nova execução, covariância ou benchmark externo.

---

## 1. Pergunta operacional

A pergunta não é:

> “RLL é verdade?”

A pergunta calculável é:

> “Dado um CSV de resultados já gerado, o RLL melhora, empata ou piora contra os baselines LCDM, wCDM e CPL segundo métricas explícitas e com claim boundary?”

---

## 2. O que pode ser calculado com certeza do CSV

| Cálculo | Fonte | Interpretação segura |
|---|---|---|
| Ranking por AICc | coluna `AICc` | Qual modelo é preferido pelo critério na tabela atual. |
| Ranking por BIC | coluna `BIC` | Qual modelo é preferido com penalização BIC na tabela atual. |
| Delta AICc vs CPL | `AICc(RLL)-AICc(CPL)` | Se RLL melhora ou piora contra CPL. |
| Delta BIC vs CPL | `BIC(RLL)-BIC(CPL)` | Se RLL sobrevive à penalização forte contra CPL. |
| Consistência `N-k=dof` | colunas `N`, `k`, `dof` | Se a tabela respeita a contagem básica de graus de liberdade. |
| H0 igual em todos os modelos | coluna `H0` | Sinal de prior/fix/borda; não prova erro, mas exige checagem. |
| Colapso de `Os0` | coluna `Os0` no RLL | Se amplitude autoral RLL foi usada ou colapsou para zero. |
| Componentes de chi2 | colunas `chi2_*` | Onde cada modelo ganha/perde dentro da tabela. |
| Presença de baselines | nomes dos modelos | Se LCDM, wCDM, CPL e RLL estão na mesma comparação. |

---

## 3. O que NÃO pode ser calculado só do CSV

| Item | Motivo | Status correto |
|---|---|---|
| Verdade física do RLL | CSV não substitui inferência física. | TOKEN_VAZIO |
| Robustez posterior | Requer MCMC/nested sampling. | TOKEN_VAZIO |
| Correção de covariância | Requer arquivos de covariância e hashes. | TOKEN_VAZIO ou PARTIAL |
| Validação growth | Requer CLASS/CAMB ou proxy declarado. | CLAIM_BLOCKED se ausente |
| Pantheon+ forte | Requer raw files + STAT+SYS covariance + hash. | CLAIM_BLOCKED se ausente |
| CMB forte | Requer covariância completa ou likelihood adequada. | PARTIAL/CLAIM_BLOCKED |
| Publicação como descoberta | Exige robustez multi-dataset e revisão. | PROIBIDO no estado parcial |

---

## 4. Script aplicado

```bash
python3 tools/scan_rll_model_evidence.py
```

Saídas padrão:

```text
results/audit/rll_model_evidence_scan.json
results/audit/rll_model_evidence_scan.md
```

Modo somente diagnóstico:

```bash
python3 tools/scan_rll_model_evidence.py --no-write
```

---

## 5. Regras de claim

### PASS_LIMITED

Permitido somente se:

```text
RLL delta AICc vs CPL <= 0
RLL delta BIC vs CPL <= 0
baselines presentes
N-k=dof consistente
registry válido
```

Mesmo assim, o claim é limitado até covariância/reprodutibilidade/MCMC.

### CLAIM_BLOCKED

Bloquear se:

```text
CPL ausente
RLL ausente
RLL pior que CPL por AICc/BIC
Os0 colapsa para zero
N-k-dof inconsistente
registry ausente/inválido
```

### PARTIAL

Usar quando:

```text
resultado existe, mas covariância/CMB/Pantheon/growth ainda está incompleto
```

---

## 6. Interpretação da tabela atual conhecida

Na tabela atual `results/structure_d/joint_real_likelihood.csv`, o scanner deve detectar:

```text
best_by_AICc = CPL_w0waCDM_joint_real
best_by_BIC  = CPL_w0waCDM_joint_real
H0_all_equal = True
RLL Os0      = 0.0
claim_status = CLAIM_BLOCKED
```

Interpretação segura:

> Nesta rodada, os resultados favorecem CPL/w0waCDM. O RLL não deve reivindicar melhora porque fica pior por AICc/BIC e sua amplitude autoral `Os0` colapsa para zero.

Interpretação proibida:

> “RLL está provado” ou “RLL vence” com base nessa rodada.

---

## 7. Próxima integração operacional

- [ ] Adicionar o scanner ao CI.
- [ ] Fazer o pipeline de likelihood chamar o scanner após gerar CSV.
- [ ] Fazer relatórios importarem `rll_model_evidence_scan.json`.
- [ ] Bloquear release acadêmico quando `claim_status=CLAIM_BLOCKED`.
- [ ] Rodar ablação H0/r_d/CPL/covariância/neutrinos/growth.

---

## 8. Retroalimentação

```text
F_ok   = cálculo seguro definido e script aplicado
F_gap  = scanner ainda não está integrado no CI/pipeline de likelihood
F_next = conectar scanner ao workflow e aos relatórios de resultado
```
