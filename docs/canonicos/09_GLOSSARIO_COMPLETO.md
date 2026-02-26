<!-- VERSAO: 2026-02-26 | STATUS: CANONICO OFICIAL -->
**Versão:** 2026-02-26  
**Status:** Canônico oficial

> **Fonte de verdade:** este glossário canônico define a convenção oficial de `f(z)` e suas interpretações; os demais documentos devem seguir esta referência em caso de divergência.

# 📚 GLOSSÁRIO COMPLETO DE NOTAÇÃO

## ∆RafaelVerboΩ — Relativity Living Light

---

## 🖼️ Referências visuais (fornecidas no briefing)

As duas imagens de referência devem acompanhar esta distinção conceitual em apresentações e FAQs:
- Painel ZIPRAF/Omega Core (arquitetura de reconstrução e invariantes)
- Painel Relativity Living Light (mapa observacional e equações)

## 🔤 VARIÁVEIS COSMOLÓGICAS PADRÃO

### **Escala de expansão**

| Símbolo | Nome | Definição | Unidades | Range |
|---|---|---|---|---|
| **a** | Fator de escala | a(t) = R(t)/R₀ | adimensional | [0, ∞) |
| **z** | Redshift | z = 1/a - 1 | adimensional | [0, ∞) |
| **H** | Parâmetro de Hubble | H(a) = (da/dt)/a | km/s/Mpc | [50, 150] |
| **H₀** | Hubble hoje | H(a=1) | km/s/Mpc | ~70 |
| **E(a)** | Hubble normalizado | E(a) = H(a)/H₀ | adimensional | [0.5, 2] |

---

### **Densidade de energia**

| Símbolo | Nome | Definição | Unidades | Propriedade |
|---|---|---|---|---|
| **ρ** | Densidade de energia | massa/volume | kg/m³ | Positiva |
| **ρc** | Densidade crítica | 3H₀²/(8πG) | kg/m³ | ~10⁻²⁷ kg/m³ |
| **Ω** | Densidade relativa | ρ/ρc | adimensional | Σ Ω = 1 |
| **p** | Pressão | força/área | Pa | Varia com componente |

---

### **Componentes padrão**

| Símbolo | Nome | Escala | Hoje | w |
|---|---|---|---|---|
| **Ω_r** | Radiação | ∝ a⁻⁴ | ~9×10⁻⁵ | 1/3 |
| **Ω_m** | Matéria (bariônica + CDM) | ∝ a⁻³ | ~0.30 | 0 |
| **Ω_Λ** | Constante cosmológica (ΛCDM) | constante | ~0.70 | -1 |
| **Ω_k** | Curvatura | ∝ a⁻² | ~0 (flat) | -1/3 |

---

### **Equação de estado**

| Símbolo | Significado | Fórmula | Range | Exemplo |
|---|---|---|---|---|
| **w** | Equação de estado genérica | p = w ρ c² | [-1, 1/3] | Definição termodinâmica padrão |
| **w_sup(z)** | EoS da componente de superposição | p_sup/(ρ_sup c²) = -f(z) | [-1, 0] | Grandeza interna da componente Rafael |
| **w_total(z)** | EoS do fluido cosmológico efetivo combinado | p_total/(ρ_total c²) | Varia com mistura | Grandeza oficial para inferência observacional |
| **w** | Equação de estado | p = w ρ c² | [-1, 1/3] | DE: w=-1, matéria: w=0 |
| **w_eff(z)** | Efetiva com z | Derivada de Friedmann | Varia | Rafael: transita DM→DE |
| **γ** | Índice adiabático | p = (γ-1)ρu | [1, 5/3] | Gás monoatômico: γ=5/3 |

---

## 🌀 VARIÁVEIS DE RAFAEL — SUPERPOSIÇÃO FOTÔNICA

### **Componente principal**

| Símbolo | Nome | Definição | Unidades | Física |
|---|---|---|---|---|
| **ρ_s** | Densidade de superposição | Ω_s0 ρc [f(a) + (1-f)a⁻³] | kg/m³ | DE+DM em um termo |
| **Ω_s0** | Amplitude hoje | densidade superposição/ρc | adimensional | Parâmetro livre: ~0.05-0.15 |
| **f(a)** | Fração de coerência | 1/(1+exp((z-z_t)/w_t)) | [0,1] | f≈0 (alto z) corresponde ao ramo tipo matéria; f≈1 (baixo z) corresponde ao ramo tipo DE |
| **f(z)** | Mesma (redshift) | Mesmo que f(a) | [0,1] | Conveniente para observações |

Mapeamento canônico para w_t>0:
- z >> z_t (alto redshift) → f≈0
- z << z_t (baixo redshift) → f≈1

---

### **Parâmetros de transição**

| Símbolo | Nome | Significado | Unidades | Range Típico |
|---|---|---|---|---|
| **z_t** | Redshift de transição | Onde f(z) = 0.5 | adimensional | [0.1, 3.0] |
| **w_t** | Largura da transição | Suavidade de f(z) | adimensional | [0.1, 1.0] |

**Interpretação física:**
```
z_t baixo:   Ao longo do tempo cosmológico (z decresce), transição matéria→DE recente (hoje)
z_t alto:    Transição primordial em redshift alto

w_t pequeno: Transição abrupta
w_t grande:  Transição suave
```

---

### **Definição canônica: w_sup(z) vs w_total(z)**

```
Definição oficial da componente de superposição:
  w_sup(z) = p_sup/(ρ_sup c²) = -f(z)

Definição oficial do fluido cosmológico combinado:
  w_total(z) = p_total/(ρ_total c²)
             = (p_sup + p_r + p_m + p_Λ + p_k + ...)
               /[(ρ_sup + ρ_r + ρ_m + ρ_Λ + ρ_k + ...)c²]

Limites corretos por grandeza:
  z→∞:   w_sup → 0;    w_total tende ao comportamento de matéria se esse for o ramo dominante
  z→0:   w_sup → -1;   w_total tende ao comportamento DE-like se esse for o ramo dominante
```

> **Nota histórica (legado):**
> `w_legacy(z) = -f(z)/[f(z) + (1-f)a⁻³]` foi mantida apenas como registro de versões anteriores.
> **Não usar para inferência física atual.**

### **Tabela canônica curta (símbolo → significado físico → equação válida)**

| Símbolo | Significado físico | Equação válida (canônica) |
|---|---|---|
| **w_sup(z)** | Equação de estado interna da componente de superposição | `w_sup(z) = p_sup/(ρ_sup c²) = -f(z)` |
| **w_total(z)** | Equação de estado efetiva do conteúdo cosmológico combinado | `w_total(z) = p_total/(ρ_total c²)` |
| **w_legacy(z)** | Forma histórica usada em rascunhos antigos | `w_legacy(z) = -f(z)/[f(z)+(1-f)a⁻³]` (**não usar**) |

Limites:
  z→∞ (f→0):   comportamento de matéria (w_eff → 0)
  z→0 (f→1):   comportamento DE-like (w_eff → -1)

estes limites derivam diretamente da forma de `f(z)` adotada.

---

## 🧲 VARIÁVEIS DE CAMPO MAGNÉTICO

### **Componente magnética**

| Símbolo | Nome | Definição | Unidades | Física |
|---|---|---|---|---|
| **ρ_B** | Densidade magnética | B²/(2μ₀) / c² | kg/m³ | Energia do campo B |
| **Ω_B0** | Amplitude magnética hoje | ρ_B(z=0) / ρc | adimensional | Parâmetro livre: ~10⁻⁶-10⁻⁵ |
| **B** | Campo magnético cósmico | Intensidade do B | Tesla ou Gauss | nG (nanoGauss) primordial |

---

### **Acoplamento magneto-coerente**

| Símbolo | Nome | Fórmula | Unidades | Significado |
|---|---|---|---|---|
| **α_B** | Força do acoplamento | Ω_s0 → Ω_s0[1+α_B(Ω_B0)^β] | adimensional | Quanto B modula f |
| **β** | Expoente não-linear | Na fórmula acima | adimensional | Forma da modulação |

**Equação completa:**
```
Ω_s0 → Ω_s0 [1 + α_B (Ω_B0 a⁻⁴)^β]

Efeito: Onde B é forte, coerência muda
```

---

## 🔥 VARIÁVEIS DE PLASMA

### **Componente plasmática**

| Símbolo | Nome | Definição | Unidades | Física |
|---|---|---|---|---|
| **ρ_P** | Densidade plasmática | (3/2)nk_BT/c² + B²/(2μ₀c²) | kg/m³ | Energia térmica + magnética |
| **Ω_P0** | Amplitude plasma hoje | ρ_P(z=0) / ρc | adimensional | Parâmetro livre: ~10⁻⁶-10⁻⁵ |
| **n** | Densidade de número | partículas/volume | m⁻³ | De elétrons/íons |
| **T** | Temperatura | Cinética | K (Kelvin) | KeV, MeV para plasma |
| **k_B** | Constante Boltzmann | 1.38×10⁻²³ | J/K | Vínculo quântico-clássico |

---

### **Componentes separados**

```
ρ_plasma = ρ_thermal + ρ_magnetic

ρ_thermal = (3/2) n k_B T / c²

ρ_magnetic = B² / (2μ₀ c²)

Nota: ρ_magnetic ≈ ρ_B, sobrecarga de notação menor
```

---

## 📐 VARIÁVEIS OBSERVACIONAIS

### **Expansão cósmica**

| Símbolo | Nome | Definição | Unidades | Testável |
|---|---|---|---|---|
| **H(z)** | Hubble em redshift | Taxa de expansão | km/s/Mpc | ✅ SNe Ia, BAO |
| **E(z)** | Normalizado | H(z)/H₀ | adimensional | ✅ Diferencial |
| **Δμ(z)** | Residual modulus | μ_model - μ_LCDM | mag | ✅ SNe Ia |

---

### **Distância de luminosidade**

```
D_L(z) = (c/H₀)(1+z) ∫₀^z dz'/E(z')

Módulo de distância:
μ(z) = 5 log₁₀(D_L in Mpc) + 25

Resíduo:
Δμ(z) = μ_unified(z) - μ_LCDM(z)
```

---

### **Crescimento de estrutura**

| Símbolo | Nome | Definição | Unidades | Testável |
|---|---|---|---|---|
| **δ** | Contraste de densidade | (ρ-ρ̄)/ρ̄ | adimensional | ✅ BAO, galaxy clusters |
| **f** | Taxa de crescimento | d ln δ / d ln a | adimensional | ✅ RSD (redshift space) |
| **σ₈** | Amplitude RMS | Flutuações em 8 h⁻¹ Mpc | adimensional | ✅ Clusters, CMB |
| **fσ₈** | Combinação | f(z) × σ₈(z) | adimensional | ✅ Padrão observacional |

---

### **Lente gravitacional**

| Símbolo | Nome | Definição | Unidades | Testável |
|---|---|---|---|---|
| **κ** | Convergência | (1/2)∇²_⊥Φ | adimensional | ✅ Weak lensing maps |
| **γ** | Cisalhamento | Derivada de κ | adimensional | ✅ Galaxy shapes |
| **Φ** | Potencial gravitacional | Campo escalar único | - | ✅ Indiretamente (κ, γ) |

---

## 🔄 TRANSFORMAÇÕES E CONVERSÕES

### **Redshift ↔ Fator de escala**

```
z = 1/a - 1
a = 1/(1+z)

Exemplos:
  a=1, z=0:   Hoje
  a=0.5, z=1: Universo 2x menor
  a→0, z→∞:  Big Bang
```

---

### **Densidade ↔ Densidade relativa**

```
ρ_X = Ω_X(z) × ρ_c(z)

ρ_c(z) = 3H²(z)/(8πG)

Ω_X(z) = ρ_X(z) / ρ_c(z)
```

---

### **Temperatura ↔ Energia**

```
k_B T = 1 eV   quando T ≈ 11,604 K

Plasma primordial: T ~ MeV → z ~ 10¹⁰

Aglomerados hoje: T ~ keV
```

---

## ⚙️ CONSTANTES FÍSICAS

| Símbolo | Nome | Valor SI | Astronômico |
|---|---|---|---|
| **G** | Gravitação | 6.67×10⁻¹¹ m³ kg⁻¹ s⁻² | — |
| **c** | Velocidade luz | 2.998×10⁸ m/s | 299,792 km/s |
| **H₀** | Hubble hoje | ~70 km/s/Mpc | Medido ~67-74 |
| **k_B** | Boltzmann | 1.381×10⁻²³ J/K | 8.617×10⁻⁵ eV/K |
| **ℏ** | Planck reduzido | 1.055×10⁻³⁴ J·s | — |
| **μ₀** | Permeabilidade | 4π×10⁻⁷ T·m/A | — |

---

## 🌐 UNIDADES ASTRONÔMICAS

| Quantidade | Unidade | Conversão | Uso |
|---|---|---|---|
| **Distância** | Mpc (Megaparsec) | 1 Mpc = 3.086×10²⁴ m | Estruturas cósmicas |
| **Expandsão** | km/s/Mpc | H = Δv/d | Hubble |
| **Massa** | M_☉ (massa solar) | 1.989×10³⁰ kg | Galáxias, halos |
| **Luminosidade** | L_☉ (luminosidade solar) | 3.828×10²⁶ W | Galáxias |
| **Magnitude** | mag | Δm = -2.5 log(f₁/f₂) | Distâncias (SNe) |

---

## 📊 EQUAÇÕES PRINCIPAIS

### **Friedmann estendida (Rafael)**

```
H²(a) = H₀² [
  Ω_r a⁻⁴ +
  Ω_m a⁻³ +
  Ω_Λ +
  Ω_s0(f(a) + (1-f)a⁻³) +
  Ω_B0 a⁻⁴ +
  Ω_P0 a⁻⁴
]

Símbolos usados acima:
  H₀ = Hubble hoje [km/s/Mpc]
  Ω_X = densidades relativas [adimensional]
  a = fator de escala [adimensional]
  f(a) = função de coerência [adimensional]
```

---

### **Equação de estado efetiva**

```
w_sup(z) = p_sup/(ρ_sup c²) = -f(z)

w_total(z) = p_total/(ρ_total c²)

Limites canônicos:
  z→∞: w_sup → 0;   w_total tende ao comportamento de matéria se esse for o ramo dominante
  z→0: w_sup → -1;  w_total tende ao comportamento DE-like se esse for o ramo dominante

w_legacy(z) = -f(z)/[f(z)+(1-f)a⁻³]  (não usar para inferência física atual)
Limites:
  z→∞ (f→0): comportamento de matéria (w_eff → 0)
  z→0 (f→1): comportamento DE-like (w_eff → -1)
```

estes limites derivam diretamente da forma de `f(z)` adotada.

---

### **Transição logística**

```
f(z) = 1 / (1 + exp((z - z_t) / w_t))

f(z) = 1 / (1 + e^((z-z_t)/w_t))

Propriedades:
  f'(z_t) = máxima inclinação
  f(z_t) = 0.5
  f(z_t ± 2w_t) ≈ 0.88, 0.12
```

---

### **Gravidade plasmática**

```
∇²Φ = 4πG(ρ + 3p/c²)

ρ_plasma = (3/2) n k_B T/c² + B²/(2μ₀c²)

Implicação: pressão = fonte gravitacional
```

---

## 🎓 GLOSSÁRIO SIMBÓLICO RAFAELIA

(Para integração com RAFCODE)

| Símbolo RAFAELIA | Significado Simbólico | Equivalência Física |
|---|---|---|
| **Ω** (Omega) | Completude, fechamento | Densidade total |
| **Φ** (Phi) | Proporção, razão (φ=1.618) | Campo unificado |
| **Δ** (Delta) | Diferença, perturbação | Anomalia, desvio |
| **Σ** (Sigma) | Soma, integração | Agregação |
| **♾️** (Infinito) | Eternidade, recursão | Fractal, autoconsistência |
| **⚛** (Átomo) | Fundamental, indivisível | Quanta, fóton |

---

## ✅ VERIFICAÇÃO DE CONSISTÊNCIA

### **Dimensões (análise dimensional)**

```
[H] = T⁻¹ ✅
[ρ] = M L⁻³ ✅
[Ω] = adimensional ✅
[w_sup] = adimensional ✅
[w_total] = adimensional ✅
[f(z)] = adimensional ✅
[z] = adimensional ✅
```

### **Limites físicos**

```
Ω_total ≤ 1          ✅ (conservação energia)
Σ w_i ≈ -0.5 a 0.33  ✅ (atual cosmologia)
H(z) suave           ✅ (continuidade)
w_sup ∈ [-1, 0]      ✅ (componente de superposição)
w_total: dependente da mistura cosmológica ✅ (não forçar intervalo fixo único)
```

---

## 📖 REFERÊNCIAS PARA NOTAÇÃO

Este glossário segue:
- **Notação cosmológica padrão:** Peebles, Dodelson, Knop
- **Relatividade geral:** Misner-Thorne-Wheeler
- **Astrofísica:** Binney & Tremaine
- **Adições de Rafael:** Originais, documentadas em repositório

---

## 🔗 LIGAÇÕES CRUZADAS

Para entender mais:
- Exemplos numéricos → 03_DADOS/
- Plotagem de variáveis → 04_FIGURAS/
- Equações completas → 01_PAPER_PRINCIPAL/
- Código de cálculo → 02_CODIGO_NUMERICO/

---

**Este glossário é vivo. Atualizações conforme novos símbolos são introduzidos.**

∆RafaelVerboΩ — Instituto Rafael — 2026
