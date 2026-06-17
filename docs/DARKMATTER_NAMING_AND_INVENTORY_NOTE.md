# Dark Matter — Nota de Nome, Inventário e Divergência de Contagem

**Status:** nota explicativa pública  
**Arquivo canônico atual:** [`../darkmatter.md`](../darkmatter.md)  
**Arquivo legado corrigido:** ` darkmatter.md` com espaço inicial

---

## 1. O que aconteceu

Havia um arquivo de raiz chamado:

```text
 darkmatter.md
```

O primeiro caractere do nome era um espaço. Isso criou ambiguidade entre:

- o nome visualmente esperado: `darkmatter.md`;
- o nome real anterior: ` darkmatter.md`;
- links URL-encoded: `%20darkmatter.md`;
- resultados de inventário e busca.

O caminho canônico foi normalizado para:

```text
darkmatter.md
```

## 2. Por que isso importava

Um espaço inicial pode causar:

- link Markdown quebrado;
- erro em shell quando o caminho não é corretamente escapado;
- busca humana falhar;
- contagem de inventário parecer contraditória;
- scripts tratarem o arquivo como caso especial;
- documentação pública parecer desorganizada.

## 3. Sobre os números 308, 335, 368, 388

Esses números podem representar categorias diferentes. Eles não devem ser comparados sem contexto.

| Número | Possível significado | Situação |
|---:|---|---|
| 308 | contagem antiga, parcial ou derivada de versão anterior | não é o valor atual confirmado para `darkmatter.md` |
| 335 | linhas do arquivo `darkmatter.md` no inventário observado | valor coerente com o caso Dark Matter |
| 368 | quantidade de arquivos Markdown no inventário atual observado | métrica global, não linhas do Dark Matter |
| 388 | possível contagem de outra versão, outra categoria ou antes/depois de inclusão de documentos | exige commit/artefato específico para confirmar |

## 4. Regra correta de leitura

Sempre declarar a categoria da contagem:

```text
arquivo específico → line_count
repositório inteiro → tracked_files_total
Markdown total → markdown_files
catálogo processado → cataloged_files
falhas/ignorados → uncataloged_or_error_files
```

## 5. Papel do `darkmatter.md`

O arquivo `darkmatter.md` é um pacote de validação cosmológica real para RLL. Ele concentra:

- DESI DR2 BAO;
- Planck/CMB distance priors;
- cronômetros cósmicos H(z);
- fσ8;
- mapeamento logístico RLL → `w_eff(a)`;
- comparação por χ², AIC, AICc, BIC e Bayes;
- entregáveis de dados, workflow e script de validação.

## 6. Decisão normativa

- `darkmatter.md` é o caminho canônico.
- `docs/DARKMATTER_RLL_LINK_MAP.md` é o mapa de ligações.
- `docs/DARKMATTER_NAMING_AND_INVENTORY_NOTE.md` explica a divergência histórica.
- `docs/NORMATIZACAO_NOMES_ARQUIVOS_RLL.md` define a regra geral para nomes.

## 7. Próxima etapa recomendada

Regenerar inventários após a normalização:

```bash
python3 tools/docs_inventory.py
python3 tools/docs_inventory.py --check
```

Depois disso, atualizar:

```text
docs/DOCUMENTATION_FULL_INVENTORY.md
data/results/repo_inventory.json
data/results/repo_inventory.tsv
```

---

*O erro do nome virou documentação de integridade: caminho corrigido, rastro preservado.*
