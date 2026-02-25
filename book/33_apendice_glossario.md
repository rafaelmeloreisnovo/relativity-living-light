<a id="topo"></a>
# 33. Apêndice — Glossário Consolidado

Versão: 1.0  
Status: vigente  
Atualizado em: 2026-02-25

[⬅️ Capítulo anterior](./32_roadmap_medio_longo_prazo.md) | [📚 Sumário do livro](./README.md) | [Capítulo próximo ➡️](./34_apendice_faq.md)

**Versão editorial:** 2026-02-25
**Status:** Consolidado e profissionalizado (evolução estrutural 33x)
**Atualizado em:** 2026-02-25
**Fonte canônica primária:** `docs/canonicos/09_GLOSSARIO_COMPLETO.md`

Ponto único para termos técnicos, siglas, variáveis e nomenclaturas do modelo **Relativity Living Light** com leitura rápida e rastreável.

## Navegação interna

- [1) Variáveis cosmológicas padrão](#1-variáveis-cosmológicas-padrão)
- [2) Superposição fotônica (setor unificado)](#2-superposição-fotônica-setor-unificado)
- [3) Setor magnético](#3-setor-magnético)
- [4) Setor plasmático](#4-setor-plasmático)
- [5) Observáveis e validação](#5-observáveis-e-validação)
- [6) Conversões e fórmulas úteis](#6-conversões-e-fórmulas-úteis)
- [7) Notas de governança do glossário](#7-notas-de-governança-do-glossário)

---

## 1) Variáveis cosmológicas padrão

| Símbolo | Nome | Definição | Unidade | Faixa/Observação |
|---|---|---|---|---|
| **a** | Fator de escala | a(t)=R(t)/R₀ | adimensional | [0,∞) |
| **z** | Redshift | z=1/a−1 | adimensional | [0,∞) |
| **H** | Parâmetro de Hubble | H(a)=ȧ/a | km/s/Mpc | depende do ajuste |
| **H₀** | Hubble atual | H(a=1) | km/s/Mpc | ~70 (ordem de grandeza) |
| **E(a)** | Hubble normalizado | E(a)=H(a)/H₀ | adimensional | leitura comparativa |
| **ρ** | Densidade de energia | massa/volume | kg/m³ | positiva por componente |
| **ρc** | Densidade crítica | 3H₀²/(8πG) | kg/m³ | ~10⁻²⁷ kg/m³ |
| **Ω** | Densidade relativa | Ω=ρ/ρc | adimensional | ΣΩ≈1 (modelo flat) |
| **p** | Pressão | força/área | Pa | varia por componente |
| **w** | Equação de estado | p=wρc² | adimensional | matéria: 0, DE: −1 |

[⬆ Voltar ao topo](#33-apêndice--glossário-consolidado)

---

## 2) Superposição fotônica (setor unificado)

| Símbolo | Nome | Definição | Unidade | Faixa/Observação |
|---|---|---|---|---|
| **ρ_s** | Densidade de superposição | Ω_s0ρc[f(a)+(1−f)a⁻³] | kg/m³ | termo unificado DE↔DM |
| **Ω_s0** | Amplitude atual da superposição | ρ_s(z=0)/ρc | adimensional | parâmetro livre |
| **f(a), f(z)** | Fração de coerência | 1/(1+exp((z−z_t)/w_t)) | adimensional | varia entre 0 e 1 |
| **z_t** | Redshift de transição | ponto onde f(z)=0.5 | adimensional | controla época da transição |
| **w_t** | Largura da transição | suavidade logística | adimensional | menor = transição mais abrupta |
| **w_eff(z)** | EoS efetiva do setor | −f(z)/[f(z)+(1−f)a⁻³] | adimensional | interpola entre −1 e 0 |

**Leitura prática (rápida):**
- **z_t** baixo → transição tardia (mais próxima do Universo atual).
- **z_t** alto → transição mais primordial.
- **w_t** pequeno → troca mais brusca; **w_t** grande → troca mais suave.

[⬆ Voltar ao topo](#33-apêndice--glossário-consolidado)

---

## 3) Setor magnético

| Símbolo | Nome | Definição | Unidade | Faixa/Observação |
|---|---|---|---|---|
| **ρ_B** | Densidade magnética | B²/(2μ₀c²) | kg/m³ | energia do campo B |
| **Ω_B0** | Fração magnética atual | ρ_B(z=0)/ρc | adimensional | tipicamente pequena |
| **B** | Campo magnético cósmico | intensidade de campo | Tesla/Gauss | usado em escalas cosmológicas |
| **α_B** | Força de acoplamento | modulação em Ω_s0 | adimensional | calibra impacto magnético |
| **β** | Expoente de acoplamento | potência não linear | adimensional | controla curvatura da modulação |

**Forma de acoplamento usada no acervo:**

```text
Ω_s0 → Ω_s0 [1 + α_B (Ω_B0 a⁻⁴)^β]
```

[⬆ Voltar ao topo](#33-apêndice--glossário-consolidado)

---

## 4) Setor plasmático

| Símbolo | Nome | Definição | Unidade | Faixa/Observação |
|---|---|---|---|---|
| **ρ_P** | Densidade plasmática | (3/2)nk_BT/c² + B²/(2μ₀c²) | kg/m³ | parte térmica + magnética |
| **Ω_P0** | Fração plasmática atual | ρ_P(z=0)/ρc | adimensional | parâmetro de contribuição |
| **n** | Densidade numérica | partículas/volume | m⁻³ | elétrons/íons |
| **T** | Temperatura | energia cinética média | K | pode ser expressa em keV/MeV |
| **k_B** | Constante de Boltzmann | 1.38×10⁻²³ | J/K | vínculo termo-estatístico |

[⬆ Voltar ao topo](#33-apêndice--glossário-consolidado)

---

## 5) Observáveis e validação

| Símbolo | Nome | Definição | Unidade | Uso observacional |
|---|---|---|---|---|
| **H(z)** | Expansão em redshift | taxa de expansão | km/s/Mpc | BAO, cosmic chronometers |
| **E(z)** | Hubble normalizado | H(z)/H₀ | adimensional | comparação direta entre modelos |
| **μ(z)** | Módulo de distância | função de D_L | mag | SNe Ia |
| **Δμ(z)** | Residual de distância | μ_model−μ_LCDM | mag | diagnóstico de desvio |
| **δ** | Contraste de densidade | (ρ−ρ̄)/ρ̄ | adimensional | estrutura em larga escala |
| **f** | Taxa de crescimento | dlnδ/dlna | adimensional | RSD |
| **σ₈** | Amplitude RMS (8 h⁻¹Mpc) | flutuação linear | adimensional | CMB + LSS |
| **fσ₈** | Observável combinado | f×σ₈ | adimensional | padrão para crescimento |
| **κ** | Convergência de lente | (1/2)∇²⊥Φ | adimensional | weak lensing |
| **γ** | Cisalhamento | derivada angular de κ | adimensional | distorção de forma |
| **Φ** | Potencial gravitacional | potencial escalar efetivo | — | inferido indiretamente |

[⬆ Voltar ao topo](#33-apêndice--glossário-consolidado)

---

## 6) Conversões e fórmulas úteis

### Redshift ↔ fator de escala

```text
z = 1/a − 1
a = 1/(1+z)
```

### Distância de luminosidade e residual

```text
D_L(z) = (c/H₀)(1+z) ∫₀^z dz'/E(z')
μ(z) = 5 log₁₀(D_L em Mpc) + 25
Δμ(z) = μ_unified(z) − μ_LCDM(z)
```

### Regra de leitura rápida de limites

```text
z → ∞  : dinâmica em regime primordial
z → 0  : dinâmica no regime tardio
f → 1  : comportamento tipo DE
f → 0  : comportamento tipo matéria
```

[⬆ Voltar ao topo](#33-apêndice--glossário-consolidado)

---

## 7) Notas de governança do glossário

- Este capítulo é o **nó editorial consolidado** para consulta no livro canônico.
- Em caso de divergência textual, prevalece a fonte: `docs/canonicos/09_GLOSSARIO_COMPLETO.md`.
- Fontes legadas relacionadas:
  - `09_GLOSSARIO_COMPLETO.md`
  - `09_GLOSSARIO_COMPLETO-1.md`
  - `RMR/09_GLOSSARIO_COMPLETO.md`
- Ao incluir novos termos no repositório, atualizar este capítulo e a fonte canônica para manter rastreabilidade.
Referência editorial única para símbolos, definições e convenções usadas no livro.

## Fontes canônicas usadas
- `docs/canonicos/09_GLOSSARIO_COMPLETO.md`
- `09_GLOSSARIO_COMPLETO.md` (legado)

Regra de precedência textual: em conflito, prevalece `docs/canonicos/09_GLOSSARIO_COMPLETO.md`.

## Navegação interna
- [Conteúdo incorporado (itens soltos/localizados)](#sec-conteudo-incorporado)
- [Parâmetros de expansão e transição](#sec-parametros-expansao)
- [Densidades cosmológicas normalizadas](#sec-densidades)
- [Observáveis de estrutura em larga escala](#sec-estrutura)
- [Indicadores observacionais e calibração](#sec-indicadores)
- [Notas de consolidação](#sec-notas)

<a id="sec-conteudo-incorporado"></a>
## Conteúdo incorporado (itens soltos/localizados)
Documentos e artefatos relacionados incorporados nesta etapa:
## Índice rápido
- [Cosmologia padrão](#cosmologia-padrão)
- [Superposição](#superposição)
- [Magnetismo](#magnetismo)
- [Plasma](#plasma)
- [Observáveis](#observáveis)
- [Conversões](#conversões)

## Cosmologia padrão

| Símbolo | Nome | Definição | Unidade | Faixa/Observação |
|---|---|---|---|---|
| **a** | Fator de escala | Razão entre escala em *t* e a escala atual: \(a(t)=R(t)/R_0\) | adimensional | \(a=1\) hoje; \(a \to 0\) no passado remoto |
| **z** | Redshift | \(z=1/a-1\) | adimensional | \(z=0\) hoje; \(z>0\) para o passado |
| **H(z)** | Parâmetro de Hubble | Taxa de expansão em função de *z* | km/s/Mpc | Em ΛCDM, tipicamente cresce com *z* |
| **H₀** | Hubble atual | Valor de \(H(z)\) em \(z=0\) | km/s/Mpc | Faixa observacional ~67–74 |
| **Ω_m** | Fração de matéria | Densidade de matéria relativa à crítica | adimensional | Ordem de grandeza atual ~0,3 |
| **Ω_Λ** | Fração de energia escura | Componente de vácuo em ΛCDM | adimensional | Ordem de grandeza atual ~0,7 |
| **w** | Equação de estado | Relação pressão-densidade: \(p=w\rho c^2\) | adimensional | Matéria: 0; radiação: 1/3; Λ: -1 |

## Superposição

| Símbolo | Nome | Definição | Unidade | Faixa/Observação |
|---|---|---|---|---|
| **Ω_s0** | Amplitude de superposição hoje | Fração atual da componente de superposição | adimensional | Parâmetro livre do modelo |
| **f(a)** | Fração de coerência (em *a*) | Fração logística de estado coerente da componente | adimensional | Varia entre 0 e 1 |
| **f(z)** | Fração de coerência (em *z*) | \(f(z)=\frac{1}{1+\exp((z-z_t)/w_t)}\) | adimensional | Controlada por \(z_t\) e \(w_t\) |
| **z_t** | Redshift de transição | Redshift no qual \(f(z_t)=0{,}5\) | adimensional | Define a época central da transição |
| **w_t** | Largura da transição | Escala de suavização da logística de \(f(z)\) | adimensional | Menor valor ⇒ transição mais abrupta |
| **w_eff(z)** | EoS efetiva da superposição | \(w_{eff}(z)=-\frac{f(z)}{f(z)+(1-f)a^{-3}}\) | adimensional | Interpola entre comportamento tipo DE e DM |

### Exemplo de uso — `f(z)`
> Em ajuste de dados de expansão, `f(z)` controla **quando** e **quão suave** é a transição entre regimes efetivos no termo de superposição. Um cenário com `z_t` maior desloca a transição para épocas mais antigas.

### Exemplo de uso — `w_eff`
> Ao comparar modelos no diagrama `w(z)`, `w_eff` resume a dinâmica da componente unificada: próximo de `-1` em regime tipo energia escura e próximo de `0` em regime tipo matéria.

## Magnetismo

| Símbolo | Nome | Definição | Unidade | Faixa/Observação |
|---|---|---|---|---|
| **B** | Campo magnético cósmico | Intensidade do campo magnético médio efetivo | T (ou G) | Escalas cosmológicas costumam ser tratadas em nG |
| **ρ_B** | Densidade magnética | \(\rho_B = B^2/(2\mu_0 c^2)\) | kg/m³ | Contribuição energética associada ao campo |
| **Ω_B0** | Fração magnética hoje | \(\rho_B(z=0)/\rho_c\) | adimensional | Tipicamente pequena em relação a Ω_m |
| **α_B** | Acoplamento magneto-coerente | Coeficiente de modulação magnética da superposição | adimensional | Parâmetro fenomenológico |
| **β** | Expoente de não linearidade | Expoente do termo de modulação magnética | adimensional | Ajusta curvatura da resposta |

## Plasma

| Símbolo | Nome | Definição | Unidade | Faixa/Observação |
|---|---|---|---|---|
| **ρ_P** | Densidade plasmática | Soma de contribuição térmica e magnética do plasma | kg/m³ | \(\rho_P\sim\frac{3}{2}nk_BT/c^2 + B^2/(2\mu_0c^2)\) |
| **Ω_P0** | Fração plasmática hoje | \(\rho_P(z=0)/\rho_c\) | adimensional | Parâmetro adicional do modelo |
| **n** | Densidade numérica | Número de partículas por volume | m⁻³ | Depende do meio (intergaláctico, intracluster etc.) |
| **T** | Temperatura do plasma | Escala térmica média das partículas | K | Frequentemente expressa também em eV/keV/MeV |
| **k_B** | Constante de Boltzmann | Conversão entre energia e temperatura | J/K | Valor SI: \(1{,}380649\times10^{-23}\) |

## Observáveis

| Símbolo | Nome | Definição | Unidade | Faixa/Observação |
|---|---|---|---|---|
| **E(z)** | Hubble normalizado | \(E(z)=H(z)/H_0\) | adimensional | Facilita comparação entre modelos |
| **D_L(z)** | Distância de luminosidade | Distância inferida via fluxo-luminosidade | Mpc | Base para análise de supernovas |
| **μ(z)** | Módulo de distância | \(\mu = 5\log_{10}(D_L/\mathrm{Mpc})+25\) | mag | Observável direto em SNe Ia |
| **Δμ(z)** | Resíduo de distância | \(\Delta\mu=\mu_{modelo}-\mu_{\Lambda CDM}\) | mag | Quantifica desvio em relação ao modelo de referência |
| **f** | Taxa de crescimento | \(f=d\ln\delta/d\ln a\) | adimensional | Mede crescimento de estrutura |
| **σ₈** | Amplitude de flutuação | RMS em 8 \(h^{-1}\) Mpc | adimensional | Normalização de estrutura em larga escala |
| **fσ₈** | Observável de crescimento | Produto \(f(z)\sigma_8(z)\) | adimensional | Principal alvo de medidas RSD |

### Exemplo de uso — `fσ8`
> Em comparação com dados de redshift-space distortions, curvas de `fσ8(z)` permitem distinguir cenários com mesma expansão de fundo (`H(z)`) mas crescimento estrutural diferente.

### Exemplo de uso — `Δμ`
> Em análises de supernovas, `Δμ(z)` é usado para visualizar sistematicamente onde o modelo fica acima/abaixo de ΛCDM ao longo do redshift.

## Conversões

| Símbolo | Nome | Definição | Unidade | Faixa/Observação |
|---|---|---|---|---|
| **z \leftrightarrow a** | Redshift ↔ fator de escala | \(z=1/a-1\), \(a=1/(1+z)\) | adimensional | Conversão fundamental para todas as equações de evolução |
| **ρ_c(z)** | Densidade crítica | \(\rho_c(z)=3H^2(z)/(8\pi G)\) | kg/m³ | Referência para definir todos os Ω |
| **ρ_X \leftrightarrow Ω_X** | Densidade física ↔ relativa | \(\rho_X=\Omega_X\rho_c\), \(\Omega_X=\rho_X/\rho_c\) | kg/m³ e adimensional | Relação usada em tabelas e códigos |
| **k_B T** | Temperatura ↔ energia | Conversão térmica (eV, keV, MeV) | J ou eV | Regra útil: 1 eV ≈ 11.604 K |

---

Nota editorial: este capítulo consolida a notação para consulta rápida e pode ser atualizado quando novos símbolos entrarem no corpo principal do livro.
> ⚠️ **Canonicidade:** fonte primária deste capítulo: `docs/canonicos/09_GLOSSARIO_COMPLETO.md`.

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
| **w** | Equação de estado | p = w ρ c² | [-1, 1/3] | DE: w=-1, matéria: w=0 |
| **w_eff(z)** | Efetiva com z | Derivada de Friedmann | Varia | Rafael: transita DE→DM |
| **γ** | Índice adiabático | p = (γ-1)ρu | [1, 5/3] | Gás monoatômico: γ=5/3 |

---

## 🌀 VARIÁVEIS DE RAFAEL — SUPERPOSIÇÃO FOTÔNICA

### **Componente principal**

| Símbolo | Nome | Definição | Unidades | Física |
|---|---|---|---|---|
| **ρ_s** | Densidade de superposição | Ω_s0 ρc [f(a) + (1-f)a⁻³] | kg/m³ | DE+DM em um termo |
| **Ω_s0** | Amplitude hoje | densidade superposição/ρc | adimensional | Parâmetro livre: ~0.05-0.15 |
| **f(a)** | Fração de coerência | 1/(1+exp((z-z_t)/w_t)) | [0,1] | 1→DE, 0→DM |
| **f(z)** | Mesma (redshift) | Mesmo que f(a) | [0,1] | Conveniente para observações |

---

### **Parâmetros de transição**

| Símbolo | Nome | Significado | Unidades | Range Típico |
|---|---|---|---|---|
| **z_t** | Redshift de transição | Onde f(z) = 0.5 | adimensional | [0.1, 3.0] |
| **w_t** | Largura da transição | Suavidade de f(z) | adimensional | [0.1, 1.0] |

**Interpretação física:**
```
z_t baixo:   Transição DE→DM recente (hoje)
z_t alto:    Transição primordial

w_t pequeno: Transição abrupta
w_t grande:  Transição suave
```

---

### **Equação de estado derivada**

```
w_eff(z) = -f(z) / [f(z) + (1-f)a⁻³]

Limites:
  z→∞ (f→1):   w_eff → -1  (DE-like)
  z→0 (f→0):   w_eff → 0   (DM-like)
```

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

[⬆️ voltar ao topo](#topo)

<a id="sec-parametros-expansao"></a>
## Parâmetros de expansão e transição
<a id="w_eff"></a>
- **`w_eff`**: parâmetro de estado efetivo (equação de estado efetiva do conteúdo cosmológico).

<a id="z_t"></a>
- **`z_t`**: redshift de transição entre regimes de desaceleração e aceleração da expansão.

[⬆️ voltar ao topo](#topo)

<a id="sec-densidades"></a>
## Densidades cosmológicas normalizadas
<a id="Ω_s0"></a>
- **`Ω_s0`**: densidade normalizada do setor escalar (ou componente `s`) no tempo presente.

<a id="Ω_B0"></a>
- **`Ω_B0`**: densidade bariônica normalizada no tempo presente.

<a id="Ω_P0"></a>
- **`Ω_P0`**: densidade normalizada da componente `P` no tempo presente.

[⬆️ voltar ao topo](#topo)

<a id="sec-estrutura"></a>
## Observáveis de estrutura em larga escala
<a id="fσ8"></a>
- **`fσ8`**: produto da taxa de crescimento linear `f` pela amplitude de flutuações `σ8`.

[⬆️ voltar ao topo](#topo)

<a id="sec-indicadores"></a>
## Indicadores observacionais e calibração
<a id="Δμ"></a>
- **`Δμ`**: variação no módulo de distância (resíduo observacional em relação a um modelo de referência).

[⬆️ voltar ao topo](#topo)

<a id="sec-notas"></a>
## Notas de consolidação
- Este capítulo funciona como nó canônico para evitar dispersão de arquivos soltos.
- Atualize este capítulo quando novos materiais da mesma temática forem adicionados ao repositório.
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

[⬆️ voltar ao topo](#topo)

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
w_eff(z) = -f(z) / [f(z) + (1-f)a⁻³]

w_eff(z) = p_eff / ρ_eff c²

Limites:
  z→∞: w_eff → -1
  z→0: w_eff → 0
```

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
[w_eff] = adimensional ✅
[f(z)] = adimensional ✅
[z] = adimensional ✅
```

### **Limites físicos**

```
Ω_total ≤ 1          ✅ (conservação energia)
Σ w_i ≈ -0.5 a 0.33  ✅ (atual cosmologia)
H(z) suave           ✅ (continuidade)
w_eff ∈ [-1, 1/3]    ✅ (limites teóricos)
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

## Manutenção

Quando surgirem novos termos/símbolos:
1. Atualize primeiro `docs/canonicos/09_GLOSSARIO_COMPLETO.md`.
2. Reincorpore os blocos canônicos neste capítulo 33.
3. Revise rapidamente consistência de notação literal (Ω, Δ, Σ, κ, γ, etc.) antes do commit.
