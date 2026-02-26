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

## Regra de nomenclatura (consolidada com `RMR/04_FIGURAS_README.md`)

- Preferir sempre o prefixo `unified_` para resultados do modelo unificado.
- Manter caminhos no padrão absoluto relativo ao repositório: `figs/paper/<arquivo>.png`.
- Em caso de duplicidade de nomes (variantes antigas vs. atuais), declarar explicitamente o arquivo canônico neste capítulo.

## Notas de consolidação
- Este capítulo funciona como nó canônico para evitar dispersão de arquivos soltos.
- Atualize este capítulo quando novos materiais da mesma temática forem adicionados ao repositório.

## Referências e convenções terminológicas
- Convenção editorial: usar exclusivamente as formas **DESI DR2**, **BOSS DR12** e **pós-PhD** (quando houver menção à etapa pós-doutoral).
