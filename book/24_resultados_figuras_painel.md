# 24. Resultados — Painel de Figuras

[⬅️ Capítulo anterior](./23_resultados_estatisticos.md) | [📚 Sumário do livro](./README.md) | [Capítulo próximo ➡️](./25_limitacoes_status_atual.md)

Reúne o painel visual canônico para leitura rápida dos resultados.

## Conteúdo incorporado (itens soltos/localizados)
Documentos e artefatos relacionados incorporados nesta etapa:

- figs/paper/
- README.md
- RMR/04_FIGURAS_README.md

## Painel canônico de resultados

### Leitura canônica do painel

A leitura do painel segue o fluxo expansão → crescimento → lentes/escala local → inferência, preservando a rastreabilidade métrica de cada figura para uma conclusão observacional específica.

Resultado a leitura sequencial do painel por blocos métricos para interpretação consistente do modelo é sustentada por [Planck2018, DESI-DR2-2025, BOSS-DR12-2017].

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

## Conclusão observacional por métrica

- **Expansão (`H(z)/H_ΛCDM`, `Δμ`)**: verifica compatibilidade global da história de expansão e estabilidade de resíduos.
  Resultado a conclusão de compatibilidade de expansão por razão `H(z)` e resíduos `Δμ` é sustentada por [Planck2018, PantheonPlus-2022, DESI-DR2-2025].
- **Crescimento (`fσ₈`)**: testa coerência entre background e formação de estrutura em regime linear.
  Resultado a conclusão sobre crescimento estrutural via `fσ₈` como teste de coerência dinâmica é sustentada por [DESI-DR2-2025, eBOSS-DR16-2021, Planck2018].
- **Lensing (`κ`, SIS)**: mede resposta do potencial projetado frente a distribuição efetiva de massa/pressão.
  Resultado a conclusão de lensing por convergência e perfil SIS como validação de potencial projetado é sustentada por [DES-Y3-Lensing-2022, Cluster-Lensing-Review-2021, Planck2018].
- **Inferência posterior**: avalia degenerescências e regiões credíveis para `Ω_s0`, `z_t`, `w_t`.
  Resultado a conclusão inferencial por pós-processamento de parâmetros e degenerescências é sustentada por [DESI-DR2-2025, BOSS-DR12-2017, Planck2018].

## Referências de rastreabilidade

- [Planck2018] Planck Collaboration (2018), *Planck 2018 results. VI. Cosmological parameters*.
- [DESI-DR2-2025] DESI Collaboration (2025), *Data Release 2 cosmological constraints*.
- [BOSS-DR12-2017] Alam et al. (2017), *BOSS DR12 consensus cosmology*.
- [eBOSS-DR16-2021] eBOSS Collaboration (2021), *DR16 cosmological analyses*.
- [PantheonPlus-2022] Scolnic et al. (2022), *Pantheon+ Analysis*.
- [DES-Y3-Lensing-2022] DES Collaboration (2022), *Dark Energy Survey Year 3 lensing results*.
- [Cluster-Lensing-Review-2021] Umetsu (2021), *Cluster lensing review*.

## Notas de consolidação
- Este capítulo funciona como nó canônico para evitar dispersão de arquivos soltos.
- Atualize este capítulo quando novos materiais da mesma temática forem adicionados ao repositório.
