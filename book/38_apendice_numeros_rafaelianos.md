# 38. Apêndice — Números Rafaelianos

[⬅️ Capítulo anterior](./37_apendice_trilha_autoral.md) | [📚 Sumário do livro](./README.md) | [Capítulo próximo ➡️](./39_apendice_referencias_fontes.md)

Conjunto temático de textos numéricos e simbólicos específicos.

## Conteúdo incorporado (itens soltos/localizados)
Documentos e artefatos relacionados incorporados nesta etapa:

- docs/numeros_rafaelianos/Readme.md
- docs/numeros_rafaelianos/Numeros.md
- docs/numeros_rafaelianos/harmonica.md

## Tabela canônica de números estruturais

> Escopo: esta tabela define **uso técnico mínimo** para os números 42, 84, 72 e 144 dentro do modelo RLL. Quando esses números forem citados fora destes critérios (ex.: uso histórico, estilístico ou editorial), a citação deve ser explicitamente marcada como convenção não-física.

| Número estrutural | Definição operacional | Papel no modelo | Critério de testabilidade/falsificação | Status (hipótese, convenção, inferência) |
|---|---|---|---|---|
| **42** | Tamanho canônico de janela para ajuste local de `H(z)` e resíduos: `N_janela = 42` pontos válidos por bloco. | Escala-base de estabilidade numérica para estimativas locais de parâmetros (`z_t`, `w_t`, `Ω_s0`). | Falsificado se, em validação cruzada, `N=42` produzir erro preditivo e instabilidade sistematicamente piores do que uma faixa vizinha (`N=36–48`) com diferença estatisticamente robusta. | **Hipótese operacional** |
| **84** | Regime de robustez definido como duplicação da janela-base: `N_robustez = 84` pontos. | Teste de sensibilidade de escala (verificar se parâmetros mantêm consistência ao dobrar suporte amostral). | Falsificado se a mudança `42→84` deslocar parâmetros-chave além das bandas de incerteza esperadas e piorar critérios de informação (AIC/BIC) sem ganho de ajuste. | **Inferência metodológica** |
| **72** | Discretização angular canônica para análise de anisotropia magneto-plasmática: `72` setores de `5°` (`72×5° = 360°`). | Resolução direcional para comparar assinaturas de rotação/Faraday com variações de lensing e crescimento. | Falsificado se a decomposição em 72 setores não capturar estrutura além do ruído e for dominada por aliasing, enquanto resoluções alternativas (ex.: 36 ou 144) apresentem ganho estatístico consistente. | **Convenção técnica** |
| **144** | Grade refinada padrão de mapa residual: `12×12 = 144` células (ou equivalente em discretização 2D). | Nível de refinamento para inspeção de estruturas subdominantes em mapas de resíduos (`H(z)`, `fσ₈`, lensing). | Falsificado se a malha 144 introduzir sobreajuste/instabilidade (alta variância sem ganho de poder explicativo) frente a malhas mais simples com melhor desempenho fora da amostra. | **Hipótese operacional** |

## Nota de escopo sobre usos não técnicos

- Uso **editorial/histórico/simbólico** de 42, 84, 72 ou 144 não deve ser interpretado como previsão física.
- Sempre que ocorrer uso não técnico, registrar a etiqueta: `Nota de escopo: convenção editorial/histórica (sem papel inferencial no modelo).`

## Notas de consolidação
- Este capítulo funciona como nó canônico para evitar dispersão de arquivos soltos.
- Atualize este capítulo quando novos materiais da mesma temática forem adicionados ao repositório.

---
