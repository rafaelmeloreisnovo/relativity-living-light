# README de Advertência — DOI, Cronologia e Integridade Probatória

## Objetivo
Este documento registra, de forma explícita, como interpretar cronologia e força de prova entre GitHub e DOI de referência do projeto.

## DOI de referência
- DOI citado: `10.5281/zenodo.17188137`
- Função: preservação/citação de artefatos científicos no Zenodo.

## Regra de interpretação
1. **Fonte primária de cronologia de desenvolvimento:** histórico GitHub (commits, branches, tags, releases).
2. **Fonte primária de metadado de DOI:** Zenodo/DataCite (quando exposto publicamente em estado Findable).
3. **Sem metadado direto público do DOI:** usar linguagem prudente, distinguindo claramente:
   - prova direta (metadado oficial),
   - prova indiciária (posição estrutural, inferências, interpolação).

## Declaração prática
Quando houver divergência de percepção temporal, adotar a seguinte ordem:
- (a) Git log para desenvolvimento e autoria incremental;
- (b) DOI para arquivamento/citação;
- (c) relatório técnico explicitando limites de inferência para data exata do DOI.

## Nota de governança
Este arquivo complementa `README.md` e `LICENSE.md` para reduzir ambiguidade jurídica, acadêmica e comunicacional.


## Estimativa indiciária de datas (supostas)
Sem metadado direto público do DOI, só é possível estimar uma data **suposta** por posição estrutural entre registros públicos vizinhos.

Âncoras públicas consideradas:
- Registro 17101188: **11/09/2025**
- Registro 17471910: **29/10/2025**
- Alvo: 17188137

Cálculo linear indiciário:
- \(\Delta_{total}=17471910-17101188=370722\)
- \(\Delta_{alvo}=17188137-17101188=86949\)
- proporção p = 86949/370722 ≈ 0.2345
- intervalo entre âncoras: **48 dias**
- avanço estimado: 48 × 0.2345 ≈ 11.26 dias

**Data central estimada (não oficial): ~22/09/2025.**

### Linguagem recomendada
- Afirmação forte e segura: o DOI alvo está numericamente entre registros públicos de **11/09/2025** e **29/10/2025**.
- Afirmação indiciária: estimativa central em torno de **22/09/2025**.
- Não afirmar como fato absoluto: data oficial exata sem retorno direto de metadado Zenodo/DataCite.



## Prova adicional por commit assinado (GitHub Verified)
Quando houver commit/tag com assinatura verificada no GitHub, isso constitui **evidência direta de cronologia do repositório** (Git), independente da disponibilidade pública imediata do metadado do DOI.

Registro informado:
- Assinatura verificada no GitHub (`GPG key ID: B5690EEEBB952194`)
- Data/hora de verificação indicada: **19/09/2025 03:58**

Interpretação correta:
1. Esse registro prova com alta força a existência de atividade/versionamento no GitHub nessa data.
2. Esse registro **não substitui** o metadado oficial de criação/publicação do DOI no Zenodo/DataCite.
3. Em matriz probatória, entra como prova direta da trilha Git e reforço da coerência temporal global.

## Nota de integração conceitual (modelo multiescala e multilinguagem)
No contexto de formalismos toroidais, entropia/sintropia, variação linguística e canais de tradução, recomenda-se separar três camadas para preservar integridade semântica e probatória:

1. **Camada formal (matemática):** equações, operadores e invariantes explicitamente definidos (ex.: mapeamentos em \(\mathbb{T}^7\), termos espectrais, métricas de correlação).
2. **Camada empírica (observacional):** dados, timestamps, assinaturas verificadas, hashes, trilhas de versionamento e metadados públicos auditáveis.
3. **Camada interpretativa (linguagem/cognição):** tradução entre idiomas, diferenças de prosódia/cadência e variações de sentido dependentes de contexto cultural e neurocognitivo.

Princípio operacional: nenhuma inferência interpretativa deve sobrescrever evidência direta de cronologia; e nenhuma evidência de cronologia deve ser usada para afirmar, sozinha, equivalência semântica entre traduções complexas.
