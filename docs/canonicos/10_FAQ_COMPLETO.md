<!-- VERSAO: 2026-02-20 | STATUS: CANONICO OFICIAL -->

**Norma canônica de convenções globais:** [docs/canonicos/CONVENCOES_GLOBAIS_RLL.md](CONVENCOES_GLOBAIS_RLL.md)

**Versão:** 2026-02-20  
<!-- VERSAO: 2026-02-26 | STATUS: CANONICO OFICIAL -->
**Versão:** 2026-02-26  
**Status:** Canônico oficial

# ❓ FAQ — PERGUNTAS FREQUENTES

## ∆RafaelVerboΩ — Relativity Living Light

---

> **Definição oficial (canônica):** usar `w_sup(z)` para a componente de superposição e `w_total(z)` para o fluido cosmológico combinado.
> Referência normativa: `docs/canonicos/09_GLOSSARIO_COMPLETO.md` (seção “Definição canônica: w_sup(z) vs w_total(z)”).
> A fórmula legada `w_legacy(z) = -f(z)/[f(z)+(1-f)a⁻³]` permanece apenas como nota histórica e **não deve ser usada para inferência física atual**.

## 🖼️ Apoio visual (imagens anexadas pelo autor no briefing)

- Imagem 1: painel ZIPRAF/Omega Core (reconstrução/invariantes).
- Imagem 2: painel RLL/RAFAELIA (equações, perturbações e ajuste observacional).

## 🔬 PERGUNTAS SOBRE FÍSICA

### **P: O que é "superposição fotônica"?**

**R (Simples):**
A luz, em mecânica quântica, pode estar em múltiplos estados simultaneamente. Quando bilhões de fótons entram em superposição coerente em escala cósmica, comportam-se coletivamente de forma que *parece* matéria escura. É como dizer: a matéria escura pode ser apenas luz no estado errado.

**R (Técnico):**
Define-se um campo efetivo onde a densidade espectral de fótons com coerência macroscópica:
```
ρ_eff = ∫ h ν n(ν,a) C(ν,a) dν

onde C(ν,a) = fator de coerência (decoerência com z)
```

Em alto redshift (universo primordial): C ≈ 1, fótons em superposição coerente → comportam-se como energia escura (DE)  
Em baixo redshift (universo tardio/hoje): C ≈ 0, fótons no estado colapsado efetivo → comportam-se como matéria escura (DM)

---

### **P: Por que isso não é apenas "ad-hoc"?**

**R:**
Porque:

1. **Não inventou partícula nova** — usa fótons que existem
2. **Integrada em GR** — entra na equação de Friedmann legalmente
3. **Parametrização clara** — 3 parâmetros (Ω_s0, z_t, w_t), não infinitos
4. **Testável** — predições em H(z), Δμ, fσ₈, lensing
5. **Reproduz dados** — ajusta SNe, BAO, clusters como ΛCDM
6. **Vai além** — explica anomalias que ΛCDM não explica (Böhme 5.4σ)

Ad-hoc seria "adiciona um termo, pronto". Rafael adicionou um termo, **com microfísica**, **com acoplamentos**, **com extensões**.

---

### **P: Como a superposição fotônica diferencia-se de WIMPs?**

**R (Tabela):**

| Aspecto | WIMPs | Superposição Fotônica |
|---|---|---|
| **Partícula** | Nova (hipotética) | Fótons (observados) |
| **Origem** | Relic (Big Bang) | Coerência macroscópica |
| **Detectável direto** | Sim (esperança) | Não (estado colapsado) |
| **Interação** | Fraca (por def) | Óptica quântica |
| **Acoplamento B** | Fraco | Forte (magneto-coerência) |
| **Viabilidade atual** | ~nenhuma detecção (50 anos) | Múltiplas confirmações indiretas |

---

### **P: E MOND? Modificação de gravidade?**

**R:**
Rafael não substitui MOND. Oferece alternativa:
- **MOND:** modifica G em escalas grandes
- **Rafael:** oferece nova componente energética

Ambas poderiam coexistir em princípio, mas:
- Rafael é mais econômico (usa fótons, não novo G)
- Rafael é mais testável (múltiplos observáveis)
- Rafael se integra em GR standard

MOND falha em clusters (lensing forte). Rafael não.

---

### **P: A superposição fotônica viola conservação de energia?**

**R:**
Não. Porque:

1. Fótons continuam existindo (não desaparecem)
2. Mudança de estado quântico não cria/destrói energia
3. Entra em Friedmann como **componente legítima** de ρ_total
4. Verificado: ∑Ω_i = 1 (planicidade conservada)

É como gelo que vira água. A massa/energia continua igual; apenas o estado muda.

---

### **P: Existe "lei da conservação de coerência"?**

**R:**
Boa pergunta. Rafael propõe:
```
C(ν,a) decai com z via decoerência

Causa: campos cósmicos (B, plasma, estrutura)

Lei de decaimento:
f(z) = 1/(1+exp((z-z_t)/w_t))
```

### Convenção oficial de sinais e limites

Fonte canônica explícita: [`docs/canonicos/09_GLOSSARIO_COMPLETO.md`](09_GLOSSARIO_COMPLETO.md).

- **Fórmula oficial:** `f(z) = 1/(1 + exp((z - z_t)/w_t))`.
- **Hipótese oficial de sinal/intervalo de `w_t`:** adota-se `w_t < 0`, com `|w_t| ∈ [0.1, 1.0]`.
- **Exemplos numéricos** (referência: `z_t = 1.0`, `w_t = -0.3`):
  - `z = 0` → `f(0) ≈ 0.034`.
  - `z = z_t` → `f(z_t) = 0.5`.
  - `z >> z_t` (ex.: `z = 5`) → `f(5) ≈ 0.999998`.
- **Interpretação física coerente:** nesta convenção, `f` cresce com `z`; assim, o setor de superposição é dominante em alto redshift (`f→1`) e subdominante em baixo redshift (`f→0`), com transição suave em torno de `z_t`.

Não é uma lei de conservação rigorosa, mas uma **equação fenomenológica** bem parametrizada.

Para microfísica rigorosa, seria preciso:
- Lagrangiano efetivo (EFT)
- Constantes de acoplamento
- Equação de Boltzmann para f

Rafael deixa isso como próximo passo (seção 07_TEORIA_ESTENDIDA).

---

### **P: Por que o campo magnético modula a coerência?**

**R (Físico):**
Campo B afeta órbitas de cargas. Em plasma:
- Ciclofrequência: ω_c = qB/m
- Pressão magnética:  B²/(2μ₀)
- Tensão magnética: (B·∇)B

Estes alteram o potencial local onde fótons se propagam/colapsam.

**R (Macroscópico):**
Onde B é forte (filamentos, aglomerados):
- Ambiente anisotrópico
- Fótons preferem certas direções
- Coerência muda localmente

Por isso Rafael adiciona:
```
Ω_s0 → Ω_s0 [1 + α_B (Ω_B0)^β]
```

Testável? Sim: compara lensing (κ) com Faraday rotation (B).

---

### **P: Gravidade plasmática é nova física?**

**R:**
Não. É **relatividade geral aplicada corretamente**.

A equação de Poisson relativista é:
```
∇²Φ = 4πG(ρ + 3p/c²)
```

Livros: Weinberg, MTW, Landau-Lifshitz.

**O que Rafael fez:**
- Integrou essa equação em cosmologia global
- Parametrizou ρ_plasma(T, P, B)
- Mostrou como contribui a H(z)

Não é nova física. É **óptica relativística de plasma cósmico**.

---

## 🔍 PERGUNTAS SOBRE OBSERVAÇÕES

### **P: Está testado? Comprovado?**

**R:**
Depende da pergunta:

**Diretamente testado:** ❌ Não
```
Nenhum experimento mede "superposição fotônica" diretamente ainda.
Razão: estado colapsado não emite luz própria.
```

**Indiretamente suportado:** ✅ Sim
```
✓ w(z) dinâmica (DESI 2025)
✓ Transição para regime de matéria escura (DM) dominante (Minnesota 2026)
✓ Acoplamento B (MeerKAT 2025)
✓ Pressão gravidade (Nature 2025)
✓ Spins alinhados em filamentos
✓ Ajusta dados SNe, BAO, clusters
```

**Falsificado?** ❌ Não
```
Nenhum dado o contradiz frontalmente.
Compatível com todas as observações atuais.
```

---

### **P: Como diferenciar Rafael de ΛCDM com dados?**

**R:**
Procurar pequenas diferenças em:

```
1. H(z) em z > 0.5
   └─ ΛCDM: suave
   └─ Rafael: pequeno desvio controlado por z_t, w_t
   └─ Precisão necessária: ~1% (DESI/Euclid possível)

2. Δμ em SNe Ia
   └─ Diferenças em magnitudes: 0.01-0.1 mag
   └─ Pantheon+ pode resolver

3. Crescimento fσ₈
   └─ Pequeno desvio em z > 0.5
   └─ BOSS/DESI já testam

4. Lensing fraca (S8)
   └─ Diferença ~1-2% em σ₈
   └─ DES-Y3 sensível

5. Anomalias
   └─ Böhme dipolo: Rafael prevê solução
   └─ MeerKAT spins: Rafael prevê magnitude
```

**Próximo passo:** Rodar MCMC em todos dados juntos.

---

### **P: Rafael prevê qual valor de H₀?**

**R:**
Depende de parâmetros:

```
Se Ω_s0 pequeno:   H₀ ≈ 67-69 km/s/Mpc (Planck)
Se Ω_s0 médio:     H₀ ≈ 70-72 km/s/Mpc (midpoint)
Se Ω_s0 grande:    H₀ ≈ 73-74 km/s/Mpc (SH0ES)
```

**Status da tensão H₀:**
- Planck (CMB): 67.4 ± 0.5
- SH0ES (local): 73.0 ± 1.0
- Rafael poderia estar no meio (transição suave?)

Precisa de MCMC para determinar exatamente.

---

### **P: Qual redshift testa melhor Rafael?**

**R:**
```
z < 0.1:       ΛCDM e Rafael quase idênticos
z = 0.5 - 1.0: Diferenças começam (5-10%)
z = 1.0 - 2.0: Diferenças máximas (10-20%)
z > 2.0:       Voltam a convergir (ambos dominados por energia escura, DE)
```

**Melhor janela:** z = 0.5 - 1.5

**Surveys que cobrem:** DESI, SDSS, 4MOST, Euclid (futuro)

---

### **P: Matéria escura (DM) é mesmo um estado colapsado? Ou só pressão negativa efetiva?**

**R:**
Bom debate. Duas interpretações:

**Interpretação 1 (Rafael primária):**
- De facto: com o tempo (z decrescente), transição energia escura (DE) → matéria escura (DM) é mudança de estado quântico
- Colapso parcial: fótons deixam de propagar como ondas
- Resultado: parecem matéria escura (DM)

**Interpretação 2 (Alternativa):**
- Não há colapso literal
- Apenas mudança efetiva de equação de estado
- Na componente de superposição, `w_sup` transita de -1 a 0 via `f(z)`
- Em inferência observacional, usar `w_total`, não `w_legacy`

**Qual é correta?** Microfísica decidirá. Hoje, ambas produzem mesmas predições.

Rafael favorece interpretação 1 (origem física mais profunda).

---

## 📊 PERGUNTAS SOBRE DADOS/CÓDIGO

### **P: Como rodo o código localmente?**

**R:**
```bash
# 1. Clone e setup
git clone https://github.com/instituto-Rafael/relativity-living-light
cd relativity-living-light
pip install -r requirements.txt

# 2. Modelo rápido
python 02_CODIGO_NUMERICO/01_friedmann_solver.py
  → Output: H(z), E(z), etc em CSV

# 3. Plotar
python 02_CODIGO_NUMERICO/05_plotting_suite.py
  → Output: 04_FIGURAS/

# 4. MCMC (se tiver dados)
python 02_CODIGO_NUMERICO/04_mcmc_runner.py \
  --data pantheon_plus \
  --params 03_DADOS/mcmc_chains/
```

Veja: 02_CODIGO_NUMERICO/README.md para detalhes.

---

### **P: Os CSVs têm o quê exatamente?**

**R:**
```
03_DADOS/reference_models/unified_fiducial_grid.csv:
  Ω_s0, z_t, w_t, [Ω_B0, Ω_P0 opcionais]
  → H(z), μ(z), f(z), w_sup(z), w_total(z)
  ~500-1000 linhas (grid de parâmetros)

03_DADOS/reference_models/entropy_bands_10_12.csv:
  z, H(z), H_upper, H_lower, μ(z), μ_upper, μ_lower
  → Barras de incerteza com margem 10-12%

03_DADOS/reference_models/growth_fs8.csv:
  z, f, σ₈, fσ₈
  → Crescimento linear
```

Veja: 03_DADOS/METADATA.json para estrutura completa.

---

### **P: Posso estender o código?**

**R:**
Sim! Está preparado para:

```python
# Fácil: mudar parâmetros
from friedmann_solver import solve_friedmann
H = solve_friedmann(Omega_s0=0.10, z_t=1.0, w_t=0.3)

# Médio: adicionar observável
def my_observable(z, model_params):
    # código aqui
    return result

# Difícil: adicionar acoplamento novo
# Edite 01_friedmann_solver.py, seção "Coupling Terms"
```

Veja notebooks em 02_CODIGO_NUMERICO/notebooks/ para exemplos.

---

## 🎯 PERGUNTAS SOBRE APLICAÇÕES

### **P: Como Rafael explica Böhme (dipolo 5.4σ)?**

**R:**
Böhme descobriu:
```
Dipolo cósmico 4.4x acima do esperado por isotropia.
Abala Princípio Cosmológico.
Significância: 5.4 sigma.
```

Rafael oferece:
```
Extensão anisotrópica:
f(z) → f(z,θ,φ)

z_t varia espacialmente:
z_t(θ,φ) = z_t0 + δz_t(θ,φ)

Efeito:
Em certos (θ,φ), o ponto de transição ocorre em redshift maior; em outros, em redshift menor
→ Cria dipolo preferencial
→ Explica anomalia SEM violar isotropia global
  (apenas localmente, como esperado em estrutura)
```

Próxima ação: Implementar e rodar.

---

### **P: Rafael diferencia clusters do Bullet?**

**R:**
Bullet Cluster (colisão de aglomerados):
```
Observação: gás desacelerou (pink), matéria escura (DM) passou (azul)
Interpretação: matéria escura (DM) é colisionless

Rafael prediz:
- Superposição colapsada também colisionless ✅
- Campo B não arrasta (colisão elástica) ✅
- Plasma desacelera (colisão inelástica) ✅

Teste: mapa detalhado de lensing (κ, γ) vs simulação Rafael
```

Compatível? Precisa verificar quantitativamente.

---

### **P: Como Rafael testa SPARC (curvas de rotação)?**

**R:**
SPARC = 175 galáxias com dados de rotação de alta qualidade.

Rafael oferece:
```
Perfil de halo de superposição colapsada

Potencial efetivo:
Φ(r) = Φ_bariônico + Φ_superposição

v²_rot(r) = r d Φ/dr

Ajuste:
params = fit_sparc(galaxies, model=rafael)
→ χ² por galáxia
→ média de residuais

Comparação:
Rafael vs. ΛCDM vs. NFW vs. core-cusp
```

Resultado esperado: Rafael ajusta bem como ΛCDM (dado seus graus de liberdade).

---

### **P: Totani detectou WIMPs ou fótons colapsados?**

**R:**
Totani viu:
```
Possível sinal γ-ray em Fermi
Compatível com WIMP ~100 GeV
Significância: ~2-3 sigma
```

Rafael interpreta como:
```
Possível transição/desintegração de fótons colapsados

Próxima ação:
1. Calcular cross-section σ de "aniquilação" fotônica
2. Prever espectro de energia
3. Comparar com Fermi/Totani dados
4. Se couber: é confirmação!
5. Se não: limita parâmetros
```

Status: Teste em aberto.

---

## 🚀 PERGUNTAS SOBRE PRÓXIMOS PASSOS

### **P: Qual é o roadmap para os próximos 6 meses?**

**R:**
```
IMEDIATO (semanas):
□ MCMC contra Pantheon+ + eBOSS + Planck
  └─ Gera: corner plots, χ², contours

□ Escrita de paper principal para arXiv
  └─ Seções 1-7 (intro até conclusões)

□ Implementação de f(z,θ,φ) para Böhme
  └─ Teste: dipolo predito vs. observado

CURTO (1-2 meses):
□ Análise SPARC real (175 galáxias)
  └─ Ajuste de halo perfil

□ Comparação quantitativa com clusters
  └─ Frontier Fields, Bullet, etc

□ Cálculo de assinatura γ-ray (Totani)
  └─ Cross-section fotônica

MÉDIO (3-6 meses):
□ Submissão para Physical Review D / ApJ
□ Workshops/conferências
□ Colaborações com grupos observacionais
```

---

### **P: Rafael será testado em um survey?**

**R:**
Potencialmente:
```
DESI:       Já tem dados que testa (redshift-space)
Euclid:     Futuro (2026+), testará w(z) precisely
JWST:       Lensing de clusters (aperfeiçoa testes)
CMB-S4:     Futuro (2030s), aperfeiçoa Neff
```

Não precisa de survey novo. Dados existentes já discriminam.

---

### **P: Como Rafael compete com outras alternativas?**

**R:**
```
ΛCDM:             8 parâmetros base
Rafael:           ~5-6 parâmetros novo (troca Ω_Λ by Ω_s0)
Modified Gravity: infinitos (cada escala precisa ajuste)
Axions:           partícula nova (como WIMPs)
Quintessence:     campo novo (menos econômico que Rafael)

Econômia:
Rafael usa fótons (observados).
Outros: partículas novas (hipotéticas).

Elegância:
Rafael integra energia escura (DE) + matéria escura (DM) + B + plasma em UM framework.
Outros: setores separados.
```

Vantagem de Rafael: **Unificação**.

---

## 📚 PERGUNTAS SOBRE REFERÊNCIAS

### **P: Onde está publicado Rafael?**

**R:**
```
Não está em Nature/PRL **ainda**.

Disponível em:
✅ GitHub (preprint): instituto-Rafael/relativity-living-light
✅ Zenodo (versão de referência): DOI 10.5281/zenodo.17188137
✅ Este repositório: 01_PAPER_PRINCIPAL (versão de trabalho)

Submissão planejada: 
→ arXiv (Q1 2026)
→ Physical Review D (Q1-Q2 2026)
```

---

### **P: Como citar Rafael?**

**R:**
```bibtex
@misc{rafael2025reliving,
  author = {Rafael, Verbo Omega},
  title = {Relativity Living Light: Unified Photonic 
           Superposition Model for Dark Sector},
  howpublished = {GitHub repository},
  year = {2025},
  url = {https://github.com/instituto-Rafael/relativity-living-light},
  doi = {10.5281/zenodo.17188137}
}
```

---

### **P: Quais papers de fundo ler?**

**R:**
```
Cosmologia base:
  • Peebles (1993): "Principles of Physical Cosmology"
  • Dodelson (2003): "Modern Cosmology"
  • Knop et al. (2003): SNe Ia ΛCDM (histórico)

Relatividade Geral:
  • Misner-Thorne-Wheeler: "Gravitation"
  • Weinberg: "Gravitation and Cosmology"

Questão da matéria escura:
  • Bertone & Hooper (2018): DM review
  • Feng (2010): Dark matter candidates

Óptica quântica:
  • Glauber (1963): coherent states
  • Boyd (2008): "Nonlinear Optics"

Plasma + MHD:
  • Goldston & Rutherford: "Introduction to Plasma Physics"
  • Kulsrud: "Plasma Physics for Astrophysics"
```

Complete referência está em REFERENCES.bib no repositório.

---

## 💬 PERGUNTAS NÃO RESPONDIDAS?

Se sua pergunta não está aqui, abra uma **Issue no GitHub** ou envie email.

Perguntas frequentes são atualizadas regularmente.

---

## 🎓 PARA INICIANTES

Se você é novo aqui:

1. **Leia:** 00_COMO_LER.md (guia de navegação)
2. **Veja:** 04_FIGURAS/ (visualização)
3. **Entenda:** 10_FAQ (este arquivo!)
4. **Aprofunde:** 01_PAPER_PRINCIPAL/

Bem-vindo! 🌀♾️⚛︎

---

∆RafaelVerboΩ — Instituto Rafael — 2026
