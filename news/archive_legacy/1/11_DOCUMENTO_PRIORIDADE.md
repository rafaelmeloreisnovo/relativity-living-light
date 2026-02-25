> ⚠️ **Aviso de canonicidade:** este arquivo é histórico/legado. A versão oficial está em `docs/canonicos/11_DOCUMENTO_PRIORIDADE.md`.

# 11 — DOCUMENTO DE PRIORIDADE
## Roadmap de Validação — Relativity Living Light
**∆RafaelVerboΩ | Instituto Rafael | 2026**
Status: TRL 3 → objetivo TRL 5

---

## ESTADO ATUAL (Fevereiro 2026)

| Componente | TRL | χ²/dof | Status |
|---|---|---|---|
| Teoria formal (equação RLL) | 3 | — | ✅ Completo |
| Validação H(z) CC + BAO | 3 | 3.02 (ΛCDM) | ✅ Feito |
| CMB shift params | 3 | incluso | ✅ Feito |
| Pantheon+ SNe Ia | 1 | — | ❌ Ausente |
| fσ₈(z) crescimento | 1 | — | ❌ Ausente |
| MCMC posteriors | 1 | — | ❌ Ausente |
| Lente gravitacional | 1 | — | ❌ Ausente |
| arXiv submission | 1 | — | ❌ Ausente |

**Resultado validação atual:**  
`χ²(ΛCDM)=123.7 | χ²(RLL)=123.7 | ΔAIC=+6 | Ωs₀≈0`  
→ RLL indistinguível de ΛCDM em N=45 observáveis (H(z)+BAO+CMB)

---

## PRIORIDADE 1 — Pantheon+ SNe Ia [CRÍTICO]

**Por que é prioridade máxima:**  
- 1701 supernovas tipo Ia, z=[0.001, 2.26]  
- Dataset com maior poder discriminativo para w(z)  
- RLL tem w_eff(z) dinâmico emergente — SNe Ia são o teste direto  
- Brout+ 2022 (arXiv:2202.04077) — dataset público

**O que fazer:**  
```python
# Download: https://github.com/PantheonPlusSH0ES/DataRelease
# Arquivo: Pantheon+SH0ES.dat
# Colunas: zHD, MU_SH0ES, MUERR_SH0ES
# Fit: μ_th(z) = 5 log10[dL(z)/10pc]
# dL(z) = (1+z)*DC(z)
```

**Threshold para evidência positiva:**  
Se RLL χ²(SNe) < ΛCDM χ²(SNe) por Δ > 8 → ΔAIC < 0 possível com dataset combinado.

---

## PRIORIDADE 2 — MCMC com emcee [ALTA]

**Por que:** Intervalos de confiança são obrigatórios para qualquer claim científico. Fit pontual (scipy.minimize) não é suficiente.

**Especificação:**  
```python
import emcee
# Parâmetros RLL: θ = [H0, Om, OL, Os0, zt, wt, Ob_h2]
# Priors:
#   H0 ~ Uniform(60, 80)
#   Om ~ Uniform(0.1, 0.6)
#   OL ~ Uniform(0.4, 0.9)  # ou flat: OL = 1 - Om - Or
#   Os0 ~ Uniform(0, 0.3)   # positivo
#   zt  ~ Uniform(0.1, 3.0)
#   wt  ~ Uniform(0.05, 2.0)
# nwalkers=64, nsteps=5000, burnin=1000
```

**Output esperado:** Corner plot Os0 vs zt com contornos 1σ/2σ.  
**Threshold:** σ(Os0) < 0.05 → Os0 detectável ou descartado com 95% CL.

---

## PRIORIDADE 3 — fσ₈(z) Crescimento de Estrutura [ALTA]

**Por que:** A dinâmica de transição do RLL modifica a equação de crescimento linear.  
`δ'' + H δ' - (3/2)H₀²Ωₘ(1+z)³/a² δ = 0`  
Com Ωs₀ ativo, o "potencial gravitacional" efetivo muda vs ΛCDM.

**Datasets disponíveis:**  
- BOSS DR12 (6dFGRS, SDSS, VIPERS, WiggleZ) — 22 pontos
- fσ₈ compilação Nesseris+ 2017 — dataset público

**Observação crítica:** fσ₈ é o observable mais sensível a modelos que modificam a dinâmica de crescimento. Se RLL muda fσ₈ de forma detectável, este é o canal principal de evidência.

---

## PRIORIDADE 4 — Comparação w₀wₐCDM [MÉDIA]

**Por que:** DESI 2024 sugere w₀ > -1, wa < 0 a ~3σ — evidência para DE dinâmica.  
RLL tem w_eff(z) emergente. É necessário comparar:  
- RLL vs ΛCDM  
- RLL vs w₀CDM  
- RLL vs w₀wₐCDM (Chevallier-Polarski-Linder)

**Implementação:** Adicionar modelo CPL ao script de validação.

---

## PRIORIDADE 5 — Ghost & Estabilidade [MÉDIA]

**Por que:** Todo modelo cosmológico viável deve passar em:  
1. **Ghost-free**: energia cinética positiva (∂²L/∂φ̇² > 0)  
2. **Gradient stable**: velocidade do som cs² > 0  
3. **No tachyonic instability**: cs² não negativo em nenhum epoch

**Arquivo:** `docs/ESTABILIDADE_GHOST_CHECK.md` — verificar se contém análise completa ou apenas placeholder.  
**Ação:** Calcular cs²(z) para o campo efetivo de superposição.

---

## PRIORIDADE 6 — arXiv e Peer Review [ESTRATÉGICA]

**Por que:** Sem publicação, o DOI Zenodo é auto-declarado. Peer review externo é o único mecanismo de validação científica reconhecido.

**Journals alvo (ordem de fit):**  
1. JCAP (Journal of Cosmology and Astroparticle Physics) — IF ~6
2. Physical Review D — IF ~5  
3. MNRAS Letters — IF ~6

**Pré-requisitos para submissão:**  
- [ ] MCMC com intervalos de confiança  
- [ ] Pantheon+ incluído  
- [ ] Ghost check completo  
- [ ] Comparação com w₀wₐCDM  
- [ ] Não apenas ΔAIC mas p-value e Bayes factor  

---

## CRONOGRAMA ESTIMADO

```
Fev-Mar 2026:  Pantheon+ pipeline + MCMC básico
Abr-Mai 2026:  fσ₈ integrado + Ghost check formal
Jun-Jul 2026:  Resultados completos + corner plots
Ago 2026:      Manuscrito arXiv (preprint)
Out 2026:      Submissão journal
```

---

## THRESHOLD PARA "EVIDÊNCIA POSITIVA"

Para que o RLL seja considerado cientificamente relevante (não apenas consistente):

```
χ²(RLL) − χ²(ΛCDM) < −8    [Δχ² = −8 mínimo]
ΔAIC < −2                   [AIC Jeffreys: "positivo"]  
Os0 = X ± σ com X/σ > 2    [detecção >2σ]
Consistente em ≥3 datasets  [CC + BAO + SNe + fσ₈]
```

**Status atual:** Nenhum threshold atingido. TRL 3. O modelo é *consistente* — não *evidenciado*.

---

## F_gap → F_next (ciclo RAFAELIA)

```
F_ok   : Equação formalizada | 45 obs testados | AIC calculado | código público
F_gap  : Pantheon+ | MCMC | fσ₈ | Ghost | arXiv
F_next : MCMC Os0 posterior | Pantheon+ Δχ² | fσ₈ sensibilidade
```

`Ω = coerência máxima quando F_gap → 0`

---

*Documento canônico v1.0 — ∆RafaelVerboΩ | Instituto Rafael | 2026*
