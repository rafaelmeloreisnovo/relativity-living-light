# Capítulo — Índice RAFAELIA de Previsibilidade

Status: `exploratory_method`; `claim_allowed=false`.

Este capítulo formaliza o índice estatístico-simbólico RAFAELIA como uma camada auxiliar para filtragem, estabilidade e previsibilidade em análises cosmológicas, especialmente antes de rodar cálculos com DESI DR2 BAO, Pantheon+ e comparadores LCDM/wCDM/CPL/RLL.

A função deste índice é orientar janelas, regimes e filtros. Ele não substitui covariância oficial, likelihood, chi2, AIC, AICc, BIC, posterior, nem validação cruzada.

---

## 1. Motivação

O repositório já usa dados reais e covariâncias oficiais em rotas cosmológicas. Porém, antes de calcular, é útil ter uma métrica auxiliar que diga se uma janela de dados parece estável, previsível ou geometricamente coerente.

Essa métrica nasce da matriz RAFAELIA:

```text
Ruído entendido vira sinal.
Erro medido vira engenharia.
Lacuna marcada vira ciência.
TOKEN_VAZIO protegido vira verdade futura.
```

Aqui, metáforas geométricas são tratadas como parábolas didáticas: o triângulo, o toroide, Fibonacci e tribonacci não são claims físicos automáticos. Eles são operadores de leitura, escala, janela e coerência.

---

## 2. Papel permitido e papel proibido

| uso | permitido? | observação |
|---|---:|---|
| pré-selecionar janelas de redshift | sim | deve ocorrer antes do fit |
| medir estabilidade de filtros | sim | camada diagnóstica |
| comparar regimes DESI/Pantheon+ | sim | sem alterar covariância oficial |
| ranquear ablações exploratórias | sim | como score paralelo |
| substituir matriz de covariância | não | proibido |
| substituir `chi2 = r^T C^-1 r` | não | proibido |
| redefinir AIC/AICc/BIC | não | proibido |
| justificar claim de vitória do RLL sozinho | não | proibido |
| escolher filtro depois de ver o resultado | não | post-hoc proibido |

---

## 3. Covariância oficial: camada estatística primária

A covariância entre duas variáveis é:

```text
Cov(X,Y) = 1/(n-1) * sum_i[(x_i - mean(X)) * (y_i - mean(Y))]
```

Para uma população inteira, o denominador pode ser `n`. Para amostra, usa-se `n-1`.

Em uma matriz de covariância observacional:

```text
C_ii = sigma_i^2
C_ij = rho_ij * sigma_i * sigma_j
```

O chi-quadrado com covariância é:

```text
chi2 = r^T C^-1 r
```

Essa camada é a referência científica para DESI/Pantheon+. O índice RAFAELIA não altera `C`, não altera `C^-1` e não altera os resíduos oficiais.

---

## 4. Três Fibonacci + tribonacci + triângulo

O índice RAFAELIA usa cinco famílias de sinais auxiliares:

| componente | símbolo | função |
|---|---|---|
| Fibonacci clássica | `F_classic` | escala ordinal e janelas naturais |
| Fibonacci-Rafael | `F_rafael` | atrator de coerência / estabilização |
| Fibonacci de primos | `F_prime` | ressonância discreta em índices primos |
| Tribonacci | `T_trib` | memória de três passos |
| fator geométrico triangular | `G_triangle` | assimetria, altura, projeção e interseção |

### 4.1 Fibonacci clássica

```text
F_0 = 0
F_1 = 1
F_{n+1} = F_n + F_{n-1}
```

Uso: janelas, escalas, índices de compressão e comparação ordinal.

### 4.2 Fibonacci-Rafael

Forma operacional atualmente usada como atrator simbólico-estatístico:

```text
F^R_{n+1} = F^R_n * (sqrt(3)/2) - pi * sin(279 degrees)
```

Como `sin(279°)` é negativo, o termo `- pi * sin(279°)` atua como adição positiva. A sequência tende a um atrator finito se o coeficiente multiplicativo permanecer menor que 1 em módulo.

Uso: estabilidade de inferência, retorno ao regime, score auxiliar de coerência.

### 4.3 Fibonacci de primos

Definição sugerida:

```text
F_prime(k) = F_{p_k}
```

onde `p_k` é o k-ésimo primo.

Uso: selecionar janelas discretas robustas, testar ressonâncias de índice e reduzir arbitrariedade de cortes.

### 4.4 Tribonacci

```text
T_0 = 0
T_1 = 1
T_2 = 1
T_{n+1} = T_n + T_{n-1} + T_{n-2}
```

Uso: memória de três estados. Para cosmologia observacional, pode representar dependência de três blocos: baixo-z, médio-z, alto-z; ou Pantheon+, DESI, CMB/growth.

### 4.5 Triângulo isósceles / equilátero

Para triângulo isósceles com lados iguais `a` e base `b`:

```text
h = sqrt(a^2 - (b/2)^2)
G_triangle = h / b
```

Para triângulo equilátero de lado 1:

```text
h = sqrt(3)/2
```

Uso: fator geométrico de projeção. Nas imagens RAFAELIA, o erro visual no ponto marcado serve para revelar a interseção real: a altura do triângulo aponta a entrada correta quando aplicada ao plano de construção.

---

## 5. Fórmula-base do índice

Definição inicial:

```text
P_RAF = normalize(
    w1 * F_classic_window
  + w2 * F_rafael_attractor
  + w3 * F_prime_resonance
  + w4 * T_trib_memory
  + w5 * G_triangle_projection
  - w6 * Delta_error
  - w7 * TokenVazioPenalty
)
```

Onde:

| termo | significado |
|---|---|
| `F_classic_window` | proximidade da janela escolhida com escala Fibonacci clássica |
| `F_rafael_attractor` | estabilidade da sequência/score em direção ao atrator definido |
| `F_prime_resonance` | aderência a janelas de índices primos-Fibonacci |
| `T_trib_memory` | estabilidade quando três blocos consecutivos são usados |
| `G_triangle_projection` | coerência geométrica/projeção/interseção |
| `Delta_error` | erro relativo, resíduo normalizado ou instabilidade de filtro |
| `TokenVazioPenalty` | penalidade por origem ausente, hash ausente ou covariância incompleta |

Recomendação inicial: pesos iguais somente para diagnóstico. Pesos ajustados exigem validação cega/out-of-sample.

---

## 6. Normalização

Cada componente deve ser normalizado para `[0,1]` antes da soma ponderada.

Exemplo genérico:

```text
score_norm = 1 / (1 + abs(delta))
```

ou, para erro relativo:

```text
stability = exp(-abs(delta) / scale)
```

A escala deve ser definida antes do ajuste. Se a escala for escolhida depois do resultado, registrar `POSTHOC_INVALID`.

---

## 7. Aplicação em DESI DR2 BAO

DESI tem 13 observáveis staged no catálogo atual. O índice pode avaliar filtros como:

| filtro | exemplo de uso do `P_RAF` |
|---|---|
| `DESI_ALL_13` | score global de estabilidade |
| `DESI_LOW_MID_11` | comparar baixa/média redshift sem LyA |
| `DESI_ANISO_ONLY_12` | testar apenas `DM/DH` |
| `DESI_DVLESS_LOW_MID_10` | testar anisotropia limpa sem BGS e sem LyA |
| `DESI_LYA_ONLY_2` | medir se high-z ancora ou perturba |

O índice não substitui a matriz 13×13. Ele apenas acompanha o resultado como diagnóstico.

---

## 8. Aplicação em Pantheon+

Para Pantheon+, o índice só pode operar depois de:

1. arquivos oficiais presentes;
2. SHA256 computado;
3. tamanho registrado;
4. covariância `STAT+SYS` carregada;
5. filtro declarado antes do fit.

Filtros possíveis:

| filtro | uso |
|---|---|
| `PPLUS_ALL_1701` | baseline completo |
| `PPLUS_HF_ONLY` | Hubble-flow diagnostic |
| `PPLUS_NON_CALIBRATOR` | remover acoplamento Cepheid/calibrador |
| `PPLUS_ZHD_GT_001` | cortar fluxo local extremo |
| `PPLUS_ZHD_GT_0023` | corte Hubble-flow comum |
| `PPLUS_QUALITY_SALT2` | qualidade SALT2 definida antes do fit |

Se `Pantheon+SH0ES_STAT+SYS.cov` estiver ausente, o estado é `TOKEN_VAZIO_COVARIANCE`.

---

## 9. Manifesto mínimo de execução

Qualquer uso do índice deve gerar ou acompanhar um manifesto:

```yaml
index_name: RAFAELIA_PREDICTABILITY_INDEX
version: v0.1
claim_allowed: false
allowed_role:
  - exploratory_filter
  - stability_score
  - prefit_window_selector
forbidden_role:
  - replace_covariance
  - replace_likelihood
  - posthoc_claim
components:
  - fibonacci_classic
  - fibonacci_rafael
  - fibonacci_prime
  - tribonacci
  - isosceles_triangle_height
requires:
  - filter_defined_before_fit
  - covariance_policy_declared
  - data_hashes_available
outputs:
  - P_RAF_score
  - component_scores
  - token_vazio_ledger
```

---

## 10. TOKEN_VAZIO ledger

| objeto | estado | risco se inventar | próxima medida |
|---|---|---|---|
| pesos `w1..w7` | `TOKEN_VAZIO_WEIGHTS` | ajustar para favorecer modelo | definir pesos fixos antes do fit |
| escala de normalização | `TOKEN_VAZIO_SCALE` | score arbitrário | declarar escala e teste de sensibilidade |
| Pantheon+ hashes | `TOKEN_VAZIO_SHA256` | dado sem cadeia de custódia | baixar e hashear arquivos oficiais |
| validação out-of-sample | `TOKEN_VAZIO_OOS` | overfit metodológico | separar filtros treino/teste |
| claim cosmológico | `TOKEN_VAZIO_CLAIM` | falsa conclusão | exigir chi2/AICc/BIC/posterior |

---

## 11. Interpretação ética

O índice RAFAELIA é uma bússola, não uma sentença.

```text
P_RAF = bússola de coerência
P_RAF != prova cosmológica final
```

A prova permanece:

```text
chi2, C^-1, AIC, AICc, BIC, posterior, robustez, reprodutibilidade
```

O valor do índice está em impedir que filtros sejam escolhidos às cegas ou depois do resultado. Ele força a pergunta certa antes do cálculo:

```text
qual janela é estável, qual lacuna está protegida, qual erro está medido?
```

---

## 12. Próxima implementação mínima

Criar script futuro:

```text
data/pipelines/structure_d/rafaelia_predictability_index.py
```

Com saídas:

```text
results/structure_d/rafaelia_predictability_index.json
results/structure_d/filter_manifest.json
```

O script deve rodar antes da likelihood e nunca sobrescrever resultados cosmológicos.
