# Diagnóstico RLL vs CPL/w0waCDM no joint real atual

**Objetivo:** explicar, sem overclaim, por que CPL/w0waCDM vence a execução atual e por que RLL retorna ao limite LCDM com `Os0=0.0`.

## 1. Por que CPL vence o joint real atual

### Fato computacional

No arquivo `results/structure_d/joint_real_likelihood.json`, CPL/w0waCDM tem os menores valores entre os modelos avaliados:

| modelo | chi2 | AIC | AICc | BIC | k | status | interpretação |
|---|---:|---:|---:|---:|---:|---|---|
| LCDM | 84.48241222580135 | 94.48241222580135 | 95.51689498442204 | 105.27682764259971 | 5 | baseline | referência rígida com pior ajuste que CPL |
| wCDM | 83.71037717797158 | 95.71037717797158 | 97.1840613884979 | 108.66367567812961 | 6 | baseline dinâmico simples | pequena melhora em chi2, penalizada por complexidade |
| CPL/w0waCDM | 62.071708706289364 | 76.07170870628937 | 78.07170870628937 | 91.18389028980707 | 7 | preferido nesta execução | melhora substancial em chi2 e vence mesmo penalizado |
| RLL | 84.48241222572261 | 100.48241222572261 | 103.10059404390444 | 117.75347689259999 | 8 | candidato não preferido | chi2 quase LCDM, penalizado por complexidade |

### Interpretação

CPL vence porque sua redução de `chi2` é grande o suficiente para compensar a penalização por parâmetros adicionais. Nesta execução, CPL melhora simultaneamente componentes importantes do ajuste, incluindo DESI BAO, growth proxy e CMB shift. Como `maxiter=3`, isso deve ser lido como evidência operacional de smoke test, não como posterior cosmológico final.

## 2. Por que RLL não vence

### Fato computacional

RLL tem `chi2=84.48241222572261`, praticamente igual a LCDM (`84.48241222580135`). A diferença é de ordem `1e-10`, insuficiente para compensar o acréscimo de parâmetros (`k=8`).

### Hipótese

A camada dinâmica RLL não foi ativada na execução atual porque o parâmetro `Os0` retornou exatamente ao limite inferior `0.0`.

### Lacuna

Ainda não há varredura robusta de seeds, posterior, perfil de likelihood, teste de sensibilidade a bounds/prior ou comparação funcional `w_eff_RLL(z)` contra `w_CPL(z)`.

## 3. Por que `Os0=0.0` faz RLL voltar ao limite LCDM

### Fato computacional

`Os0` é o parâmetro que ativa a contribuição extra da camada RLL no modelo conjunto. Quando `Os0=0.0`, essa contribuição é removida na fronteira do espaço de parâmetros. Com isso, `zt` e `wt` podem permanecer numericamente presentes, mas deixam de alterar materialmente a expansão quando a amplitude da camada é zero.

### Interpretação

O ajuste fica degenerado com LCDM: os parâmetros extras existem na contagem de complexidade, mas não entregam melhora de `chi2`. Por isso, RLL fica praticamente igual a LCDM em ajuste e pior em critérios de informação.

## 4. Por que AIC/AICc/BIC penalizam RLL

### Fato computacional

- LCDM usa `k=5`.
- CPL usa `k=7`.
- RLL usa `k=8`.
- RLL não reduz `chi2` de forma material contra LCDM.

### Interpretação

AIC, AICc e BIC premiam melhoria de ajuste e penalizam complexidade. Se um modelo adiciona parâmetros sem reduzir `chi2`, ele perde por construção nesses critérios. Essa penalização é correta e desejável para evitar overfitting.

## 5. Por que RLL precisa ser comparado diretamente contra CPL

Antes do PR #396, LCDM era o adversário mínimo. Após a inclusão de wCDM e CPL/w0waCDM, o adversário científico relevante mudou. CPL tem flexibilidade dinâmica em `w(z)` e, nesta execução, captura uma direção de ajuste que RLL não capturou. Portanto, qualquer claim futuro do RLL deve responder a duas perguntas:

1. RLL supera LCDM com penalização por complexidade?
2. RLL também compete com CPL/w0waCDM em `chi2`, AIC, AICc, BIC e estabilidade de posterior?

Enquanto a resposta à segunda pergunta for negativa ou `TOKEN_VAZIO`, não há claim de superioridade.

## 6. Como comparar `w_eff_RLL(z)` contra `w_CPL(z)`

### Definição operacional para CPL

Para CPL/w0waCDM:

```text
w_CPL(z) = w0 + wa * z / (1 + z)
```

com os valores atuais:

```text
w0 = -0.3
wa = -1.835701089847297
```

### Procedimento recomendado

1. Escolher uma grade comum de redshift, por exemplo `z in [0, 2.5]`, com pontos densos nos redshifts de BAO e Hz.
2. Calcular `w_CPL(z)` para o best-fit CPL.
3. Derivar ou implementar `w_eff_RLL(z)` a partir da função de expansão RLL usada no pipeline.
4. Comparar:
   - erro médio absoluto entre curvas;
   - erro ponderado nos redshifts observados;
   - capacidade de reproduzir inclinação dinâmica;
   - estabilidade sob seeds e maxiter.
5. Registrar `TOKEN_VAZIO_FORMULA` se `w_eff_RLL(z)` ainda não estiver formalmente implementado.

## 7. Testes que podem mostrar se RLL captura a dinâmica CPL

| teste | finalidade | resultado esperado se RLL for competitivo | status atual |
|---|---|---|---|
| Fit robusto `maxiter=100`, seeds 1–10 | verificar estabilidade | deltas estáveis e `Os0` não colapsando sempre | `TOKEN_VAZIO_ROBUST_FIT` |
| Perfil de likelihood em `Os0` | saber se zero é preferência real | mínimo fora de zero ou evidência de fronteira | `TOKEN_VAZIO_PROFILE` |
| Ablação `Os0>0` | testar camada RLL ativa | melhora de chi2 sem penalização excessiva | `TOKEN_VAZIO_ABLATION` |
| Sem growth proxy | testar influência do crescimento interno | ranking consistente | `TOKEN_VAZIO_ABLATION` |
| Sem CMB shift | testar influência de compressed CMB parcial | ranking consistente | `TOKEN_VAZIO_ABLATION` |
| DESI+Hz apenas | isolar expansão | RLL melhora expansão sem growth/CMB | `TOKEN_VAZIO_ABLATION` |
| `w_eff_RLL(z)` vs `w_CPL(z)` | comparar dinâmica efetiva | curvas próximas na região de dados | `TOKEN_VAZIO_FORMULA` |
| MCMC/nested sampling | posterior robusto | evidência e incertezas defensáveis | `TOKEN_VAZIO_POSTERIOR` |

## 8. Claims permitidos e proibidos

### Permitidos

- RLL possui pipeline auditável.
- O repositório agora compara LCDM, wCDM, CPL e RLL.
- CPL/w0waCDM é preferido no joint real atual.
- RLL colapsa para o limite LCDM nesta execução por `Os0=0.0`.
- RLL permanece candidato testável.
- Não há evidência suficiente para concluir erro estrutural do RLL.

### Proibidos

- RLL está confirmado.
- RLL vence LCDM no joint real atual.
- RLL vence CPL.
- RLL resolve energia escura.
- RLL resolve H0.
- RLL resolve S8.
- RLL deve ser descartado.

## Conclusão

CPL/w0waCDM é o modelo preferido no joint real atual porque melhora substancialmente `chi2` e permanece melhor após AIC/AICc/BIC. RLL não vence porque `Os0=0.0` desativa sua camada adicional, deixando o ajuste praticamente igual ao LCDM e pior nos critérios de informação. Isso não descarta o RLL, mas redefine a próxima etapa: o RLL precisa ser testado contra CPL com fit robusto, ablações, posterior e comparação funcional de dinâmica efetiva.
