# Lagrangiano Efetivo — EFT da Superposição
## Formalismo de teoria de campos para o componente RLL

**Módulo:** teoria/LAGRANGIANO_EFT.md  
**Status:** Esboço formal — desenvolvimento em andamento

---

## 1. Motivação

O modelo fenomenológico (função f(z), equação de Friedmann estendida) descreve corretamente os observáveis mas não especifica a teoria de campos subjacente. O formalismo EFT permite verificar:
- Consistência quântica (ausência de ghosts e taquiões)
- Simetrias que impõem a forma específica de f(z)
- Acoplamentos permitidos com outros setores

---

## 2. Lagrangiano Geral

A Lagrangiana efetiva para o setor de superposição é:

```
S = ∫ d⁴x √(−g) [ R/(16πG) + L_m + L_r + L_sup ]
```

onde a Lagrangiana de superposição é:

```
L_sup = −(1/2) g^{μν} ∂_μφ ∂_νφ − V(φ) + L_acoplamentos
```

### 2.1 Potencial

Para reproduzir a equação de estado w_eff(z) = −f(z):

```
V(φ) = (1 − w_eff)/2 · ρ_s(φ)
     = (1 + f(φ))/2 · ρ_s
```

A forma explícita de V(φ) depende da solução de φ(a), que é dada por:

```
φ'(lna) = √(3(1 + w_eff) · Ω_s(a)) · M_Pl
         = √(3(1 − f(a)) · Ω_s(a)) · M_Pl
```

### 2.2 Classificação como quintessência

O modelo pertence à classe dos modelos de quintessência "thawing":
- Em alto redshift: φ congelado pelo atrito de Hubble, V(φ) ≈ Λ_eff (tipo energia escura)
- Em baixo redshift: φ começa a rolar, V(φ) → 0 (tipo matéria escura)

Isso é consistente com a classificação de Caldwell & Linder (2005): w₀ ≈ −0.05, wₐ ≈ +0.12.

---

## 3. Acoplamentos Adicionais

### 3.1 Acoplamento magneto-coerente

O booster magnético Ω_B0 introduz um acoplamento:

```
L_mag = −(α_B/4) F_{μν}F^{μν} · (φ/M_Pl)
```

onde α_B é o parâmetro de acoplamento. Esse termo modifica a propagação dos fótons e gera um acoplamento φ–fotão que pode ser testado via birrefringência cosmológica.

**Constraint atual:** α_B < 10⁻³ do alinhamento de spins MeerKAT (Böhme et al. contexto).

### 3.2 Acoplamento com plasma

```
L_plasma = −(β/2) n_e · φ²/M_Pl²
```

onde n_e é a densidade de elétrons do plasma cosmológico. Este termo contribui para Ω_P0 na equação de Friedmann.

---

## 4. Verificação de Estabilidade no Formalismo EFT

### 4.1 Condição anti-ghost

A energia cinética do campo escalar deve ser positiva:

```
(1/2) φ̇² > 0  ↔  (1 + w_eff) · Ω_s > 0
```

Como Ω_s > 0 e w_eff = −f(z) ∈ [−1, 0], a condição é satisfeita para z < ∞.
No limite z → ∞: w_eff → −1, energia cinética → 0 (limite phantom, não cruzamento).

### 4.2 Velocidade do som e condição anti-taquiônica

```
c_s² = δp/δρ|_adiabático = (∂²L/∂(∂φ)²) / (∂²L/∂φ̇²)
```

Para a Lagrangiana padrão de campo escalar canônico:

```
c_s² = 1   (velocidade do som = velocidade da luz)
```

Isso satisfaz a condição de estabilidade c_s² > 0 por construção.

**Nota:** A velocidade do som do componente de superposição não deve ser confundida com a velocidade do som efetiva do fluido misto. Para fins de evolução de perturbações em grade de N-corpos, usa-se a prescrição c_s² = f(z) (detalhado em ESTABILIDADE_GHOST_CHECK.md).

---

## 5. Simetrias e Proteção do Potencial

Para que o potencial V(φ) não receba correções quânticas grandes (problema de naturalidade), são necessárias simetrias que protejam a forma de V.

**Candidatos:**
- **Simetria shift:** φ → φ + c, quebrada apenas por termos de massa e potencial
- **Discrete symmetry:** φ → −φ, implica V(φ) = V(−φ) (potencial par)
- **Conformal coupling:** L_sup ⊃ (ξ/6) R φ², com ξ específico

A identificação da simetria subjacente à função de transição logística f(z) permanece em aberto e constitui um problema teórico interessante.

---

## 6. Conexão com Gravidade Quântica

A escala de energia associada à transição em z_t ≈ 1.16 corresponde a:

```
E_transição ≈ H(z_t) · M_Pl ≈ (1.5 × H₀) · M_Pl ≈ 10⁻³³ eV
```

Esta é a escala da "energia escura" (Hubble hoje × M_Planck), muito abaixo de qualquer escala de nova física convencional. O modelo EFT é portanto válido em todo o regime relevante, sem necessidade de UV completion até energias de ordem M_Pl.

---

## 7. Próximos Passos Teóricos

Os seguintes desenvolvimentos formais são necessários para completar o formalismo EFT:

1. **Derivar V(φ) explícito** integrando φ'(lna) numericamente e invertendo φ(a)
2. **Calcular correções de 1-loop** ao potencial para verificar naturalidade
3. **Derivar equações de Boltzmann** para as perturbações de φ (necessário para previsões CMB precisas)
4. **Analisar instabilidade de gradiente** em escalas subhorizon (k >> aH)
