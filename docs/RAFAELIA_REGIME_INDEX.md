# RAFAELIA REGIME INDEX — classificação de regimes documentais

> Índice operacional para separar fórmula, hipótese, metáfora, evidência, validação, legado e material autoral dentro do ecossistema Relativity Living Light / RAFAELIA.

## Objetivo

Este arquivo organiza documentos grandes e textos soltos do repositório por **regime de uso**, evitando que hipótese, símbolo, fórmula e prova sejam confundidos.

Regra central:

```text
símbolo inspira; hipótese orienta; fórmula modela; dado testa; métrica decide; limite protege.
```

---

## 1. Núcleo canônico-científico

Arquivos usados como referência técnica principal para fórmulas, parâmetros, limites de claim, dados e validação.

| Arquivo | Regime | Uso recomendado | Observação |
|---|---|---|---|
| `docs/FORMULAS_CANONICAS_INDEX.md` | `[CANÔNICO-CIENTÍFICO]` | referência oficial de fórmulas | manter como fonte de citação formal |
| `rll_equation_registry.yml` | `[CANÔNICO-CIENTÍFICO]` | registro estruturado de equações e claim boundaries | bom para auditoria automática |
| `docs/BOOSTERS.md` | `[MODELO-CIENTÍFICO]` | descrição dos boosters `Ω_s0`, `Ω_B0`, `Ω_P0` | tratar valores típicos como priors/hipóteses |
| `docs/VALIDATION_DATA_MATRIX_RLL_MCRP.md` | `[VALIDAÇÃO]` | matriz Hipótese/Dado/Modelo/Métrica | referência para separar sintético, parcial real e real validado |
| `docs/RLL_CLAIM_BOUNDARIES.md` | `[LIMITE-EPISTÊMICO]` | disciplina de claims e vocabulário permitido | obrigatório antes de claims fortes |
| `docs/REFERENCES.md` | `[REFERÊNCIAS]` | fontes e bibliografia | exigir fonte primária quando possível |

---

## 2. Núcleo operacional para paper, testes e execução

Arquivos que transformam o modelo em trilha testável, scripts, paper ou comparação estatística.

| Arquivo | Regime | Uso recomendado | Observação |
|---|---|---|---|
| `docs/PLANO_ABCD_JWST_AGN_SMBH.md` | `[OPERACIONAL-PAPER]` | roteiro A→B→C→D para paper e fechamento de modelo | contém termos gaussianos, AIC/BIC e critérios de parcimônia |
| `docs/PAPER_CORRIGIDO.tex` | `[PAPER-DRAFT]` | base LaTeX de paper | revisar contra fórmulas canônicas antes de submissão |
| `main.tex` | `[PAPER-DRAFT]` | entrada LaTeX raiz | manter alinhado a `docs/PAPER_CORRIGIDO.tex` |
| `docs/rll_validation_real.py` | `[SCRIPT-VALIDAÇÃO]` | validação com dados reais/semirreais | checar entradas, hashes e outputs |
| `docs/fisher_forecast.py` | `[SCRIPT-FORECAST]` | previsão Fisher / sensibilidade | útil para roadmap observacional |
| `docs/panteon_likelihood.py` | `[SCRIPT-LIKELIHOOD]` | likelihood Pantheon/Pantheon+ | exigir compatibilidade com covariâncias |
| `rll_vs_lcdm.py` | `[SCRIPT-COMPARAÇÃO]` | comparação RLL vs ΛCDM | reportar `χ²`, AIC, BIC e penalidade por parâmetros |

---

## 3. Núcleo integrador RAFAELIA

Arquivos que unem ciência, símbolo, espiritualidade, autoria, mercado, proteção e visão total. Devem ser preservados, mas rotulados.

| Arquivo | Regime | Uso recomendado | Observação |
|---|---|---|---|
| `docs/MAPA_RAFAELIA_TOTAL.md` | `[INTEGRADOR-SIMBÓLICO]` | mapa total das camadas RAFAELIA | não usar como prova científica sem extração formal |
| `docs/SUPREMO UNIFICADO.md` | `[INTEGRADOR-SIMBÓLICO]` | síntese ampla / linguagem totalizante | separar símbolo de validação |
| `docs/MAPA FRACTAL.md` | `[SIMBÓLICO-ESTRUTURAL]` | valores, metáforas e mapeamento fractal | útil para navegação conceitual |
| `docs/MAPA CIENTIESPIRITUAL.md` | `[SIMBÓLICO-ESPIRITUAL]` | ponte ciência-espírito | não substituir definições físicas |
| `docs/numeros_rafaelianos/` | `[NUMEROLÓGICO-AUTORAL]` | constantes, harmônicas e números do sistema | declarar como camada autoral até validação externa |

---

## 4. Núcleo histórico, legado e preservação

Arquivos grandes ou duplicados preservados por rastreabilidade. Não devem ser fonte canônica quando existir versão oficial.

| Arquivo | Regime | Uso recomendado | Observação |
|---|---|---|---|
| `docs/README_HISTORICO_INTEGRAL_47d054c.md` | `[HISTÓRICO-LEGADO]` | preservação integral do README anterior | fonte de contexto, não fonte canônica |
| `docs/README_ROOT_LEGACY_ARCHIVE.md` | `[HISTÓRICO-LEGADO]` | arquivo raiz legado | manter para auditoria |
| `news/archive_legacy/` | `[HISTÓRICO-LEGADO]` | versões antigas e duplicatas | usar apenas com rastreabilidade |
| `ANALISE_COMPLETA/` | `[ANÁLISE-SECUNDÁRIA]` | análises de repositório, bibliografia e hierarquias | útil para inventário e revisão |
| `to_Add/FILE_MANIFEST.csv` | `[INVENTÁRIO-TÉCNICO]` | lista caminho/tamanho/extensão/hash | excelente para auditoria de arquivos soltos |
| `docs/DOCUMENTATION_FULL_INVENTORY.md` | `[INVENTÁRIO-TÉCNICO]` | inventário bruto publicado | não define prioridade canônica |

---

## 5. Núcleo de dados, figuras e artefatos

Arquivos que exigem cadeia de custódia: origem, versão, licença, data de acesso, hash, script e resultado reproduzível.

| Caminho | Regime | Uso recomendado | Observação |
|---|---|---|---|
| `data/real/` | `[DADO-REAL]` | dados observacionais reais | exigir origem e versão |
| `data/real/cosmology/` | `[DADO-COSMOLOGIA]` | BAO, H(z), SNe, CMB, fσ8 quando disponível | validar covariâncias e unidades |
| `data/posterior_unified_synth.csv` | `[DADO-SINTÉTICO/POSTERIOR]` | amostras ou resultados sintéticos | não declarar como real validado |
| `results/` | `[RESULTADO]` | saídas de ajuste e comparação | deve apontar script, input e commit |
| `figs/paper/` | `[FIGURA-PAPER]` | gráficos para publicação | deve rastrear script gerador |
| `figs/archive/` | `[FIGURA-LEGADO]` | figuras preservadas | não usar como evidência isolada |

---

## 6. Regra de promoção de status

Um trecho pode subir de regime apenas se cumprir os critérios mínimos:

```text
[SIMBÓLICO] -> [HIPÓTESE]
  exige formulação testável e variável observável.

[HIPÓTESE] -> [MODELO]
  exige equação, parâmetros, domínio de validade e unidade.

[MODELO] -> [VALIDAÇÃO]
  exige dado, script, métrica, baseline, incerteza e reprodutibilidade.

[VALIDAÇÃO] -> [REAL VALIDADO]
  exige dados reais processados, cadeia de custódia, comparação externa e resultados reproduzíveis.
```

---

## 7. Vocabulário recomendado

Use:

```text
modelo candidato
arquitetura de inferência
hipótese operacional
ponte conceitual
métrica a validar
evidência indireta
fonte secundária
necessita fonte primária
status sintético
parcial real em preparação
real validado somente com cadeia completa
```

Evite sem evidência forte:

```text
prova definitiva
supera ΛCDM
revolucionário comprovado
validação total
previsão determinística universal
```

---

## 8. Próxima triagem recomendada

Ordem sugerida para leitura e rotulagem:

1. `docs/FORMULAS_CANONICAS_INDEX.md`
2. `rll_equation_registry.yml`
3. `docs/BOOSTERS.md`
4. `docs/PLANO_ABCD_JWST_AGN_SMBH.md`
5. `docs/VALIDATION_DATA_MATRIX_RLL_MCRP.md`
6. `docs/MAPA_RAFAELIA_TOTAL.md`
7. `docs/README_HISTORICO_INTEGRAL_47d054c.md`
8. `to_Add/FILE_MANIFEST.csv`

---

## 9. Síntese RAFAELIA

```text
Cosmos sem dado = semente.
RLL com equação = modelo.
Catálogo com observação = teste.
Métrica com reprodutibilidade = validação.
Limite explícito = ética científica.
```
