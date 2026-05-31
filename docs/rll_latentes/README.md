# RLL-LATENTES — matriz técnica para sementes ignoradas em dados científicos

**Status:** especificação documental v0.1, orientada a revisão por pares, sem reivindicação de descoberta empírica até execução reprodutível dos pipelines.

**Escopo:** converter a proposta **Coerência × Amor × Prova** em uma estrutura operacional formal para curadoria de outliers, resíduos, eventos rejeitados e sinais de baixa razão sinal-ruído em física, química, biologia, biomedicina, astrobiologia, neurociência e domínios instrumentais correlatos.

## Navegação interna

- [1. Fronteira epistemológica](#1-fronteira-epistemológica)
- [2. Definição matemática mínima](#2-definição-matemática-mínima)
- [3. Dois ciclos de operação](#3-dois-ciclos-de-operação)
- [4. Expansão por áreas científicas](#4-expansão-por-áreas-científicas)
- [5. Pipeline e dados catalogados](#5-pipeline-e-dados-catalogados)
- [6. Testes estruturais e falsificabilidade](#6-testes-estruturais-e-falsificabilidade)
- [7. Limites de linguagem, analogia e prova](#7-limites-de-linguagem-analogia-e-prova)
- [8. Sete passos futuros integrados](#8-sete-passos-futuros-integrados)

## 1. Fronteira epistemológica

O módulo RLL-LATENTES não deve ser lido como mecanismo de confirmação automática. Ele é uma disciplina de **triagem conservadora**: toda assinatura candidata permanece no estado `hypothesis_candidate` até que existam proveniência, controle instrumental, hipótese nula explícita, teste de falsificação e replicação externa.

A palavra **Amor**, neste contexto, é tecnicamente normalizada como **cuidado operacional com a cadeia de medição**: integridade de aquisição, documentação de calibração, tratamento de incerteza, declaração de vieses, auditoria de seleção e respeito ao dado negativo. A formalização evita metáforas soltas: qualquer imagem heurística só entra no repositório quando puder ser traduzida em variável observável, operador, distribuição, métrica ou critério de rejeição.

## 2. Definição matemática mínima

Para uma semente latente `L`, define-se o índice conservador:

```math
S_L = \frac{C\,I\,P\,E\,R_c}{1 + R_u + A_m + V_b}
```

com `C`, `I`, `P`, `E`, `R_c`, `A_m` e `V_b` em `[0,1]`, e `R_u >= 0`. A leitura recomendada é ordinal e triagem-orientada:

- `S_L < 0.2`: resíduo sem prioridade, salvo valor pedagógico ou controle negativo.
- `0.2 <= S_L < 0.4`: semente fraca; exige melhoria de instrumentação ou metadados.
- `0.4 <= S_L < 0.7`: candidata fértil; recomenda-se replicação, simulação nula e pré-registro.
- `S_L >= 0.7`: candidata robusta para análise dedicada, ainda sem linguagem de descoberta.
- `S_L > 1`: somente possível quando o numerador e o denominador forem calibrados por convenção estendida; não deve ser usado como limiar universal sem validação interlaboratorial.

A versão multidimensional solicitada pode ser representada por um toro operacional:

```math
\mathbf{s}=(u,v,\psi,\chi,\rho,\delta,\sigma)\in\mathbb{T}^7=(\mathbb{R}/\mathbb{Z})^7
```

onde as componentes são coordenadas normalizadas de fase, contexto, proveniência, entropia, estado de pipeline, distorção instrumental e estabilidade semântica. A projeção `ToroidalMap(x)` deve aceitar apenas entradas com metadados de origem, hash, época e incerteza.

## 3. Dois ciclos de operação

### Ciclo A — evidência, falsificação e rollback

1. **Ingestão:** registrar DOI, URL, licença, checksum, versão, data de acesso e caminho local.
2. **Normalização:** converter para schema tabular ou tensorial com unidades explícitas.
3. **Hipótese nula:** definir o modelo de ruído antes do ajuste exploratório.
4. **Score RLL-LATENTES:** calcular `S_L` com intervalos de sensibilidade.
5. **Teste adversarial:** permutar rótulos, quebrar fases, simular ruído, remover lotes e repetir.
6. **Failover:** se dados primários falharem, usar fonte secundária catalogada sem reescrever a conclusão.
7. **Rollback:** preservar artefatos intermediários e registrar motivo de reversão.

### Ciclo B — transferência transdisciplinar controlada

1. **Mapeamento de invariantes:** energia, massa, carga, momento, entropia, informação, estequiometria, conservação topológica, continuidade temporal ou causalidade estatística.
2. **Dicionário de variáveis:** associar cada analogia a variável medida, unidade, sensor e falsificador.
3. **Janela semântica:** bloquear conclusões quando a relação for apenas linguística, estética ou narrativa.
4. **Reverberação harmônica:** permitir análise espectral, autocorrelação, coerência de fase e ressonância somente quando houver série temporal ou campo amostrado.
5. **Replicação cruzada:** exigir pelo menos uma fonte externa ou simulação independente antes de elevar prioridade.

## 4. Expansão por áreas científicas

| Área | Objeto latente admissível | Invariantes e controles | Falsificador forte |
| --- | --- | --- | --- |
| Física quântica | Resíduos em espectros, fases, contagens ou correlações | unitariedade, conservação de energia, estatística de Poisson/binomial, calibração do detector | desaparecimento sob blindagem, randomização de fase ou detector independente |
| Física de partículas | Eventos de baixa energia, canais raros, discrepâncias de reconstrução | luminosidade integrada, eficiência, pile-up, trigger, simulação de fundo | incompatibilidade com controle lateral ou Monte Carlo validado |
| Cosmologia observacional | BAO, supernovas, lentes, CMB, crescimento de estrutura | covariância, seleção, máscara angular, redshift, calibração fotométrica | perda de significância ao trocar likelihood, catálogo ou prior |
| Física clássica e geofísica | Oscilações, anomalias magnéticas, fluidos, modos normais | conservação, viscosidade, condições de contorno, instrumentação ambiental | sumiço ao corrigir temperatura, pressão, posição ou sazonalidade |
| Química | Picos espectrais, cinética residual, estados metaestáveis | balanço de massa/carga, estequiometria, pH, temperatura, solvente | ausência em branco, padrão certificado ou espectrômetro alternativo |
| Biologia molecular | Expressão gênica rara, conformações, variantes estruturais | replicatas, batch effect, controle celular, anotação de linhagem | não replicação em coorte independente ou ensaio ortogonal |
| Biomedicina | Biomarcadores marginais, subfenótipos, efeitos adversos raros | desenho de estudo, consentimento, estratificação, correção múltipla | falha em validação prospectiva ou em endpoint pré-registrado |
| Astrobiologia | Bioassinaturas fracas, atmosferas exoplanetárias, química prebiótica | equilíbrio químico, fotólise, atividade estelar, contaminação | explicação abiótica suficiente ou ausência em novo trânsito/espectro |
| Neurociência | Microestados, conectividade, EEG/MEG/fMRI residual, variação linguística | BIDS, movimento, fisiologia, correção temporal, controle cognitivo | desaparecimento após controle de movimento, batch, idioma ou tarefa |
| Linguagem e cognição | Diferenças acústicas, prosódicas e semânticas entre idiomas | frequência fundamental, envelope, fonemas, semântica vetorial, desenho psicométrico | ausência de efeito em tarefa controlada ou modelo nulo multilíngue |

## 5. Pipeline e dados catalogados

O catálogo operacional está em [`data/rll_latentes/observations.yml`](../../data/rll_latentes/observations.yml). Ele registra fontes recentes e estáveis para DESI, ATLAS/CERN, LVK/GWOSC, Euclid, NASA Exoplanet Archive, Human Cell Atlas, wwPDB e OpenNeuro, além de caminhos de artefatos e comandos de coleta sugeridos.

A regra de contribuição é simples: nenhum item do catálogo implica resultado positivo. Cada fonte apenas define um **alvo reprodutível** para que o índice `S_L` possa ser testado contra dados reais, controles negativos e simulações.

## 6. Testes estruturais e falsificabilidade

Testes mínimos para qualquer nova semente:

- validação de schema do YAML;
- existência de DOI ou URL oficial;
- checksum quando houver download materializado;
- hipótese nula escrita antes da inferência;
- métrica `S_L` acompanhada de intervalo ou sensibilidade;
- teste de permutação ou bootstrap;
- controle negativo;
- trilha de rollback;
- declaração explícita de limitação.

## 7. Limites de linguagem, analogia e prova

Metáforas, parábolas e pontes culturais podem auxiliar a descoberta de perguntas, mas não podem ocupar o lugar de prova. No RLL-LATENTES, uma metáfora só se torna item técnico se for traduzida por:

```math
\text{analogia operacional}=\text{domínio de origem}+\text{invariante}+\text{variável mensurável}+\text{falsificador}+\text{incerteza}
```

Quando qualquer componente faltar, o item deve permanecer como `conceptual_note`, não como `evidence_claim`.


## 8. Sete passos futuros integrados

As sugestões futuras foram consolidadas em [`FUTURE_STEPS.md`](FUTURE_STEPS.md), com uma rota de sete passos para endurecimento de schema, coleta reprodutível, núcleo determinístico de score, modelos nulos, proveniência criptográfica, orquestração fullstack e pacote acadêmico de validação.

A versão YAML desses passos está registrada em [`data/rll_latentes/observations.yml`](../../data/rll_latentes/observations.yml) no bloco `future_steps`, permitindo que automações futuras leiam os mesmos marcos de aceite sem depender apenas do texto narrativo.
