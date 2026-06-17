# SEGUE 1 — Convergencia Cientifica e Falsificabilidade RLL

Status: entrega operacional v0.1
Data: 2026-06-16
Base: SEGUE_5_PROTOCOLO_OPERACIONAL_RLL.md

## 1. Resultado da varredura inicial

Nao havia pull request aberto no momento da varredura operacional.

Consequencia:

- nao houve merge automatico;
- nao houve promocao de branch sem revisao;
- o caminho coerente foi registrar esta entrega diretamente no main;
- branches pendentes so devem ser promovidos quando adicionarem upgrade valido, pequeno, auditavel e reversivel.

## 2. Ancora canonica do ciclo

Arquivos centrais para qualquer proximo passo serio:

1. docs/CANONICAL_SOURCES.md
2. docs/canonicos/00_COMO_LER.md
3. docs/canonicos/13_EPISTEMOLOGIA_RAFAELIA_RLL.md
4. docs/canonicos/14_MODELO_COSMOLOGICO_RLL.md
5. docs/canonicos/21_MODELO_VETORIAL_INFORMACIONAL.md
6. knowledge_ecosystem/schemas/info_prime.schema.json
7. src/rll/latentes.py

Regra:

RAW_TEXT -> CLAIMS -> VETORES -> METRICAS -> INFERENCIA -> PROVA

Proibido:

TEXTO -> RESUMO -> ASSOCIACAO -> TEORIA

## 3. Regra para merge de branches futuras

Um branch so deve ser integrado ao main quando satisfizer:

- nao contradiz docs/canonicos/13_EPISTEMOLOGIA_RAFAELIA_RLL.md;
- nao promove metafora para CLAIM_ALLOWED;
- nao cria formula sem unidade, dominio e falsificador;
- nao substitui TOKEN_VAZIO por chute;
- melhora documento canonico, referencia, codigo, teste ou rastreabilidade;
- tem patch pequeno ou revisao claramente auditavel.

Estados possiveis:

- MERGE_OK: upgrade pequeno, coerente e revisivel.
- HOLD_REVIEW: precisa leitura de dependencia.
- TOKEN_VAZIO: nao ha ancora suficiente.
- REJECT_OVERCLAIM: promove claim alem da evidencia.
- SPLIT_REQUIRED: mudanca grande demais para um unico merge.

## 4. Convergencia cientifica: definicao operacional

Convergencia cientifica no RLL nao significa misturar todas as areas.

Significa:

metafora -> modelo -> variavel -> medida -> incerteza -> falsificador -> referencia -> reproducibilidade

A convergencia verdadeira ocorre quando linguagens diferentes apontam para a mesma estrutura auditavel sem apagar suas diferencas.

Exemplo:

- parabola mostra intuicao;
- fisica define grandeza;
- estatistica estima incerteza;
- codigo executa teste;
- bibliografia localiza ancestralidade;
- claim_state limita a conclusao.

## 5. Falsificabilidade academica seria

Toda hipotese RLL deve ter pelo menos um falsificador:

- dado que poderia contradizer;
- modelo adversario;
- criterio de decisao;
- limiar estatistico;
- fonte de dados;
- unidade e dominio;
- condicao para regressao a TOKEN_VAZIO.

Regra curta:

Se nao pode falhar, ainda nao e ciencia testavel.

## 6. Bibliografia minima seria para proximos ciclos

A proxima escrita academica deve priorizar fontes estruturantes:

- Popper 1959: falsificabilidade e logica da descoberta cientifica.
- Shannon 1948: informacao e comunicacao.
- Fisher 1925 e Cramer 1946: estimacao e limite de incerteza.
- Jaynes 2003 e Gelman et al. 2014: inferencia bayesiana.
- Chandrasekhar 1950; Rybicki e Lightman 1979: transferencia radiativa.
- Hogg 1999: medidas de distancia em cosmologia.
- Planck Collaboration 2020: parametros cosmologicos de referencia.
- DESI 2024/2025: BAO e energia escura dinamica como adversario serio.
- Abbott et al. 2017: astronomia multi-mensageira em GW170817.
- DataCite, FAIR, CFF e ICMJE: metadados, citacao, responsabilidade e autoria.

## 7. Hotfixes recomendados para o proximo Segue

Prioridade P0:

- revisar docs/canonicos/21_MODELO_VETORIAL_INFORMACIONAL.md;
- corrigir a leitura de H_claim = 0 como certeza absoluta;
- alinhar S_L > 0.7 com src/rll/latentes.py, onde o status e requires_independent_replication;
- trocar monotonicidade rigida da entropia por regra mais honesta: evidencia pode reduzir incerteza em expectativa, mas contradicoes podem aumentar H_claim e exigir regressao de claim_state.

Prioridade P1:

- criar tabela de modelos adversarios para RLL: LCDM, wCDM, CPL/w0waCDM, IDE, scalar field, modified gravity quando aplicavel.
- listar quais datasets podem falsificar cada claim.

Prioridade P2:

- transformar bibliografia curta em BibTeX ou references.md formal.

## 8. Parabola curta

Cinco mestres olhavam uma estrela distante.

O poeta viu uma lembranca de fogo.
O fisico mediu o espectro.
O estatistico mediu a duvida.
O programador executou o teste.
O guardiao escreveu TOKEN_VAZIO onde faltava prova.

Quando todos falaram juntos, nao nasceu confusao.
Nasceu convergencia.

Porque cada um ficou no seu nivel:
parabola, modelo, medida, codigo e limite.

## 9. R3

F_ok = Segue 1 registrado com ancora canonica, regra de merge e plano de falsificabilidade.
F_gap = nenhum PR aberto foi encontrado para merge; branches futuras exigem revisao caso a caso.
F_next = Segue 2 deve aplicar hotfix no documento 21: entropia, CLAIM_ALLOWED e S_L.
