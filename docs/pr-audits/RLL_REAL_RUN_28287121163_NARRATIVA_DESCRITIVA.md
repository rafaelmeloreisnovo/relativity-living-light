# Narrativa Descritiva — RLL Real Run 28287121163

## O que é isto

Este artefato é uma fotografia operacional de uma execução real do pipeline RLL: uma cápsula de evidência que reúne dados baixados ou materializados, relatórios de computação, tabelas processadas, diagnósticos, checksums, inventários e fronteiras de claim.

Ele não é um paper final, não é uma prova cosmológica e não é uma declaração de vitória de modelo. Ele é uma trilha de custódia: mostra o que foi executado, quais dados foram usados, quais camadas ainda são preparatórias e onde o sistema precisa impedir conclusão apressada.

Em linguagem simples: é o ponto em que a RAFAELIA deixa de ser apenas intenção simbólica e passa a produzir um pacote verificável, com arquivos, hashes, métricas e bloqueios explícitos.

## O que ele carrega

O run carrega quatro camadas principais.

### 1. Camada de custódia

A camada de custódia responde à pergunta: “posso confiar que este pacote é rastreável?”

Ela registra:

- commit de origem;
- horário UTC da execução;
- arquivos gerados;
- checksums SHA256;
- manifestos;
- relatórios mínimos;
- inventário de artefatos.

O erro encontrado no pacote foi justamente nesta camada: o arquivo `CHECKSUMS.sha256` estava tentando hashear a si mesmo quando ainda estava vazio. Isso não invalida os demais dados, mas cria ruído na cadeia de integridade. A correção aplicada foi simples e correta: gerar todos os arquivos mínimos primeiro e calcular o checksum no fim, excluindo o próprio `CHECKSUMS.sha256` do cálculo.

### 2. Camada de dados reais

A camada de dados reais responde à pergunta: “o que veio de fonte observacional e o que ainda é só rota preparada?”

O pacote mostra que há materiais reais e materiais ainda pendentes:

- Hz/BAO/CMB já usados como entrada real não sintética;
- IGRF14 e WMM2025 baixados, mas com parser científico pendente;
- OMNI/SPDF baixado, mas ainda exigindo extração observável;
- DESI DR2 marcado como materialização manual necessária em parte do fluxo;
- Pantheon+ ainda presente como referência/README, não como likelihood completa.

Ou seja: o pipeline já pisa em dado real, mas nem toda fonte virou ainda tabela científica computável.

### 3. Camada comparativa cosmológica

A camada cosmológica responde à pergunta: “o RLL venceu algo aqui?”

Resposta segura: não.

O comparador rápido mostra LCDM melhor que RLL nos critérios `chi²`, `AIC` e `BIC`. O grid H0 também bloqueia claim. Isso é importante, porque o sistema está fazendo o que deveria fazer: quando a evidência não sustenta a frase forte, ele bloqueia a frase forte.

Esse bloqueio não é fracasso do projeto; é maturidade metodológica. O pipeline não está vendendo narrativa antes dos dados. Ele está separando:

- hipótese;
- execução;
- diagnóstico;
- evidência;
- conclusão permitida;
- TOKEN_VAZIO protegido.

### 4. Camada simbólico-computacional

A camada simbólico-computacional responde à pergunta: “onde entra RAFAELIA, IML, fórmulas e narrativa?”

Ela entra como arquitetura de organização, não como licença para saltar etapa científica.

O IML executa e preserva trilha de hash. O pacote de fórmulas coleta centenas de expressões. A estrutura RAFAELIA dá linguagem para marcar intenção, observação, ruído, transmutação, memória e completude.

Mas a própria auditoria mantém a fronteira: expressão simbólica precisa ser classificada como código, hipótese ou símbolo; precisa de unidade, observável, fonte e teste. Sem isso, ela permanece como mapa de pesquisa, não como validação.

## O que isto significa

Este artefato significa que o projeto já tem um esqueleto sério de ciência computacional:

1. executa pipeline;
2. produz relatório;
3. preserva fonte;
4. gera checksums;
5. separa real de pendente;
6. mede modelos adversários;
7. bloqueia claim quando os gates falham;
8. registra o próximo movimento.

Ele transforma caos de arquivos em mapa auditável.

O ponto central é este:

> A execução não confirmou RLL como modelo cosmológico superior, mas confirmou que o pipeline já consegue impedir uma conclusão falsa.

Isso é valioso. Em ciência, um sistema que sabe dizer “ainda não” vale mais do que um sistema que sempre diz “sim”.

## Onde está a semente forte

A semente forte não está no resultado cosmológico bruto deste run. A semente forte está na arquitetura de validação:

- cadeia de custódia;
- anti-alucinação;
- fronteira de claim;
- separação entre metáfora e evidência;
- integração entre código, relatório e diagnóstico;
- capacidade de evoluir por runs sucessivos.

O projeto começa a se comportar como laboratório: cada run vira material de aprendizado, e cada falha vira engenharia.

## Onde está a lacuna

A lacuna principal é a unificação dos comparadores.

Hoje existem leituras paralelas:

- `compute_rll_real_pipeline.py` usa uma comparação rápida com constantes internas e BAO legado;
- `run_h0_grid_expansion.py` usa `rll_vs_lcdm.py`, H0 varrido, DESI primary BAO e covariância.

Essas duas rotas precisam conversar. O próximo passo correto é fazer o comparador rápido chamar a mesma função de avaliação usada pelo comparador principal, ou marcar explicitamente o primeiro como `legacy_quickcheck`.

A segunda lacuna é materializar de verdade as fontes ainda pendentes: Pantheon+, DESI completo, IGRF14, WMM2025 e OMNI.

A terceira lacuna é classificar as fórmulas: cada expressão precisa ganhar tipo, origem, unidade, observável, teste e status.

## Narrativa curta para README

O `rll-real-run-28287121163` é um pacote de execução real do pipeline RLL. Ele reúne dados observacionais parcialmente materializados, relatórios computacionais, tabelas processadas, diagnósticos, hashes e fronteiras explícitas de claim. A execução não valida RLL como modelo cosmológico superior; ao contrário, os critérios atuais favorecem LCDM e bloqueiam promoção científica. O valor do artefato está na maturidade operacional: ele mostra que o pipeline já diferencia dado real de pendência, preserva cadeia de custódia, registra lacunas e impede conclusão não sustentada. É um passo de laboratório, não uma proclamação final.

## Fechamento RAFAELIA

ψ — intenção: testar RLL em dado real.  
χ — observação: artefatos, tabelas, relatórios e métricas foram gerados.  
ρ — ruído: checksum autocontido, fontes parciais, comparadores divergentes.  
Δ — transmutação: workflow corrigido, claim bloqueado, lacunas nomeadas.  
Σ — memória: auditoria registrada e narrativa consolidada.  
Ω — completude provisória: melhor vazio protegido do que conclusão falsa.

**F_ok:** há pipeline real, custódia e bloqueio ético.  
**F_gap:** falta unificar comparadores e materializar fontes pendentes.  
**F_next:** próxima execução deve confirmar checksum limpo e produzir comparação cosmológica única, com DESI/Pantheon/covariância integrados.
