# Arquivo técnico — `docs/root_md_archive` (refatoração pós‑doc)

> **Objetivo**: consolidar os arquivos históricos `.md` removidos da raiz em um acervo auditável, com leitura formal, taxonomia mínima e orientação de integração acadêmica ao `README.md` principal.

## Escopo e papel do diretório

Este diretório preserva materiais legados e versões autorais que não constituem a trilha canônica operacional do repositório. Seu uso correto é:

1. **Preservação histórica** de formulações, glossários e narrativas intermediárias.
2. **Referência de contexto** para revisão técnica, comparação semântica e rastreabilidade.
3. **Insumo para curadoria**: itens daqui podem ser promovidos para documentos canônicos após revisão metodológica.

## Critérios de uso acadêmico (formal)

- Tratar os arquivos como **fontes secundárias** até validação cruzada com `docs/INDICE_MESTRE.md`.
- Quando houver discrepância terminológica, priorizar o texto canônico mais recente em `docs/`.
- Em citação técnica, indicar explicitamente se o conteúdo é: **histórico**, **hipótese**, **síntese** ou **procedural**.

## Inventário com atitude técnica recomendada por arquivo

| Arquivo | Natureza predominante | Atitude de uso recomendada |
|---|---|---|
| `00_COMO_LER.md` | Navegação/metodologia | Usar como protocolo de leitura e entrada para curadoria documental. |
| `06_COMPARACOES_DETALHADAS.md` | Comparativo técnico | Extrair apenas argumentos verificáveis e reconciliar com resultados em `results/`. |
| `09_GLOSSARIO_COMPLETO.md` | Vocabulário canônico-base | Utilizar para alinhamento terminológico em textos técnicos. |
| `09_GLOSSARIO_COMPLETO-1.md` | Variante histórica de glossário | Usar apenas para diffs semânticos e evolução de nomenclatura. |
| `10_FAQ_COMPLETO.md` | Perguntas e respostas técnicas | Referenciar como camada pedagógica, não como norma metodológica final. |
| `11_DOCUMENTO_PRIORIDADE.md` | Priorização estratégica | Aproveitar para planejamento, exigindo atualização por evidência recente. |
| `Readme_dha.md` | Síntese autoral temática | Tratar como material conceitual e mapear para equivalentes canônicos. |
| `Readmedha2.md` | Continuidade de síntese | Usar para rastrear evolução argumentativa e consistência interna. |
| `Readmedha3.md` | Refinamento de síntese | Verificar convergência com hipóteses testáveis e métricas explícitas. |
| `Readmeumedha.md` | Variação de enquadramento | Preservar como referência de framing sem substituir documentação oficial. |
| `Ratrabalho2.md` | Documento de trabalho | Ler como rascunho técnico, exigindo validação e normalização antes de reuso. |
| `Tarafaelesta.md` | Texto autoral/manifesto | Classificar como contextual; evitar uso direto em inferência quantitativa. |
| `TrabalhoRagarl.md` | Material de elaboração | Aproveitar para extração de hipóteses e trilha de decisões históricas. |
| `UMEA Unified Multi-Scale Effective Action.md` | Formulação teórica | Tratar como proposta formal sujeita a validação matemática e observacional. |

## Integração com o `README.md` da raiz

A integração institucional desta pasta deve ocorrer por:

- link direto no `README.md` raiz para este índice (`docs/root_md_archive/README.md`);
- subseção dedicada listando cada arquivo e seu papel de integração;
- indicação explícita de que o conteúdo aqui é **arquivo histórico curado**, não substituto de normas canônicas.

## Fluxo de curadoria recomendado

1. **Classificar** arquivo por natureza (histórico, método, hipótese, síntese).
2. **Comparar** com documentos canônicos e dados reproduzíveis.
3. **Promover** trechos validados para `docs/` com referência cruzada.
4. **Registrar** no histórico de release o que foi absorvido, alterado ou descontinuado.

## Resultado esperado da refatoração

- Maior legibilidade para avaliação pós‑doc.
- Redução de ambiguidade entre conteúdo canônico e histórico.
- Base documental tecnicamente auditável para integração interdisciplinar (física, matemática, linguagem e sistemas complexos).

## Camada de integração conceitual (álgebra + geometria + topologia + linguagem)

Para atender ao programa interdisciplinar descrito pelo autor (toro \\(\mathbb{T}^7\\), dinâmica informacional, espectro/frequência e tradução multilíngue), este acervo deve ser lido por camadas:

1. **Camada formal**: estruturas matemáticas (mapeamentos, operadores, recorrências, entropia, métricas).
2. **Camada física**: hipóteses dinâmicas (acoplamentos, transições, observáveis espectrais e correlações).
3. **Camada computacional**: algoritmos de hash/CRC/árvore de Merkle, simulação e validação reproduzível.
4. **Camada linguística-cognitiva**: variações de significado entre idiomas (entonação, acentuação, cadência) como transformação de sinal semântico.

### Princípio operacional de leitura

- **Sem abstração excessiva**: converter cada afirmação em objeto verificável (equação, dado, experimento ou script).
- **Baixo overhead**: preferir passos curtos e mensuráveis de integração documental.
- **Rastreabilidade**: toda promoção de conteúdo histórico deve indicar origem, revisão e versão canônica de destino.

### O que "carrega o conhecimento" neste contexto

O conhecimento útil é carregado pela combinação de:

- **forma matemática** (estrutura do modelo),
- **evidência observacional** (dados e testes),
- **implementação computacional** (reprodutibilidade),
- **estabilidade semântica** (termos consistentes entre idiomas e domínios).

Sem a convergência dos quatro vetores acima, conteúdo permanece hipótese narrativa; com convergência, torna-se conhecimento técnico integrável.
