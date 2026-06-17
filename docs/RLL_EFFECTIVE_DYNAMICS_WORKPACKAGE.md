# RLL — Effective Dynamics Workpackage

**Status:** pacote de trabalho analítico para derivar funções efetivas a partir de artefatos versionados.  
**Escopo:** pós-processamento diagnóstico; não executa novo fit, não altera dados brutos, não altera resultados canônicos, não altera `claim_allowed=false`.

---

## 1. Objetivo

Organizar a camada analítica necessária para comparar RLL contra LCDM, wCDM e CPL/w0waCDM em espaço funcional, não apenas por métricas escalares.

Este workpackage implementa a primeira etapa do `F_next` definido em:

```text
RLL_FRONTIER_DYNAMICS_AND_ANOMALY_LEDGER.md
```

---

## 2. Arquivos criados

| Arquivo | Função |
|---|---|
| `scripts/analysis/structure_d_effective_dynamics.py` | calcula funções efetivas pós-fit |
| `tests/test_structure_d_effective_dynamics.py` | cobre invariantes básicos do analisador |

---

## 3. Entradas

Entrada padrão:

```text
results/structure_d/joint_real_likelihood.json
```

A entrada deve ser um JSON de likelihood conjunta com campo:

```text
rows[]
```

contendo os modelos:

```text
LCDM_joint_real
wCDM_joint_real
CPL_w0waCDM_joint_real
RLL_joint_real
```

---

## 4. Saídas

Diretório padrão:

```text
results/structure_d/effective_dynamics/
```

Arquivos gerados:

```text
joint_real_likelihood_effective_dynamics.csv
joint_real_likelihood_effective_dynamics_manifest.json
```

Esses arquivos são derivados e não substituem outputs canônicos.

---

## 5. Quantidades computadas

| Quantidade | Significado |
|---|---|
| `E(z)` | expansão normalizada `H(z)/H0` |
| `H(z)` | taxa de expansão em km/s/Mpc |
| `rho_de_eff(z)` | densidade efetiva residual após matéria/radiação |
| `w_eff(z)` | equação de estado efetiva reconstruída |
| `q(z)` | parâmetro de desaceleração |
| `D_C_Mpc(z)` | distância comóvel por integração |
| `rll_transition_f(z)` | fração logística RLL, quando modelo é RLL |
| `rll_logit_f(z)` | logit da transição RLL |

---

## 6. Formalismo

### 6.1 Expansão normalizada

```math
E(z)=H(z)/H_0
```

### 6.2 Densidade escura efetiva

```math
\rho_{DE,eff}(z)\propto E^2(z)-\Omega_m(1+z)^3-\Omega_r(1+z)^4
```

### 6.3 Equação de estado efetiva

```math
w_{eff}(z)=-1+\frac{1+z}{3}\frac{d\ln\rho_{DE,eff}(z)}{dz}
```

### 6.4 Parâmetro de desaceleração

```math
q(z)=-1+\frac{1+z}{2E^2(z)}\frac{dE^2(z)}{dz}
```

### 6.5 Distância comóvel

```math
D_C(z)=\frac{c}{H_0}\int_0^z\frac{dz'}{E(z')}
```

### 6.6 Logit da transição RLL

```math
f(z)=\frac{1}{1+\exp((z-z_t)/w_t)}
```

```math
\operatorname{logit}_{RLL}(z)=\ln\left(\frac{1-f(z)}{f(z)}\right)
```

---

## 7. Comando de uso

```bash
python scripts/analysis/structure_d_effective_dynamics.py
```

Com saída customizada:

```bash
python scripts/analysis/structure_d_effective_dynamics.py \
  --input-json results/structure_d/joint_real_likelihood.json \
  --output-dir results/structure_d/effective_dynamics \
  --z-min 0.0 \
  --z-max 3.0 \
  --n-grid 301
```

---

## 8. Interpretação científica

Este pacote permite responder perguntas que AIC/BIC sozinhos não respondem:

```text
A curva w_eff_RLL(z) se aproxima de w_CPL(z)?
A transição logística cria assinatura própria em q(z)?
RLL altera distâncias integradas de forma observável?
O logit da transição é compatível com uma reconstrução efetiva?
```

---

## 9. Claim boundary

Este pacote não permite afirmar:

```text
RLL confirmado
RLL resolve energia escura
RLL resolve H0/S8
RLL vence CPL
```

Permite afirmar:

```text
funções efetivas foram derivadas de artefatos existentes
comparação funcional RLL vs CPL tornou-se tecnicamente possível
próxima etapa robusta pode ser formulada em termos de curvas, não apenas escalares
```

---

## 10. R3

```text
F_ok   = estrutura analítica para E/H/w_eff/q/distâncias/logit criada.
F_gap  = script ainda precisa ser executado no CI/local; plots e comparador GEDE ainda faltam.
F_next = criar gerador de figuras/tabelas para comparar RLL vs CPL em espaço funcional.
```
