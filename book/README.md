# Livro Canônico — Relativity Living Light

Trilha principal oficial do acervo consolidado em capítulos sequenciais.

> **Nota canônica:** a formulação canônica do framework vive em `../docs/canonicos/FRAMEWORK_RESUMO_CANONICO.md`.

## Sumário sequencial

- [01. Fundamentos — Visão Geral](./01_fundamentos_visao_geral.md)
- [02. Fundamentos — Status de Dados e Maturidade](./02_fundamentos_status_dados.md)
- [03. Fundamentos — Preservação e Integridade Documental](./03_fundamentos_preservacao_integridade.md)
- [04. Formalismo — Equação Unificada](./04_formalismo_equacao_unificada.md)
- [05. Formalismo — Função de Transição](./05_formalismo_funcao_transicao.md)
- [06. Formalismo — Parâmetros e Componentes](./06_formalismo_parametros_componentes.md)
- [07. Formalismo — Lagrangiano e EFT](./07_formalismo_lagrangiano_eft.md)
- [08. Hipóteses — Hipótese Central](./08_hipoteses_hipotese_central.md)
- [09. Hipóteses — Setor Magnético e Plasmático](./09_hipoteses_setor_magnetico_plasmatico.md)
- [10. Hipóteses — Entropia e Margens de Robustez](./10_hipoteses_entropia_margens.md)
- [11. Metodologia — Pipeline de Validação](./11_metodologia_pipeline_validacao.md)
- [12. Metodologia — Dados Mock](./12_metodologia_dados_mock.md)
- [13. Metodologia — Dados Reais](./13_metodologia_dados_reais.md)
- [14. Metodologia — Notebooks e Scripts](./14_metodologia_notebooks_scripts.md)
- [15. Validação Observacional — Expansão H(z)](./15_validacao_expansao_hz.md)
- [16. Validação Observacional — Supernovas (Δμ)](./16_validacao_supernovas_dmu.md)
- [17. Validação Observacional — Frações de Energia](./17_validacao_fracoes_energia.md)
- [18. Validação Observacional — Crescimento fσ8](./18_validacao_crescimento_fs8.md)
- [19. Validação Observacional — Lentes em Aglomerados](./19_validacao_lentes_aglomerados.md)
- [20. Validação Observacional — Curvas de Rotação](./20_validacao_rotacao_galaxias.md)
- [21. Validação Observacional — DESI/BOSS](./21_validacao_desi_boss.md)
- [22. Validação Observacional — JWST/AGN/SMBH](./22_validacao_jwst_agn_smbh.md)
- [23. Resultados — Estatística e Ajustes](./23_resultados_estatisticos.md)
- [24. Resultados — Painel de Figuras](./24_resultados_figuras_painel.md)
- [25. Limitações — Estado Atual](./25_limitacoes_status_atual.md)
- [26. Limitações — Degenerescências de Parâmetros](./26_limitacoes_degenerescencias.md)
- [27. Limitações — Escopo Científico vs Autoral](./27_limitacoes_escopo_cientifico.md)
- [28. Governança — Índice Mestre](./28_governanca_indice_mestre.md)
- [29. Governança — Inventário Completo](./29_governanca_inventario_completo.md)
- [30. Governança — Releases e Reformas](./30_governanca_releases_reformas.md)
- [31. Roadmap — Curto Prazo](./31_roadmap_curto_prazo.md)
- [32. Roadmap — Médio e Longo Prazo](./32_roadmap_medio_longo_prazo.md)
- [33. Apêndice — Glossário Consolidado](./33_apendice_glossario.md)
- [34. Apêndice — FAQ Consolidado](./34_apendice_faq.md)
- [35. Apêndice — Como Ler o Acervo](./35_apendice_como_ler.md)
- [36. Apêndice — Análises Completas](./36_apendice_analises_completas.md)
- [37. Apêndice — Trilha Autoral RAFAELIA](./37_apendice_trilha_autoral.md)
- [38. Apêndice — Números Rafaelianos](./38_apendice_numeros_rafaelianos.md)
- [39. Apêndice — Referências e Fontes Canônicas](./39_apendice_referencias_fontes.md)

## Estrutura temática
- Fundamentos: capítulos 01–03
- Formalismo: capítulos 04–07
- Hipóteses: capítulos 08–10
- Metodologia e validação observacional: capítulos 11–24
- Limitações: capítulos 25–27
- Governança e roadmap: capítulos 28–32
- Apêndices: capítulos 33–39

## Fluxo operacional canônico do livro

- **Entrada científica:** `../docs/`
- **Dados de entrada e execução:** `../data/`
- **Saídas e tabelas finais:** `../results/`

Referência de organização obrigatória: `../docs/DOCUMENTATION_ORGANIZATION_MASTER.md`.
Os módulos Structure D utilizados pelo fluxo ficam em `../data/pipelines/structure_d/`.
`../to_Add/` permanece somente como histórico de ingestão.


## Execução por GitHub Actions

- Workflow: `.github/workflows/rll-book-data-pipeline.yml`
- A trilha do livro pode ser executada por `book_scope`.
- Os artifacts gerados conectam capítulos, dados, fontes, claims e resultados.
- Status permanece “Parcial real em preparação” até execução real com dados, métricas e reprodutibilidade.
