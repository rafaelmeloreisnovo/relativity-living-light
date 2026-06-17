# RLL — Auditoria 6Sigma pós-PR396

**Status:** auditoria conservadora pós-merge do PR #396.  
**Escopo:** `joint_real_likelihood`, documentação de lacunas, origem de parâmetros, justiça comparativa cosmológica e artefatos atuais de `results/structure_d/`.  
**Regra de verdade:** quando faltar dado, benchmark, covariância, backend ou validação, registrar `TOKEN_VAZIO` em vez de inferir resultado.

## 1. Sumário executivo

### Fatos computacionais

- O pipeline evoluiu após o PR #396: agora há ledger de cálculos ausentes, registro formal de origem de parâmetros, AICc, modelos LCDM/wCDM/CPL/RLL e materialização de covariância DESI para BAO.
- O repositório agora compara **LCDM**, **wCDM**, **CPL/w0waCDM** e **RLL** no artefato conjunto real `results/structure_d/joint_real_likelihood.json`.
- O resultado conjunto atual contém `N=64` pontos efetivos e foi produzido com `maxiter=3` para todos os modelos; portanto, é **smoke/sanity test**, não fit final.
- O modelo preferido nesta execução é **CPL/w0waCDM**, com `chi2=62.071708706289364`, `AIC=76.07170870628937`, `AICc=78.07170870628937` e `BIC=91.18389028980707`.
- O RLL retorna `Os0=0.0` e colapsa para o limite LCDM: `chi2_RLL=84.48241222572261` é numericamente quase igual a `chi2_LCDM=84.48241222580135`.
- RLL é pior que LCDM em AIC/AICc/BIC nesta execução porque adiciona parâmetros (`k=8`) sem reduzir `chi2` de modo material.
- `claim_allowed` deve permanecer `false` porque gates críticos ainda falham: benchmark de crescimento externo ausente, Pantheon+ parcial, CMB compressed likelihood parcial e fit robusto ainda não executado.

### Interpretação conservadora

- **CPL/w0waCDM é o novo adversário técnico principal do RLL**, não apenas LCDM.
- O colapso `Os0=0.0` **não prova erro estrutural do RLL**; ele indica que, sob a execução atual, os dados/otimizador/bounds/prior/parametrização não ativaram a camada RLL.
- O estado atual sustenta apenas a afirmação: **RLL possui pipeline auditável e permanece candidato testável**, sem claim de superioridade.

## 2. Define

### Problema definido

Determinar, com metodologia DMAIC/6Sigma, se o pipeline pós-PR396 está suficientemente maduro para claims científicos e diagnosticar por que o RLL não supera CPL/w0waCDM no joint real atual.

### Escopo operacional

| Item | Incluído | Excluído |
|---|---:|---:|
| Artefato `joint_real_likelihood.json` | sim | não sobrescrever |
| Documentação pós-PR396 | sim | não alterar dados brutos |
| Diagnóstico RLL vs CPL | sim | não declarar vencedor RLL |
| Causa raiz de `Os0=0.0` | sim | não inventar posterior |
| Fit pesado, MCMC ou nested sampling | não nesta tarefa | planejar |

### CTQ primários

1. Comparação justa entre LCDM, wCDM, CPL e RLL.
2. Rastreamento de origem de parâmetros.
3. Critérios de informação com penalização por complexidade: AIC, AICc e BIC.
4. Separação explícita entre fato computacional, hipótese, lacuna, risco e próximo teste.
5. Preservação de `claim_allowed=false` enquanto gates críticos falharem.

## 3. Measure

### Artefatos medidos

| Artefato | Estado atual | Evidência operacional |
|---|---|---|
| `docs/RLL_MISSING_CALCULATIONS_LEDGER.md` | existe | ledger de lacunas disponível |
| `docs/RLL_PARAMETER_ORIGIN_TABLE.md` | existe | origem documental de parâmetros |
| `data/inputs/cosmology_joint/parameter_origin_registry.json` | existe | registro estruturado de origem |
| `src/rll/cosmology_fairness.py` | existe | utilitários conservadores de fairness |
| `data/pipelines/structure_d/likelihood.py` | contém AICc | penalização finite-sample disponível |
| `data/pipelines/structure_d/joint_real_likelihood.py` | contém LCDM/wCDM/CPL/RLL | comparação multiparadigma |
| `results/structure_d/joint_real_likelihood.json` | existe | resultado real conjunto atual |
| `results/structure_d/joint_real_likelihood_covariance_manifest.json` | existe | manifesto de covariância |
| Growth CLASS/CAMB | `TOKEN_VAZIO_BACKEND` | backend externo ausente |
| Pantheon+ completo | `TOKEN_VAZIO_DATASET` | materialização parcial |
| CMB compressed likelihood completa | `TOKEN_VAZIO_COVARIANCE` | likelihood parcial |

### Resultado quantitativo atual

| modelo | chi2 | AIC | AICc | BIC | N | k | parâmetros destacados |
|---|---:|---:|---:|---:|---:|---:|---|
| LCDM | 84.48241222580135 | 94.48241222580135 | 95.51689498442204 | 105.27682764259971 | 64 | 5 | referência base |
| wCDM | 83.71037717797158 | 95.71037717797158 | 97.1840613884979 | 108.66367567812961 | 64 | 6 | `w=-0.9725236468940587` |
| CPL/w0waCDM | 62.071708706289364 | 76.07170870628937 | 78.07170870628937 | 91.18389028980707 | 64 | 7 | `w0=-0.3`, `wa=-1.835701089847297` |
| RLL | 84.48241222572261 | 100.48241222572261 | 103.10059404390444 | 117.75347689259999 | 64 | 8 | `Os0=0.0`, `zt=0.48913585347939664`, `wt=0.5725207843474277` |

## 4. Analyze

### Fato computacional

CPL reduz `chi2` em aproximadamente `22.4107` contra LCDM e também supera LCDM em AIC/AICc/BIC. RLL reduz `chi2` contra LCDM por apenas `~7.9e-11`, efetivamente zero para interpretação cosmológica nesta execução.

### Hipóteses técnicas

| hipótese | fato associado | lacuna | risco | próximo teste |
|---|---|---|---|---|
| Dados atuais não favorecem camada RLL | `Os0=0.0` | sem posterior robusto | falso negativo se fit raso | rodar seeds 1–10 com `maxiter=100` |
| Bounds/prior favorecem zero | `Os0` toca limite inferior | sem perfil de likelihood | preferência induzida por parametrização | ablação `Os0>0` e prior físico |
| `maxiter=3` insuficiente | todos os modelos usam 3 iterações | sem convergência documentada | ranking instável | robust fit com tolerância e repetição |
| Parametrização RLL não reproduz CPL | CPL melhora fortemente `chi2` | sem mapa `w_eff_RLL(z)` vs `w_CPL(z)` | RLL subflexível no regime relevante | comparar funções efetivas em grade de z |
| Growth/CMB influenciam seleção | CPL melhora DESI, fsigma8 e CMB shift | benchmark externo ausente | proxy interna enviesar ranking | instalar CLASS/CAMB e testar sem growth/CMB |
| Pantheon+ ausente/parcial altera seleção | SN completa não entra no joint atual | `TOKEN_VAZIO_DATASET` | seleção cosmológica incompleta | materializar Pantheon+ com covariância |

## 5. Improve

### Melhorias já obtidas pós-PR396

- Inclusão de baseline wCDM.
- Inclusão de baseline CPL/w0waCDM.
- Inclusão de AICc para penalização em amostra finita.
- Registro formal de origem dos parâmetros.
- DESI full covariance pronta para BAO.
- Separação mais explícita entre dados reais e fronteiras sintéticas.

### Melhorias mínimas recomendadas

1. Executar fit robusto com `STRUCTURE_D_JOINT_MAXITER=100` e seeds 1–10.
2. Registrar hashes de entrada e saída por execução.
3. Gerar tabela de estabilidade de `chi2`, AICc, BIC e frequência de `Os0=0.0`.
4. Executar ablação RLL sem growth proxy, sem CMB shift e em subconjuntos DESI+Hz.
5. Implementar comparação direta `w_eff_RLL(z)` vs `w_CPL(z)`.
6. Materializar Pantheon+ completo antes de qualquer claim cosmológico ampliado.
7. Instalar e registrar CLASS/CAMB para growth benchmark externo.

## 6. Control

### Controles de qualidade obrigatórios

| controle | regra | ação se falhar |
|---|---|---|
| `claim_allowed` | permanecer `false` se qualquer gate crítico falhar | bloquear claim |
| dados brutos | não alterar `data/real/**` | rollback imediato |
| resultados existentes | não sobrescrever sem README explicativo | criar novo artefato versionado |
| lacunas | usar `TOKEN_VAZIO` | não inferir |
| fit smoke | rotular `maxiter=3` como sanity/smoke | não publicar como final |
| comparador técnico | incluir CPL/w0waCDM | não limitar a LCDM |

### Gates de controle

- **Gate dados:** DESI BAO pronto; Pantheon+ completo = `TOKEN_VAZIO_DATASET`; CMB compressed covariance completa = `TOKEN_VAZIO_COVARIANCE`.
- **Gate growth:** CLASS/CAMB ausente = `TOKEN_VAZIO_BACKEND`.
- **Gate otimização:** `maxiter=3` = `TOKEN_VAZIO_ROBUST_FIT`.
- **Gate estatístico:** RLL não melhora AIC/AICc/BIC = claim bloqueado.

## 7. CTQ table

| CTQ | especificação | medida atual | status |
|---|---|---|---|
| Comparação multiparadigma | LCDM, wCDM, CPL, RLL no mesmo pipeline | presente | conforme |
| Penalização por complexidade | AIC, AICc, BIC | presente | conforme |
| Covariância BAO | DESI full covariance materializada | presente | conforme para BAO |
| Growth externo | CLASS/CAMB | `TOKEN_VAZIO_BACKEND` | bloqueado |
| Pantheon+ | SN com covariância materializada | `TOKEN_VAZIO_DATASET` | parcial |
| CMB compressed | covariância/likelihood completa | `TOKEN_VAZIO_COVARIANCE` | parcial |
| Fit robusto | maxiter alto, seeds múltiplas | `maxiter=3` | smoke apenas |
| Claim policy | false se gate crítico falhar | `claim_allowed=false` | conforme |

## 8. Defect table

| defeito 6Sigma | manifestação | severidade | contenção | correção proposta |
|---|---|---:|---|---|
| D1: Fit raso | `maxiter=3` | alta | rotular como smoke | rodar `maxiter=100/1000` |
| D2: Growth sem benchmark externo | `skipped_missing_backend` | alta | bloquear claim | instalar CLASS/CAMB |
| D3: Pantheon+ parcial | ausência no joint completo | média/alta | `TOKEN_VAZIO_DATASET` | materializar SN e covariância |
| D4: CMB shift parcial | likelihood compressed incompleta | média/alta | `TOKEN_VAZIO_COVARIANCE` | incluir covariância/validação |
| D5: RLL no limite LCDM | `Os0=0.0` | alta para claim | não declarar vitória | investigar bounds/prior/parametrização |
| D6: Novo baseline dominante | CPL vence | alta | reposicionar adversário técnico | comparar RLL diretamente contra CPL |

## 9. Risk matrix

| risco | probabilidade | impacto | nível | mitigação |
|---|---|---|---|---|
| Overclaim científico | média | muito alto | crítico | manter `claim_allowed=false` |
| Concluir falso negativo RLL por fit raso | média | alto | alto | seeds e maxiter robustos |
| Ignorar CPL como adversário | alta | alto | crítico | tornar CPL baseline obrigatório |
| Viés por proxy de growth | média | alto | alto | benchmark CLASS/CAMB e ablação |
| Viés por dataset incompleto | média | alto | alto | Pantheon+ e CMB completos |
| Reprodutibilidade insuficiente | média | médio | médio | hashes, ambiente, seeds |

## 10. Claim gate atualizado

### Claims permitidos

- RLL possui pipeline auditável.
- O repositório agora compara LCDM, wCDM, CPL e RLL.
- CPL/w0waCDM é preferido no joint real atual.
- RLL colapsa para o limite LCDM nesta execução por `Os0=0.0`.
- RLL permanece candidato testável.
- Não há evidência suficiente para concluir erro estrutural do RLL.

### Claims proibidos

- RLL está confirmado.
- RLL vence LCDM no joint real atual.
- RLL vence CPL.
- RLL resolve energia escura.
- RLL resolve H0.
- RLL resolve S8.
- RLL deve ser descartado.

### Decisão de gate

`claim_allowed=false` deve permanecer enquanto houver qualquer um dos seguintes estados: `TOKEN_VAZIO_BACKEND`, `TOKEN_VAZIO_DATASET`, `TOKEN_VAZIO_COVARIANCE`, `TOKEN_VAZIO_ROBUST_FIT` ou piora de AIC/AICc/BIC contra baselines.

## 11. Próximos testes mínimos

1. Reproduzir a execução atual sem sobrescrever resultados canônicos.
2. Rodar `maxiter=100` para seeds 1–10.
3. Calcular distribuição de deltas RLL-LCDM e RLL-CPL para `chi2`, AIC, AICc e BIC.
4. Medir frequência de `Os0=0.0`.
5. Rodar ablações: sem growth, sem CMB, DESI+Hz, DESI+Hz+CMB, DESI+Hz+fsigma8.
6. Comparar `w_eff_RLL(z)` contra `w_CPL(z)` em grade comum.
7. Materializar Pantheon+ e CMB compressed likelihood completa.
8. Instalar CLASS/CAMB e repetir growth benchmark.

## 12. Conclusão conservadora

O PR #396 elevou a maturidade auditável do pipeline RLL, principalmente por adicionar critérios de informação, baselines wCDM/CPL, registro de origem de parâmetros e covariância DESI para BAO. Entretanto, o resultado real conjunto atual é apenas um smoke/sanity test (`maxiter=3`). Nesta execução, CPL/w0waCDM é preferido; RLL cai no limite LCDM por `Os0=0.0` e é penalizado por AIC/AICc/BIC. Isso não prova erro estrutural do RLL, mas exige diagnóstico robusto de parametrização, bounds, prior, backend de growth, datasets parciais e comparação direta contra CPL. Até esses gates passarem, a única decisão responsável é manter `claim_allowed=false`.
