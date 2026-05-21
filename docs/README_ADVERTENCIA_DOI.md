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
