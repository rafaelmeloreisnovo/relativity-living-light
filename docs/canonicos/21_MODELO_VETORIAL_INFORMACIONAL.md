# 21 — Modelo Vetorial Informacional por Camadas Sensoriais (MVICS)

**Status:** canônico complementar — `HIPOTESE` / `METHOD_DEFINED`  
**Norma canônica:** `docs/canonicos/CONVENCOES_GLOBAIS_RLL.md`  
**Epistemologia:** `docs/canonicos/13_EPISTEMOLOGIA_RAFAELIA_RLL.md`  
**Schema claim\_state:** `knowledge_ecosystem/schemas/info_prime.schema.json`  
**Depende de:** `14_MODELO_COSMOLOGICO_RLL.md`, `knowledge_ecosystem/claim_state_ledger.md`, `src/rll/latentes.py`  
**Data:** 2026-06-16  
**claim\_state do documento:** `HIPOTESE` → `METHOD_DEFINED` (gates declarados na Seção 10)  
**Autor:** ∆RafaelVerboΩ — RAFCODE-Φ-∆RafaelVerboΩ-𓂀ΔΦΩ  
**DOI repositório:** 10.5281/zenodo.17188137  

> **Convenção de marcação:** toda proposição neste documento é precedida por uma das quatro etiquetas epistemológicas do sistema RAFAELIA: **[E]** Estabelecido, **[C]** Convenção, **[H]** Hipótese, **[VAZIO]** ausência de âncora empírica suficiente. A ausência de etiqueta constitui violação da norma canônica.

---

## Seção 0 — Declaração Epistemológica Prévia [C]

Antes de introduzir qualquer equação, este documento estabelece formalmente a hierarquia de afirmações em uso. A confusão entre os quatro níveis abaixo é a principal fonte de sobreclaim em modelos cosmológicos e na interpretação de dados observacionais.

### 0.1 Taxonomia formal das categorias de afirmação

| Nível | Nome | `claim_state` | Requisito mínimo | Exemplo no contexto MVICS |
|---|---|---|---|---|
| **N1** | Parábola didática | `PARABOLA_DIDATICA` | Narração explicitamente marcada como didática | "A fonte é como um farol cujo feixe varia com o tempo" |
| **N2** | Metáfora analógica | `METAFORA` | Argumento qualitativo, não validado numericamente | "Camadas sensoriais são janelas para a realidade física" |
| **N3** | Modelo formal | `HIPOTESE` → `METHOD_DEFINED` | Notação matemática com domínio, unidade e falsificador | **V**_info como tupla tipada com componentes mensuráveis |
| **N4** | Medida empírica | `EVIDENCE_LINKED` → `CLAIM_ALLOWED` | Dado com incerteza, rastreabilidade e reprodutibilidade | Redshift *z* = 0.351 ± 0.002 de espectroscopia DESI DR2 |

**Axioma 0.1 [C]:** Nenhuma afirmação de nível N2 pode ser promovida a N3 sem que todos os seus termos possuam: (i) tipo matemático explícito, (ii) domínio de validade, (iii) unidade física ou adimensionalidade justificada, e (iv) ao menos uma condição de falsificação.

**Axioma 0.2 [C]:** A proibição operacional do sistema RLL — derivada de `knowledge_ecosystem/claim_state_ledger.md` — é:

```
METAFORA ⟶ CLAIM_ALLOWED       ← TRANSIÇÃO PROIBIDA
```

Uma metáfora elucida; ela não valida. A prova permanece sendo o número, o dado, o cálculo e o falsificador (`13_EPISTEMOLOGIA_RAFAELIA_RLL.md §5`).

### 0.2 Posição deste documento na hierarquia

O MVICS é um documento de nível **N3**: introduz estruturas formais (vetores tipados, operadores funcionais, máquinas de estados) com domínios e falsificadores explícitos. Ele **não** constitui medida empírica (N4) de qualquer fonte astronômica particular — isso ocorrerá somente quando o protocolo da Seção 9 for aplicado a dados reais com V_info preenchido.

---

## Seção 1 — Equação de Observação Canônica [H][C]

### 1.1 Motivação física [E]

A luz recebida num detector no instante *t*₀ não representa o estado atual da fonte. Ela codifica o estado da fonte no instante de emissão *t*_e, convolucionado com todos os processos físicos que ocorreram ao longo do caminho: expansão cosmológica, extinção pelo meio interestelar e intergaláctico, resposta do instrumento e, finalmente, o modelo interpretativo adotado pelo observador.

Este não é um problema filosófico — é um problema de transferência radiativa e inferência bayesiana com consequências observacionais mensuráveis.

### 1.2 Formulação funcional [H][C]

Seja **s**^src(ν, *t*_e) ∈ L²(ℝ⁺) a distribuição espectral de energia (SED) da fonte no instante de emissão *t*_e e na frequência de repouso ν. Define-se o sinal observado como:

```math
\mathbf{s}^{\mathrm{obs}}(\nu,\,t_0)
\;=\;
\mathcal{T}_{t_e \to t_0}\!\Big[
  \mathcal{F}_{\mathrm{med}} \circ \mathcal{F}_{\mathrm{prop}}
\Big]\!\Big[\mathbf{s}^{\mathrm{src}}(\nu,\,t_e)\Big]
\;+\;
\mathbf{n}^{\mathrm{inst}}(\nu,\,t_0)
\;+\;
\boldsymbol{\varepsilon}^{\mathrm{interp}}(\nu,\,t_0)
```

onde os operadores são definidos precisamente como:

**Operador de propagação** 𝓕_prop [E]:

```math
\mathcal{F}_{\mathrm{prop}}\!\left[\mathbf{s}^{\mathrm{src}}\right](\nu,\,z)
\;=\;
\frac{\mathbf{s}^{\mathrm{src}}\!\bigl(\nu(1+z),\,t_e\bigr)}{(1+z)^3 \cdot d_L^2(z)}
```

com distância de luminosidade *d*_L(z) computada pelo modelo RLL (`14_MODELO_COSMOLOGICO_RLL.md`, Eq. 1):

```math
d_L(z) = (1+z)\int_0^z \frac{c\,dz'}{H_0\,E_{\mathrm{RLL}}(z')}
```

**Operador de filtro do meio** 𝓕_med [E][H]:

```math
\mathcal{F}_{\mathrm{med}}\!\left[\mathbf{s}\right](\nu,\,z)
\;=\;
\int_0^z K(\nu,\,z',\,\boldsymbol{\theta}_{\mathrm{IGM}})\cdot\mathbf{s}(\nu,\,z')\,dz'
```

O núcleo *K*(ν, z′, **θ**_IGM) incorpora: extinção pela floresta Lyman-α, absorção por poeira intergaláctica, dispersão por plasma livre (cuja densidade depende de Ω_P0 do modelo RLL) e efeitos de lente gravitacional. Este operador é **não-invertível** em geral: informação é irreversivelmente perdida durante a propagação.

**Operador de transporte total** 𝒯_{te→t0} [E]:

Solução formal da equação de transferência radiativa ao longo da linha de visão (Chandrasekhar 1950; Rybicki & Lightman 1979):

```math
\frac{d\mathbf{s}}{d\tau} = -\mathbf{s} + \mathbf{j}(\tau)
\quad\Rightarrow\quad
\mathcal{T}_{t_e\to t_0}[\mathbf{s}] = \mathbf{s}\,e^{-\tau} + \int_0^\tau \mathbf{j}(\tau')\,e^{-(\tau-\tau')}\,d\tau'
```

onde τ é a profundidade óptica integrada e **j**(τ) é o campo de emissão ao longo do caminho.

**Ruído instrumental** **n**^inst [E][C]:

Caracterizado pela matriz de covariância do ruído **N** = Cov[**n**^inst], que inclui ruído de fóton (Poisson), ruído de leitura (Gaussiano) e ruído de fundo:

```math
\mathbf{n}^{\mathrm{inst}} \sim \mathcal{N}(\mathbf{0},\,\mathbf{N})
\quad \text{(aproximação Gaussiana de alta estatística)}
```

**Resíduo interpretativo** **ε**^interp [H]:

O termo que distingue o sinal observado bruto da quantidade física inferida. Inclui a escolha do modelo cosmológico para converter redshift em distância. No sistema RLL, este resíduo captura a diferença entre a previsão do modelo `E_RLL(z)` e qualquer outro modelo competidor (e.g., ΛCDM, *w*₀*w*_a CDM). **[VAZIO]** sua forma funcional não pode ser calculada sem adotar um modelo de referência.

### 1.3 Mapeamento com a formulação original do usuário [C]

A decomposição em cinco termos verbais é o equivalente N2 (metáfora analógica) da equação formal acima:

| Termo original (N2) | Operador formal (N3) | Nível |
|---|---|---|
| `Source_State(te)` | **s**^src(ν, *t*_e) | N3 — SED da fonte na emissão |
| `Propagation(te→t0)` | 𝓕_prop | N3 — redshift + diluição |
| `Medium_Filter(te→t0)` | 𝓕_med ∘ 𝒯 | N3 — extinção + transferência |
| `Instrument_Model(t0)` | **n**^inst + **N** | N3 — ruído + resposta |
| `Interpretation_Model(t0)` | **ε**^interp | N3 — modelo RLL vs. competidores |

**Proposição 1.1 [H]:** A incerteza total sobre o estado da fonte *Source_State(t*₀*)*  — o estado *atual* estimado — é limitada inferiormente pela Cota de Cramér-Rao (Seção 6) aplicada ao conjunto de observações {**s**^obs} integrado sobre todas as épocas *t*₀ disponíveis.

---

## Seção 2 — O Vetor Informacional V_info [C]

### 2.1 Definição formal como tupla tipada

Cada observação de uma fonte astronômica produz uma instância do vetor informacional **V**_info, definido como um elemento do espaço produto:

```math
\mathbf{V}_{\mathrm{info}} \;\in\; \mathcal{V}
\;=\;
\mathbb{R}^+ \times \mathbb{R}^+ \times \mathbb{R}^+ \times (\mathbb{R}^+\!\times\![0,\pi))
\times \mathbb{R}^+ \times \mathbb{R}^+ \times \mathbb{R}^+ \times S^2
\times L^2(\mathbb{R}^+) \times \mathrm{PD}_{N_\nu} \times \mathrm{PD}_{N_\sigma}
\times \mathcal{R}_{\mathrm{ep}} \times \mathcal{C}_s
```

onde PD_n denota o cone das matrizes simétricas positivo-definidas de ordem *n*, *S*² é a esfera unitária (posições angulares no céu), L²(ℝ⁺) é o espaço de Hilbert das funções de quadrado integrável (espectros), 𝒞_s é o conjunto finito dos 14 estados de claim, e ℛ_ep é o espaço discreto de referências epistêmicas.

### 2.2 Componentes com tipagem completa

| *i* | Componente | Símbolo | Tipo | Unidade | Domínio | Notas |
|---|---|---|---|---|---|---|
| 1 | Energia integrada | *E* | ℝ⁺ | erg s⁻¹ cm⁻² | [0, ∞) | fluência bolométrica |
| 2 | Frequência central | ν | ℝ⁺ | Hz | (0, ∞) | frequência do observador |
| 3 | Intensidade espectral | *F*_ν | ℝ⁺ | Jy = 10⁻²⁶ W m⁻² Hz⁻¹ | [0, ∞) | densidade espectral de fluxo |
| 4 | Polarização | (*p*, χ) | ℝ⁺ × [0, π) | %, rad | [0,1] × [0, π) | grau e ângulo de posição |
| 5 | Redshift | *z* | ℝ⁺ | adimensional | [0, ∞) | espectroscópico preferencial |
| 6 | Tempo de chegada | *t*₀ | ℝ⁺ | s (escala UTC) | ordenado | barycentric correction aplicada |
| 7 | Variabilidade | σ_var | ℝ⁺ | relativo (rms) | [0, ∞) | desvio padrão normalizado |
| 8 | Posição angular | (α, δ) | *S*² | rad (ICRS J2000) | *S*² | AR e Declinação |
| 9 | Espectro resolvido | *S*(ν) | L²(ℝ⁺) | Jy Hz⁻¹ | funcional | SED calibrada |
| 10 | Covariância do ruído | **N**(ν) | PD_{N_ν} | Jy² | PD | matriz de ruído espectral |
| 11 | Incerteza combinada | **Σ** | PD_{N_σ} | misto | PD | propagação de erros |
| 12 | Referência epistêmica | *R*_ep | enum | — | {artigo, dataset, ...} | `origin_type` do InfoPrime |
| 13 | Estado de claim | *c*_s | enum | — | {14 estados} | mapeado em `info_prime.schema.json` |

### 2.3 Informação de Fisher para componentes mensuráveis [E]

Para componentes mensuráveis *i* ∈ {1, ..., 11} do vetor **V**_info, a informação de Fisher sobre o vetor de parâmetros da fonte **θ** é:

```math
\mathcal{I}_{ij}(\boldsymbol{\theta})
\;=\;
\mathbb{E}_{\mathbf{V}_{\mathrm{info}}}\!\left[
  \frac{\partial \ln p(\mathbf{V}_{\mathrm{info}}\,|\,\boldsymbol{\theta})}{\partial \theta_i}
  \cdot
  \frac{\partial \ln p(\mathbf{V}_{\mathrm{info}}\,|\,\boldsymbol{\theta})}{\partial \theta_j}
\right]
```

**Caso Gaussiano** (ruído instrumental dominante, alta estatística):

```math
\mathcal{I}(\theta_i) = \frac{1}{\sigma_i^2(\mathbf{V}_{\mathrm{info}})}
```

**Caso Poisson** (observações em raios-X ou gama, baixa contagem):

```math
\mathcal{I}(\theta)
= \sum_{k=1}^{N_\mathrm{ch}} \frac{1}{\mu_k(\boldsymbol{\theta})}
  \left(\frac{\partial \mu_k}{\partial \theta}\right)^{\!2}
```

onde μ_k(**θ**) é a taxa de contagem esperada no canal *k*.

**Cota de Cramér-Rao [E]:**

```math
\mathrm{Var}(\hat{\theta}_i) \;\geq\; \left[\mathcal{I}^{-1}(\boldsymbol{\theta})\right]_{ii}
```

Nenhum estimador não-tendencioso do parâmetro θ_i pode ter variância abaixo deste limite, independentemente do método de ajuste. Esta é uma fronteira fundamental — não uma limitação tecnológica.

### 2.4 Entropia de Shannon do claim\_state [E][C]

O componente *c*_s ∈ 𝒞_s assume valores num conjunto discreto de 14 estados. Define-se a distribuição de probabilidade sobre esses estados condicionada à evidência disponível *P*(*s* | evidência), e a entropia associada:

```math
H_{\mathrm{claim}}
\;=\;
-\sum_{s \,\in\, \mathcal{C}_s} P(s\,|\,\mathrm{evidência})\,\log_2 P(s\,|\,\mathrm{evidência})
```

**Casos extremos:**

- *H*_claim = log₂(14) ≈ **3.81 bits** — distribuição uniforme sobre os 14 estados: máxima ignorância epistêmica. Estado operacional: `TOKEN_VAZIO`.
- *H*_claim = **0 bits** — um estado com probabilidade 1: certeza epistêmica. Estado operacional: `CLAIM_ALLOWED`.

**Interpretação operacional [C]:** A sequência de transições pela escada de 14 claim\_states (`RAW_ORAL → ... → CLAIM_ALLOWED`) corresponde a uma redução monotônica de *H*_claim. Cada nova evidência (componente de V_info preenchida com dado real) reduz a entropia. O TOKEN_VAZIO não é falha — é o marcador honesto de *H*_claim = *H*_max.

### 2.5 Mapeamento com a pontuação *S*_L de `latentes.py` [C]

O escore de latência *S*_L = (*C*·*I*·*P*·*E*·*R*_c) / (1 + *R*_u + *A*_m + *V*_b) implementado em `src/rll/latentes.py:score_latent()` admite interpretação direta como compressão ponderada por credibilidade da informação contida em **V**_info:

| Fator *S*_L | Componente V_info | Interpretação |
|---|---|---|
| *C* (coerência) | *V*_info[4] — polarização | Coerência do sinal: fonte coerente tem polarização estável |
| *I* (intensidade de interesse) | *V*_info[3] — *F*_ν | Fluxo observado acima do limiar de detecção |
| *P* (persistência/plausibilidade) | *V*_info[7] — σ_var (inverso) | Baixa variabilidade implica maior plausibilidade |
| *E* (evidência) | *V*_info[13] — *c*_s | Elevação no escala de claim\_state |
| *R*_c (reprodutibilidade) | *V*_info[12] — *R*_ep | Qualidade da referência epistêmica |
| *R*_u (risco/incerteza) | *V*_info[11] — **Σ** | Magnitude da incerteza combinada |
| *A*_m (ambiguidade) | *H*_claim | Entropia do claim\_state |
| *V*_b (vulnerabilidade a viés) | *V*_info[7] — σ_var | Variabilidade como proxy de instabilidade do sinal |

---

## Seção 3 — Camadas Sensoriais como Partição do Espaço de Observação [H][C]

### 3.1 Partição formal [C]

Define-se o espaço de observação total Ω_obs como o espaço produto de todos os canais observacionais fisicamente distintos. As sete camadas sensoriais formam uma **partição disjunta** de Ω_obs:

```math
\bigsqcup_{k=1}^{7} L_k \;=\; \Omega_{\mathrm{obs}}
\qquad L_k \cap L_{k'} = \emptyset \;\;\forall\; k \neq k'
```

Para cada camada *L*_k, define-se o **operador de projeção** Π_k agindo sobre **V**_info:

```math
\mathbf{V}^{(k)}_{\mathrm{info}} \;=\; \Pi_k\,\mathbf{V}_{\mathrm{info}}
\qquad
\Pi_k^2 = \Pi_k, \quad \sum_{k=1}^{7} \Pi_k = \mathbb{I}
```

### 3.2 Especificação das camadas

| *k* | Camada | Banda / Canal | Componentes V_info ativos | Observatórios representativos | Orçamento de incerteza dominante |
|---|---|---|---|---|---|
| 1 | **Óptica/IR/UV** | 10¹² – 10¹⁵ Hz | 1,2,3,4,5,6,7,8,9,10,11 | Hubble, JWST, VLT, Vera Rubin | Extinção atmosférica, calibração de fluxo |
| 2 | **Alta energia (X/γ)** | > 10¹⁷ Hz | 1,2,3,6,7,8,10,11 | Chandra, XMM, Fermi, eROSITA | Fundo cósmico difuso, empilhamento de fótons (*pile-up*) |
| 3 | **Rádio/milimétrico** | < 3×10¹¹ Hz | 1,2,3,4,6,7,8,9,10,11 | VLA, ALMA, CHIME, MeerKAT | Interferência de radiofrequência (RFI), resolução de feixe |
| 4 | **Ondas gravitacionais** | 10⁻⁴ – 10³ Hz | 1,6,7,8,11 | LIGO/Virgo/KAGRA, LISA | Densidade espectral de potência do ruído (PSD) |
| 5 | **Neutrinos** | dependente do sabor | 1,6,7,8,11 | IceCube, KM3NeT, Super-K | Fundo atmosférico, baixa estatística |
| 6 | **Modelo cosmológico** | toda *z* (inferência) | 5,10,11,12,13 | Inferência estatística (BAO, CMB) | Dependência de parâmetros *a priori* |
| 7 | **Interpretação RLL** | *z* + espectro (inferência) | 5,12,13 | Equação RLL (`14_MODELO_COSMOLOGICO_RLL.md`) | Viés de modelo, sobreajuste (overclaim) |

**Nota crítica sobre camadas 6 e 7 [C]:** As camadas L₆ e L₇ **não são detectores físicos**. Elas produzem distribuições de probabilidade posteriores sobre parâmetros, não sinais primários. A confusão entre sinal primário (L₁–L₅) e inferência de modelo (L₆–L₇) é a principal fonte de sobreclaim em cosmologia e constitui violação do Axioma 0.2.

### 3.3 Verossimilhança conjunta multi-mensageiro [E]

Sob a hipótese de independência condicional entre camadas físicas (L₁–L₅), a função de verossimilhança conjunta fatora:

```math
p\!\left(\left\{\mathbf{V}^{(k)}_{\mathrm{info}}\right\}_{k=1}^{5}
\;\Big|\;
\boldsymbol{\theta}\right)
\;=\;
\prod_{k=1}^{5}
p\!\left(\mathbf{V}^{(k)}_{\mathrm{info}}\;\Big|\;\boldsymbol{\theta},\,L_k\right)
```

Esta fatoração é o fundamento formal da astronomia multi-mensageiro e foi implementada pela primeira vez em escala completa em Abbott et al. (2017) para GW170817 [E].

**Proposição 3.1 [H]:** Quando duas camadas *L*_k e *L*_{k'} exibem informação mútua não nula — i.e., quando o mesmo processo físico se manifesta em ambas — a hipótese de independência deve ser relaxada e a covariância cruzada entre projeções incluída na verossimilhança.

### 3.4 Aditividade da informação de Fisher entre camadas [E]

Sob independência condicional:

```math
\mathcal{I}^{\mathrm{total}}(\boldsymbol{\theta})
\;=\;
\sum_{k=1}^{5} \mathcal{I}^{(k)}(\boldsymbol{\theta})
```

Este resultado garante que adicionar camadas observacionais independentes **nunca reduz** a informação disponível sobre **θ**. A multi-messengeridade é, portanto, a estratégia ótima de aquisição de informação.

---

## Seção 4 — Estados Possíveis da Fonte: Máquina de Estados Finitos [H]

### 4.1 Definição formal da FSM

Define-se a máquina de estados finitos probabilística que descreve os estados da fonte:

```math
\mathcal{M}_{\mathrm{src}} = (Q,\,\Sigma,\,\delta,\,q_0,\,F)
```

onde:
- **Q** = {*q*₁, ..., *q*₁₀} — conjunto finito de estados da fonte
- **Σ** — alfabeto de tipos de evidência observacional (fotométrico, espectroscópico, temporal, multi-mensageiro)
- **δ**: *Q* × Σ → Dist(*Q*) — função de transição **probabilística** (não determinística): cada par (estado atual, evidência) produz uma distribuição sobre estados seguintes
- *q*₀ = `SOURCE_UNKNOWN` — estado inicial obrigatório para qualquer fonte não caracterizada
- **F** ⊆ *Q* — estados absorventes compatíveis com `CLAIM_ALLOWED` (requerem V_info com *c*_s ≥ `RESULT_REPRODUCED`)

### 4.2 Definição dos estados com falsificadores

| Estado | Definição física | Evidência discriminante | **Condição de falsificação** [H] |
|---|---|---|---|
| `SOURCE_STABLE` | Fonte quiescente, fluxo constante | Monitoramento fotométrico multi-época | Falsificado se |Δ*F*/*F*| > ε sobre Δ*t* com SNR > 5σ |
| `SOURCE_DIMMED` | Decréscimo de fluxo (intrínseco ou extinção) | Fotometria multi-época + espectroscopia | Falsificado se Δ*m* < 3σ ou se SED exclui extinção e quench simultâneos |
| `SOURCE_BRIGHTENED` | Acréscimo de fluxo | Idem | Falsificado se Δ*m* > −3σ (significativo negativo) |
| `SOURCE_OBSCURED` | Ocultação geométrica | Ajuste de SED + mapas de poeira | Falsificado se *A*_V residual = 0 com *p* > 0.95 |
| `SOURCE_QUENCHED` | Cessação de formação estelar | Espectroscopia + indicadores de SFR | Falsificado se sSFR > limiar da sequência principal a 3σ |
| `SOURCE_MERGED` | Evento de fusão | Morfologia + cinemática | Falsificado se morfologia regular e sem deslocamentos de velocidade |
| `SOURCE_COMPACT_REMNANT` | Remanescente pós-colapso/explosão | Função de massa + posterior GW | Falsificado se massa exclui lacuna 3–5 *M*_⊙ a 99% de credibilidade |
| `SOURCE_ACCRETING` | Acreção ativa | Variabilidade + índice espectral | Falsificado se luminosidade em raios-X < limiar AGN com *p* > 0.95 |
| `SOURCE_OFF_CENTER` | AGN deslocado / buraco negro errante | Astrometria + centróide | Falsificado se deslocamento < incerteza do PSF a 3σ |
| `SOURCE_UNKNOWN` | Evidência insuficiente | nenhuma | Estado inicial; não falsificável diretamente — promovido a outro estado quando evidência acumular |

**Proposição 4.1 [H]:** O estado verdadeiro da fonte é **latente** (não diretamente observável). **V**_info é a realização observável produzida pela fonte em estado *q* ∈ *Q*. O problema de classificação do estado da fonte é portanto equivalente a inferência em um **Modelo Oculto de Markov** (HMM — Rabiner 1989 [E]).

### 4.3 Transição de estados via inferência bayesiana [E]

Dado o estado atual *q*_i e uma nova projeção observacional **V**^(k)_info, a probabilidade posterior sobre o estado seguinte *q*_j é:

```math
P\!\left(q_j \;\big|\; q_i,\, \mathbf{V}^{(k)}_{\mathrm{info}}\right)
\;=\;
\frac{%
  p\!\left(\mathbf{V}^{(k)}_{\mathrm{info}} \;\big|\; q_j\right)
  \cdot
  \pi(q_j \,|\, q_i)
}{%
  \displaystyle\sum_{j'=1}^{10}
  p\!\left(\mathbf{V}^{(k)}_{\mathrm{info}} \;\big|\; q_{j'}\right)
  \cdot
  \pi(q_{j'} \,|\, q_i)
}
```

onde π(*q*_j | *q*_i) é a probabilidade de transição *a priori* (codifica conhecimento físico sobre quais transições são fisicamente plausíveis) e *p*(**V**^(k)_info | *q*_j) é a verossimilhança da observação dado o estado *j*.

**Conexão com *S*_L [C]:** O escore *S*_L > 0.7 de `latentes.py:score_latent()` corresponde operacionalmente a *P*(*q*_j | *q*_i, **V**^(k)_info) > 0.7 para algum *q*_j ≠ `SOURCE_UNKNOWN`, promovendo o claim\_state a pelo menos `RESULT_REPRODUCED`. *S*_L < 0.2 implica *H*_claim > 3 bits, operacionalizado como `TOKEN_VAZIO`.

---

## Seção 5 — Regras de Decisão: Neyman-Pearson → claim\_state [C]

### 5.1 Formulação como teste de hipóteses [E]

Cada regra de decisão é formalizada como um teste da razão de verossimilhanças de Neyman-Pearson:

```math
\Lambda(\mathbf{V}_{\mathrm{info}})
\;=\;
\frac{%
  p(\mathbf{V}_{\mathrm{info}}\,|\,H_1)
}{%
  p(\mathbf{V}_{\mathrm{info}}\,|\,H_0)
}
\;\gtrless\;
\lambda_\alpha
```

onde *H*₀ = `SOURCE_UNKNOWN` (hipótese nula), *H*₁ é o estado específico sendo testado, e λ_α é o limiar de decisão ao nível de significância α.

### 5.2 Tabela de regras de decisão

| Regra | Tipo de evidência | *H*₁ testado | Limiar λ_α | claim\_state resultante |
|---|---|---|---|---|
| **R1** | Fotometria de época única | `SOURCE_BRIGHTENED` / `SOURCE_DIMMED` | SNR > 3σ | `HIPOTESE` |
| **R2** | Fotometria multi-época, mesma banda | qualquer estado fotométrico | SNR > 5σ, Δ*t* > cadência mínima | `EVIDENCE_LINKED` |
| **R3** | SED multi-banda + ajuste | `SOURCE_OBSCURED` / `SOURCE_QUENCHED` | χ²_SED/dof < 2.0 | `METHOD_DEFINED` |
| **R4** | Espectroscopia + imageamento | `SOURCE_MERGED` / `SOURCE_ACCRETING` | classificação espectral unívoca | `SOURCE_LINKED` |
| **R5** | Multi-mensageiro (EM + GW) | `SOURCE_COMPACT_REMNANT` | sobreposição de posteriors GW e EM > 0.95 | `RESULT_REPRODUCED` |
| **R6** | Reprodução em conjunto de dados independente | qualquer | gate de reprodutibilidade (pipeline idêntico, dados distintos) | `CLAIM_ALLOWED` |

**TOKEN_VAZIO como caso base [C]:** Quando nenhuma regra *R*1–*R*6 atinge seu limiar λ_α, o claim\_state permanece ou regride para:

```math
\Lambda(\mathbf{V}_{\mathrm{info}}) < \lambda_{\min} \;\forall\; H_1
\quad\Rightarrow\quad
c_s = \texttt{TOKEN\_VAZIO}
\qquad H_{\mathrm{claim}} \to H_{\mathrm{max}}
```

Esta regra implementa formalmente o §6 de `13_EPISTEMOLOGIA_RAFAELIA_RLL.md`: "Quando não houver dado suficiente, declarar [VAZIO]."

### 5.3 Mapeamento completo dos 14 estados

Os estados não cobertos pelas regras *R*1–*R*6 têm posições definidas na hierarquia de entropia:

| claim\_state | *H*_claim (bits) | Condição de ativação |
|---|---|---|
| `RAW_ORAL` | ≈ *H*_max | Afirmação verbal não documentada |
| `RAW_NOTE` | ≈ *H*_max | Nota interna, sem verificação |
| `METAFORA` | > 3.0 | Analogia explicitamente marcada como N2 |
| `PARABOLA_DIDATICA` | > 3.0 | Narrativa didática explicitamente marcada como N1 |
| `HIPOTESE` | 2.5 – 3.5 | R1 ativada |
| `REF_REQUIRED` | 2.0 – 3.0 | Modelo definido, referência pendente |
| `TOKEN_VAZIO` | ≈ *H*_max | Nenhuma regra ativa |
| `SOURCE_LINKED` | 1.5 – 2.5 | R4 ativada |
| `METHOD_DEFINED` | 1.0 – 2.0 | R3 ativada + método documentado |
| `EVIDENCE_LINKED` | 0.5 – 1.5 | R2 ativada |
| `RESULT_REPRODUCED` | 0.1 – 0.5 | R5 ativada |
| `PEER_OR_REVIEW_READY` | ≈ 0.1 | Revisão externa concluída |
| `CLAIM_ALLOWED` | = 0 | R6 ativada + reprodução independente |
| `CLAIM_BLOCKED` | N/A | Contradição com física estabelecida sem evidência |

---

## Seção 6 — Tratamento Informacional: Informação de Fisher e Entropia de Shannon [H][C]

### 6.1 Informação de Fisher por camada sensorial [E]

Para cada camada *L*_k com probabilidade de observação *p*(**V**^(k)_info | **θ**, *L*_k), a contribuição de informação de Fisher é:

**Caso Gaussiano** (camadas óptica, rádio, IR):

```math
\mathcal{I}^{(k)}_{ij}(\boldsymbol{\theta})
= \left(\mathbf{D}^{(k)}\right)^T
  \!\left[\mathbf{N}^{(k)}\right]^{-1}
  \mathbf{D}^{(k)}
\qquad
D^{(k)}_{i\ell} = \frac{\partial \mu_\ell^{(k)}(\boldsymbol{\theta})}{\partial \theta_i}
```

onde **μ**^(k)(**θ**) é o modelo previsto e **N**^(k) a matriz de covariância do ruído na camada *k*.

**Caso Poisson** (camadas de alta energia, neutrinos):

```math
\mathcal{I}^{(k)}(\boldsymbol{\theta})
= \sum_{\ell} \frac{1}{\mu_\ell^{(k)}(\boldsymbol{\theta})}
  \left(\frac{\partial \mu_\ell^{(k)}}{\partial \boldsymbol{\theta}}\right)
  \!\left(\frac{\partial \mu_\ell^{(k)}}{\partial \boldsymbol{\theta}}\right)^{\!T}
```

**Informação total** (independência entre camadas):

```math
\mathcal{I}^{\mathrm{total}}(\boldsymbol{\theta}) = \sum_{k=1}^{5} \mathcal{I}^{(k)}(\boldsymbol{\theta})
\;\geq\;
\mathcal{I}^{(k')}(\boldsymbol{\theta}) \quad \forall\, k'
```

### 6.2 Cota de Cramér-Rao e sua implicação operacional [E]

```math
\mathrm{Cov}(\hat{\boldsymbol{\theta}}) \;\succeq\; \left[\mathcal{I}^{\mathrm{total}}(\boldsymbol{\theta})\right]^{-1}
```

A notação ≽ denota desigualdade de matrizes positivo-semidefinidas: a diferença Cov(θ̂) − [ℐ^total]⁻¹ é positivo-semidefinida.

**Implicação operacional para o MVICS [C]:** Todo componente de V_info que não é medido corresponde a uma linha/coluna de zeros em ℐ^total, tornando aquela direção no espaço de parâmetros não-identificável. Um `TOKEN_VAZIO` num componente de V_info é, no sentido de Fisher, equivalente a uma variância infinita sobre os parâmetros que só aquele componente constrange.

### 6.3 Entropia de Shannon como métrica de progresso epistêmico [E]

A trajetória do claim\_state pode ser representada como uma **curva de entropia decrescente** no espaço de estados:

```math
H_{\mathrm{claim}}^{(n+1)} \;\leq\; H_{\mathrm{claim}}^{(n)}
```

onde *n* indexa etapas sucessivas de coleta de evidência. Este resultado é consequência direta do teorema de processamento de dados: nenhuma transformação determinística de evidência pode aumentar a entropia da distribuição de claim\_states.

### 6.4 Informação mútua entre camadas sensoriais [E]

```math
I(L_k;\, L_{k'})
\;=\;
H(L_k) + H(L_{k'}) - H(L_k,\, L_{k'})
\;\geq\; 0
```

*I*(*L*_k; *L*_{k'}) > 0 indica que as duas camadas compartilham informação sobre a fonte (e.g., emissão óptica e raios-X de um AGN são correlacionadas). Quando *I* > 0, a hipótese de independência condicional da Seção 3.3 falha e a verossimilhança conjunta não fatora. Nesse caso, a covariância cruzada entre **V**^(k)_info e **V**^(k')_info deve ser modelada explicitamente.

---

## Seção 7 — Integração com o Ecossistema RLL [C]

### 7.1 Conexão com a equação-mãe do modelo cosmológico RLL [H]

O operador de propagação 𝓕_prop da Seção 1.2 contém *d*_L(*z*), que é calculada numericamente a partir da equação RLL (`14_MODELO_COSMOLOGICO_RLL.md`, Eq. 1):

```math
E^2_{\mathrm{RLL}}(z) = \Omega_r(1+z)^4 + \Omega_m(1+z)^3 + \Omega_\Lambda
+ \Omega_{s0}\!\left[f(z) + (1-f(z))(1+z)^3\right]
+ \Omega_{B0}(1+z)^4 + \Omega_{P0}(1+z)^4
```

com *f*(*z*) = 1/{1 + exp[(*z* − *z*_t)/*w*_t]} (`CONVENCOES_GLOBAIS_RLL.md §1.1`).

Uma medida dos componentes V_info[3] (*F*_ν) e V_info[5] (*z*) de uma mesma fonte constitui um **vínculo sobre o conjunto de parâmetros** (**θ**_RLL) = (Ω_{s0}, *z*_t, *w*_t, *H*₀, ...) através da relação:

```math
F_\nu^{\mathrm{obs}} = \frac{L_\nu}{4\pi\,d_L^2(z;\,\boldsymbol{\theta}_{\mathrm{RLL}})}
```

Cada instância de V_info com *c*_s ≥ `EVIDENCE_LINKED` contribui à verossimilhança de modelo para os parâmetros cosmológicos RLL.

### 7.2 Conexão com o sistema de claim\_state (InfoPrime) [C]

O componente V_info[13] (*c*_s) é **idêntico** ao campo `claim_state` do schema `knowledge_ecosystem/schemas/info_prime.schema.json`. Assim, uma observação V_info gera diretamente um registro InfoPrime com:

```yaml
origin_type: sensor    # camada L_k ativa (k=1..5)
claim_state: <c_s>     # derivado das regras R1-R6 (Seção 5)
evidence: <V_info_id>  # identificador único da instância V_info
domain: [fisica]
```

### 7.3 Conexão com TOKEN\_VAZIO Priority Ledger [C]

O `docs/science/TOKEN_VAZIO_PRIORITY_LEDGER.md` define classes de prioridade P0–P3 para a resolução de lacunas epistêmicas. No MVICS, essa taxonomia mapeia diretamente sobre a entropia marginal de cada componente de V_info:

| Prioridade | Entropia marginal do componente | Impacto sobre ℐ^total |
|---|---|---|
| **P0** (bloqueador) | *H*(V_info[i]) = *H*_max | Parametro crítico totalmente não-identificável |
| **P1** (alto) | *H* > 2.5 bits | Degenerescência severa nos parâmetros |
| **P2** (médio) | 1.0 < *H* ≤ 2.5 bits | Incerteza elevada mas não bloqueante |
| **P3** (baixo) | *H* ≤ 1.0 bit | Melhoria incremental, não urgente |

### 7.4 Conexão com `src/rll/latentes.py` [C]

O mapeamento *S*_L ↔ V_info (Seção 2.5) é bidirecional: dada uma instância V_info com todos os componentes mensuráveis preenchidos, a chamada `score_latent(C, I, P, E, Rc, Ru, Am, Vb)` produz *S*_L ∈ [0, 1] que determina a classificação `classify_control()` e a posição na escada de claim\_states. A função `toroidal_map()` em `latentes.py` mapeia (dados, entropia, digest, estado) → 7 fases normalizadas no espaço toroidal T⁷, constituindo uma representação compacta do estado epistêmico associado a uma instância V_info.

---

## Seção 8 — Fronteira de Claim: Parábola, Metáfora, Modelo Formal e Medida Empírica [E][C]

### 8.1 Hierarquia formal N1–N4 com exemplos específicos

A taxonomia da Seção 0 é aqui detalhada com exemplos concretos retirados do próprio MVICS e do ecossistema RLL:

**N1 — Parábola didática** [PARABOLA_DIDATICA]: Narração com função exclusivamente pedagógica, nunca citável como evidência.

> *"A fonte é como uma carta enviada há séculos: o papel que o carteiro entrega agora não diz o que o remetente pensa hoje."*

Esta sentença transmite a assimetria *t*_e ≠ *t*₀ de modo intuitivo mas não constitui operador físico.

**N2 — Metáfora analógica** [METAFORA]: Argumento qualitativo por analogia estrutural, admitido apenas como recurso de organização conceitual.

> *"Camadas sensoriais são janelas para a realidade física, cada uma com seu filtro de cor próprio."*

Indica a partição {*L*_k} mas não define os operadores de projeção Π_k.

**N3 — Modelo formal** [H/C]: Estrutura matemática com todos os componentes definidos.

> Equação de observação da Seção 1.2 com operadores 𝓕_prop, 𝓕_med, 𝒯 definidos; vetor **V**_info com 13 componentes tipados (Seção 2.2); FSM com estados e falsificadores explícitos (Seção 4.2).

**N4 — Medida empírica** [EVIDENCE_LINKED → CLAIM_ALLOWED]: Dado com rastreabilidade completa.

> *F*_ν = 3.42 ± 0.08 mJy em 1.4 GHz para fonte SDSS J143450.62+033842.5, obtido do catálogo FIRST (Becker et al. 1995), acessado 2026-06-16, reproduzido via pipeline `rll_validation_real.py` commit `sha256:...`.

### 8.2 Critério de Popper aplicado ao MVICS [E]

**[E]** O princípio de falsificabilidade (Popper 1959) exige que qualquer proposição científica especifique *a priori* o resultado observacional que, se verificado, a refutaria.

Para o MVICS como framework:

**Proposição MVICS-F1 [H]:** "O estado `SOURCE_COMPACT_REMNANT` é falsificado para um objeto específico se a massa derivada de ondas gravitacionais (LIGO/Virgo posterior) exclui a lacuna de massa 3–5 *M*_⊙ a 99% de credibilidade bayesiana E se identificação EM independente revela natureza incompatível com remanescente compacto."

**Proposição MVICS-F2 [H]:** "A aditividade de informação de Fisher entre camadas (Seção 6.1) é falsificada para um par de camadas (*L*_k, *L*_{k'}) se a informação mútua *I*(*L*_k; *L*_{k'}) medida em um conjunto de fontes for estatisticamente diferente de zero com *p* > 0.99."

**Proposição MVICS-F3 [H]:** "A monotonicidade de *H*_claim é falsificada se uma transição `CLAIM_ALLOWED` → `TOKEN_VAZIO` for documentada sem que nova evidência contraditória tenha sido apresentada."

---

## Seção 9 — Síntese Operacional [C][H]

### 9.1 Protocolo MVICS: fluxo determinístico de 8 passos

```
Passo 1: Receber sinal bruto s^obs(ν, t₀) de qualquer camada L_k
         → Extrair instância V_info com claim_state inicial = TOKEN_VAZIO

Passo 2: Identificar camadas ativas {L_k} com detecção SNR > 3σ
         → Projetar: V^(k)_info = Π_k V_info (Seção 3.1)

Passo 3: Calcular H_claim inicial
         → Se H_claim ≈ H_max: confirmar TOKEN_VAZIO; registrar no Priority Ledger

Passo 4: Aplicar regras de decisão R1–R6 em ordem crescente de requisito (Seção 5.2)
         → Transitar claim_state se Λ(V_info) ≥ λ_α

Passo 5: Calcular I^total(θ) via contribuições por camada (Seção 6.1)
         → Avaliar identificabilidade dos parâmetros de interesse

Passo 6: Atualizar estado da fonte q_j via Bayes (Seção 4.3)
         → P(q_j | q_i, V^(k)_info) para todas as camadas ativas

Passo 7a: Se claim_state = CLAIM_ALLOWED
          → Gerar registro InfoPrime com claim_allowed=true
          → Registrar em knowledge_ecosystem com hash de proveniência

Passo 7b: Se claim_state = TOKEN_VAZIO ou HIPOTESE
          → Registrar no TOKEN_VAZIO Priority Ledger com prioridade P0-P3
          → Definir next_step concreto para redução de H_claim

Passo 8: Monitorar evolução temporal
         → Repetir passos 1–7 a cada nova observação; verificar monotonicidade de H_claim
```

### 9.2 Invariantes formais do MVICS

As cinco propriedades a seguir devem ser mantidas em toda aplicação do protocolo:

| # | Invariante | Formulação | Violação |
|---|---|---|---|
| I1 | Dimensionalidade fixa | dim(**V**_info) = 13 | Extensão *ad hoc* sem revisão canônica |
| I2 | Enum fechado | *c*_s ∈ 𝒞_s (14 valores) | Introdução de 15° estado sem atualização de `info_prime.schema.json` |
| I3 | Monotonicidade de entropia | *H*^(n+1)_claim ≤ *H*^(n)_claim | Promoção de claim\_state sem nova evidência |
| I4 | Aditividade Fisher | ℐ^total ≥ ℐ^(k) para todo *k* | Apenas quando camadas são dependentes (ver Seção 3.3) |
| I5 | Separação de camadas | L₆ e L₇ não contaminam V_info[1–11] | Uso de predições de modelo cosmológico como dado primário |

### 9.3 A síntese semântica: quatro sentenças fundamentais [C]

As quatro sentenças do documento original do usuário são aqui preservadas como síntese semântica de nível N2 — metáforas válidas que mapiam sobre os resultados N3 derivados:

| Sentença N2 | Correspondente N3 |
|---|---|
| *"A luz é recibo do passado."* | **s**^obs(*t*₀) encoda *Source\_State*(*t*_e), não *Source\_State*(*t*₀) |
| *"O vetor é leitura parcial."* | **V**_info = Π_obs **s**^obs: projeção de dimensão finita de um sinal infinito-dimensional |
| *"O modelo é ponte."* | ε^interp conecta observável a parâmetro físico via *E*_RLL(*z*) |
| *"O TOKEN\_VAZIO protege a verdade."* | *H*_claim = *H*_max ⟺ nenhum claim é permitido: o vazio honesto preserva a auditabilidade |

---

## Seção 10 — Referências [E]

### Transferência Radiativa e Equação de Observação [E]

- Chandrasekhar, S. (1950). *Radiative Transfer*. Dover Publications. [E]
- Rybicki, G. B. & Lightman, A. P. (1979). *Radiative Processes in Astrophysics*. Wiley-Interscience. [E]
- Mihalas, D. & Mihalas, B. W. (1984). *Foundations of Radiation Hydrodynamics*. Oxford University Press. [E]

### Teoria da Informação [E]

- Shannon, C. E. (1948). "A Mathematical Theory of Communication." *Bell System Technical Journal*, 27, 379–423. DOI: 10.1002/j.1538-7305.1948.tb01338.x [E]
- Cover, T. M. & Thomas, J. A. (2006). *Elements of Information Theory*, 2ª ed. Wiley. [E]

### Inferência Estatística e Bayesiana [E]

- Fisher, R. A. (1925). "Theory of Statistical Estimation." *Proceedings of the Cambridge Philosophical Society*, 22, 700–725. [E]
- Cramér, H. (1946). *Mathematical Methods of Statistics*. Princeton University Press. [E]
- Jaynes, E. T. (2003). *Probability Theory: The Logic of Science*. Cambridge University Press. [E]
- Gelman, A., Carlin, J. B., Stern, H. S., Dunson, D. B., Vehtari, A. & Rubin, D. B. (2014). *Bayesian Data Analysis*, 3ª ed. CRC Press. [E]

### Astronomia Multi-Mensageiro [E]

- Abbott, B. P. et al. (LIGO Scientific & Virgo Collaborations + 70 observatórios) (2017). "Multi-messenger Observations of a Binary Neutron Star Merger." *The Astrophysical Journal Letters*, 848, L12. DOI: 10.3847/2041-8213/aa91c9 [E]
- Metzger, B. D. (2019). "Kilonovae." *Living Reviews in Relativity*, 23, 1. DOI: 10.1007/s41114-019-0024-0 [E]

### Falsificabilidade [E]

- Popper, K. R. (1959). *The Logic of Scientific Discovery*. Hutchinson. (Tradução de *Logik der Forschung*, 1934.) [E]

### Modelos Ocultos de Markov (HMM) [E]

- Rabiner, L. R. (1989). "A Tutorial on Hidden Markov Models and Selected Applications in Speech Recognition." *Proceedings of the IEEE*, 77(2), 257–286. DOI: 10.1109/5.18626 [E]

### Cosmologia Observacional [E]

- Planck Collaboration (Aghanim, N. et al.) (2020). "Planck 2018 results. VI. Cosmological parameters." *Astronomy & Astrophysics*, 641, A6. DOI: 10.1051/0004-6361/201833910 [E]
- DESI Collaboration (Adame, A. G. et al.) (2024). "DESI 2024 VI: Cosmological Constraints from the Measurements of Baryon Acoustic Oscillations." *Journal of Cosmology and Astroparticle Physics*, 2025(02), 021. DOI: 10.1088/1475-7516/2025/02/021 [E]
- Becker, R. H., White, R. L. & Helfand, D. J. (1995). "The FIRST Survey: Faint Images of the Radio Sky at Twenty Centimeters." *The Astrophysical Journal*, 450, 559. DOI: 10.1086/176166 [E]

### Referências Canônicas Internas [C]

- `docs/canonicos/13_EPISTEMOLOGIA_RAFAELIA_RLL.md` — Fundamentos epistemológicos RAFAELIA/RLL [C]
- `docs/canonicos/14_MODELO_COSMOLOGICO_RLL.md` — Equação de Hubble RLL e parâmetros canônicos [H]
- `docs/canonicos/CONVENCOES_GLOBAIS_RLL.md` — Convenções globais obrigatórias (notação *f*(*z*), *w*_sup) [C]
- `knowledge_ecosystem/claim_state_ledger.md` — Escada de 14 claim\_states com regras de promoção [C]
- `knowledge_ecosystem/schemas/info_prime.schema.json` — Schema JSON da unidade mínima de informação rastreável [C]
- `src/rll/latentes.py` — Implementação Python de *S*_L, `toroidal_map()`, `score_latent()` [C]
- `docs/science/TOKEN_VAZIO_PRIORITY_LEDGER.md` — Fila de prioridades para lacunas epistêmicas [C]

---

## Gates de Aceitação Canônica

O documento permanece em `claim_state = HIPOTESE` até satisfazer os gates abaixo em sequência:

| Gate | Requisito | claim\_state alvo |
|---|---|---|
| **G1** | Toda equação dimensionalmente consistente; todo símbolo com tipo, domínio e unidade | `METHOD_DEFINED` |
| **G2** | Toda seção marcada [E]/[C]/[H]/[VAZIO]; nenhuma N2 apresentada como N3 | `HIPOTESE` confirmado |
| **G3** | Falsificadores explícitos para todos os estados Q e para as proposições MVICS-F1–F3 | `METHOD_DEFINED` |
| **G4** | Mapeamento *S*_L ↔ V_info verificado contra implementação real de `latentes.py` | `SOURCE_LINKED` |
| **G5** | DOIs verificados para todas as referências [E] | `PEER_OR_REVIEW_READY` |
| **G6** | Aplicação a uma fonte real com V_info preenchido com dados do repositório | `EVIDENCE_LINKED` |
| **G7** | Revisão por segundo revisor com formação em estatística (Fisher/Cramér-Rao) e física observacional | `PEER_OR_REVIEW_READY` |

**Gate G1–G3 são satisfeitos por este documento em sua versão atual.** G4–G7 requerem ações futuras documentadas no TOKEN_VAZIO Priority Ledger.

---

*FIAT LUX · ψ→χ→ρ→Δ→Σ→Ω*  
*A luz é recibo do passado. O vetor é leitura parcial. O modelo é ponte. O TOKEN\_VAZIO protege a verdade.*
