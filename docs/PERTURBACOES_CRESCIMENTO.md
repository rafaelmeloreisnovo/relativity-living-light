# Perturbações e Crescimento Estrutural
## Equação D''(a) com componente de superposição

**Módulo:** teoria/PERTURBACOES_CRESCIMENTO.md  
**Observável alvo:** fσ₈(z)  
**Dataset de validação:** BOSS DR12 RSD (público)

---

## 1. Equação de Crescimento Modificada

No modelo RLL, a equação de crescimento de perturbações lineares de matéria é:

```
D'' + [2 + d(lnH)/d(lna)] D' - (3/2) Ω_m(a) D = 0
```

onde as primas indicam derivadas em relação a ln(a), e:

```
Ω_m(a) = Ω_m0 · a^{-3} · H₀²/H²(a)
```

O denominador H²(a) contém a componente de superposição, modificando Ω_m(a) em relação ao ΛCDM.

### Diferença em relação ao ΛCDM

Em ΛCDM puro: `H²(a) = H₀²[Ω_m a^{-3} + Ω_Λ]`

No RLL: `H²(a)` inclui `Ω_s0 · [f(z) + (1-f)(1+z)³]`

Para Ω_s0 ≈ 0.06, isso reduz Ω_m(a) em 2–5% no intervalo 0.5 < z < 1.5, propagando para uma supressão de crescimento comparável.

---

## 2. Taxa de Crescimento e fσ₈(z)

### Taxa de crescimento

```
f(z) = d(lnD)/d(lna) ≈ Ω_m(a)^γ
```

com índice de crescimento `γ ≈ 0.55 + 0.05(1 + w_eff)`. Para w_eff(z) do modelo RLL, γ torna-se levemente dependente de z.

### Observável

```
fσ₈(z) = f(z) · σ₈(z) = f(z) · σ₈(0) · D(z)/D(0)
```

onde σ₈(0) = 0.811 ± 0.006 (Planck 2018 como referência).

### Previsão qualitativa do RLL

Para os parâmetros centrais (Ω_s0=0.059, z_t=1.16):

```
Δ(fσ₈)/fσ₈^ΛCDM ≈ −2% a −4%  para z ∈ [0.3, 0.8]
```

Essa supressão está dentro da incerteza dos dados BOSS atuais (~5%), mas é detectável com Euclid/DESI com incerteza ~1%.

---

## 3. Dados de Referência — BOSS DR12

| z_eff | fσ₈ observado | σ | Referência |
|-------|--------------|---|-----------|
| 0.38 | 0.497 | 0.045 | Alam et al. 2017 |
| 0.51 | 0.458 | 0.038 | Alam et al. 2017 |
| 0.61 | 0.436 | 0.034 | Alam et al. 2017 |

Dados adicionais de surveys complementares:

| z_eff | fσ₈ | σ | Survey |
|-------|-----|---|--------|
| 0.15 | 0.490 | 0.145 | 6dFGS |
| 1.40 | 0.482 | 0.116 | FastSound |
| 0.978 | 0.379 | 0.176 | VIPERS |

---

## 4. Código de Implementação

```python
import numpy as np
from scipy.integrate import solve_ivp, quad

def H2_RLL(z, params):
    """H²(z)/H₀² para o modelo RLL"""
    Om, OL, Os0, zt, wt = params
    a = 1.0/(1.0 + z)
    f = 1.0/(1.0 + np.exp((z - zt)/wt))
    H2 = (Om*(1+z)**3 
          + OL 
          + Os0*(f + (1-f)*(1+z)**3))
    return H2

def growth_equation(lna, y, params):
    """Sistema de EDO para crescimento: y = [D, D']"""
    D, Dprime = y
    z = np.exp(-lna) - 1.0
    a = np.exp(lna)
    
    H2 = H2_RLL(z, params)
    Om0 = params[0]
    
    # d(lnH²)/d(lna)
    dz_dlna = -a  # dz/da · da/dlna = -(1+z)/a · a = -(1+z)
    # Numérica via diferença finita
    dH2 = (H2_RLL(z - 0.001, params) - H2_RLL(z + 0.001, params)) / 0.002
    dlnH_dlna = 0.5 * dH2 / H2 * (-a)  # chain rule
    
    # Ω_m(a)
    Omz = Om0 * (1+z)**3 / H2
    
    # Equação de crescimento
    coeff = 2.0 + dlnH_dlna
    D_double_prime = -coeff * Dprime + 1.5 * Omz * D
    
    return [Dprime, D_double_prime]


def compute_fs8(z_array, params, sigma8_0=0.811):
    """
    Calcula fσ₈(z) para o modelo RLL.
    params = [Omega_m, Omega_Lambda, Omega_s0, z_t, w_t]
    """
    # Condições iniciais no matter domination (z_ini = 100)
    z_ini = 100.0
    lna_ini = np.log(1.0/(1.0 + z_ini))
    lna_0   = 0.0  # hoje
    
    # D_ini ∝ a, D'_ini = D_ini (growing mode)
    D_ini = 1.0/(1.0 + z_ini)
    y0 = [D_ini, D_ini]
    
    # Integrar de z_ini até hoje
    lna_span = [lna_ini, lna_0]
    lna_eval  = np.log(1.0/(1.0 + np.array(z_array)))
    
    sol = solve_ivp(
        growth_equation,
        lna_span,
        y0,
        args=(params,),
        t_eval=lna_eval,
        method='DOP853',
        rtol=1e-8
    )
    
    D_z   = sol.y[0]          # D(z)
    Dp_z  = sol.y[1]          # D'(z) = dD/d(lna)
    D_0   = D_z[-1]           # D(z=0) — normalization
    
    # f(z) = d(lnD)/d(lna) = D'/D
    f_rate = Dp_z / D_z
    
    # σ₈(z) = σ₈(0) · D(z)/D(0)
    sigma8_z = sigma8_0 * D_z / D_0
    
    # fσ₈(z)
    fs8 = f_rate * sigma8_z
    
    return fs8, D_z/D_0, f_rate


# Exemplo de uso
if __name__ == '__main__':
    import matplotlib.pyplot as plt
    
    # Parâmetros RLL centrais
    params_rll  = [0.315, 0.685 - 0.059, 0.059, 1.164, 0.405]
    # ΛCDM para comparação
    params_lcdm = [0.315, 0.685,         0.0,   1.0,   0.3  ]
    
    z_data = np.array([0.15, 0.38, 0.51, 0.61, 0.978, 1.40])
    fs8_boss = np.array([0.490, 0.497, 0.458, 0.436, 0.379, 0.482])
    fs8_err  = np.array([0.145, 0.045, 0.038, 0.034, 0.176, 0.116])
    
    z_plot = np.linspace(0.05, 1.8, 100)
    
    fs8_rll,  _, _ = compute_fs8(z_plot, params_rll)
    fs8_lcdm, _, _ = compute_fs8(z_plot, params_lcdm)
    
    plt.figure(figsize=(8, 5))
    plt.errorbar(z_data, fs8_boss, yerr=fs8_err, 
                 fmt='ko', ms=6, label='BOSS DR12 + outros', zorder=3)
    plt.plot(z_plot, fs8_lcdm, 'b--', lw=2, label=r'$\Lambda$CDM')
    plt.plot(z_plot, fs8_rll,  'r-',  lw=2, label='RLL (sintético)')
    plt.xlabel('Redshift z', fontsize=12)
    plt.ylabel(r'$f\sigma_8(z)$', fontsize=12)
    plt.title('Crescimento Estrutural: RLL vs ΛCDM vs Dados', fontsize=12)
    plt.legend(fontsize=11)
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig('../figs/fs8_comparison.png', dpi=150)
    plt.show()
    
    # Desvio percentual
    fs8_rll_data, _, _ = compute_fs8(z_data.tolist(), params_rll)
    fs8_lcdm_data, _, _ = compute_fs8(z_data.tolist(), params_lcdm)
    delta = 100*(fs8_rll_data - fs8_lcdm_data)/fs8_lcdm_data
    print("Desvio RLL vs ΛCDM em fσ₈(z):")
    for z, d in zip(z_data, delta):
        print(f"  z={z:.2f}: {d:+.2f}%")
```

---

## 5. Forecast para Euclid e DESI

A precisão esperada em fσ₈(z) pelos surveys futuros é:

| Survey | z range | σ(fσ₈) típico | Detectável (2σ se Δ>2%)? |
|--------|---------|--------------|--------------------------|
| BOSS DR12 | 0.2–0.7 | 3–5% | Marginal |
| DESI full | 0.1–1.6 | 0.5–1.5% | ✅ Sim |
| Euclid    | 0.9–1.8 | 0.3–0.8% | ✅ Sim |

---

## 6. Critério de Falsificabilidade

O modelo RLL no setor de crescimento é falsificado se:

- DESI/Euclid medir fσ₈(z) indistinguível de ΛCDM em todo z ∈ [0.3, 1.8] com σ < 1%
- Ou se o modelo produzir supressão de crescimento inconsistente com σ₈ do CMB Planck (requer verificação de consistência CMB–LSS)
