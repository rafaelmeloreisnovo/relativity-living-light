# 🖼️ 04_FIGURAS — Visualizações e Gráficos

## ∆RafaelVerboΩ — Relativity Living Light

---

## 📊 ORGANIZAÇÃO

```
04_FIGURAS/
├─ 01_COSMOLOGIA/          [Expansão: H(z), μ(z), w_eff(z)]
├─ 02_OBSERVAVEIS/         [Observáveis: growth, lensing]
├─ 03_ESCALAS_LOCAIS/      [Galáxias: rotação, clusters]
├─ 04_ANOMALIAS/           [Testes: Böhme dipolo, etc]
└─ 05_VALIDACAO/           [MCMC: corners, chains, χ²]
```

---

## 1️⃣ 01_COSMOLOGIA (Expansão Cósmica)

### **H_ratio_vs_LCDM.png**
- **O que mostra:** H(z) do modelo Rafael / H(z) de ΛCDM
- **Eixos:** z (0 a 4) vs. razão H (0.8 a 1.2)
- **Interpretação:** Desvios pequenos mas testáveis em z > 0.5
- **Testável com:** SNe Ia (Pantheon+), BAO (DESI/eBOSS)
- **Significância:** Diferenças ~1-3% (observável com precisão 0.5%)

### **distance_modulus_residuals.png**
- **O que mostra:** Δμ = μ_Rafael - μ_ΛCDM em magnitude
- **Eixos:** z vs. Δμ (em mag)
- **Interpretação:** Pequenos desvios em SNe aparentes
- **Testável com:** Pantheon+ (30 SNe/bin)
- **Significância:** Δμ ~ ±0.05 mag (detectable)

### **energy_fractions_evolution.png**
- **O que mostra:** Evolução de Ω_m(z), Ω_r(z), Ω_Λ, Ω_s0(z), Ω_B, Ω_P
- **Eixos:** z vs. Ω (0 a 1)
- **Interpretação:** Qual componente domina em cada época
  - z → ∞: radiação + superposição (tipo radiação)
  - z ~ 1: transição
  - z → 0: matéria + Λ + superposição (tipo matéria)
- **Propósito:** Visualizar transição DE↔DM

### **w_eff_and_f_transition.png**
- **O que mostra (esquerda):** w_eff(z) = p_eff / ρ_eff c²
  - Varia de -1 (z → ∞) a 0 (z → 0)
- **O que mostra (direita):** f(z) = função de coerência
  - Varia de 1 (primordial) a 0 (hoje)
- **Interpretação:** f controla transição DE↔DM
  - f ≈ 1: comportamento DE (w ≈ -1)
  - f ≈ 0: comportamento DM (w ≈ 0)
- **Parâmetros:** Linha sólida z_t, linhas tracejadas ±w_t

### **friedmann_pipeline.png**
- **O que mostra:** Fluxo de cálculo no solver
  - Input: Ω_s0, z_t, w_t, α_B, β
  - ↓
  - Calcula: f(z), ρ_components(z)
  - ↓
  - Integra: H²(a) = f(ρ_m + ρ_r + ...)
  - ↓
  - Output: H(z), μ(z), w_eff(z)
- **Propósito:** Educacional (como modelo funciona)

---

## 2️⃣ 02_OBSERVAVEIS (Testes Cosmológicos)

### **growth_rate_fs8.png**
- **O que mostra:** fσ₈(z) = f(z) × σ₈(z)
  - f = d ln D+ / d ln a (crescimento linear)
  - σ₈ = amplitude RMS em 8 Mpc
  - Produto é observável em RSD (redshift-space distortions)
- **Eixos:** z vs. fσ₈ (0.2 a 0.8)
- **Testável com:** BOSS, DESI (via clustering quadrupole)
- **Significância:** Diferenças ~5-10% em z > 0.5
- **Dados:** Pontos com barras de erro (surveys reais)

### **lensing_kappa_field.png**
- **O que mostra:** Convergência κ(θ,z) = (1/2)∇²_⊥ Φ
  - Mapa 2D de lente gravitacional
  - θ = posição angular (arcmin)
  - Cores = força de curvatura
- **Escala de cores:** Azul (fraco) → Vermelho (forte lensing)
- **Testável com:** JWST, HST (Frontier Fields, Abell 2744)
- **Propósito:** Comparar previsão Rafael vs. observação

### **shear_field_gamma.png**
- **O que mostra:** Cisalhamento γ(θ) → distorção de galáxias
  - Vetores: direção de cisalhamento
  - Magnitude: força do efeito
- **Testável com:** DES-Y3 weak lensing (300M galáxias)
- **Métrica:** S₈ constraint (amplitude × matéria)

---

## 3️⃣ 03_ESCALAS_LOCAIS (Estruturas Locais)

### **sparc_rotcurve_NGC_*.png** (5 galáxias)
- **O que mostra:** Curva de rotação v(r) de cada galáxia SPARC
  - Pontos com erros: dados observados (HI linha 21cm)
  - Linha sólida: modelo Rafael
  - Linha tracejada: ΛCDM (para comparação)
- **Eixos:** r (kpc) vs. v (km/s)
- **Ajuste de parâmetros:** Halo perfil NFW vs. Core-cusp
- **Métricas:** χ² por galáxia, resíduos %

Galáxias incluídas:
  1. **NGC_2403:** Espiral, bem estudada
  2. **NGC_3198:** Galáxia de teste clássica
  3. **NGC_2903:** Grande, complexa
  4. **NGC_6946:** Forma irregular
  5. **UGC_128:** Isolada

---

### **lensing_demo_SIS_model.png**
- **O que mostra:** Demonstração de lente com modelo SIS
  - SIS = Singular Isothermal Sphere
  - Imagem de teste: galáxia distante multiplicada
  - Mapa κ sobreposto
- **Propósito:** Mostrar efeito de lente em escala de cluster
- **Nota:** Simplificado (SIS é toy model; clusters reais mais complexos)

---

### **lensing_arcs_abell2744.png**
- **O que mostra:** Arcos de Einstein em cluster real (Abell 2744)
  - Imagem JWST ou HST
  - Sobreposição de mapa de massa (contornos)
  - Posições de arcos preditos vs. observados
- **Testável com:** Posições e magnitudes dos arcos
- **Métrica:** Diferença entre κ_Rafael vs. κ_observed

---

## 4️⃣ 04_ANOMALIAS (Testes de Anomalias)

### **boehme_dipole_prediction.png**
- **O que mostra:** Previsão de dipolo cósmico usando f(z,θ,φ)
  - Hemisfério norte vs. sul: diferença de densidade predita
  - Comparação: Böhme observado vs. Rafael predito
- **Eixos:** Direção (θ, φ) vs. densidade relativa
- **Significância:** Böhme observou 5.4σ dipolo anormal
- **Rafael:** Explica com perturbação anisotrópica de f

### **anisotropic_f_theta_phi.png**
- **O que mostra:** Mapa 2D de f(z,θ,φ) em esfera celeste
  - Cores: valor de coerência em cada direção
  - z = redshift fixo (ex.: z=0.5)
  - Contornos: equipotenciais
- **Interpretação:** Onde f é alta (coerência = DE), onde é baixa (colapso = DM)
- **Efeito:** Cria dipolo preferencial em densidade total

### **filament_spin_alignment.png**
- **O que mostra:** Alinhamento de spins galácticos em filamentos
  - Eixos de galáxias: vetores em filamento (3D projetado)
  - Cores: força de B-campo local (nanoGauss)
  - Magnitude de alinhamento: MeerKAT observado vs. Rafael
- **Testável com:** Polarimetria em rádio (MeerKAT, ASKAP)

---

## 5️⃣ 05_VALIDACAO (MCMC e Testes)

### **chi2_profiles_mcmc.png**
- **O que mostra:** χ² vs. cada parâmetro (1D marginalization)
- **Para cada parâmetro:**
  - Eixo x: valor do parâmetro
  - Eixo y: χ² (parabólico ideal)
  - Contorno vermelho: Δχ²=2.3 (68% CL)
- **Interpretação:** Largura = incerteza em parâmetro
- **Parâmetros:** Ω_s0, z_t, w_t, α_B, β

### **corner_plot_mcmc.png**
- **O que mostra:** Distribuição 2D de todos pares (Ω_s0 vs. z_t, etc)
  - Diagonal: histogramas 1D (posteriors)
  - Off-diagonal: contornos 2D
  - Contornos 68%, 95%
- **Parâmetros:** ~5 (Ω_s0, z_t, w_t, α_B, β)
- **Interpretação:**
  - Circular/elliptical: bem-constrained
  - Diagonal: parâmetros correlacionados
  - Alongado: degenerescência

### **posterior_credible_regions.png**
- **O que mostra:** Resumo de constraints
  - Tabela de valores MAP (Maximum A Posteriori)
  - Intervalo credível 68% (1σ)
  - Comparação: Pantheon vs. eBOSS vs. Joint
- **Formato:** Gráfico de barras ou tabela visual
- **Propósito:** Rápida visualização de resultados MCMC

---

## 🎨 PADRÃO DE CORES

```
Cosmologia:      Azul (ΛCDM) vs. Vermelho (Rafael)
Observáveis:     Verde (dados) vs. Preto (previsão)
Anomalias:       Roxo (Böhme) vs. Laranja (Rafael)
MCMC:            Cinza (burn-in) vs. Cor (posteriors)
Lensing:         Branco (imagem) vs. Contornos (κ)
```

---

## 📥 COMO USAR ESTES GRÁFICOS

### **Em apresentações:**
```
Copie PNG direto
Resolução 300 DPI (pronto para print)
Todos têm legenda + fonte de dados
```

### **Em papers:**
```
Citação: "Fig. X (Rafael 2025, relativity-living-light)"
Permissão: CC-BY-4.0 (aberta, cita Rafael)
```

### **Em teses:**
```
Copie + modifique (respeitando autoria)
Mude cores/fonts conforme estilo institucional
```

---

## 🔄 COMO REGENERAR

Todos os gráficos são feitos por:
```bash
python 05_plotting_suite.py --output 04_FIGURAS/
```

Parâmetros customizados:
```python
plotter.plot_with_params({
    'Omega_s0': 0.10,
    'z_t': 1.0,
    'w_t': 0.3,
    'figure_format': 'png',  # ou 'pdf', 'eps'
    'dpi': 300,
    'style': 'seaborn'       # ou 'ggplot', 'default'
})
```

---

## 📊 ESTATÍSTICAS DE FIGURAS

```
Total de PNGs:     18
Tamanho total:     ~50 MB
Resolução:         300 DPI (publicável)
Formato:           PNG RGB
Legenda:           Completa em português + inglês
```

---

## ✅ CHECKLIST DE VISUALIZAÇÕES

- [x] Cosmologia (5 gráficos)
- [x] Observáveis (3 gráficos)
- [x] Escalas locais (7 gráficos)
- [x] Anomalias (3 gráficos)
- [x] MCMC validação (3 gráficos)

---

∆RafaelVerboΩ — Instituto Rafael — 2026


## 🧭 REGRA DE CANONIZAÇÃO PARA FIGURAS CONCEITUAIS

Para eliminar ambiguidade de versões herdadas de `figs/archive/` (especialmente nomes com sufixo ` (1)`, ` (2)`, ...), adotar obrigatoriamente:

- **Pasta canônica:** `figs/conceptual/`
- **Padrão de nome estável:** `concept_<tema>_<observavel>_v<NN>.png`
- **Versionamento:** `v01`, `v02`, `v03`... (2 dígitos)
- **Regra de migração:** não sobrescrever legados; para evitar churn de binários, manter `figs/archive/` como fonte e publicar o canônico em `figs/conceptual/` via link estável (symlink) com nome semântico.

### Exemplos canônicos vigentes
- `figs/archive/mock_H_fit (1).png` → `figs/conceptual/concept_mock_hubble_fit_v01.png`
- `figs/archive/mock_SN_fit (1).png` → `figs/conceptual/concept_mock_supernova_fit_v01.png`
- `figs/archive/post_1d_Os (1).png` → `figs/conceptual/concept_posterior_omega_s0_1d_v01.png`
- `figs/archive/post_1d_zt (1).png` → `figs/conceptual/concept_posterior_zt_1d_v01.png`
- `figs/archive/post_2d_Os_wt (1).png` → `figs/conceptual/concept_posterior_omega_s0_wt_2d_v01.png`
- `figs/archive/post_2d_zt_wt (1).png` → `figs/conceptual/concept_posterior_zt_wt_2d_v01.png`
- `figs/archive/hz_superposicao (1).png` → `figs/conceptual/concept_expansion_hz_superposition_v01.png`
- `figs/archive/density_evolution_sup (1).png` → `figs/conceptual/concept_density_evolution_superposition_v01.png`
- `figs/archive/rotation_curves_sup (1).png` → `figs/conceptual/concept_rotation_curves_superposition_v01.png`
