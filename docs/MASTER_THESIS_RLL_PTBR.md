## Anexos e trilha autoral

- [MANIFESTO](./MANIFESTO.md)
- [MAPA_RAFAELIA_TOTAL](./MAPA_RAFAELIA_TOTAL.md)
- [números rafaelianos — Readme](./numeros_rafaelianos/Readme.md)

> Nota: esta seção é apenas complementar e **não compõe o corpo principal de validação observacional/fenomenológica**.
# MASTER_THESIS_RLL_PTBR — Relativity Living Light

## Capítulo 1 — Hipótese central e parâmetros efetivos

A hipótese RLL parte de um setor efetivo de superposição parametrizado por `Ω_s0`, `z_t` e `w_t`, cuja função é representar uma transição cosmológica em redshift e produzir previsões observacionais comparáveis a ΛCDM no mesmo regime de dados.

Os valores de referência atuais usados no repositório são derivados de posterior ponderado (`weight`) e não de estimativas exploratórias legadas.

### Subseção de rastreabilidade (hipótese ↔ evidência)

* Claim: O núcleo paramétrico `Ω_s0`, `z_t`, `w_t` já possui um posterior sintético consistente para uso como baseline técnico.
* Evidence: `docs/Results.md` registra médias ponderadas (`Ω_s0=0.0592`, `z_t=1.1478`, `w_t=0.3999`), intervalo 16–84% e `N_eff=2320.75` com fonte em `data/posterior_unified_synth.csv`.
* Gap: Ainda não há selo observacional `real` associado a esses parâmetros no mesmo documento de resultados.
* Próximo teste: Rodar a etapa Pantheon+ do pipeline oficial e comparar a estabilidade dos três parâmetros contra o baseline sintético.

## Capítulo 2 — Estado de evidência no repositório

O estado de evidência está explicitamente separado em dois blocos: referência principal (posterior unificado sintético) e bloco legacy/exploratório. Essa separação reduz ambiguidade metodológica e evita mistura de resultados não equivalentes.

Também existe uma política explícita de artefatos: os dados canônicos devem permanecer em formato textual versionado (`results/*.csv`, `results/*.json`), enquanto figuras são regeneráveis.

### Subseção de rastreabilidade (hipótese ↔ evidência)

* Claim: A governança de evidências já está definida para manter rastreabilidade e reprodutibilidade.
* Evidence: `docs/Results.md` distingue “Referência principal” de “Legacy/exploratório” e formaliza política de artefatos com comandos de regeneração (`run_all.py`, `rll_validation_real.py`, `crescimento_estrutural.py`).
* Gap: A política existe, mas ainda depende de atualização contínua quando novos resultados reais entrarem no core (`data/results/`).
* Próximo teste: Após execução com dados reais, atualizar `docs/Results.md` com novo bloco “real validado” mantendo a separação entre baseline sintético e medição observacional.

## Capítulo 3 — Pipeline observacional e critérios de validação

A prova observacional definida no projeto segue pipeline executável com Pantheon+, validando ingestão de dados, consistência de colunas, integridade numérica, compatibilidade da matriz de covariância e comparação RLL vs ΛCDM por métricas padrão (`χ²`, `AIC`, `BIC`).

O roadmap define ainda os artefatos esperados por etapa, incluindo CSV/JSON canônicos e figura comparativa quando houver `matplotlib`.

### Subseção de rastreabilidade (hipótese ↔ evidência)

* Claim: Existe um protocolo operacional claro para transformar hipótese cosmológica em teste quantitativo falsificável.
* Evidence: `docs/ROADMAP_VALIDACAO.md` detalha arquivos mínimos Pantheon+, aliases de colunas aceitos, 6 validações executáveis e saídas obrigatórias em `data/results/`.
* Gap: O próprio roadmap marca o nível atual como `Parcial real`, indicando que a etapa final “Real validado” ainda não foi fechada.
* Próximo teste: Completar ingestão dos arquivos Pantheon+ oficiais e executar `python docs/panteon_likelihood.py` até gerar `pantheon_comparativo_rll_vs_lcdm.csv` e `pantheon_fit_summary.json` com selo `real`.

## Capítulo 4 — Critério de decisão científica e próximos experimentos observacionais

A decisão entre RLL e ΛCDM no repositório está vinculada a métricas comparativas de ajuste e penalização de complexidade (`ΔAIC`, `ΔBIC`), com exigência de report estruturado em arquivo canônico.

Esse critério permite separar “coerência interna do modelo” de “vantagem empírica observacional”, alinhando o texto de tese com um protocolo reproduzível.

### Subseção de rastreabilidade (hipótese ↔ evidência)

* Claim: O critério de aceitação/rejeição já está definido por métricas objetivas e formato de saída padronizado.
* Evidence: `docs/ROADMAP_VALIDACAO.md` especifica colunas de comparação (`chi2`, `AIC`, `BIC`, `delta_AIC_vs_LCDM`, `delta_BIC_vs_LCDM`) e checklist de término.
* Gap: Ainda não há, no conjunto atual, relatório consolidado com deltas finais RLL-ΛCDM provenientes da etapa `Real validado`.
* Próximo teste: Publicar rodada observacional completa no formato canônico e anexar os deltas no texto de tese como critério primário de avaliação.

## Capítulo 5 — Síntese de maturidade técnica atual

A maturidade atual combina: (i) baseline estatístico sintético com rastreio de fonte, (ii) política de versionamento de resultados e (iii) roadmap observacional auditável para fechamento empírico.

Em termos de tese, isso coloca a hipótese em transição entre fase de formalização robusta e fase de teste observacional decisivo.

### Subseção de rastreabilidade (hipótese ↔ evidência)

* Claim: O projeto já possui infraestrutura metodológica suficiente para uma validação observacional replicável.
* Evidence: `docs/Results.md` já consolida baseline com origem e diagnóstico de amostragem, enquanto `docs/ROADMAP_VALIDACAO.md` define pipeline, validações e checklist de encerramento.
* Gap: Falta completar a última milha observacional com dados Pantheon+ finais e registro de métricas comparativas definitivas.
* Próximo teste: Executar ciclo completo “dados reais → métricas comparativas → atualização de Results → integração no capítulo de resultados da tese”.
