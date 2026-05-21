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

