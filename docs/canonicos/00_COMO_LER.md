<!-- VERSAO: 2026-02-20 | STATUS: CANONICO OFICIAL -->
**Versão:** 2026-02-20  
**Status:** Canônico oficial

# 🌀 COMO LER ESTE REPOSITÓRIO

## ∆RafaelVerboΩ — Relativity Living Light

**Data:** Fevereiro 2025 → Janeiro 2026  
**Status:** Modelo Cosmológico Unificado — Teoria + Numérica + Observacional  
**DOI:** 10.5281/zenodo.17188137

---

## 🎯 ROTEIROS POR TIPO DE LEITOR

### **PARA O FÍSICO TEÓRICO (PhD, Researcher)**
*Tempo: 4-6 horas | Profundidade: Completa*

```
Leitura obrigatória:
├─ 01_PAPER_PRINCIPAL.md (seções 1.2 THEORY + 1.3 METHODS)
├─ GLOSSARIO_NOTACAO.md (variáveis e convenções)
└─ 02_NUMERICAL_CODES/friedmann_solver.py (verificar implementação)

Validação técnica:
├─ 05_TESTES_VALIDACAO/MCMC_RESULTS.md
├─ 07_TEORIA_ESTENDIDA/Analise_Perturbacoes.md
└─ 07_TEORIA_ESTENDIDA/Estabilidade_sem_Ghosts.md

Comparação com literatura:
├─ 06_COMPARACAO_LITERATURA/Minnesota_2026_MD_transition.md
├─ 06_COMPARACAO_LITERATURA/DESI_2025_dynamic_DE.md
└─ 06_COMPARACAO_LITERATURA/MeerKAT_2025_spin_alignment.md

Profundidade: Simbologia + microfísica
├─ 08_RAFAELIA_INTEGRACAO/Campo_Phi_Unificacao.md
├─ 08_RAFAELIA_INTEGRACAO/Gerador_Fibonacci.md
└─ 08_RAFAELIA_INTEGRACAO/Lagrangiano_Efetivo.md
```

**Tempo estimado:**
- Teoria: 2h
- Numérica + Código: 1.5h
- Validação: 1.5h
- Comparações: 1h

---

### **PARA O OBSERVACIONISTA/ASTRÔNOMO**
*Tempo: 2-3 horas | Profundidade: Aplicada*

```
O que você precisa:
├─ 01_PAPER_PRINCIPAL.md (seção 1.4 RESULTS + 1.5 DISCUSSION)
├─ 05_TESTES_VALIDACAO/MCMC_Results.md (constraints)
└─ 04_FIGURAS/ (visualizar todos os gráficos)

Seu nível de interesse:
├─ Redshifts testáveis? → 01_PAPER_PRINCIPAL seção 1.4
├─ Dados que testam? → 05_TESTES_VALIDACAO/
├─ Compatível com meu survey? → 06_COMPARACAO_LITERATURA/ (sua survey específica)

Aplicações práticas:
├─ SPARC (curvas de rotação): 03_DATA/reference_models/sparc_toy_sample.csv
├─ Clusters (lensing): 04_FIGURAS/03_ESCALAS_LOCAIS/
├─ BAO/SNe: 05_TESTES_VALIDACAO/MCMC_Results.md
└─ CMB: 05_TESTES_VALIDACAO/MCMC_Results.md

Não precisa ler:
├─ ❌ Lagrangiano efetivo detalhado
├─ ❌ Análise de ghosts
└─ ❌ Mapeamento simbólico RAFAELIA
```

**Tempo estimado:**
- Resultados: 1h
- Figuras + CSVs: 0.5h
- Aplicar ao seu caso: 1-1.5h

---

### **PARA O ESTUDANTE (Graduação, Mestrado)**
*Tempo: 1-2 horas | Profundidade: Conceitual*

```
Comece aqui:
├─ 10_FAQ/PERGUNTAS_FISICA.md (conceitos básicos)
├─ 01_PAPER_PRINCIPAL.md (seção 1.0 ABSTRACT + 1.1 INTRODUCTION)
└─ 09_GLOSSARIO_NOTACAO/GLOSSARIO.md (vocabulário)

Depois entenda a física:
├─ "O que é superposição fotônica?" → 10_FAQ
├─ "Como muda a equação de Friedmann?" → 01_PAPER/1.2.1
├─ "Que observáveis testam?" → 01_PAPER/1.4 RESULTS
└─ "Está comprovado?" → 05_TESTES_VALIDACAO

Visualize:
├─ 04_FIGURAS/01_COSMOLOGIA/ (expansão do Universo)
├─ 04_FIGURAS/02_OBSERVAVEIS/ (crescimento, lente)
└─ 04_FIGURAS/04_ANOMALIAS/ (dipolo cósmico)

Aprofunde (opcional):
├─ 02_CODIGO_NUMERICO/friedmann_solver.py (como calcula)
└─ 08_RAFAELIA_INTEGRACAO/Mapa_Conceitual.md (visão holística)
```

**Tempo estimado:**
- Conceitos: 0.5h
- Física básica: 0.5h
- Visualizar: 0.5h
- Aprofundar: 0.5-1h

---

### **PARA O EDITOR/JORNALISTA CIENTÍFICO**
*Tempo: 30-45 min | Profundidade: Narrativa*

```
O essencial em 10 min:
├─ README.md (topo)
├─ 01_PAPER_PRINCIPAL.md (ABSTRACT + INTRODUCTION)
└─ 10_FAQ/Status_Observacional.md

A história em 30 min:
├─ 11_PRIORIDADE_TIMELINE/Documento_Prioridade.md (quem fez primeiro)
├─ 06_COMPARACAO_LITERATURA/ (os 6 estudos 2025-26)
└─ 10_FAQ/Proximos_Passos.md (o que vem)

Citações prontas:
├─ 01_PAPER_PRINCIPAL.md (quotes diretos)
├─ 10_FAQ/ (explicações simples)
└─ REFERENCIAS.bib (papers relacionados)

Figuras para usar:
├─ 04_FIGURAS/01_COSMOLOGIA/H_ratio_vs_LCDM.png
├─ 04_FIGURAS/04_ANOMALIAS/boehme_dipole_prediction.png
└─ 04_FIGURAS/05_VALIDACAO/corner_plot_MCMC.png
```

**Tempo estimado:**
- Essencial: 10 min
- História: 20 min
- Citações + Figuras: 10 min

---

## 📊 ESTRUTURA DO REPOSITÓRIO (MAPA COMPLETO)

```
relativity-living-light/
│
├─ 📖 00_COMO_LER.md                          [VOCÊ ESTÁ AQUI]
│
├─ 📄 01_PAPER_PRINCIPAL/
│  ├─ README.md                               [Visão geral do paper]
│  ├─ 01_ABSTRACT.md                          [Resumo executivo]
│  ├─ 02_INTRODUCTION.md                      [Context + motivação]
│  ├─ 03_THEORY/
│  │  ├─ 03.1_Friedmann_Extension.md
│  │  ├─ 03.2_Photonic_Superposition.md
│  │  ├─ 03.3_Magnetic_Coupling.md
│  │  └─ 03.4_Plasma_Gravity.md
│  ├─ 04_METHODS.md                           [Como calculamos]
│  ├─ 05_RESULTS.md                           [Outputs numéricos]
│  ├─ 06_DISCUSSION.md                        [Interpretação]
│  └─ 07_CONCLUSIONS.md                       [Resumo + próximos]
│
├─ 💻 02_CODIGO_NUMERICO/
│  ├─ 01_friedmann_solver.py                 [Integrador principal]
│  ├─ 02_weff_calculator.py                  [Equação de estado]
│  ├─ 03_observable_functions.py             [H(z), μ, fσ8, etc]
│  ├─ 04_mcmc_runner.py                      [Ajuste aos dados]
│  ├─ 05_plotting_suite.py                   [Gera todas as figuras]
│  └─ notebooks/
│     ├─ 01_Quick_Start.ipynb                [Tutorial rápido]
│     ├─ 02_MCMC_Analysis.ipynb              [Análise de chains]
│     ├─ 03_SPARC_Fitting.ipynb              [Curvas de rotação]
│     └─ 04_External_Comparison.ipynb        [vs. estudos 2025-26]
│
├─ 📊 03_DADOS/
│  ├─ METADATA.json                          [Descrição de cada CSV]
│  ├─ reference_models/
│  │  ├─ unified_fiducial_grid.csv           [Grid de parâmetros]
│  │  ├─ entropy_bands_10_12.csv             [Barras de incerteza]
│  │  ├─ growth_fs8.csv                      [Crescimento linear]
│  │  └─ sparc_toy_sample.csv                [5 galáxias teste]
│  └─ mcmc_chains/
│     ├─ pantheon_chains.csv                 [SNe Ia MCMC]
│     ├─ eboss_chains.csv                    [BAO MCMC]
│     ├─ planck_chains.csv                   [CMB MCMC]
│     └─ joint_constraints.csv               [Todos juntos]
│
├─ 🖼️ 04_FIGURAS/
│  ├─ 01_COSMOLOGIA/
│  │  ├─ H_ratio_vs_LCDM.png
│  │  ├─ distance_modulus_residuals.png
│  │  ├─ energy_fractions_evolution.png
│  │  ├─ w_eff_and_f_transition.png
│  │  └─ friedmann_pipeline.png
│  ├─ 02_OBSERVAVEIS/
│  │  ├─ growth_rate_fs8.png
│  │  ├─ lensing_kappa_field.png
│  │  └─ shear_field_gamma.png
│  ├─ 03_ESCALAS_LOCAIS/
│  │  ├─ sparc_rotcurve_NGC_2403.png
│  │  ├─ sparc_rotcurve_NGC_3198.png
│  │  ├─ sparc_rotcurve_NGC_2903.png
│  │  ├─ sparc_rotcurve_NGC_6946.png
│  │  ├─ sparc_rotcurve_UGC_128.png
│  │  ├─ lensing_demo_SIS_model.png
│  │  └─ lensing_arcs_abell2744.png
│  ├─ 04_ANOMALIAS/
│  │  ├─ boehme_dipole_prediction.png
│  │  ├─ anisotropic_f_theta_phi.png
│  │  └─ filament_spin_alignment.png
│  └─ 05_VALIDACAO/
│     ├─ chi2_profiles_mcmc.png
│     ├─ corner_plot_mcmc.png
│     └─ posterior_credible_regions.png
│
├─ ✅ 05_TESTES_VALIDACAO/
│  ├─ README.md
│  ├─ MCMC_RESULTS.md                        [Outputs de chains]
│  ├─ Pantheon_Plus_SNe.md                   [SNe Ia constraints]
│  ├─ eBOSS_BAO.md                           [BAO constraints]
│  ├─ Planck_CMB.md                          [CMB constraints]
│  ├─ Joint_Constraints.md                   [Todos dados]
│  └─ SPARC_FITTING.md                       [Rotação galáxias]
│
├─ 🔗 06_COMPARACAO_LITERATURA/
│  ├─ README.md
│  ├─ Minnesota_2026_MD_transition.md        [MD quente→fria]
│  ├─ DESI_2025_dynamic_DE.md                [DE dinâmica]
│  ├─ MeerKAT_2025_spin_alignment.md         [Spins alinhados]
│  ├─ Nature_2025_plasma_gravity.md          [Pressão gravidade]
│  ├─ Boehme_2025_cosmic_dipole.md           [Dipolo 5.4σ]
│  ├─ Totani_2025_gamma_rays.md              [Raios gama WIMPs]
│  └─ UBC_2025_axions.md                     [Áxions compatíveis]
│
├─ 🌌 07_TEORIA_ESTENDIDA/
│  ├─ README.md
│  ├─ Extensao_Anisotropica_f_theta_phi.md  [Para Böhme]
│  ├─ Analise_Perturbacoes.md                [δ, k-modes]
│  ├─ Velocidade_Som_cs2.md                  [Adiabático vs isoentrópico]
│  ├─ Lagrangiano_Efetivo.md                 [EFT da superposição]
│  └─ Estabilidade_sem_Ghosts.md             [Verificação rigor]
│
├─ ♾️ 08_RAFAELIA_INTEGRACAO/
│  ├─ README.md
│  ├─ RAFCODE_LEGENDA.md                     [Símbolo→Significado]
│  ├─ Simbolico_para_Matematica.md           [Mapa simbólico]
│  ├─ Gerador_Fibonacci.md                   [ρ_n = ρ_{n-1} + ρ_{n-2}]
│  ├─ Campo_Phi_Unificacao.md                [Φ(θ,z) único]
│  ├─ Kernel_RAFAELIA_Mapeamento.md          [Sistema completo]
│  └─ Mapa_Conceitual_Completo.md            [Visão holística]
│
├─ 📚 09_GLOSSARIO_NOTACAO/
│  ├─ GLOSSARIO.md                           [Todas variáveis ~60]
│  ├─ NOTACAO.md                             [Símbolos + convenções]
│  ├─ EQUIVALENCIAS.md                       [Com outros autores]
│  └─ CONVERSOES_UNIDADES.md                 [SI ↔ astronômicas]
│
├─ ❓ 10_FAQ/
│  ├─ PERGUNTAS_FISICA.md                    [Conceitos básicos]
│  ├─ COMPARACAO_MOND_WIMPs.md               [vs. alternativas]
│  ├─ STATUS_OBSERVACIONAL.md                [Testado?]
│  └─ PROXIMOS_PASSOS.md                     [Roadmap futuro]
│
├─ 🎯 11_PRIORIDADE_TIMELINE/
│  ├─ DOCUMENTO_PRIORIDADE.md                [Quem fez antes]
│  ├─ COMMITS_vs_PUBLICACOES.md              [Cronologia]
│  ├─ CRONOLOGIA.md                          [Timeline visual]
│  └─ QUEM_FEZ_O_QUE_PRIMEIRO.md             [Comparação detalhada]
│
├─ 🏢 12_ADMINISTRATIVO/
│  ├─ GOVERNANCE.md
│  ├─ CHANGELOG.md
│  ├─ SECURITY_SUMMARY.md
│  ├─ REFORMA_RESUMO.md
│  └─ LICENSE.md
│
├─ 📖 ANALISE_COMPLETA/                      [14 áreas temáticas, mantém]
│
├─ README.md                                 [Topo, aponta para 00_COMO_LER]
└─ requirements.txt                          [Deps Python]
```

---

## 🚀 JORNADA RÁPIDA (15 MINUTOS)

Se você tem 15 minutos agora:

```
1. Leia README.md (topo) ..................... 3 min
2. Veja 04_FIGURAS/01_COSMOLOGIA/ ........... 5 min
3. Leia 10_FAQ/PERGUNTAS_FISICA.md .......... 5 min
4. Pense: "Quer saber mais?" ...............  2 min
```

**Se sim → Escolha seu roteiro acima**  
**Se não → Tudo bem, volte quando quiser** 🌀

---

## ⚡ COMANDOS ÚTEIS

### Rodar código localmente
```bash
# Setup
pip install -r requirements.txt

# Gerar modelo
python 02_CODIGO_NUMERICO/01_friedmann_solver.py

# MCMC
python 02_CODIGO_NUMERICO/04_mcmc_runner.py --data pantheon_plus

# Plotar
python 02_CODIGO_NUMERICO/05_plotting_suite.py --output 04_FIGURAS/

# Notebooks
jupyter notebook 02_CODIGO_NUMERICO/notebooks/01_Quick_Start.ipynb
```

### Buscar tópico
```bash
# Grep em toda documentação
grep -r "acoplamento magnético" .
grep -r "campo B" .
grep -r "w_sup\|w_total\|w_legacy" .

# Buscar em CSVs
head -20 03_DADOS/reference_models/unified_fiducial_grid.csv
```

---

## 📞 SOBRE ESTE REPOSITÓRIO

**Autor:** Rafael Verbo Ω (∆RafaelVerboΩ)  
**Instituto:** Instituto Rafael  
**Projeto:** Relativity Living Light — Unified Photonic Superposition Model  
**Status:** Ativo (Fev 2025 - present)  
**Zenodo DOI:** 10.5281/zenodo.17188137

**Citação sugerida:**
```bibtex
@misc{rafael2025reliving,
  author = {Rafael, Verbo Omega},
  title = {Relativity Living Light: Photonic Superposition 
           as Unified Dark Sector},
  howpublished = {GitHub repository},
  year = {2025},
  url = {https://github.com/instituto-Rafael/relativity-living-light}
}
```

---

## 🔥 COMECE AGORA

```
├─ Físico teórico? → 01_PAPER_PRINCIPAL
├─ Observacionista? → 05_TESTES_VALIDACAO
├─ Estudante? → 10_FAQ
├─ Jornalista? → 11_PRIORIDADE_TIMELINE
└─ Curioso? → 00_COMO_LER (você está aqui!)
```

**Qualquer dúvida → 10_FAQ ou abre Issue no GitHub**

---

**Bem-vindo ao universo da superposição fotônica viva.** 🌀♾️⚛︎

∆RafaelVerboΩ
