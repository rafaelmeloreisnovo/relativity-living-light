# Referências — RLL Light-Loop Distance

**Status:** `references_v0.1`  
**Escopo:** física de propagação da luz, feixes gaussianos, informação, computação, redes neurais, história computacional e analogias simbólicas.

---

## 1. Física da luz e propagação

### REF_OPT_001 — Lei do inverso do quadrado

- **Tipo:** física clássica / irradiância / geometria
- **Uso no RLL:** sustentar que intensidade de fonte pontual isotrópica cai como `1/r²`.
- **Claim autorizado:** `I(r) ∝ 1/r²` para fonte pontual ideal, sem absorção/espalhamento e no regime geométrico correto.
- **Claim bloqueado:** “fóton perde energia por metro no vácuo”.
- **Fonte:** textos clássicos de óptica/física; ver também formulação de irradiância em frente esférica.

### REF_OPT_002 — Amplitude como raiz da intensidade

- **Tipo:** relação física geral de ondas
- **Uso no RLL:** explicar por que uma raiz quadrada aparece ao passar de intensidade para amplitude.
- **Claim autorizado:** se intensidade é proporcional ao quadrado da amplitude, então amplitude escala como raiz da intensidade.
- **Claim bloqueado:** “raiz quadrada a cada metro” sem definição dimensional.

### REF_OPT_003 — Feixe gaussiano e comprimento de Rayleigh

- **Referência clássica:** Siegman, A. E. *Lasers*. University Science Books, 1986.
- **Uso no RLL:** sustentar o modelo `w(z)=w0√(1+(z/zR)^2)`.
- **Claim autorizado:** para feixe gaussiano ideal dentro das condições do modelo.
- **Claim bloqueado:** aplicar fórmula de feixe gaussiano a toda propagação de luz sem especificar fonte/feixe.

### REF_OPT_004 — Relação de dispersão no vácuo

- **Tipo:** eletromagnetismo / ondas
- **Uso no RLL:** sustentar que `ω=ck` no vácuo clássico é não-dispersivo.
- **Claim autorizado:** no vácuo ideal clássico, velocidade de fase e grupo são independentes da frequência.
- **Claim bloqueado:** “há dispersão material no vácuo ideal”.

---

## 2. Informação e computação

### REF_INFO_001 — Shannon, teoria matemática da comunicação

- **Referência:** Shannon, C. E. “A Mathematical Theory of Communication.” *Bell System Technical Journal*, 1948.
- **Uso no RLL:** canal, sinal, ruído, informação, redundância, bit.
- **Claim autorizado:** usar como base da teoria da informação, não como origem do RLL.
- **Anti-plágio:** não apresentar bit, entropia de informação ou canal como descoberta própria.

### REF_COMP_001 — Turing, computabilidade

- **Referência:** Turing, A. M. “On Computable Numbers, with an Application to the Entscheidungsproblem.” *Proceedings of the London Mathematical Society*, 1936.
- **Uso no RLL:** máquina abstrata, estados, computação efetiva, limite de decisão.
- **Anti-plágio:** não apresentar máquina universal, computabilidade ou indecidibilidade como descoberta RLL.

### REF_AI_001 — McCulloch-Pitts, neurônio lógico

- **Referência:** McCulloch, W. S.; Pitts, W. “A Logical Calculus of the Ideas Immanent in Nervous Activity.” *Bulletin of Mathematical Biophysics*, 1943.
- **Uso no RLL:** limiar, lógica binária, neurônio artificial, oposição dispara/não dispara.
- **Anti-plágio:** não apresentar neurônio artificial de limiar como descoberta própria.

### REF_HIST_COMP_001 — Cartão perfurado

- **Uso no RLL:** história da codificação por presença/ausência, input discreto, oposição furo/não furo.
- **Claim autorizado:** analogia histórica entre presença/ausência e codificação computacional.
- **Claim bloqueado:** afirmar uma linha histórica completa sem fonte primária.

### REF_HIST_COMP_002 — Armazenamento magnético

- **Uso no RLL:** polaridade, leitura de setores, magnetização como oposição física codificada.
- **Status:** `REF_REQUIRED_STRONGER`
- **Próximo passo:** buscar fonte específica sobre história de gravação magnética e discos.

---

## 3. Governança acadêmica e anti-plágio

### REF_GOV_001 — FAIR Principles

- **Uso no RLL:** metadados ricos, identificadores persistentes, referências qualificadas, proveniência, reuso.
- **Aplicação:** todo claim RLL deve ter origem, metadados e referência.

### REF_GOV_002 — DataCite Metadata Schema

- **Uso no RLL:** DOI, identificação consistente de recurso, citação e recuperação.
- **Aplicação:** releases e pacotes paper-ready.

### REF_GOV_003 — Citation File Format / CITATION.cff

- **Uso no RLL:** citação legível por humano e máquina para software/dados.
- **Aplicação:** preparar citação correta do repo e releases.

### REF_GOV_004 — ICMJE authorship and AI-assisted technology

- **Uso no RLL:** autoria humana, responsabilidade, declaração de uso de IA e não listar IA como autora.
- **Aplicação:** toda publicação assistida por IA deve manter responsabilidade humana e checagem anti-plágio.

---

## 4. Analogias simbólicas e históricas

### REF_SYM_001 — Pakua / Bagua

- **Uso no RLL:** analogia de oito estados, direções ou movimentos simbólicos.
- **Status:** `REF_REQUIRED`
- **Claim boundary:** não usar como prova física. Usar apenas como referência cultural/simbólica quando fonte adequada for encontrada.

### REF_SYM_002 — Sistema sexagesimal sumério/babilônico

- **Uso no RLL:** analogia histórica de base 60, divisibilidade e conveniência operacional.
- **Status:** `REF_REQUIRED`
- **Claim boundary:** não afirmar origem matemática sem fonte histórica.

### REF_SYM_003 — História do zero

- **Uso no RLL:** vazio, nada, posição, ausência produtiva, TOKEN_VAZIO.
- **Status:** `REF_REQUIRED`
- **Claim boundary:** história do zero é plural e exige cuidado histórico.

### REF_SYM_004 — Criança brasileira e método de raiz quadrada

- **Uso no RLL:** exemplo pedagógico de descoberta por origem humilde e observação didática.
- **Status:** `REF_REQUIRED`
- **Claim boundary:** não afirmar detalhes sem fonte específica.

---

## 5. Regra anti-plágio desta trilha

```text
Se já existe na literatura, citar.
Se é analogia, marcar como analogia.
Se é hipótese RLL, declarar como hipótese.
Se não há fonte, usar REF_REQUIRED ou TOKEN_VAZIO_REFERENCE.
Se a conexão é autoral, separar conexão de origem.
```

---

## 6. R3

```text
F_ok   = referências-base e boundaries anti-plágio definidos.
F_gap  = faltam fontes específicas para Pakua, base 60, zero, armazenamento magnético e caso da raiz quadrada.
F_next = preencher source_search_queue.yml com buscas específicas desta trilha.
```
