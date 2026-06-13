# README — `joint_real_likelihood.json`

Este README explica o artefato `results/structure_d/joint_real_likelihood.json` produzido após o PR #396. Ele é descritivo e não altera os dados reais nem sobrescreve resultados existentes.

## 1. O que é este arquivo

`joint_real_likelihood.json` é um resultado conjunto de likelihood cosmológica em dados observacionais reais. Ele compara quatro famílias de modelos no mesmo pipeline:

1. `LCDM_joint_real`;
2. `wCDM_joint_real`;
3. `CPL_w0waCDM_joint_real`;
4. `RLL_joint_real`.

O arquivo registra métricas de ajuste (`chi2`) e critérios de informação (`AIC`, `AICc`, `BIC`) com contagem de pontos `N=64` e número de parâmetros `k` por modelo.

## 2. Quais datasets entram

Conforme o próprio JSON, a execução atual usa:

| bloco | caminho registrado | papel |
|---|---|---|
| Hz | `data/real/Hz_data_real.csv` | expansão H(z) |
| DESI DR2 BAO primary | `data/real/cosmology/desi_dr2_bao_primary_points.csv` | BAO |
| DESI DR2 BAO covariance | `data/real/desi_dr2_bao_covariance.csv` | covariância BAO materializada |
| fsigma8 | `data/real/cosmology/fsigma8_growth_real.csv` | crescimento/proxy de estrutura |
| CMB shift | `data/real/CMB_shift_real.json` | compressed CMB parcial |
| parameter registry | `data/inputs/cosmology_joint/parameter_origin_registry.json` | origem de parâmetros |

Itens ainda parciais ou ausentes devem ser tratados como `TOKEN_VAZIO` quando usados para claim forte:

- Pantheon+ completo: `TOKEN_VAZIO_DATASET`.
- CMB compressed likelihood completa: `TOKEN_VAZIO_COVARIANCE`.
- Growth com CLASS/CAMB: `TOKEN_VAZIO_BACKEND`.

## 3. Quais modelos entram

| modelo | descrição operacional | k |
|---|---|---:|
| LCDM | baseline cosmológico rígido | 5 |
| wCDM | extensão com `w` constante | 6 |
| CPL/w0waCDM | extensão dinâmica com `w0` e `wa` | 7 |
| RLL | candidato de transição dinâmica com `Os0`, `zt`, `wt` | 8 |

## 4. Resultado atual resumido

| modelo | chi2 | AIC | AICc | BIC | status nesta execução |
|---|---:|---:|---:|---:|---|
| LCDM | 84.48241222580135 | 94.48241222580135 | 95.51689498442204 | 105.27682764259971 | baseline |
| wCDM | 83.71037717797158 | 95.71037717797158 | 97.1840613884979 | 108.66367567812961 | não preferido |
| CPL/w0waCDM | 62.071708706289364 | 76.07170870628937 | 78.07170870628937 | 91.18389028980707 | preferido no smoke atual |
| RLL | 84.48241222572261 | 100.48241222572261 | 103.10059404390444 | 117.75347689259999 | não preferido |

## 5. Por que CPL é preferido nesta execução

CPL/w0waCDM é preferido porque reduz `chi2` de forma substancial contra LCDM e RLL, e a melhora permanece mesmo após penalização por parâmetros extras em AIC, AICc e BIC. Nesta execução, CPL usa `w0=-0.3` e `wa=-1.835701089847297`.

## 6. Por que RLL não é preferido nesta execução

RLL retorna `Os0=0.0`, o que desativa a amplitude da camada adicional RLL. O resultado fica praticamente igual ao LCDM em `chi2`, mas com maior número de parâmetros (`k=8`). Por isso, RLL é penalizado em AIC/AICc/BIC.

Essa observação **não prova erro estrutural do RLL**. Ela indica que a parametrização, bounds, prior, robustez do otimizador e comparação contra CPL precisam ser investigadas.

## 7. Por que `claim_allowed=false`

`claim_allowed=false` é obrigatório porque:

- RLL não vence AIC/AICc/BIC no joint real atual;
- a execução usa `maxiter=3`, logo é smoke/sanity test;
- growth benchmark externo está ausente;
- Pantheon+ completo ainda não está materializado no joint;
- CMB compressed likelihood completa ainda é parcial;
- comparação robusta RLL vs CPL ainda não foi feita.

## 8. Por que `growth_benchmark=skipped_missing_backend`

O JSON informa que os backends externos `camb` e `classy` foram verificados, mas não estavam disponíveis no ambiente. Portanto, o benchmark externo de crescimento foi pulado e qualquer avaliação de `D+`/`fσ8` permanece uma aproximação interna. Esse estado deve ser registrado como `TOKEN_VAZIO_BACKEND` para claims fortes.

## 9. Por que `maxiter=3` limita a conclusão

A execução atual usou `maxiter=3` em todos os modelos. Esse valor é adequado para smoke/sanity test rápido, mas não é suficiente para declarar convergência, estabilidade de posterior ou ranking cosmológico final. A conclusão correta é operacional: o pipeline roda e gera comparação auditável, mas o resultado não é fit final.

## 10. Como interpretar `Os0=0.0`

`Os0=0.0` significa que a amplitude da camada RLL caiu no limite inferior. Nesse limite, o RLL volta ao comportamento LCDM no ajuste atual. `zt` e `wt` ainda aparecem no JSON, mas não ativam contribuição efetiva quando a amplitude `Os0` é zero.

## 11. Como reproduzir ou rerodar futuramente

### Smoke equivalente

```bash
STRUCTURE_D_JOINT_MAXITER=3 python data/pipelines/structure_d/joint_real_likelihood.py
```

### Robust fit recomendado

```bash
STRUCTURE_D_JOINT_MAXITER=100 python data/pipelines/structure_d/joint_real_likelihood.py
```

### Controle recomendado antes de rerodar

1. Não sobrescrever resultados canônicos sem criar arquivo versionado ou README explicativo.
2. Registrar seed, `maxiter`, versões de Python/SciPy/NumPy e hashes de entradas.
3. Preservar `claim_allowed=false` enquanto houver `TOKEN_VAZIO_BACKEND`, `TOKEN_VAZIO_DATASET`, `TOKEN_VAZIO_COVARIANCE` ou `TOKEN_VAZIO_ROBUST_FIT`.
