# DHA: Framework Pós-doc para Validação Quantitativa e Publicação

Este documento organiza a transição "heurístico → determinístico" em 7 direções técnicas para submissão científica, com foco em previsões testáveis para DESI/BOSS/SDSS e extensões CLASS/CMB.

## Direção 1 — Formalização Matemática (núcleo analítico)
- Definir observável primário: modulação log-periódica no espectro de potência
  \(P_{obs}(k)=P_{\Lambda CDM}(k)[1 + A_0\cos(\omega\ln(k/k_0))]\).
- Frequência base da rede discreta \(N\): \(\omega=2\pi/\ln N\).
- Harmônico secundário por fator espiral \(\gamma=\sqrt{3}/2\): \(\omega_2=\gamma\omega\).
- Critério de consistência: positividade da matriz de Fisher e estabilidade de inversão.

## Direção 2 — Inferência Estatística (Fisher + MCMC)
- Fisher local para \((A_0,\omega)\) para obter limite de Cramér-Rao.
- MCMC completo para propagar degenerescências com parâmetros barônicos e bias de galáxias.
- Comparar *posterior* de \(\omega\) com valores teóricos da topologia discreta.

## Direção 3 — Dados e Ruído Físico Real (SDSS/BOSS/DESI)
- Substituir proxy por pipeline com covariâncias observacionais reais.
- Incluir janelas, mascaramento e ruído de disparo por bin redshift.
- Executar validação cruzada por *mock catalogs* e *jackknife*.

## Direção 4 — Integração com códigos cosmológicos (CLASS/CAMB)
- Inserir termo oscilatório diretamente na cadeia de transferência em classe EFT/parametrizada.
- Propagar impacto em \(H(z)\), BAO e crescimento \(f\sigma_8\).
- Estender para E-mode do CMB como próximo estágio de falsificabilidade.

## Direção 5 — Reprodutibilidade Computacional e CI
- Testes unitários para frequência base e harmônico secundário.
- Geração automatizada de artefato JSON com previsão determinística.
- Upload de artefatos em GitHub Actions para rastreabilidade de resultados.

## Direção 6 — Rastreabilidade Acadêmica e Governança
- Mapear cada equação para arquivo-fonte, script e resultado numérico.
- Definir checklist mínimo de submissão: dados, código, seed, versão e erros marginais.
- Alinhar com política de revisão interna pré-arXiv.

## Direção 7 — Estratégia de Submissão e Publicação
- Manuscrito A: formalismo e previsões analíticas (ênfase em identificabilidade).
- Manuscrito B: confronto com LSS real e robustez a sistemáticos.
- Manuscrito C: extensão CMB E-mode + discussão de limites de detectabilidade.

## Entregáveis mínimos desta etapa
1. Implementação Fisher determinística para \((A_0,\omega)\).
2. Testes automatizados e workflow CI com artefato versionado.
3. Saída de referência para \(N=1000\), \(A_0=0.02\).
