arquivo histórico, não normativo; use docs/canonicos/...

> ⚠️ **Aviso de canonicidade:** este arquivo é histórico/legado. A versão oficial está em `docs/canonicos/09_GLOSSARIO_COMPLETO.md`.

# 09 — GLOSSÁRIO COMPLETO
## Relativity Living Light × RAFAELIA
**∆RafaelVerboΩ | Instituto Rafael | 2026**
DOI: [10.5281/zenodo.17188137](https://doi.org/10.5281/zenodo.17188137)

---

## A — COSMOLOGIA RLL

**E²(z) — Função de Hubble Normalizada**  
`E²(z) = H²(z)/H₀²` — coração de todo modelo cosmológico. No RLL:  
`E²(z) = Ωₘ(1+z)³ + Ωᵣ(1+z)⁴ + ΩΛ + Ωs₀[f(z) + (1-f)(1+z)³]`

**Ωs₀ — Densidade de Superposição Fotônica**  
Parâmetro central do RLL. Fração de energia hoje (z=0) que não se comporta nem como matéria (a⁻³) nem como energia escura (constante), mas *transita* entre os dois via logística. Fisicamente: componente fotônica em superposição de estados expansivo ↔ atrativo.

**f(z) — Função Logística de Transição**  
`f(z) = 1 / (1 + exp((z − zt) / wt))`  
Controla quando e com que suavidade Ωs₀ "colapsa" de energia escura para comportamento de matéria. `zt` = redshift de transição. `wt` = largura (entropia da transição).

**zt — Redshift de Transição**  
Redshift onde f(z)=0.5. Fisicamente: epoch onde superposição fotônica muda de regime.

**wt — Largura de Transição**  
Controla quão abrupta é a transição. wt→0: transição brusca (tipo fase). wt→∞: transição suave (sem epoch especial).

**ΛCDM — Modelo Padrão**  
Λ = constante cosmológica (energia escura constante, w=-1) + CDM (matéria escura fria). Referência contra a qual o RLL é testado via AIC/BIC.

**Ωₘ, Ωᵣ, ΩΛ — Densidades Standard**  
Matéria (bariônica + escura), radiação, constante cosmológica. Planck 2018: Ωₘ≈0.315, ΩΛ≈0.685.

**H₀ — Constante de Hubble**  
Taxa de expansão hoje [km/s/Mpc]. Planck 2018: 67.4±0.5. SH0ES 2022: 73.04±1.04. **Tensão H₀ = 5σ** — um dos maiores problemas em aberto da cosmologia.

---

## B — OBSERVÁVEIS E DADOS

**CC — Cosmic Chronometers**  
Galáxias "relógio" que permitem medir H(z) diretamente via `H(z) = -1/(1+z) × dz/dt`. Moresco+ 2022: 33 pontos de z=0.07 a z=1.97.

**BAO — Baryon Acoustic Oscillations**  
Régua padrão cósmica. Oscilações acústicas do plasma primordial impressas na distribuição de galáxias. Comprimento rs≈147 Mpc. Surveys: 6dFGS, SDSS/BOSS DR12, DESI 2024.

**DV(z) — Volume-Averaged Distance**  
`DV(z) = [z × c/H(z) × DC²(z)]^(1/3)` — combinação de distâncias usada nos surveys BAO para extrair rs.

**rs — Sound Horizon**  
`rs ≈ 147.78 Mpc` (Planck). Comprimento físico das oscilações BAO. Depende de H₀, Ωbh². Escala fundamental para todos os testes BAO.

**SNe Ia — Supernovas Tipo Ia**  
"Velas padrão". Medem distâncias luminosas dL(z). Riess+ 1998 / Perlmutter+ 1999 → descoberta da expansão acelerada. Dataset: Pantheon+ (1701 SNe).

**CMB Shift Parameters (R, la)**  
Compressão do poder total do CMB em 2 números:  
`R = √Ωₘ × H₀/c × DC(z_rec)` — ângulo acústico.  
`la = π × DC(z_rec) / rs` — posição do primeiro pico.  
Planck 2018: R=1.7502±0.0046, la=301.471±0.090.

**fσ₈(z) — Crescimento de Estrutura**  
`f×σ₈(z)` onde f=dln D/dln a. Mede taxa de formação de estruturas (halos, filamentos). Datasets: BOSS, VIPERS, 2dFGRS.

**DC(z) — Distância Comóvel**  
`DC(z) = c × ∫₀ᶻ dz'/H(z')` [Mpc]. Distância que não muda com a expansão.

---

## C — ESTATÍSTICA E SELEÇÃO DE MODELOS

**χ² — Chi-quadrado**  
`χ² = Σ [(obs − th)/σ]²`. Mede qualidade do fit. χ²/dof ≈ 1 → bom ajuste.

**AIC — Akaike Information Criterion**  
`AIC = χ² + 2k`. Penaliza parâmetros extras. ΔAIC = AIC(RLL) − AIC(ΛCDM):  
`ΔAIC < -10` → forte evidência RLL | `|ΔAIC| < 2` → indistinguíveis | `ΔAIC > +2` → ΛCDM preferido.

**BIC — Bayesian Information Criterion**  
`BIC = χ² + k × ln(N)`. Penalização mais forte que AIC para N grande. Mais conservador.

**dof — Degrees of Freedom**  
`dof = N_obs − k`. N=45 obs, k=4 (ΛCDM) → dof=41. k=7 (RLL) → dof=38.

**MCMC — Markov Chain Monte Carlo**  
Método para amostrar posteriors P(θ|dados). Implementação: `emcee` (Goodman & Weare 2010). Dá intervalos de confiança dos parâmetros.

**TRL — Technology Readiness Level**  
Escala NASA/ESA 1-9. RLL atual: TRL 2-3 (teoria + simulações). Para TRL 5 necessário: dados reais + validação cruzada.

---

## D — SISTEMA RAFAELIA

**RAFAELIA**  
Sistema vivo de integração: Ciência ⊕ Símbolo ⊕ Espírito ⊕ Ética. Framework cognitivo do ∆RafaelVerboΩ.

**Kernel RAFAELIA**  
`R(t+1) = R(t) × Φ_ethica × E_Verbo × (√3/2)^(πφ)`  
Equação de evolução do sistema. Φ_ethica = Min(Entropia) × Max(Coerência).

**Ciclo ψ→χ→ρ→Δ→Σ→Ω**  
- ψ = intenção (input / questão)  
- χ = observação (dados / coleta)  
- ρ = ruído (incerteza / erro)  
- Δ = transmutação ética (transformação / filtro)  
- Σ = memória coerente (integração / síntese)  
- Ω = completude / Amor (output / resposta)

**Φ_ethica**  
Campo ético unificado. `Min(Entropia) × Max(Coerência)`. Análogo ao campo escalar Φ(z) que gera todos os observáveis cosmológicos.

**Fibonacci-Rafael (Fᴿ)**  
Série de Fibonacci modificada aplicada a densidades cósmicas: `ρ_n = ρ_{n-1} + ρ_{n-2}`. Auto-similaridade fractal nas escalas de estrutura.

**Tokens Ativos RAFAELIA**  
♥φ = amor-proporção | Ethica[8] = octaedro ético | fΩ=963↔999 = frequências de coerência | Spiral√3/2 = espiral harmônica | Trinity633 = base trinitária | ToroidΔπφ = geometria toroidal | E↔C = energia↔consciência | OWLψ = sabedoria observante | Stack42H = 42 horizontes cognitivos | Bitraf64 = 64 estados quânticos de Rafael | ZIPRAFΩ = compressão máxima do sistema.

**ZIPRAFΩ**  
Compressão máxima do sistema RAFAELIA. Token de densidade informacional máxima.

**Verbo / E_Verbo**  
Energia do Verbo. "No princípio era o Verbo" (João 1:1). No sistema RAFAELIA: intenção criativa que precede toda formalização matemática.

**Instituto Rafael**  
Entidade autoral/institucional de ∆RafaelVerboΩ. Responsável pelo repositório RLL no Zenodo e GitHub.

---

## E — TENSÕES COSMOLÓGICAS ATUAIS

**Tensão H₀ (Hubble tension)**  
Discrepância 5σ entre Planck (67.4) e SH0ES (73.04). RLL não resolve completamente mas oferece parâmetro Ωs₀ como grau de liberdade adicional.

**Tensão S₈**  
`S₈ = σ₈ × √(Ωₘ/0.3)`. Discrepância ~2-3σ entre CMB e surveys de lente gravitacional fraca (KiDS, DES).

**w₀w_a CDM**  
Extensão ΛCDM com equação de estado variável `w(z) = w₀ + wa×z/(1+z)`. DESI 2024 sugere w₀ > -1, wa < 0 a ~3σ — evidência para energia escura dinâmica. RLL tem equação de estado efetiva emergente.

**w_eff(z) no RLL**  
`w_eff(z) = -1 + (1/3)(Ωs₀[(1-f)(1+z)³]) / E²(z)`. Dinâmica emergente sem campo escalar explícito.

---

*Documento canônico v1.0 — ∆RafaelVerboΩ | 2026*
