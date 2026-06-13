# Causa raiz conservadora: `Os0=0.0` no RLL joint real atual

**Escopo:** investigar por que o RLL retorna `Os0=0.0` na execução atual de `results/structure_d/joint_real_likelihood.json`, sem inventar posterior, sem alterar dados brutos e sem declarar confirmação ou descarte do modelo.

## 1. Fato computacional observado

No resultado atual:

- `RLL_joint_real` retorna `Os0=0.0`.
- `chi2_RLL=84.48241222572261`.
- `chi2_LCDM=84.48241222580135`.
- A diferença `chi2_RLL - chi2_LCDM` é aproximadamente `-7.874e-11`, numericamente desprezível para interpretação cosmológica.
- RLL usa `k=8`, enquanto LCDM usa `k=5`.
- RLL tem AIC/AICc/BIC piores que LCDM e CPL nesta execução.
- A execução usou `maxiter=3`, logo é smoke/sanity test e não fit final.

## 2. Interpretação de `Os0=0` como limite LCDM

`Os0` representa a amplitude da camada adicional RLL. Quando `Os0=0.0`, a camada extra tem amplitude nula. Nesse limite, os parâmetros `zt` e `wt` podem aparecer no JSON, mas sua influência física efetiva é desligada pela amplitude zero. Assim, o modelo RLL fica degenerado com LCDM para o ajuste de expansão/crescimento usado nesta execução.

Essa leitura é um **fato de parametrização operacional**, não uma prova de que o RLL é estruturalmente falso. O diagnóstico correto exige separar:

- preferência real dos dados por `Os0=0`;
- efeito de bounds/prior;
- insuficiência de otimização;
- limitação da forma funcional RLL;
- influência de proxies e datasets parciais.

## 3. Tabela de hipóteses de causa raiz

| hipótese | evidência atual | risco | teste mínimo | status |
|---|---|---|---|---|
| A: dados atuais não favorecem camada RLL | melhor ajuste retorna `Os0=0.0`; `chi2` igual a LCDM | concluir falso negativo se a execução for rasa | rodar seeds 1–10 com `maxiter=100` e medir frequência de `Os0=0` | `TOKEN_VAZIO_ROBUST_FIT` |
| B: bounds/prior favorecem zero | `Os0` está exatamente no limite inferior | mínimo pode ser artefato de fronteira | perfil de likelihood em `Os0`; repetir com `Os0>0` fixado ou prior físico | `TOKEN_VAZIO_PROFILE` |
| C: `maxiter=3` é insuficiente | otimizador foi limitado a 3 iterações | ranking e parâmetros instáveis | repetir execução atual e depois `maxiter=100/1000` | `TOKEN_VAZIO_CONVERGENCE` |
| D: parametrização RLL atual não reproduz CPL | CPL reduz `chi2` em ~22.41 contra LCDM; RLL não reduz | RLL pode ser subflexível na direção dinâmica favorecida | comparar `w_eff_RLL(z)` e `w_CPL(z)` em grade observacional | `TOKEN_VAZIO_FORMULA` |
| E: RLL precisa de prior físico ou reparametrização | parâmetro de amplitude colapsa no zero | camada física pode estar mal condicionada | testar reparametrização positiva, regularização ou prior físico documentado | `TOKEN_VAZIO_PRIOR` |
| F: growth proxy/CMB shift influenciam preferência | growth benchmark externo está `skipped_missing_backend`; CMB compressed é parcial | ranking pode depender de aproximações internas | ablações sem growth, sem CMB, e benchmark CLASS/CAMB | `TOKEN_VAZIO_BACKEND` |
| G: ausência de Pantheon+ altera seleção | Pantheon+ completo não está materializado no joint atual | seleção cosmológica incompleta | incluir Pantheon+ com covariância e repetir comparação | `TOKEN_VAZIO_DATASET` |

## 4. Mapa DMAIC da causa raiz

### Define

O defeito operacional é: RLL adiciona parâmetros, mas retorna ao limite LCDM (`Os0=0.0`) e não melhora os critérios de informação.

### Measure

Medições atuais:

- `Os0=0.0`.
- `delta_chi2_RLL_minus_LCDM ≈ -7.874e-11`.
- `delta_AIC_RLL_minus_LCDM ≈ +6.0`.
- `delta_AICc_RLL_minus_LCDM ≈ +7.5837`.
- `delta_BIC_RLL_minus_LCDM ≈ +12.4766`.
- `delta_AICc_RLL_minus_CPL ≈ +25.0289`.

### Analyze

O padrão é compatível com uma solução de fronteira: o otimizador encontrou que a amplitude extra não melhora o ajuste dentro da busca atual. Porém, como `maxiter=3`, não é possível separar preferência física de limitação computacional.

### Improve

- Rodar fit robusto com seeds múltiplas.
- Criar perfil de likelihood em `Os0`.
- Testar ablações sem growth/CMB.
- Comparar RLL diretamente contra CPL em espaço de funções efetivas.
- Testar parametrização que reduza degeneração quando `Os0` aproxima zero.

### Control

- Não transformar `Os0=0.0` em claim de descarte.
- Não transformar `Os0=0.0` em claim de confirmação de LCDM.
- Não publicar ranking como final enquanto `TOKEN_VAZIO_ROBUST_FIT` existir.
- Manter `claim_allowed=false`.

## 5. Próximo teste mínimo recomendado

Executar uma bateria leve, mas robusta:

```bash
for seed in 1 2 3 4 5 6 7 8 9 10; do
  STRUCTURE_D_JOINT_SEED=$seed \
  STRUCTURE_D_JOINT_MAXITER=100 \
  python data/pipelines/structure_d/joint_real_likelihood.py
done
```

**Observação de controle:** esse comando é uma recomendação futura. Não foi executado nesta auditoria para evitar fit pesado e sobrescrita indevida de resultados existentes.

## 6. Conclusão conservadora

A causa raiz imediata do comportamento RLL é `Os0=0.0`, que desativa a camada adicional e devolve o modelo ao limite LCDM. A causa raiz científica ainda é indeterminada. As hipóteses principais são preferência dos dados, bounds/prior, fit raso, parametrização insuficiente, ausência de prior físico, influência de proxies growth/CMB e ausência de Pantheon+. O estado correto é investigação aberta com `claim_allowed=false`.
