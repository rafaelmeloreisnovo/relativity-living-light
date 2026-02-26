# 24. Resultados — Painel de Figuras

[⬅️ Capítulo anterior](./23_resultados_estatisticos.md) | [📚 Sumário do livro](./README.md) | [Capítulo próximo ➡️](./25_limitacoes_status_atual.md)

Reúne o painel visual canônico para leitura rápida dos resultados.

## Conteúdo incorporado (itens soltos/localizados)
Documentos e artefatos relacionados incorporados nesta etapa:

- figs/paper/
- README.md
- RMR/04_FIGURAS_README.md

## Painel canônico de resultados

### 1) Cosmologia

| Figura (canônica) | Métrica/Conteúdo | Objetivo |
|---|---|---|
| `figs/paper/unified_H_ratio.png` | razão `H(z)/H_ΛCDM` | quantificar desvio na expansão |
| `figs/paper/unified_mu_residuals.png` | resíduos `Δμ(z)` | confronto com SN Ia |
| `figs/paper/unified_fractions.png` | evolução das frações de energia | leitura de transição de componentes |
| `figs/paper/unified_f_and_weff.png` | `f(z)` e `w_eff` | visualizar transição dinâmica |

### 2) Observáveis

| Figura (canônica) | Métrica/Conteúdo | Objetivo |
|---|---|---|
| `figs/paper/unified_growth_fs8.png` | `fσ₈(z)` | teste de crescimento estrutural |
| `figs/paper/fig_kappa_field.png` *(canônico)* | mapa de convergência | assinatura de lensing |

**Nota de canonização:** para o mapa κ, adotar `figs/paper/fig_kappa_field.png` como nome canônico quando coexistir variante legada (ex.: `lensing_kappa_field.png`).

### 3) Escalas locais

| Figura (canônica) | Métrica/Conteúdo | Objetivo |
|---|---|---|
| `figs/paper/rotcurve_NGC_2403.png` | curva de rotação | comparação dinâmica local |
| `figs/paper/cluster_lensing_SIS_unified.png` | lensing em cluster (SIS) | resposta do modelo em potencial projetado |

### 4) Inferência/ajuste

| Figura (canônica) | Métrica/Conteúdo | Objetivo |
|---|---|---|
| `figs/paper/corner_plot_unified_highres.png` | correlação de parâmetros | degenerescências e regiões credíveis |
| `figs/paper/post_1d_Os.png` | posterior 1D de `Ω_s0` | constraints de `Ω_s0`, `z_t`, `w_t` |
| `figs/paper/post_1d_zt.png` | posterior 1D de `z_t` | constraints de `Ω_s0`, `z_t`, `w_t` |
| `figs/paper/post_2d_Os_zt.png` | posterior 2D `Ω_s0 × z_t` | constraints de `Ω_s0`, `z_t`, `w_t` |
| `figs/paper/post_2d_Os_wt.png` | posterior 2D `Ω_s0 × w_t` | constraints de `Ω_s0`, `z_t`, `w_t` |
| `figs/paper/post_2d_zt_wt.png` | posterior 2D `z_t × w_t` | constraints de `Ω_s0`, `z_t`, `w_t` |

## Figuras conceituais avançadas

### Figura: transição de coerência/decoerência do setor de superposição
- **Caminho canônico:** `figs/conceptual/transition_coerencia_decoerencia.png`
- **Legenda técnica curta:** Curva logística `f(z)` explicitando o crossover entre regime coerente e regime de decoerência. O ponto de inflexão em `z_t` e a largura `w_t` parametrizam a transição DE→DM do setor de superposição.
- **Interpretação física e matemática:** Em `E²(a)=...+Ω_s0[f(a)+(1-f(a))a⁻³]+...`, `f→1` recupera comportamento tipo energia escura (`w_eff,sup≈-1`) e `f→0` favorece ramo atrativo com escala `a⁻³`. A figura conecta diretamente `f(z)=1/(1+exp((z-z_t)/w_t))` com a redistribuição dinâmica entre coerência e decoerência.
- **Limite de escopo — Hipótese:** A logística representa um ansatz fenomenológico efetivo; não resolve, por si, o mecanismo microfísico último da perda de coerência.

### Figura: decomposição de contribuições no background unificado
- **Caminho canônico:** `figs/conceptual/background_decomposicao_unificada.png`
- **Legenda técnica curta:** Diagrama de orçamento em `E²(a)` separando termos radiativos (`Ω_r`, `Ω_B0`, `Ω_P0`), matéria (`Ω_m` e ramo `a⁻³` da superposição) e componente coerente do setor fotônico.
- **Interpretação física e matemática:** A figura organiza a soma `Ω_r a⁻⁴ + Ω_m a⁻³ + Ω_Λ + Ω_s0[f(a)+(1-f(a))a⁻³] + Ω_B0 a⁻⁴ + Ω_P0 a⁻⁴`, destacando que setor magnético e setor plasmático entram como correções médias tipo `a⁻⁴` no background e modulam observáveis de precisão sem substituir os componentes principais.
- **Limite de escopo — Analogia:** O diagrama é estrutural e não implica pesos visuais proporcionais à contribuição real em cada redshift.

### Figura: mapa conceitual magneto-plasmático em halos/aglomerados
- **Caminho canônico:** `figs/conceptual/mapa_magnetoplasmatico_halos_clusters.png`
- **Legenda técnica curta:** Esquema de acoplamento entre setor magnético, plasma e coerência fotônica em ambiente de alta magnetização. Resume o papel de temperatura, turbulência e campo `B` na resposta gravitacional efetiva local.
- **Interpretação física e matemática:** Relaciona a hipótese `Ω_s0 → Ω_s0·[1+α_B(Ω_B0 a⁻⁴)^β]` e a densidade plasmática `ρ_plasma=(3/2)nk_B T/c² + B²/(2μ₀c²)` ao deslocamento local coerência/decoerência. Em paralelo, preserva-se no background a lei média tipo `a⁻⁴` para os setores magnético/plasmático.
- **Limite de escopo — Hipótese:** O acoplamento magneto-coerente é hipótese de trabalho para regime de halos e clusters; a calibração de `α_B` e `β` depende de inferência observacional dedicada.

### Figura: cadeia operacional de observáveis falsificáveis
- **Caminho canônico:** `figs/conceptual/cadeia_observaveis_falsificaveis.png`
- **Legenda técnica curta:** Fluxo causal entre parâmetros (`Ω_s0`, `z_t`, `w_t`, `Ω_B0`, `Ω_P0`) e observáveis (`H(z)`, `Δμ(z)`, `fσ₈(z)`, `κ`, `γ`). Enfatiza separação entre assinatura de background e assinatura local em estrutura.
- **Interpretação física e matemática:** A leitura operacional conecta a dinâmica de `E(a)=H(a)/H₀` e da função `f(z)` aos testes estatísticos por χ², AIC e BIC, com foco em previsões comparáveis a dados de expansão, crescimento e lensing.
- **Limite de escopo — Predição operacional:** A figura codifica previsões testáveis no pipeline de ajuste; não constitui derivação fechada de nova microfísica além do formalismo efetivo adotado.

## Regra de nomenclatura (consolidada com `RMR/04_FIGURAS_README.md`)

- Preferir sempre o prefixo `unified_` para resultados do modelo unificado.
- Manter caminhos no padrão absoluto relativo ao repositório: `figs/paper/<arquivo>.png`.
- Em caso de duplicidade de nomes (variantes antigas vs. atuais), declarar explicitamente o arquivo canônico neste capítulo.

## Notas de consolidação
- Este capítulo funciona como nó canônico para evitar dispersão de arquivos soltos.
- Atualize este capítulo quando novos materiais da mesma temática forem adicionados ao repositório.
