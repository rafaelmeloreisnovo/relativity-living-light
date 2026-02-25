# 33. Apêndice — Glossário Consolidado

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

---
