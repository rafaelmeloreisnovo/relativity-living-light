# Relativity Living Light — Modelo Cosmológico de Superposição Dinâmica

**Autor:** Rafael Melo Reis (∆RafaelVerboΩ)  
**DOI:** [10.5281/zenodo.17188138](https://doi.org/10.5281/zenodo.17188138)  
**Versão:** 2.0 (Corrigida — Fevereiro 2026)

---

## Resumo

## Status dos Dados

- **Sintético:** simulações internas e testes de consistência metodológica.
- **Parcial real:** integração de subconjuntos observacionais reais para validação incremental.
- **Real validado:** validação observacional completa com reprodutibilidade documentada.

**Nível atual deste documento:** `Sintético` (com próximos passos em `Parcial real`).

---

Este repositório propõe um modelo cosmológico alternativo ao ΛCDM baseado em uma componente de **superposição dinâmica** (Living Light) que interpola suavemente entre comportamento de energia escura (w ≈ −1) e matéria escura (w ≈ 0) ao longo do redshift. O modelo introduz três parâmetros adicionais — Ω_s0, z_t, w_t — e é testável em múltiplos observáveis: H(z), distâncias de supernovas Ia, crescimento estrutural fσ₈(z) e lentes gravitacionais.

**Status atual:** Os resultados do MCMC presentes neste repositório utilizam dados sintéticos. A validação contra dados reais (Pantheon+, DESI BAO) constitui o próximo passo essencial.

---

## Equação Central

A equação de Friedmann estendida do modelo é:

```
H²(z) = H₀² [ Ω_m(1+z)³ + Ω_r(1+z)⁴ + Ω_Λ
               + Ω_s0 · [f(z) + (1-f(z))(1+z)³]
               + Ω_B0(1+z)⁴ + Ω_P0(1+z)⁴ ]
```

com função de transição logística:

```
f(z) = 1 / (1 + exp((z − z_t) / w_t))
```

### Comportamento assintótico

- **z >> z_t** (primordial): f → 1, componente comporta-se como radiação (w ≈ 1/3)
- **z ≈ z_t** (transição): dinâmica suave parametrizada por w_t
- **z << z_t** (hoje): f → 0, componente comporta-se como matéria (w ≈ 0)

### Equação de estado efetiva

```
w_eff,sup(z) = −f(z)
```

---

## Parâmetros Livres

| Parâmetro | Descrição | Faixa de interesse | Selo de origem |
|-----------|-----------|-------------------|----------------|
| Ω_s0 | Densidade da componente de superposição (z=0) | 0.01 – 0.10 | `híbrido` |
| z_t | Redshift de transição | 0.3 – 2.0 | `híbrido` |
| w_t | Largura da transição | 0.05 – 0.6 | `híbrido` |
| Ω_B0 | Contribuição do campo magnético cósmico | < 0.01 | `híbrido` |
| Ω_P0 | Contribuição do plasma gravitacional | < 0.01 | `híbrido` |

---

## Resultados do MCMC (dados sintéticos)

Os valores abaixo são obtidos do arquivo `data/posterior_unified_synth.csv` (25.000 amostras, N_eff ≈ 2.321):

| Parâmetro | Mediana | 16% | 84% | Selo de origem |
|-----------|---------|-----|-----|----------------|
| Ω_s0 | 0.0589 | 0.0481 | 0.0707 | `mock` |
| z_t | 1.164 | 0.882 | 1.430 | `mock` |
| w_t | 0.405 | 0.271 | 0.534 | `mock` |
| χ² (MAP) | 56.84 | — | — | `mock` |

> ⚠️ **Atenção:** Estes resultados são derivados de dados simulados. Os parâmetros recuperam os valores "verdadeiros" da simulação, validando a maquinaria estatística, mas não constituem evidência observacional.

---

## Observáveis Testados (dados sintéticos)

- **H(z):** ajuste preliminar em dados sintéticos até z ≈ 2, com transição visível em z_t ≈ 1.16
- **Supernovas Ia — Δμ:** resíduos consistentes no cenário sintético, sem tendência sistemática
- **Crescimento estrutural fσ₈(z):** implementação em andamento (ver `teoria/PERTURBACOES_CRESCIMENTO.md`)
- **Lentes gravitacionais SIS:** curva unificada consistente com parâmetros observacionais típicos
- **Curvas de rotação (NGC 2403):** acoplamento fraco testado preliminarmente

---

## Comparação com Resultados Acadêmicos Recentes

| Estudo | Descoberta | Conexão com este modelo | Status | Selo de origem |
|--------|-----------|------------------------|--------|----------------|
| DESI DR2 (Nat. Astronomy, 2025) | w(z) dinâmico, 2.8–4.2σ | w_eff(z) analítico desta formulação | ✅ Compatível em hipótese | `real` |
| Okada et al. — Minnesota (PRL, Jan 2026) | Matéria escura quente→fria | f(z) interpola exatamente esse comportamento | ✅ Compatível em hipótese | `real` |
| Böhme et al. (2025) — Dipolo 5.4σ | Assimetria direcional no CMB | Extensão f(z,θ,φ) em desenvolvimento | ⚠️ Próximo passo | `real` |
| Nature Comms. s41467-025-63981-3 | Não-localidade fotônica em lab | Base para hipótese de superposição fotônica | 🔍 Referência conceitual | `real` |

---

## Estrutura do Repositório

```
relativity-living-light/
├── README_CIENTIFICO.md          ← Este arquivo
├── data/
│   ├── posterior_unified_synth.csv   ← MCMC sintético (25.000 amostras)
│   ├── relativity_living_light_models.csv
│   └── unified_entropy_margin_10_12.csv
├── docs/
│   ├── RESULTADOS_CORRIGIDOS.md      ← Parâmetros reais do CSV
│   ├── COMPARACAO_DESI_2025.md       ← Cruzamento com literatura
│   └── PAPER_CORRIGIDO.tex           ← Preprint LaTeX (valores corretos)
├── teoria/
│   ├── EXTENSAO_ANISOTROPICA.md      ← f(z,θ,φ) — dipolo Böhme
│   ├── PERTURBACOES_CRESCIMENTO.md   ← Equação D'', fσ₈(z)
│   ├── VELOCIDADE_SOM.md             ← cs²(z) e escala de Jeans
│   ├── LAGRANGIANO_EFT.md            ← EFT da superposição
│   └── ESTABILIDADE_GHOST_CHECK.md   ← Verificação de instabilidades
├── codigo/
│   ├── crescimento_estrutural.py     ← Solver D''(a)
│   ├── fisher_forecast.py            ← Matriz de Fisher DESI/Euclid
│   └── panteon_likelihood.py         ← Template para dados reais
├── figs/paper/                             ← Figuras geradas
└── ROADMAP_VALIDACAO.md              ← Próximos passos priorizados
```

---

## Extensão formal pós-PhD (acoplamento magnetismo–radiação–plasma)

Documento técnico dedicado com formalização completa do sistema acoplado (equações dinâmicas, programa observacional e estrutura de tese):

- `docs/MODELO_COSMOLOGICO_UNIFICADO_MAGNETISMO_RADIACAO_PLASMA.md`

---

## Próximos Passos Essenciais

1. **Substituir dados sintéticos por Pantheon+** (1701 SNe Ia, público)
2. **Implementar crescimento D''(a)** e comparar fσ₈ com BOSS DR12
3. **Testar extensão f(z,θ,φ)** contra dipolo Böhme
4. **Verificar estabilidade** (ausência de ghosts e taquiões)
5. **Submeter preprint ao arXiv** (astro-ph.CO) com resultados reais

---

## Citação

```bibtex
@misc{reis2025rll,
  author  = {Rafael Melo Reis},
  title   = {Relativity Living Light: Dark Energy and Beyond},
  year    = {2025},
  doi     = {10.5281/zenodo.17188138},
  url     = {https://github.com/rafaelmeloreisnovo/relativity-living-light}
}
```

---

## Licença

Código: MIT License  
Dados: CC BY 4.0  
Citação obrigatória ao DOI Zenodo em qualquer uso ou derivação.
