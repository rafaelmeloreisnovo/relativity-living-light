# 🌌 Relativity Living Light — Unified Photonic Superposition Model (v4)

## 🇧🇷 Síntese (PT)

Propomos que a **superposição fotônica** atua como um componente energético dinâmico que **transita** de w ≈ -1 (expansivo, tipo energia escura) para w ≈ 0 (atrativo, tipo matéria).
Esse estado é **modulado** por **campos magnéticos cósmicos** e pelas condições **plasmáticas** (temperatura, pressão), integrando-se de forma natural na equação de Friedmann:

E²(a) = Ω_r a⁻⁴ + Ω_m a⁻³ + Ω_Λ +
Ω_s0 [f(a) + (1-f) a⁻³]   ← superposição (DE→matéria)
+ Ω_B0 a⁻⁴                ← campo magnético
+ Ω_P0 a⁻⁴                ← plasma (T,P)

com f(z) = 1 / (1 + exp((z - z_t)/w_t)).

### Convenção oficial de sinais e limites

Fonte canônica explícita: [`docs/canonicos/09_GLOSSARIO_COMPLETO.md`](docs/canonicos/09_GLOSSARIO_COMPLETO.md).

- **Fórmula oficial / Official formula:** `f(z) = 1/(1 + exp((z - z_t)/w_t))`.
- **Hipótese oficial de sinal/intervalo de `w_t` / Official sign-range hypothesis for `w_t`:** adota-se `w_t < 0`, com `|w_t| ∈ [0.1, 1.0]`.
- **Exemplos numéricos / Numerical examples** (referência/reference: `z_t = 1.0`, `w_t = -0.3`):
  - `z = 0` → `f(0) ≈ 0.034`.
  - `z = z_t` → `f(z_t) = 0.5`.
  - `z >> z_t` (ex.: `z = 5`) → `f(5) ≈ 0.999998`.
- **Interpretação física coerente / Coherent physical interpretation:** nesta convenção `f` cresce com `z`; portanto, o setor de superposição domina em alto redshift (`f→1`) e perde peso em baixo redshift (`f→0`), com transição suave em torno de `z_t`.

Opcionalmente: **correção magneto-coerente**
Ω_s0 → Ω_s0 {1 + α_B (Ω_B0 a⁻⁴)^β}.

---

### 🔬 Observáveis e Testes com Imagens

**H(z) ratio**
![H(z) ratio](../figs/paper/unified_H_ratio.png)

**Δμ residuals**
![Δμ residuals](../figs/paper/unified_mu_residuals.png)

**Frações de energia**
![Frações](../figs/paper/unified_fractions.png)

**f(z) e w_eff(z)**
![f(z) e w_eff(z)](../figs/paper/unified_f_and_weff.png)

**Bandas de entropia (10/12) — H(z) ratio**
![Entropy margin H ratio](../figs/paper/unified_entropy_Hratio.png)

**Bandas de entropia (10/12) — Δμ**
![Entropy margin Δμ](../figs/paper/unified_entropy_dmu.png)

**Crescimento de estrutura fσ8(z)**
![fσ8(z)](../figs/paper/unified_growth_fs8.png)

**Curvas de rotação (toy SPARC, NGC 2403 demo)**
![RotCurve NGC 2403](../figs/paper/rotcurve_NGC_2403.png)

**Lensing de aglomerado (demo SIS)**
![Einstein Rings](../figs/paper/cluster_lensing_SIS_unified.png)

---

## 🇺🇸 Summary (EN)

We posit **photonic superposition** as a dynamic energy component that **transitions** from w ≈ -1 (dark-energy-like, expansive) to w ≈ 0 (matter-like, clustering).
This state is **modulated** by **cosmic magnetic fields** and **plasma conditions** (temperature, pressure), naturally extending the Friedmann equation.

---

### 🔬 Key Observables with Figures

**H(z) ratio**
![H(z) ratio](../figs/paper/unified_H_ratio.png)

**Δμ residuals**
![Δμ residuals](../figs/paper/unified_mu_residuals.png)

**Energy Fractions**
![Fractions](../figs/paper/unified_fractions.png)

**f(z) and w_eff(z)**
![f(z) and w_eff(z)](../figs/paper/unified_f_and_weff.png)

**Entropy-margin (10/12) H ratio**
![Entropy margin H ratio](../figs/paper/unified_entropy_Hratio.png)

**Entropy-margin (10/12) Δμ**
![Entropy margin Δμ](../figs/paper/unified_entropy_dmu.png)

**Structure growth fσ8(z)**
![fσ8(z)](../figs/paper/unified_growth_fs8.png)

**Rotation curve (toy SPARC, NGC 2403 demo)**
![RotCurve NGC 2403](../figs/paper/rotcurve_NGC_2403.png)

**Cluster lensing (SIS demo)**
![Einstein Rings](../figs/paper/cluster_lensing_SIS_unified.png)
