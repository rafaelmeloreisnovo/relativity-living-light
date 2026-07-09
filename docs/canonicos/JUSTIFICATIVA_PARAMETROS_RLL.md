# Justificativa e Rastreabilidade dos Parâmetros RLL

**Data**: 2026-07-07 | **Fase**: FASE 12  
**Status epistêmico**: [E] parâmetros documentados · [C] convenções identificadas · [VAZIO] motivações sem âncora  
**Marcação**: [E] Estabelecido · [C] Convenção · [H] Hipótese · [VAZIO] sem âncora empírica

> **Objetivo**: Para cada parâmetro do modelo RLL, documentar sua origem (paper, convenção, ajuste), 
> motivação física (se existe), e o TOKEN_VAZIO correspondente (se a origem é desconhecida).
> Nenhum parâmetro deve ficar "flutuante" sem marca epistêmica.

---

## 1. Parâmetros Cosmológicos Base [E — todos de Planck 2018]

Estes parâmetros têm origem direta em publicações revisadas por pares:

| Parâmetro | Valor | Fonte | Referência |
|-----------|-------|-------|-----------|
| H₀ | 67.4 km/s/Mpc | Planck 2018 TT,TE,EE+lowE+lensing | Planck Collaboration (2020), arXiv:1807.06209 |
| Ωm | 0.315 | Planck 2018 | idem |
| Ωb | 0.049 | Planck 2018 | idem |
| Ωr | ≈ 9.0×10⁻⁵ | Derivado de T_CMB = 2.7255 K | Fixsen (2009), arXiv:0911.1955 |
| ΩΛ | 1 − Ωm − Ωr − Ωs0 | Derivado (planura espacial) | Planck 2018 + convenção flat ΛCDM |
| σ₈ | 0.811 | Planck 2018 | idem |

**Status epistêmico**: [E] — todos os valores base têm âncora em paper revisado por pares.

**Nota**: O valor Ωr é *derivado* de T_CMB e não diretamente medido como parâmetro livre.
Fórmula: `Ωr = (4σ_SB/c³) · T_CMB⁴ / (3H₀²/(8πG))`, onde σ_SB é a constante de Stefan-Boltzmann.

---

## 2. Parâmetros do Setor RLL [C/VAZIO — TOKEN_VAZIO P1]

Estes parâmetros são ESPECÍFICOS do modelo RLL e não têm derivação de primeiros princípios documentada:

### 2.1 z_t — Redshift de Transição [C → TOKEN_VAZIO P1]

**Valor nominal**: z_t = 1.0  
**Definição**: Redshift central da transição logística f(z) = 1/(1+exp((z−z_t)/w_t))  
**Interpretação física**: Redshift em que f(z_t) = 0.5 — ponto médio da transição de fase do setor.

**Motivação tentativa [H]**: z_t ≈ 1.0 corresponde a:
- Redshift de transição DE→matéria dominada da FUNÇÃO f? Não, essa transição é em z~0.3.
- Epoch de formação de estruturas? Pico de star formation rate em z~1–3 (Hopkins & Beacom 2006, arXiv:astro-ph/0601463) — z_t=1.0 está na borda inferior.
- Epoch de aceleração cósmica? A aceleração começa em z≈0.6 (Riess et al. 1998) — z_t=1.0 está acima.
- Coincidência com BAO scale? z_t=1.0 é um dos redshifts-alvo dos surveys modernos — mas isso é observacional, não físico.

**Conclusão**: z_t = 1.0 é um ajuste fenomenológico. Nenhuma das motivações tentativas é suficientemente específica para classificar como [E] ou [H] fundamentado.

**STATUS**: **[C] Convenção de ajuste** — TOKEN_VAZIO P1  
**Para resolver**: MCMC joint (Gap G1) com z_t como parâmetro livre. Melhor ajuste z_t restringirá o valor e pode sugerir motivação física.

---

### 2.2 w_t — Largura de Transição [C → TOKEN_VAZIO P1]

**Valor nominal**: w_t = 0.3  
**Definição**: Controla a suavidade da transição logística. Transição ocorre em z ∈ (z_t−3w_t, z_t+3w_t) = (0.1, 1.9) para valores nominais.

**Motivação tentativa [H]**:
- w_t ~ largura típica de redshift surveys (Δz ~ 0.2–0.5)? Possível convenção numérica.
- w_t relacionado à escala de coerência de horizonte? Não documentado.
- w_t ~ 1/H(z_t) em unidades naturais? Requer cálculo.

**ANÁLISE**: Para z_t=1.0, H(z=1) ≈ H₀·E(1) ≈ 67.4·√(Ωm·8+ΩΛ) ≈ 67.4·√(0.315·8+0.685) ≈ 67.4·√3.205 ≈ 120 km/s/Mpc. A largura de Hubble em z=1 é c/H(1)~2500 Mpc — sem relação direta com w_t em unidades de redshift.

**Conclusão**: w_t = 0.3 é ajuste sem motivação de primeiros princípios documentada.

**STATUS**: **[C] Convenção de ajuste** — TOKEN_VAZIO P1  
**Para resolver**: MCMC joint (G1) com w_t livre. Ou: comparação com largura de transição de modelos EDE (Early Dark Energy) na literatura.

---

### 2.3 Ωs0 — Amplitude do Setor [C → TOKEN_VAZIO P1]

**Valor nominal**: Ωs0 ≈ 0.02–0.05 (range usado em scripts)  
**Definição**: Fração da densidade crítica hoje atribuída ao setor RLL: Ωs0 = ρ_setor(z=0)/ρ_crit.

**Motivação tentativa [H]**:
- Ωs0 pequeno para ser perturbação sub-dominante sobre ΛCDM — estratégia conservadora.
- Ωs0 ~ 2–5% pode ser parcela não atribuída a ΩΛ ou Ωm em ajustes de dados.
- DESI DR2 reporta tensão de ~3.5σ em w0waCDM vs ΛCDM — parte dessa tensão poderia ser absorvida por Ωs0 não nulo.

**ANÁLISE QUANTITATIVA**:
O setor RLL com Ωs0=0.05 modifica E(z) em:
`ΔE²/E²_ΛCDM = Ωs0·(ρ_setor−1)/E²_ΛCDM`

Em z=0: contribuição = Ωs0·0/E²_ΛCDM = 0 (por construção).
Em z=1: contribuição ≈ Ωs0·(1/f(1)+...) — requer cálculo completo.

**Conclusão**: Ωs0 não tem derivação de primeiros princípios. Valor 0.02–0.05 é heurístico.

**STATUS**: **[C] Convenção heurística** — TOKEN_VAZIO P1  
**Para resolver**: MCMC joint (G1) determinará Ωs0 observacionalmente.

---

## 3. Parâmetros Derivados [E — determinados pelos básicos]

| Parâmetro derivado | Fórmula | Dependência |
|-------------------|---------|-------------|
| ΩΛ | 1 − Ωm − Ωr − Ωs0 | ΩΛ = f(Ωm, Ωr, Ωs0) |
| f(z) | 1/(1+exp((z−z_t)/w_t)) | z_t, w_t |
| ρ_setor(z) | Ωs0·[f(z)+(1−f(z))·(1+z)³] | Ωs0, z_t, w_t |
| E²(a) | Ωr·a⁻⁴+Ωm·a⁻³+ΩΛ+Ωs0·ρ_setor | todos acima |
| w_eff(z) | −1−(dln ρ_setor/dln a)/3 | z_t, w_t |

---

## 4. Comparação com Modelos da Literatura [H]

### 4.1 Modelos de Transição Logística Similares

A função `f(z) = 1/(1+exp((z−z_t)/w_t))` aparece em vários contextos:

- **Transições abruptas de w(z)**: Bassett et al. (2002), astro-ph/0108064 — discutem kink em w(z) mas sem função logística explícita.
- **Parametrizações de transição**: Linder (2003), astro-ph/0210603 (CPL) — usa parametrização linear, não logística.
- **Early Dark Energy (EDE)**: Poulin et al. (2018), arXiv:1806.10608 — usa campo escalar com transição em z~3500 (CMB), muito diferente de z_t~1.
- **Bouncing cosmologies**: setor logístico não é padrão.

**STATUS** [H]: O setor RLL com f(z) logístico parece ser formulação original (ou sem citação direta conhecida). Sem evidência de cópia ou inspiração direta documentada.

### 4.2 Distinção Técnica vs CPL

CPL usa: `w(a) = w0 + wa·(1−a)` — parametrização linear em a.  
RLL usa: `f(z) = 1/(1+exp((z−z_t)/w_t))` — transição logística em z.

**Diferença técnica**: CPL é uma EOS evoluindo suavemente. RLL tem setor que interpola entre dois regimes físicos diferentes (DE e matéria). São arquiteturas formalmente distintas, não equivalentes por reparametrização.

**STATUS** [E]: Distinção técnica confirmada pela análise numérica de FASE 10 — trajetórias w_eff estruturalmente opostas em z>0.5.

---

## 5. Proposta de Motivação Física para z_t [H — TOKEN_VAZIO P1]

Uma motivação candidata: z_t é o redshift em que a densidade de energia escura e a densidade de matéria do *setor* se igualam internamente:

`ρ_DE_setor(z_t) = ρ_matéria_setor(z_t)`
`f(z_t)·1 = (1−f(z_t))·(1+z_t)³`

Por definição, f(z_t) = 0.5, então:
`0.5 = 0.5·(1+z_t)³`
`(1+z_t)³ = 1` → `z_t = 0`!

Isso mostra que a definição de f(z_t)=0.5 não corresponde à equipartição de energia entre os termos DE e matéria do setor — seria em z=0. Portanto, **z_t não tem essa motivação física**.

**STATUS** [E — resultado negativo]: A equipartição DE/matéria *no setor* ocorre em z=0 independente de z_t. z_t é apenas o ponto médio da transição da *função de mistura* f, não um ponto de equipartição energética.

---

## 6. Estado TOKEN_VAZIO dos Parâmetros

| Parâmetro | Status | Resolução |
|-----------|--------|-----------|
| H₀, Ωm, Ωb, Ωr | ✅ [E] Planck 2018 | Nenhuma |
| ΩΛ | ✅ [E] derivado (planaridade) | Nenhuma |
| z_t = 1.0 | ⚠️ [C] TOKEN_VAZIO P1 | MCMC joint (G1) |
| w_t = 0.3 | ⚠️ [C] TOKEN_VAZIO P1 | MCMC joint (G1) |
| Ωs0 = 0.02–0.05 | ⚠️ [C] TOKEN_VAZIO P1 | MCMC joint (G1) |

**Conclusão**: O modelo RLL tem 3 parâmetros livres sem motivação de primeiros princípios: (z_t, w_t, Ωs0). MCMC joint (Gap G1) é o desbloqueador central para constrainar esses parâmetros observacionalmente e possivelmente motivar seus valores.

**Linha de integridade**: Documentar honestamente que z_t, w_t, Ωs0 são fenomenológicos não desfaz o valor do modelo — modelos fenomenológicos com parâmetros livres são válidos (ex: CPL com w0, wa). A distinção é que o RLL tem mecanismo de fase explícito (f(z)) que o CPL não tem.

---

*Documento criado em FASE 12 (2026-07-07). Referências cruzadas: `08_ARVORE_CONCEITUAL_RLL.md §NÍVEL2`, `06_TOKEN_VAZIO_PRIORITY_LEDGER.md §Gap 6`.*
