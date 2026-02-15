# 💻 02_CODIGO_NUMERICO — Solvers e Ferramentas

## ∆RafaelVerboΩ — Relativity Living Light

---

## 📖 O QUE ESTÁ AQUI

Código Python completo para integrar numericamente o modelo unificado de Rafael.

```
├─ 01_friedmann_solver.py      [Core: Friedmann integrada]
├─ 02_weff_calculator.py       [w_eff(z) e derivadas]
├─ 03_observable_functions.py  [H(z), μ(z), fσ8(z), etc]
├─ 04_mcmc_runner.py           [Ajuste MCMC contra dados]
├─ 05_plotting_suite.py        [Gera todas as figuras]
├─ requirements.txt            [Dependências Python]
└─ notebooks/
   ├─ 01_Quick_Start.ipynb           [Tutorial 5 min]
   ├─ 02_MCMC_Analysis.ipynb         [Análise de chains]
   ├─ 03_SPARC_Fitting.ipynb         [Curvas de rotação]
   └─ 04_External_Comparison.ipynb   [vs. estudos 2025-26]
```

---

## 🚀 SETUP RÁPIDO

### **1. Instalar dependências**

```bash
pip install -r requirements.txt
```

**Dependências principais:**
- numpy, scipy, matplotlib
- pandas (para CSVs)
- emcee ou Cobaya (MCMC)
- astropy (constantes, unidades)

---

### **2. Teste rápido (30 seg)**

```bash
python 01_friedmann_solver.py --quick
```

**Output esperado:**
```
H(z=0): 70.0 km/s/Mpc
H(z=0.5): 88.4 km/s/Mpc
H(z=1.0): 117.2 km/s/Mpc
✅ Integração OK
```

---

### **3. Rodar modelo completo**

```bash
python 01_friedmann_solver.py \
  --Omega_s0 0.10 \
  --z_t 1.0 \
  --w_t 0.3 \
  --output ../03_DADOS/my_model.csv
```

**Output:** CSV com H(z), μ(z), f(z), w_eff(z) para z ∈ [0, 4]

---

## 📊 FLUXO DE USO

```
[Parâmetros] 
    ↓
[01_friedmann_solver.py] → H(z), E(z)
    ↓
[02_weff_calculator.py] → w_eff(z)
    ↓
[03_observable_functions.py] → Δμ, fσ8, κ
    ↓
[04_mcmc_runner.py] ← [Dados: SNe, BAO, CMB]
    ↓
[05_plotting_suite.py] → 04_FIGURAS/
```

---

## 📝 DESCRIÇÃO DE CADA SCRIPT

### **01_friedmann_solver.py**

**O que faz:** Integra numericamente a equação de Friedmann estendida

**Entrada:**
```python
{
  'Omega_r': 9e-5,
  'Omega_m': 0.30,
  'Omega_Lambda': 0.70,
  'Omega_s0': 0.10,       # superposição
  'z_t': 1.0,             # redshift transição
  'w_t': 0.3,             # largura transição
  'Omega_B0': 1e-5,       # campo magnético
  'Omega_P0': 1e-5,       # plasma
  'alpha_B': 0.5,         # acoplamento magneto-coerência
  'beta': 1.0,
  'H0': 70.0,             # Hubble hoje
  'z_max': 4.0,           # redshift máximo
  'n_points': 500         # pontos de integração
}
```

**Saída:**
```python
{
  'z': array([0.0, 0.01, ..., 4.0]),
  'a': 1/(1+z),
  'H': array([70.0, 70.5, ...]),
  'E': H/H0,
  'rho_total': array([...]),
  'rho_components': {
    'radiation': [...],
    'matter': [...],
    'superposition': [...],
    'magnetic': [...],
    'plasma': [...]
  }
}
```

**Uso:**
```python
from friedmann_solver import FriedmannSolver

solver = FriedmannSolver(params)
result = solver.integrate()

# Acessar
z = result['z']
H_z = result['H']
```

---

### **02_weff_calculator.py**

**O que faz:** Calcula w_eff(z) e equação de estado numérica

**Derivação:**
```
w_eff(z) = (p_eff) / (ρ_eff c²)

Entrada: H(z), ρ_components do 01_friedmann_solver

Saída: w_eff(z), derivadas dw/dz
```

**Uso:**
```python
from weff_calculator import WeeffCalculator

calc = WeeffCalculator(H_result, params)
w_eff = calc.compute_weff()
dw_dz = calc.compute_derivative()

# Plot
import matplotlib.pyplot as plt
plt.plot(calc.z, w_eff)
plt.ylabel('w_eff(z)')
```

---

### **03_observable_functions.py**

**O que faz:** Calcula todos observáveis cosmológicos

**Observáveis:**

| Função | Output | Unidades |
|---|---|---|
| `H_z(z)` | Hubble | km/s/Mpc |
| `comoving_distance(z)` | D_c | Mpc |
| `luminosity_distance(z)` | D_L | Mpc |
| `distance_modulus(z)` | μ | magnitude |
| `growth_rate(z)` | f(z) | adimensional |
| `sigma8_z(z)` | σ8(z) | amplitude |
| `f_sigma8(z)` | f×σ8 | RSD standard |
| `convergence(theta, z)` | κ | lensing convergence |

**Uso:**
```python
from observable_functions import Observables

obs = Observables(H_result)

mu = obs.distance_modulus(z=0.5)  # magnitude
fs8 = obs.f_sigma8(z=0.8)         # crescimento
kappa = obs.convergence(theta=0.1, z=1.0)  # lensing
```

---

### **04_mcmc_runner.py**

**O que faz:** Ajusta parâmetros de Rafael contra dados reais

**Dados suportados:**
- Pantheon+ (SNe Ia): H(z), Δμ
- eBOSS (BAO): DV/rd, H×rd
- Planck 2018 (CMB): priors em H0, Ωm
- DES-Y3: S8 fraco lensing

**Uso:**
```bash
# Ajuste SNe + BAO + CMB
python 04_mcmc_runner.py \
  --data pantheon_eboss_planck \
  --n_walkers 100 \
  --n_steps 5000 \
  --output_chains ../03_DADOS/mcmc_chains/

# Resultado: corner plots, χ², contours
```

**Output:**
```
../03_DADOS/mcmc_chains/
├─ posterior_samples.csv      [todas as amostras)
├─ corner_plot.png            [2D contours]
├─ chi2_profiles.png          [χ² vs. parâmetro]
└─ best_fit_params.json       [MAP estimate]
```

---

### **05_plotting_suite.py**

**O que faz:** Gera todos os gráficos para 04_FIGURAS/

**Gráficos gerados:**

```bash
python 05_plotting_suite.py --output ../04_FIGURAS/
```

Cria:
```
04_FIGURAS/01_COSMOLOGIA/
├─ H_ratio_vs_LCDM.png
├─ distance_modulus_residuals.png
├─ energy_fractions_evolution.png
├─ w_eff_and_f_transition.png
└─ friedmann_pipeline.png

04_FIGURAS/02_OBSERVAVEIS/
├─ growth_rate_fs8.png
├─ lensing_kappa_field.png
└─ shear_field_gamma.png

04_FIGURAS/03_ESCALAS_LOCAIS/
├─ sparc_rotcurve_*.png (5)
├─ lensing_demo_SIS.png
└─ lensing_arcs_abell2744.png

04_FIGURAS/04_ANOMALIAS/
├─ boehme_dipole_prediction.png
├─ anisotropic_f_theta_phi.png
└─ filament_spin_alignment.png

04_FIGURAS/05_VALIDACAO/
├─ chi2_profiles_mcmc.png
├─ corner_plot_mcmc.png
└─ posterior_credible_regions.png
```

**Uso customizado:**
```python
from plotting_suite import PlottingSuite

plotter = PlottingSuite(result_model)
plotter.plot_cosmology()
plotter.plot_observables()
plotter.plot_mcmc_results()
plotter.save_all('../04_FIGURAS/')
```

---

## 📓 NOTEBOOKS JUPYTER

### **01_Quick_Start.ipynb** — Tutorial 5 minutos

```jupyter
# Setup
import numpy as np
from friedmann_solver import FriedmannSolver

# Parâmetros
params = {
    'Omega_s0': 0.10,
    'z_t': 1.0,
    'w_t': 0.3,
}

# Rodar
solver = FriedmannSolver(params)
result = solver.integrate()

# Plot
import matplotlib.pyplot as plt
plt.plot(result['z'], result['H'])
plt.ylabel('H(z) [km/s/Mpc]')
plt.show()
```

---

### **02_MCMC_Analysis.ipynb** — Análise de chains

```jupyter
# Carregar MCMC
import pandas as pd
chains = pd.read_csv('../03_DADOS/mcmc_chains/posterior_samples.csv')

# Estatísticas
print(chains.describe())

# Corner plot
import corner
corner.corner(chains, labels=['Omega_s0', 'z_t', 'w_t', ...])

# Convergência
import emcee
# verificar tau, R_hat, etc
```

---

### **03_SPARC_Fitting.ipynb** — Curvas de rotação

```jupyter
# Carregar SPARC
from sparc_fitting import SPARC_Fitter

fitter = SPARC_Fitter('../03_DADOS/reference_models/sparc_toy_sample.csv')

# Ajustar 5 galáxias
for gal in ['NGC_2403', 'NGC_3198', ...]:
    result = fitter.fit_galaxy(gal)
    print(f"{gal}: χ² = {result['chi2']:.3f}")

# Plot
fitter.plot_all_fits('../04_FIGURAS/03_ESCALAS_LOCAIS/')
```

---

### **04_External_Comparison.ipynb** — vs. Estudos 2025-26

```jupyter
# Comparação com Minnesota
from external_comparison import ExternalComparison

comp = ExternalComparison(result_rafael)

# MD transition (Minnesota)
comp.plot_md_transition_vs_minnesota()

# w(z) dinâmica (DESI)
comp.plot_w_vs_desi()

# Alinhamento spins (MeerKAT)
comp.plot_spin_alignment_vs_meerkat()

# Etc.
```

---

## ⚙️ ESTRUTURA DE CLASSES

### **FriedmannSolver (classe principal)**

```python
class FriedmannSolver:
    def __init__(self, params):
        """
        params: dict com Omega_*, z_t, w_t, alpha_B, etc
        """
        
    def integrate(self, z_max=4, n_points=500):
        """Integra Friedmann de z=0 até z=z_max"""
        
    def get_H(self, z):
        """H(z) em qualquer z (interpolação)"""
        
    def get_rho_components(self, z):
        """ρ de cada componente"""
```

---

## 🧪 TESTES UNITÁRIOS

```bash
python -m pytest tests/ -v
```

Testes incluem:
- ✅ Continuidade H(z)
- ✅ Limite ΛCDM (Ω_s0→0)
- ✅ Planicidade (Σ Ω = 1)
- ✅ Positividade ρ
- ✅ Causality (H sempre positivo)

---

## 📊 EXEMPLOS DE SAÍDA

### **Modelo Rápido**
```bash
python 01_friedmann_solver.py --quick > output.txt
```

Output:
```
z         H(z)      E(z)      ρ_sup(z)   w_eff(z)
0.0       70.0      1.000     0.100      -0.80
0.5       88.5      1.264     0.085      -0.55
1.0       117.2     1.675     0.060      -0.20
2.0       194.8     2.783     0.025      0.05
```

### **MCMC Resultado**
```
MCMC Best Fit:
  Omega_s0 = 0.087 +0.015 -0.012  (68% CL)
  z_t = 0.95 +0.35 -0.28
  w_t = 0.28 +0.12 -0.10
  alpha_B = 0.42 +0.25 -0.20

χ² (Pantheon+): 710.2 / 1048 dof
χ² (eBOSS):    152.3 / 156 dof
χ² (Planck):   28.4 / 30 dof
```

---

## 🐛 TROUBLESHOOTING

### **Erro: "ImportError: No module named 'emcee'"**
```bash
pip install emcee
```

### **Erro: "z_max deve ser > 0"**
```python
# Verifique:
if params['z_max'] <= 0:
    raise ValueError("z_max > 0 obrigatório")
```

### **MCMC converge lentamente**
```bash
# Aumente:
--n_walkers 200   # default 100
--n_steps 10000   # default 5000
```

---

## 📚 REFERÊNCIAS

- **Numpy/Scipy:** https://docs.scipy.org/
- **Emcee (MCMC):** https://emcee.readthedocs.io/
- **Astropy:** https://docs.astropy.org/
- **Matplotlib:** https://matplotlib.org/

---

## 🎓 PARA CONTRIBUIR

Se quer estender o código:

1. **Clone branch novo:**
   ```bash
   git checkout -b feature/novo_observavel
   ```

2. **Adicione função em 03_observable_functions.py:**
   ```python
   def meu_novo_observavel(z):
       """Documentação clara"""
       return resultado
   ```

3. **Teste:**
   ```bash
   pytest tests/test_novo_observavel.py
   ```

4. **PR para main**

---

## 📞 SUPORTE

Dúvidas? Abra Issue no GitHub ou veja 10_FAQ_COMPLETO.md

---

∆RafaelVerboΩ — Instituto Rafael — 2026
