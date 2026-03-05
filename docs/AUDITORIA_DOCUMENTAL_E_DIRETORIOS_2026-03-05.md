# Auditoria documental e de diretórios — 2026-03-05

## Escopo desta revisão

Revisão focada em organização profissional/técnica do acervo textual (`.md`), com checagem de navegabilidade, coerência de índices e clareza de uso científico/acadêmico.

## Verificações realizadas

1. Leitura dos pontos de entrada (`README.md`, `README_MASTER.md`).
2. Checagem da trilha oficial do livro (`book/README.md`).
3. Checagem da trilha PhD (`newadd/readme.md`).
4. Validação de presença de índice canônico (`docs/INDICE_MESTRE.md`).
5. Conferência de alinhamento entre “entrada do repositório” e “índice mestre”.

## Achados e correções aplicadas nesta rodada

- Foi adicionada referência explícita desta auditoria no índice mestre para facilitar rastreabilidade contínua.
- Foi adicionada referência desta auditoria no `README.md` (porta de entrada), conectando descoberta → governança.

## Critérios de auditoria contínua (checklist)

- [ ] Cada documento estratégico deve estar referenciado no `docs/INDICE_MESTRE.md`.
- [ ] Cada trilha (core, livro, PhD, legado) deve ter uma entrada canônica única.
- [ ] Se houver arquivo “legacy”, ele deve apontar para a fonte canônica correspondente.
- [ ] Leituras sequenciais devem estar explícitas (ordem recomendada).
- [ ] Documentos de política (artefatos, governança, integridade) devem ser fáceis de localizar a partir da raiz.
- [ ] Títulos devem refletir escopo real (evitar títulos genéricos para conteúdo específico).
- [ ] Arquivos de auditoria/release devem ter data no nome ou no cabeçalho.
- [ ] Evitar duplicidade funcional de índice (ex.: dois “índices principais” para mesma trilha).

## 12 ideias para evolução profissional, científica e acadêmica

1. **Matriz de rastreabilidade científica** (`hipótese → dado → script → resultado → seção do livro`).
2. **Padrão mínimo de metadados em `.md`** (autor, data, status, escopo, fonte canônica).
3. **Glossário unificado de símbolos** com versão e tabela de compatibilidade de notação.
4. **Tabela de maturidade por pipeline** (Sintético/Parcial real/Real validado por módulo).
5. **Registro de decisões científicas** (ADR científico para hipóteses e cortes metodológicos).
6. **Mapa de dependência entre capítulos do livro** para revisão acadêmica dirigida.
7. **Checklist de reprodutibilidade por release** (comandos, insumos, outputs esperados).
8. **Seção de limitações por observável** (H(z), BAO, CMB shift, lentes, rotação, etc.).
9. **Painel de risco documental** (duplicidade, arquivos órfãos, links quebrados, legado sem ponte).
10. **Política de nomenclatura temporal** (`YYYY-MM-DD`) para auditorias e revisões.
11. **Template de revisão de capítulo** com critérios científicos e editoriais.
12. **Trilha de preparação para submissão acadêmica** (preprint, dados suplementares, pacote de replicação).

## Próximos passos recomendados

- Priorizar os itens 1, 4 e 7 (maior impacto em reprodutibilidade).
- Executar varredura periódica de links internos dos `.md` do repositório.
- Consolidar auditorias futuras neste mesmo diretório (`docs/`) para histórico contínuo.
