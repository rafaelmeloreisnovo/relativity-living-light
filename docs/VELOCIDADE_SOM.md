# Velocidade do Som e Escala de Jeans
## cs²(z) para o componente de superposição RLL

**Módulo:** teoria/VELOCIDADE_SOM.md  
**Relevância:** Estabilidade de perturbações, formação de estruturas

---

## 1. Definição Física

A velocidade do som determina a escala mínima de colapso gravitacional (escala de Jeans) e a propagação de perturbações no fluido.

Para o componente de superposição com densidade e pressão:

```
ρ_sup(a) = Ω_s0 ρ_c0 [f(z) + (1-f)(1+z)³]
p_sup(a) = −f(z) · Ω_s0 ρ_c0 · c²
```

---

## 2. Velocidade do Som Adiabática

```
cs²_ad = δp/δρ|_entropy = ṗ/ρ̇
```

Calculando:

```
ṗ   = −df/dt · Ω_s0 ρ_c0 c²
ρ̇   = Ω_s0 ρ_c0 [df/dt − (df/dt)(1+z)³ + (1-f) · d(1+z)³/dt]
    = Ω_s0 ρ_c0 [df/dt (1 − (1+z)³) − 3H(1+z)³(1-f)]
```

Para z >> z_t: cs²_ad → 0 (ramo tipo matéria no limite canônico)  
Para z << z_t: cs²_ad → −c² (ramo DE-like no limite canônico; forma adiabática torna-se não física)

**Problema:** cs²_ad < 0 no limite baixo-redshift (z << z_t) indica instabilidade de gradiente na forma adiabática.

---

## 3. Velocidade do Som Prescrita (solução física)

A solução padrão na literatura de campos escalares é prescrever a velocidade do som no referencial de repouso do fluido:

```
cs²_rest = c² · f(z)
```

Esta prescrição garante cs² ∈ [0, c²] por construção:

| Regime | f(z) | cs²/c² | Interpretação |
|--------|------|--------|--------------|
| z >> z_t | f → 0 | 0 | Matter-like (pressureless) |
| z ≈ z_t | f ≈ 0.5 | 0.5 | Transição |
| z << z_t | f → 1 | 1 | DE-like (não-clusterizante) |

Esta prescrição é análoga à usada em modelos de matéria escura quente e em modelos de quintessência de campo escalar canônico.

---

## 4. Escala de Jeans

A escala de Jeans — abaixo da qual o componente não colapsa gravitacionalmente — é:

```
λ_J(z) = cs · √(π / (G ρ_sup(z)))
         ≈ cs/H(z) · (3/2 · Ω_sup(a))^{-1/2}
```

Em termos de número de onda:

```
k_J(z) = a(z) H(z) / cs(z) · √(3/2 · Ω_sup(a))
```

Para os parâmetros centrais em z ≈ z_t = 1.16:

```
cs(z_t) = c · √(f(z_t)) = c · √0.5 ≈ 0.71c
H(z_t)  ≈ 1.5 H₀ ≈ 105 km/s/Mpc
k_J     ≈ a · 105 km/s/Mpc · 1/0.71 · 0.3 ≈ 0.007 h/Mpc
λ_J     ≈ 900 Mpc/h
```

Essa escala de Jeans enorme (~900 Mpc/h) significa que o componente de superposição **não colapsa** em nenhuma escala relevante para formação de estrutura (galáxias e clusters são << 10 Mpc/h). O componente se comporta efetivamente como fluido suave em todas as escalas observáveis.

---

## 5. Implicação para Perturbações

Dado que λ_J >> λ_Hubble para todo o regime relevante, as perturbações do componente de superposição não crescem por instabilidade de Jeans. O efeito do componente no crescimento de perturbações de matéria é **puramente gravitacional**, via modificação de H(z) e Ω_m(z).

Isso é matematicamente conveniente: as perturbações δ_sup podem ser tratadas como parte do "background" quando se calculam as perturbações de matéria δ_m que geram fσ₈(z).

---

## 6. Verificação Numérica

```python
import numpy as np

def jeans_scale_Mpc(z, Os0=0.059, zt=1.164, wt=0.405, Om0=0.315, OL=0.626):
    """Escala de Jeans em Mpc/h para o componente de superposição."""
    f = 1.0/(1.0 + np.exp((z - zt)/wt))
    cs_over_c = np.sqrt(f)
    
    E2 = Om0*(1+z)**3 + OL + Os0*(f + (1-f)*(1+z)**3)
    H_over_H0 = np.sqrt(E2)
    
    Omega_sup = Os0*(f + (1-f)*(1+z)**3) / E2
    
    # H₀ = 70 km/s/Mpc → 1/H₀ ≈ 4300 Mpc/h
    # λ_J = cs/H · (3/2 Ω_sup)^{-1/2}
    cs_over_H = cs_over_c / H_over_H0  # em unidades de c/H₀
    lambda_J  = (3e5 / 70.0) * cs_over_H * (1.5*Omega_sup)**(-0.5) * (1.0/(1+z))
    return lambda_J

z_test = [0.1, 0.5, 1.0, 1.16, 2.0, 3.0]
print("z    | cs/c  | λ_J [Mpc/h]")
print("-" * 35)
for z in z_test:
    f = 1.0/(1.0 + np.exp((z - 1.164)/0.405))
    lJ = jeans_scale_Mpc(z)
    print(f"{z:.2f} | {np.sqrt(f):.4f} | {lJ:.1f}")
```
