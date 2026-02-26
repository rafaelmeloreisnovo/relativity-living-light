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


## Referências técnicas e bibliográficas

- DESI Collaboration (2024). *DESI 2024 VI: BAO*. JCAP 2025, 021 (painéis de expansão/BAO).
- Alam et al. (BOSS) (2017). *Clustering of galaxies in BOSS DR12* (crescimento e clustering).
- Planck Collaboration (2020). *Planck 2018 results. VI. Cosmological parameters* (baseline CMB/lensing).
- DES Collaboration (2022). *Dark Energy Survey Year 3 results* (weak lensing e clustering).
- Bartelmann, M., & Schneider, P. (2001). *Weak gravitational lensing*. Physics Reports, 340(4-5), 291-472.
- Lelli, McGaugh, & Schombert (2016). *SPARC: Mass Models for 175 Disk Galaxies*. AJ 152, 157 (curvas de rotação).
- Brout et al. (2022). *The Pantheon+ Analysis*. ApJ 938, 110 (resíduos de distância em SN Ia).

**Fontes de consolidação no repositório:** `newadd/03_Descricao_Academica_PhD_Completa.md`, `docs/REFERENCES.md` e `book/39_apendice_referencias_fontes.md`.

## Referências consolidadas (padrão único)

1. Riess, A. G. et al. 2022. "A Comprehensive Measurement of the Local Value of the Hubble Constant with 1 km s−1 Mpc−1 Uncertainty from the Hubble Space Telescope and the SH0ES Team". ApJ, 934(1):L7. DOI:10.3847/2041-8213/ac5c5b.
2. Brout, D. et al. (Pantheon+ Collaboration; primeiro autor: D. Brout). 2022. "The Pantheon+ Analysis: Cosmological Constraints". ApJ, 938(2):110. DOI:10.3847/1538-4357/ac8e04.
3. Abbott, T. M. C. et al. (DES Collaboration; primeiro autor institucional). 2022. "Dark Energy Survey Year 3 results: Cosmological constraints from galaxy clustering and weak lensing". PRD, 105(2):023520. DOI:10.1103/PhysRevD.105.023520.
4. Lelli, F.; McGaugh, S. S.; Schombert, J. M.; Pawlowski, M. S. (SPARC Collaboration). 2016. "One Law to Rule Them All: The Radial Acceleration Relation of Galaxies". ApJ, 836(2):152. DOI:10.3847/1538-4357/836/2/152.
5. DESI Collaboration (Adame et al.; primeiro autor institucional). 2025. "DESI 2024 VI: Cosmological Constraints from the Measurements of Baryon Acoustic Oscillations". JCAP, 2025(02):021. DOI:10.1088/1475-7516/2025/02/021.

---
## Referências e convenções terminológicas
- Convenção editorial: usar exclusivamente as formas **DESI DR2**, **BOSS DR12** e **pós-PhD** (quando houver menção à etapa pós-doutoral).
## Ver também

- [Formalismo base](./04_formalismo_equacao_unificada.md)
- [Hipóteses magneto-plasmáticas](./09_hipoteses_setor_magnetico_plasmatico.md)
- [Validação DESI/BOSS](./21_validacao_desi_boss.md)
- [Validação JWST/AGN/SMBH](./22_validacao_jwst_agn_smbh.md)
Reúne o painel visual canônico para leitura rápida dos resultados e padroniza a interpretação inferencial de cada artefato em `figs/paper/`.

## Links de retorno (fundamentos e validações)

- [Formalismo da equação unificada](./04_formalismo_equacao_unificada.md)
- [Hipóteses do setor magnético-plasmático](./09_hipoteses_setor_magnetico_plasmatico.md)
- [Validação DESI/BOSS](./21_validacao_desi_boss.md)
- [Validação JWST/AGN/SMBH](./22_validacao_jwst_agn_smbh.md)

## Blocos canônicos por artefato (`figs/paper/`)

### `figs/paper/unified_H_ratio.png`
- **Objetivo científico:** testar desvio relativo da expansão em relação ao baseline ΛCDM.
- **Equação/modelo associado:** razão `E(a)/E_ΛCDM(a)` ou `H(z)/H_ΛCDM(z)`.
- **Métrica/estatística testada:** razão por redshift e tendência sistemática acima/abaixo da unidade.
- **Leitura inferencial:** reforça consistência de expansão quando a razão permanece próxima de 1; limitações surgem se houver degenerescência com calibração de `H0` e escala BAO.

### `figs/paper/H_ratio_vs_z.png`
- **Objetivo científico:** apresentar versão legada da razão de expansão para comparação histórica.
- **Equação/modelo associado:** `H(z)/H_ΛCDM(z)`.
- **Métrica/estatística testada:** razão em função de `z`.
- **Leitura inferencial:** compatível com `unified_H_ratio.png`; usar apenas como histórico de compatibilidade (não canônico).

### `figs/paper/ciencia_hz_superposicao.png`
- **Objetivo científico:** visualizar superposição entre curvas de `H(z)` em contexto de apresentação científica.
- **Equação/modelo associado:** `E(a)` na forma operacional de `H(z)`.
- **Métrica/estatística testada:** sobreposição visual de curvas e separação entre cenários.
- **Leitura inferencial:** reforça intuição sobre intervalo de redshift em que o desvio emerge; limita por depender de leitura visual e não de ajuste formal.

### `figs/paper/hz_superposicao.png`
- **Objetivo científico:** variante legada da superposição de `H(z)`.
- **Equação/modelo associado:** `E(a)`.
- **Métrica/estatística testada:** separação visual de curvas.
- **Leitura inferencial:** mantém utilidade ilustrativa; registrar como compatibilidade com `ciencia_hz_superposicao.png`.

### `figs/paper/unified_mu_residuals.png`
- **Objetivo científico:** confrontar o modelo com distância de luminosidade de SN Ia.
- **Equação/modelo associado:** `Δμ(z) = μ_modelo(z) - μ_ΛCDM(z)`.
- **Métrica/estatística testada:** resíduos de módulo de distância versus `z`.
- **Leitura inferencial:** reforça aderência ao conjunto SN quando resíduos ficam centrados em zero; limita por degenerescência entre parâmetros de transição e calibração fotométrica.

### `figs/paper/mu_residuals.png`
- **Objetivo científico:** disponibilizar versão legada do painel de resíduos de supernovas.
- **Equação/modelo associado:** `Δμ(z)`.
- **Métrica/estatística testada:** resíduo por redshift.
- **Leitura inferencial:** consistente com `unified_mu_residuals.png`; manter apenas como nota de compatibilidade.

### `figs/paper/unified_fractions.png`
- **Objetivo científico:** acompanhar evolução das frações energéticas entre regimes cosmológicos.
- **Equação/modelo associado:** `Ω_i(z)` para componentes efetivos e padrão.
- **Métrica/estatística testada:** trajetórias relativas das frações e cruzamentos de dominância.
- **Leitura inferencial:** reforça narrativa de transição entre setores; limita por degenerescências em componentes com evolução semelhante em certas faixas de `z`.

### `figs/paper/density_evolution_sup.png`
- **Objetivo científico:** variante visual da evolução de densidades para leitura de suporte.
- **Equação/modelo associado:** `Ω_i(z)` / `ρ_i(z)` normalizados.
- **Métrica/estatística testada:** evolução comparativa por componente.
- **Leitura inferencial:** utilidade de compatibilidade com `unified_fractions.png`; não substituir figura canônica.

### `figs/paper/unified_f_and_weff.png`
- **Objetivo científico:** exibir transição dinâmica em `f(z)` e resposta de `w_eff(z)`.
- **Equação/modelo associado:** `f(z)` e `w_eff = p_eff/ρ_eff`.
- **Métrica/estatística testada:** mudança de regime e posição da transição (`z_t`).
- **Leitura inferencial:** reforça mecanismo físico proposto; limita por correlação entre largura de transição e amplitude efetiva.

### `figs/paper/f_transition.png`
- **Objetivo científico:** versão legada focada na transição `f(z)`.
- **Equação/modelo associado:** `f(z)`.
- **Métrica/estatística testada:** forma da transição e inclinação.
- **Leitura inferencial:** complementar para compatibilidade histórica com `unified_f_and_weff.png`.

### `figs/paper/unified_growth_fs8.png`
- **Objetivo científico:** validar crescimento de estrutura frente a RSD.
- **Equação/modelo associado:** `fσ8(z)`.
- **Métrica/estatística testada:** ajuste da curva prevista aos pontos observacionais e barras de erro.
- **Leitura inferencial:** reforça consistência de crescimento quando acompanha tendência dos dados; limita por degenerescência com normalização de potência (`σ8`) e vieses de traçadores.

### `figs/paper/fig_kappa_field.png`
- **Objetivo científico:** mapear assinatura de lensing no campo de convergência.
- **Equação/modelo associado:** `κ(θ)` / potencial de lente projetado.
- **Métrica/estatística testada:** morfologia espacial e contraste de convergência.
- **Leitura inferencial:** reforça coerência do setor gravitacional projetado; limita por degenerescência massa-folha e reconstrução de mapa.

### `figs/paper/cluster_lensing_SIS_unified.png`
- **Objetivo científico:** testar lensing de cluster com aproximação SIS.
- **Equação/modelo associado:** perfil SIS para potencial projetado e `κ` efetivo.
- **Métrica/estatística testada:** alinhamento qualitativo de regiões de amplificação/arcos com o perfil assumido.
- **Leitura inferencial:** reforça viabilidade em escala de cluster como demonstração; limita por simplificação do perfil e ausência de subestrutura realista.

### `figs/paper/rotcurve_NGC_2403.png`
- **Objetivo científico:** verificar dinâmica local via curva de rotação galáctica.
- **Equação/modelo associado:** velocidade circular `v_c(r)` sob potencial efetivo do modelo.
- **Métrica/estatística testada:** resíduo radial e aderência do perfil previsto aos dados observados.
- **Leitura inferencial:** reforça capacidade de reproduzir cinemática local; limita por degenerescência barions-halo e incertezas em inclinação/distância.

### `figs/paper/corner_plot_unified_highres.png`
- **Objetivo científico:** resumir correlações e regiões credíveis da inferência conjunta.
- **Equação/modelo associado:** posterior multivariada `P(θ|dados)` para parâmetros cosmológicos.
- **Métrica/estatística testada:** contornos 68/95%, inclinação de elipses e largura marginal.
- **Leitura inferencial:** reforça região viável de parâmetros; limita por degenerescências estruturais entre parâmetros de transição e normalizações.

### `figs/paper/post_1d_Os.png`
- **Objetivo científico:** quantificar restrição univariada de `Ω_s0`.
- **Equação/modelo associado:** marginal `P(Ω_s0|dados)`.
- **Métrica/estatística testada:** posição do pico, largura e caudas.
- **Leitura inferencial:** reforça faixa preferida para `Ω_s0`; limita por correlação implícita com `z_t` e `w_t`.

### `figs/paper/post_1d_zt.png`
- **Objetivo científico:** quantificar restrição univariada de `z_t`.
- **Equação/modelo associado:** marginal `P(z_t|dados)`.
- **Métrica/estatística testada:** moda/mediana e dispersão posterior.
- **Leitura inferencial:** reforça redshift de transição preferido; limita por sensibilidade ao conjunto de probes incluído.

### `figs/paper/post_2d_Os_zt.png`
- **Objetivo científico:** avaliar correlação entre `Ω_s0` e `z_t`.
- **Equação/modelo associado:** marginal bivariada `P(Ω_s0, z_t|dados)`.
- **Métrica/estatística testada:** orientação e excentricidade dos contornos.
- **Leitura inferencial:** explicita degenerescência amplitude-transição; informa direção de quebra de degenerescência com novos dados.

### `figs/paper/post_2d_Os_wt.png`
- **Objetivo científico:** avaliar correlação entre `Ω_s0` e `w_t`.
- **Equação/modelo associado:** marginal bivariada `P(Ω_s0, w_t|dados)`.
- **Métrica/estatística testada:** inclinação de contorno e área credível.
- **Leitura inferencial:** reforça acoplamento entre fração setorial e largura da transição; limita por baixa ortogonalidade estatística.

### `figs/paper/post_2d_zt_wt.png`
- **Objetivo científico:** avaliar correlação entre escala temporal (`z_t`) e forma (`w_t`) da transição.
- **Equação/modelo associado:** marginal bivariada `P(z_t, w_t|dados)`.
- **Métrica/estatística testada:** contornos credíveis e possível multimodalidade.
- **Leitura inferencial:** reforça estrutura de transição compatível com dados; limita por degenerescência de forma-tempo.

### `figs/paper/fig_degeneracy.png`
- **Objetivo científico:** destacar explicitamente padrões de degenerescência entre parâmetros.
- **Equação/modelo associado:** projeções da posterior em subespaços selecionados.
- **Métrica/estatística testada:** alongamento de contornos e direções mal condicionadas.
- **Leitura inferencial:** reforça transparência sobre limitações de identificabilidade; orienta quais probes adicionais têm maior poder de quebra de degenerescência.

### `figs/paper/fig_pipeline.png`
- **Objetivo científico:** documentar pipeline de inferência/validação do modelo.
- **Equação/modelo associado:** encadeamento `E(a) → observáveis (Δμ, fσ8, κ, v_c) → posterior`.
- **Métrica/estatística testada:** consistência de fluxo e rastreabilidade metodológica.
- **Leitura inferencial:** reforça reprodutibilidade do processo; limita por não ser teste quantitativo direto.

### `figs/paper/fig_quadratic.png`
- **Objetivo científico:** inspecionar componente/quebra quadrática no comportamento do ajuste.
- **Equação/modelo associado:** termo quadrático efetivo no ajuste (dependente da parametrização adotada).
- **Métrica/estatística testada:** curvatura do ajuste e desvio do caso linear.
- **Leitura inferencial:** reforça sensibilidade a não linearidades; limita por dependência de parametrização específica.

### `figs/paper/mock_H_fit.png`
- **Objetivo científico:** validar recuperação de `H(z)` em dados sintéticos.
- **Equação/modelo associado:** ajuste de `E(a)` em mock controlado.
- **Métrica/estatística testada:** qualidade de ajuste, resíduo e recuperação dos parâmetros injetados.
- **Leitura inferencial:** reforça robustez do pipeline em cenário controlado; limita por gap entre mock idealizado e sistemáticas reais.

### `figs/paper/mock_SN_fit.png`
- **Objetivo científico:** validar recuperação de `Δμ/μ` em catálogo sintético de supernovas.
- **Equação/modelo associado:** distância de luminosidade e módulo de distância simulados.
- **Métrica/estatística testada:** erro de recuperação e dispersão residual em mock.
- **Leitura inferencial:** reforça consistência da camada fotométrica do pipeline; limita por simplificação de covariâncias observacionais.

### `figs/paper/RLL_validacao_real.png`
- **Objetivo científico:** consolidar validação do modelo em dados reais em um painel único.
- **Equação/modelo associado:** síntese multi-observável (`E(a)`, `Δμ`, `fσ8`, `κ`, dinâmica local).
- **Métrica/estatística testada:** consistência global entre ajustes e assinaturas observacionais.
- **Leitura inferencial:** reforça visão integrada do desempenho; limita por condensar múltiplas métricas em uma única peça gráfica.

### `figs/paper/rotation_curves_sup.png`
- **Objetivo científico:** painel suplementar de curvas de rotação em múltiplos sistemas.
- **Equação/modelo associado:** família de `v_c(r)`.
- **Métrica/estatística testada:** resíduos por objeto e comparação entre perfis.
- **Leitura inferencial:** reforça reprodutibilidade da dinâmica local além de um caso individual; limita por heterogeneidade de qualidade dos dados entre galáxias.

### `figs/paper/unified_entropy_Hratio.png`
- **Objetivo científico:** relacionar variação entropia-efetiva com razão de expansão.
- **Equação/modelo associado:** acoplamento de termo entrópico com `H/H_ΛCDM`.
- **Métrica/estatística testada:** coevolução entropia × razão de expansão.
- **Leitura inferencial:** reforça ligação entre setor entrópico e expansão; limita por dependência da modelagem fenomenológica da entropia.

### `figs/paper/unified_entropy_dmu.png`
- **Objetivo científico:** relacionar termo entrópico com resíduos de distância.
- **Equação/modelo associado:** acoplamento entrópico refletido em `Δμ(z)`.
- **Métrica/estatística testada:** tendência de `Δμ` sob variação entrópica.
- **Leitura inferencial:** reforça consistência fenomenológica entre expansão e distância; limita por degenerescência com calibração SN.

## Nomenclatura canônica e compatibilidade legada

- Nomes canônicos priorizam o prefixo `unified_` quando há versão consolidada do mesmo conteúdo.
- `fig_kappa_field.png` é o nome canônico para o mapa de convergência `κ`.
- Variantes legadas permanecem somente como referência de compatibilidade histórica, sem substituir o artefato canônico na interpretação principal.

## Síntese final — consistência cruzada entre probes

A leitura conjunta do painel indica **consistência cruzada entre expansão (`E(a)`/`H(z)`), crescimento (`fσ8`), lensing (`κ`) e dinâmica local (`v_c(r)`)**: as figuras de expansão e distância preservam coerência de fundo, o bloco de crescimento mantém compatibilidade com estrutura em larga escala, o bloco de lensing confirma resposta do potencial projetado e as curvas de rotação sustentam aderência em escalas galácticas. Em paralelo, os painéis de posterior e degenerescência mostram que a concordância é condicionada por correlações paramétricas (especialmente envolvendo `Ω_s0`, `z_t` e `w_t`), delimitando onde novos dados quebram degenerescências e ampliam poder inferencial.
