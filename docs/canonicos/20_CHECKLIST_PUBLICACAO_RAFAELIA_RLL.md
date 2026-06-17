# 20 — Checklist de Publicação Pública RAFAELIA/RLL

**Status:** canônico complementar  
**Origem:** derivado do documento-mãe `BIBLIA_CONHECIMENTO_RAFAELIA_RLL.md`  
**Função:** listar o que precisa estar público, verificável e seguro antes de divulgação externa.

---

## 1. Documentos mínimos no repositório público

- [x] Documento-mãe: `docs/canonicos/BIBLIA_CONHECIMENTO_RAFAELIA_RLL.md`
- [x] Epistemologia: `docs/canonicos/13_EPISTEMOLOGIA_RAFAELIA_RLL.md`
- [x] Modelo cosmológico: `docs/canonicos/14_MODELO_COSMOLOGICO_RLL.md`
- [x] Dados externos reais: `docs/canonicos/15_DADOS_EXTERNOS_REAIS_RLL.md`
- [x] Pipeline de validação: `docs/canonicos/16_PIPELINE_VALIDACAO_RLL.md`
- [x] Onda, neuro, física e linguagem: `docs/canonicos/17_ONDA_VERBO_FISICA_NEURO_LINGUAGEM.md`
- [x] Orquestrador ASCII/UTF: `docs/canonicos/18_ORQUESTRADOR_ASCII_UTF_RAFAELIA.md`
- [x] Roadmap e falsificadores: `docs/canonicos/19_ROADMAP_FALSIFICADORES_RLL.md`
- [x] Checklist de publicação: `docs/canonicos/20_CHECKLIST_PUBLICACAO_RAFAELIA_RLL.md`

## 2. Arquivos de governança que devem existir ou ser confirmados

- [ ] `LICENSE.md`
- [ ] `data/CITATION.cff` ou `CITATION.cff`
- [ ] `docs/REFERENCES.md`
- [ ] `docs/CANONICAL_SOURCES.md`
- [ ] `docs/DOCUMENTATION_FULL_INVENTORY.md`
- [ ] `docs/DATA_INTEGRITY_CHECKLIST.md`
- [ ] `SECURITY_SUMMARY.md`

## 3. Checagens antes de divulgação acadêmica

- [ ] Confirmar cada referência em fonte primária.
- [ ] Verificar DOI via metadados oficiais.
- [ ] Confirmar commits/tags de anterioridade.
- [ ] Conferir assinatura GPG indicada.
- [ ] Rodar pipeline de validação em commit limpo.
- [ ] Registrar parâmetros, dados, hashes e outputs.
- [ ] Separar claramente `[E]`, `[C]`, `[H]` e `[VAZIO]`.

## 4. Checagens de segurança e privacidade

- [ ] Não publicar dados pessoais sensíveis.
- [ ] Não publicar tokens, chaves, credenciais ou caminhos privados.
- [ ] Não publicar exports brutos de conversas privadas sem triagem.
- [ ] Não publicar arquivos zip grandes sem inventário.
- [ ] Não publicar conteúdo de terceiros sem licença clara.

## 5. Critério de prontidão

Um documento está pronto para publicação externa quando:

```text
fonte verificada + claim classificado + dado rastreável + limite declarado + licença clara
```

## 6. Regra de ouro

Quando houver dúvida, marcar `[VAZIO]` e abrir tarefa de verificação.

---

*Publicar é iluminar com responsabilidade.*