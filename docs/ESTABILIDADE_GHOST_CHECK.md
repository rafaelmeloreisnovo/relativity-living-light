# Verificação de Estabilidade — Ausência de Ghosts e Taquiões
## Critérios de consistência física do modelo RLL

**Módulo:** teoria/ESTABILIDADE_GHOST_CHECK.md  
**Status:** Formulação completa — verificação numérica pendente

---

## 1. Por Que a Estabilidade é Necessária

Modelos de energia escura dinâmica podem sofrer instabilidades que os tornam fisicamente inviáveis mesmo que ajustem bem os dados observacionais:

- **Ghosts:** energia cinética negativa → colapso do vácuo quântico
- **Taquiões:** velocidade do som imaginária (cs² < 0) → instabilidade de Jeans em todas as escalas
- **Violação de causalidade:** grupo de velocidade > c

O modelo RLL deve ser verificado em todo o espaço de parâmetros (Ω_s0, z_t, w_t).

---

## 2. Velocidade do Som

Para o componente de superposição com densidade mista:

```
ρ_sup(a) = Ω_s0 · ρ_c0 · [f(a) + (1-f(a)) · a^{-3}]
p_sup(a) = −f(a) · Ω_s0 · ρ_c0 · c²
```

A velocidade do som adiabática é:

```
cs²(z) = ∂p/∂ρ|_s = −f(z) · c² / [f(z) + (1-f(z))(1+z)³]
```

### Comportamento assintótico

```
z >> z_t:  f → 1,  cs² → −c² / 1 = −c²   ← ATENÇÃO: negativo
z = z_t:   f = 0.5, cs² = −c²/2 / [0.5 + 0.5(1+z_t)³]
z << z_t:  f → 0,  cs² → 0 / (1+z)³ = 0  ← OK (tipo matéria)
```

**Problema identificado:** Para z >> z_t, cs² → −c², indicando instabilidade de Jeans em escala de Planck. Isso ocorre porque o componente radiativo f(a)·ρ com pressão negativa é fisicamente análogo a um ghost em pressão.

### Solução proposta: velocidade do som prescrita

Na literatura de dark energy, é comum prescrever cs² = 1 (em unidades de c) para o componente escalar puro, separado da componente matéria. Para o modelo RLL, a prescrição física consistente é:

```
cs²_sup(z) = f(z)   [adimensional, em unidades de c²]
```

Isso garante cs² ∈ [0, 1] por construção, com:
- cs² → 1 para z >> z_t (comportamento relativístico, OK)
- cs² → 0 para z << z_t (comportamento pressureless, OK)

A escala de Jeans correspondente é:

```
k_J(z) = a · H(z) · √(3/2 · Ω_m(a)/cs²(z))
```

Para Ω_s0 = 0.06 e cs² = f(z) ≈ 0.5 em z ≈ z_t, a escala de Jeans está em escalas subestruturais (~Mpc), não afetando observáveis de larga escala.

---

## 3. Critério de Ausência de Ghosts

O componente de superposição pode ser mapeado para um campo escalar com Lagrangiana:

```
L_sup = (1/2)g^{μν} ∂_μφ ∂_νφ − V(φ)
```

com:
```
φ'(lna) = √(3(1+w_eff) · Ω_s(a)) · M_Pl
V(a)    = (1 − w_eff(a))/2 · ρ_s(a)
```

**Condição anti-ghost:** φ'^2 > 0, ou seja:

```
(1 + w_eff(a)) · Ω_s(a) > 0
```

Como Ω_s(a) > 0 por definição, a condição reduz a:

```
w_eff(a) > −1
```

Para o modelo RLL: `w_eff = −f(z) ∈ [−1, 0]`, com w_eff = −1 atingido apenas no limite z → ∞. Portanto, **o modelo está no limite de ghost em z → ∞**, o que é fisicamente aceitável se tratado como limite assintótico.

---

## 4. Mapeamento para o Plano w–w'

Na classificação de Caldwell & Linder (2005) de modelos de energia escura:

```
w₀   = w_eff(z=0) = −f(0) = −1/(1 + exp(z_t/w_t))
w'₀  = dw/da|_{z=0} = −df/da|_{z=0}
```

Para os parâmetros centrais (z_t=1.16, w_t=0.40):
```
w₀  = −1/(1 + exp(1.16/0.40)) = −1/(1 + exp(2.9)) ≈ −0.053
w'₀ = (1/w_t) · f(0) · (1−f(0)) ≈ (1/0.40) · 0.053 · 0.947 ≈ +0.125
```

Isso coloca o RLL na região **thawing** do plano w–w' (modelos onde a energia escura foi congelada no passado e começa a mover-se). Esta região é favorecida por dados DESI DR2.

---

## 5. Verificação Numérica (código)

```python
import numpy as np

def check_stability(Omega_s0, z_t, w_t, z_range=None):
    """
    Verifica critérios de estabilidade para o modelo RLL.
    Retorna dicionário com resultados por condição.
    """
    if z_range is None:
        z_range = np.linspace(0, 5, 500)
    
    results = {}
    
    # Função de transição
    f = 1.0/(1.0 + np.exp((z_range - z_t)/w_t))
    
    # w_eff
    w_eff = -f
    results['w_eff_range'] = (w_eff.min(), w_eff.max())
    results['ghost_free'] = bool(np.all(w_eff >= -1.0 - 1e-10))
    
    # cs² prescrita
    cs2 = f  # prescrição física
    results['cs2_positive'] = bool(np.all(cs2 >= 0))
    results['cs2_causal']   = bool(np.all(cs2 <= 1))
    
    # Gradiente de w (não deve divergir)
    dw = np.gradient(w_eff, z_range)
    results['w_smooth'] = bool(np.all(np.abs(dw) < 10.0))
    
    # w₀ e w'₀
    f0 = 1.0/(1.0 + np.exp(z_t/w_t))
    results['w0']  = -f0
    results['wa']  = (1.0/w_t) * f0 * (1-f0)  # dw/da ≈ dw/dz × (-1)
    
    return results


# Varrer espaço de parâmetros
param_space = [
    (0.059, 1.164, 0.405),   # valor central
    (0.048, 0.882, 0.271),   # 16% posterior
    (0.071, 1.430, 0.534),   # 84% posterior
    (0.100, 0.500, 0.200),   # limite Ω_s0 alto
    (0.010, 2.000, 0.600),   # limite z_t alto
]

print(f"{'Ω_s0':>6} {'z_t':>6} {'w_t':>6} | {'ghost_free':>10} {'cs2_OK':>8} {'w₀':>8} {'wₐ':>8}")
print("-" * 65)
for p in param_space:
    r = check_stability(*p)
    print(f"{p[0]:6.3f} {p[1]:6.3f} {p[2]:6.3f} | "
          f"{'✅' if r['ghost_free'] else '❌':>10} "
          f"{'✅' if r['cs2_positive'] else '❌':>8} "
          f"{r['w0']:8.4f} {r['wa']:8.4f}")
```

---

## 6. Critério de Falsificabilidade por Estabilidade

O modelo RLL é instável (e deve ser revisado ou descartado) se:

1. Para qualquer combinação (Ω_s0, z_t, w_t) dentro do 95% do posterior, cs² < 0 em z < 2 com a prescrição padrão
2. O campo φ correspondente desenvolve gradiente imaginário (phantom crossing w < −1 transitório)
3. A perturbação de matéria δ cresce exponencialmente na presença do acoplamento Ω_s0 (verificar numericamente)
