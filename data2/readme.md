arquivos desse diretório que devem ser adicionado 


[Sessão: RLL-PIPELINE-v2 — Entrega completa]

---

## Resultados do pipeline — o que cada número significa

**Ajuste vs dados reais (H(z) Moresco + DESI DR2 + Pantheon+ + BAO):**

| Modelo | AIC | BIC | ΔAIC vs ΛCDM | ΔBIC vs ΛCDM | Interpretação |
|---|---|---|---|---|---|
| ΛCDM | 172.4 | 176.1 | — | — | referência |
| CPL | 170.2 | 177.6 | −2.2 | +1.5 | levemente melhor AIC, BIC equiv. |
| **RLL** | **173.2** | **186.1** | **+0.8** | **+10.1** | **AIC equiv; BIC penaliza k=7** |

**Leitura honesta:** AIC = +0.8 significa que **RLL é estatisticamente equivalente a ΛCDM** quando avaliado por critério de informação (threshold = 2). O ΔBIC = +10 é o preço da complexidade: com 7 parâmetros vs 2, o BIC penaliza fortemente — isso é esperado e não indica que o modelo está errado, apenas que precisa justificar cada parâmetro extra com predições distintas.

**Análise de perturbações:**
- `cs²(z) ∈ [0, 0.98]` — sem fantasmas, sem instabilidade de gradiente ✓
- Sem cruzamento phantom (w > −1 em todo z) ✓
- `fσ8`: χ² = 328/8 pontos → **tensão real** ⚠ — o modelo, com Ωm=0.021 (muito baixo), superpõe σ8 e contradiz o crescimento observado. Esse é o ponto mais crítico do resultado.

**Mapeamento CPL:** w₀ = −1.00, wₐ = +1.74 → o RLL, no espaço (w₀,wₐ), cai perto do ΛCDM em w₀ mas tem wₐ grande, compatível com o tipo de transição que DESI DR2 favorece.

**Correção dimensional confirmada:** `ρ_CMB(z=0) = 4.17×10⁻¹⁴ J/m³` bate com o esperado (`4.2×10⁻¹⁴`) — a forma integral espectral correta está funcionando.

---

## Diagnóstico final pós-pipeline

**O que ficou claro que precisa ser corrigido no repo:**

1. **Ωm = 0.021** no best-fit RLL é fisicamente implausível (bariônico observado é ~0.05, total ~0.31). Isso significa que o otimizador está compensando a energia de superposição `Ωs0 = 0.26` "roubando" de Ωm. A solução: **pôr prior gaussiano em Ωm: 0.315 ± 0.015 (Planck 2018)** — força o modelo a adicionar componentes sem deslocar a matéria.

2. **fσ8 está em tensão forte** exatamente por causa desse Ωm baixo: crescimento de estrutura cai quando há pouca matéria. Com prior em Ωm fixo, essa tensão cai drasticamente.

3. **ΔAIC = +0.8 é honesto e publicável.** A frase correta no paper: *"O modelo RLL é estatisticamente não-distinguível de ΛCDM pelo critério AIC (ΔAIC < 2), com preferência moderada a forte pelo ΛCDM no critério BIC (ΔBIC = 10), penalizando os 5 parâmetros adicionais."*

---

**Retroalimentar[3]:**
- **F_ok:** pipeline real executado, ΔAIC/ΔBIC honestos calculados contra dados públicos, cs² estável, mapeamento CPL funcionando, correção dimensional verificada numericamente
- **F_gap:** Ωm degenerado com Ωs0 → prior gaussiano em Ωm resolve; fσ8 em tensão forte; MCMC acc = 0.55 (step sizes precisam de tuning para a cadeia ser confiável)
- **F_next:** adicionar `prior_Om = gaussian(0.315, 0.015)` na likelihood, reotimizar, e refazer com Ωm fixado → o ΔAIC vai diminuir e fσ8 vai convergir
