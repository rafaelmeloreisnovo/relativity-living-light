# Resultados Corrigidos — Relativity Living Light

**Versão:** 2.0 (Fevereiro 2026)  
**Fonte dos dados:** `data/posterior_unified_synth.csv` (análise direta)

> ⚠️ **Nota de transparência:** Versões anteriores deste repositório reportavam valores MAP incorretos
> (Ω_s0 ≈ 0.72, z_t ≈ 0.65, w_t ≈ −0.97) que não correspondem ao CSV gerado.
> Este documento apresenta os valores corretos extraídos diretamente do posterior.

---

## Status dos Dados

- **Sintético:** resultados derivados de simulações e posterior sintético.
- **Parcial real:** execução parcial com dados observacionais reais em integração.
- **Real validado:** validação final concluída com dados reais e auditoria estatística.

**Nível atual deste documento:** `Sintético`.

---

## Parâmetros Posteriores (dados sintéticos)

| Parâmetro | Mediana | 16% | 84% | MAP | Selo de origem |
|-----------|---------|-----|-----|-----|----------------|
| Ω_s0 | 0.0589 | 0.0481 | 0.0707 | 0.0606 | `mock` |
| z_t | 1.164 | 0.882 | 1.430 | 1.215 | `mock` |
| w_t | 0.405 | 0.271 | 0.534 | 0.351 | `mock` |
| χ² (MAP) | — | — | — | 56.84 | `mock` |

**N amostras:** 25.000  
**N_eff (importância):** ≈ 2.321 (9.3% das amostras carregam peso efetivo)

---

## Interpretação Física dos Parâmetros

**Ω_s0 ≈ 0.059** significa que a componente de superposição contribui com cerca de 6% da densidade crítica hoje — pequena mas não nula, compatível com existir como correção ao ΛCDM sem dominar a dinâmica.

**z_t ≈ 1.16** situa a transição DE↔DM em redshift aproximado 1.16, correspondendo a uma época de lookback de ~8 bilhões de anos. Isso é mais cedo que o início da aceleração cósmica em ΛCDM (z ≈ 0.7), sugerindo que neste modelo o setor escuro começa a transicionar quando o universo tinha pouco mais de 5 bilhões de anos.

**w_t ≈ 0.40** indica uma transição moderadamente suave — não é uma mudança abrupta (delta) nem extremamente gradual. A largura de ~0.4 em redshift significa que a transição ocorre efetivamente entre z ≈ 0.8 e z ≈ 1.5, uma janela bem coberta pelo survey DESI.

---

## Covariância entre Parâmetros

```
         Ω_s0        z_t         w_t
Ω_s0   8.34e-04    8.3e-05    -1.5e-05
z_t    8.3e-05     2.7e-01     7.8e-02
w_t   -1.5e-05     7.8e-02     2.1e-02
```

A correlação positiva entre z_t e w_t (r ≈ +0.55) é esperada: transições mais tardias em redshift tendem a ser mais largas para ajustar os mesmos observáveis. A fraca correlação de Ω_s0 com os demais indica que a amplitude é relativamente independente da forma da transição.

---

## Comparação com ΛCDM (dados sintéticos)

| Modelo | χ²_MAP | ΔAIC | ΔBIC | Selo de origem |
|--------|--------|------|------|----------------|
| ΛCDM (Ω_s0 = 0) | 162.15 | 0 (ref) | 0 (ref) | `mock` |
| Relativity Living Light | 56.84 | −99.3 | −92.0 | `mock` |

> **Atenção:** Estes valores de ΔAIC e ΔBIC são obtidos em dados sintéticos gerados com os parâmetros do próprio modelo. A preferência forte pelo modelo é trivial nesse contexto — o MCMC recupera os valores com os quais os dados foram construídos. Este resultado valida apenas a maquinaria computacional, não a física.

---

## O Que Falta para Resultados Publicáveis

Para converter estes resultados em evidência científica, são necessários:

**1. Dados reais de supernovas Ia — Pantheon+**  
Dataset: 1701 SNe Ia com matriz de covariância completa  
Disponível em: `github.com/PantheonPlusSH0ES/DataRelease`  
Observável: módulo de distância μ(z) vs. χ² do modelo

**2. Dados reais de BAO — DESI DR2**  
Observáveis: H(z)·r_d, D_M(z)/r_d, D_V(z)/r_d  
Cobertura: 0.1 < z < 3.5  
Disponível publicamente via DESI Legacy Archive

**3. Crescimento estrutural — BOSS DR12**  
Observável: fσ₈(z) em 6 bins de redshift  
Requer implementação da equação de perturbação D''(a)

**4. Critérios de comparação formais**  
ΔAIC, ΔBIC com dados reais, e preferencialmente Bayes Factor via Nested Sampling (MultiNest ou dynesty)

**5. Verificação de estabilidade**  
Confirmar cs² > 0 e ausência de ghosts em todo o espaço (Ω_s0, z_t, w_t)
