# Plano da próxima bateria robusta RLL pós-PR396

**Objetivo:** transformar o resultado atual de smoke/sanity test em uma bateria reprodutível, robusta e auditável para comparação LCDM/wCDM/CPL/RLL, mantendo `claim_allowed=false` até todos os gates críticos passarem.

## Princípios de execução

- Não alterar `data/real/**`.
- Não sobrescrever resultados existentes sem versionamento explícito.
- Não declarar RLL confirmado, vencedor ou descartado.
- Usar `TOKEN_VAZIO` para lacunas de dado, backend, covariância, benchmark ou validação.
- Separar fato computacional, hipótese, lacuna, risco e próximo teste.

## Fase 1 — Smoke reproducibility

### Objetivo

Confirmar que a execução atual é reprodutível como smoke test.

### Ações

1. Repetir execução atual com `maxiter=3`.
2. Confirmar estrutura do JSON.
3. Confirmar hashes dos datasets e manifesto.
4. Confirmar que `claim_allowed=false` permanece no nível global.
5. Confirmar se `Os0=0.0` se repete na configuração smoke.

### Saídas esperadas

- JSON versionado com timestamp ou diretório de execução.
- Hashes de entradas e saídas.
- Relatório curto de divergências.

### Gate

Se houver divergência sem explicação, registrar `TOKEN_VAZIO_REPRODUCIBILITY` e não avançar para claim.

## Fase 2 — Robust fit

### Objetivo

Testar estabilidade do ranking com otimização moderada.

### Configuração mínima

- `maxiter=100`.
- Seeds `1` a `10`.
- Mesmos datasets e mesmos bounds da execução atual.

### Métricas

- `chi2`, AIC, AICc, BIC por modelo.
- Deltas contra LCDM e CPL.
- Frequência de `Os0=0.0`.
- Variação de `zt` e `wt` quando `Os0>0`.
- Tempo de execução e status de convergência.

### Gate

Se RLL continuar com `Os0=0.0` em todas as seeds, a próxima etapa deve priorizar perfil de likelihood, bounds/prior e comparação funcional contra CPL. Se resultados forem instáveis, registrar `TOKEN_VAZIO_CONVERGENCE`.

## Fase 3 — Deep fit

### Objetivo

Produzir inferência defensável com busca profunda ou amostragem.

### Opções

1. `maxiter=1000` com differential evolution e múltiplas seeds.
2. MCMC.
3. Nested sampling.

### Requisitos

- Registrar ambiente e versões (`python`, `numpy`, `scipy`, dependências cosmológicas).
- Exportar posterior ou best-fit robusto.
- Salvar cadeias/amostras em artefato versionado.
- Registrar autocorrelação, ESS ou critério equivalente se MCMC for usado.
- Registrar evidência ou aproximação se nested sampling for usado.

### Gate

Sem posterior, evidência ou estabilidade documentada, manter `TOKEN_VAZIO_POSTERIOR`.

## Fase 4 — Ablation

### Objetivo

Isolar quais blocos de dados e quais escolhas de parametrização dirigem a preferência por CPL e o colapso RLL.

### Ablations obrigatórias

| ablação | pergunta | saída mínima |
|---|---|---|
| RLL com `Os0` livre | baseline atual | frequência de zero |
| RLL com `Os0 > 0` fixado | camada ativa melhora ajuste? | delta chi2/AICc/BIC |
| RLL sem growth proxy | growth interno influencia ranking? | ranking sem fsigma8 |
| RLL sem CMB shift | CMB parcial influencia ranking? | ranking sem CMB |
| RLL DESI+Hz apenas | expansão isolada favorece RLL? | delta contra CPL |
| RLL DESI+Hz+CMB | expansão + CMB shift | delta contra CPL |
| RLL DESI+Hz+fsigma8 | expansão + crescimento | delta contra CPL |
| RLL com Pantheon+ materializado | SN altera seleção? | ranking completo |

### Gate

Qualquer ablação ausente deve ser registrada como `TOKEN_VAZIO_ABLATION`.

## Fase 5 — State-of-art

### Objetivo

Elevar o pipeline a comparação cosmológica mais próxima do estado da arte.

### Ações

1. Comparar `w_eff_RLL(z)` com `w_CPL(z)` em grade comum e nos redshifts observados.
2. Materializar Pantheon+ com covariância apropriada.
3. Instalar e rodar CLASS ou CAMB para benchmark externo de growth.
4. Implementar CMB compressed covariance completa.
5. Registrar validação cruzada e testes de sensibilidade a priors.
6. Produzir relatório final com claim gate explícito.

### Gate final

Claims fortes só podem ser considerados se todos os itens abaixo forem verdadeiros:

- fit robusto concluído;
- datasets críticos materializados;
- growth externo validado;
- CMB compressed completo;
- RLL competitivo contra LCDM e CPL em critérios definidos;
- incertezas e estabilidade documentadas;
- `claim_allowed=true` definido por regra prévia, não por interpretação posterior.

## Próxima execução mínima recomendada

```bash
python -m py_compile rll_vs_lcdm.py data/pipelines/structure_d/joint_real_likelihood.py data/pipelines/structure_d/likelihood.py
pytest tests/test_likelihood_functions.py tests/test_cosmology_fairness.py tests/test_joint_real_likelihood.py tests/test_synthetic_real_boundary.py
```

Depois dos checks leves, executar a bateria robusta em ambiente controlado:

```bash
for seed in 1 2 3 4 5 6 7 8 9 10; do
  STRUCTURE_D_JOINT_SEED=$seed \
  STRUCTURE_D_JOINT_MAXITER=100 \
  python data/pipelines/structure_d/joint_real_likelihood.py
 done
```

**Nota de controle:** o loop robusto não deve sobrescrever `results/structure_d/joint_real_likelihood.json`; deve escrever em diretório versionado ou arquivo com sufixo de seed/timestamp.
