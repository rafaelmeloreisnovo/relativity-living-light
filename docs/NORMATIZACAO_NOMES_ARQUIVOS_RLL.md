# Normatização de Nomes de Arquivos — RLL

**Status:** documento normativo de manutenção  
**Escopo:** repositório público `instituto-Rafael/relativity-living-light`  
**Objetivo:** evitar divergências de inventário, links quebrados e ambiguidade de caminhos.

---

## 1. Regra canônica

Nomes de arquivos e diretórios devem evitar:

- espaço inicial ou final;
- quebras de linha invisíveis;
- duplicidade apenas por maiúsculas/minúsculas;
- acentos em nomes de caminho operacional;
- símbolos difíceis para shell, URL ou GitHub Actions;
- nomes genéricos sem contexto quando houver risco de colisão.

## 2. Padrão recomendado

Usar nomes ASCII, descritivos e estáveis:

```text
lowercase-or-UPPERCASE_contexto_claro.ext
```

Exemplos bons:

```text
darkmatter.md
docs/DARKMATTER_RLL_LINK_MAP.md
docs/canonicos/14_MODELO_COSMOLOGICO_RLL.md
data/results/repo_inventory.json
```

## 3. Caso especial corrigido

O arquivo de raiz existia como:

```text
 darkmatter.md
```

com espaço inicial. Esse nome foi normalizado para:

```text
darkmatter.md
```

Motivo da correção:

- o espaço inicial quebra comandos shell simples;
- links Markdown precisam de `%20`;
- inventários podem contar o arquivo de forma confusa;
- buscas humanas tendem a procurar `darkmatter.md`, não ` darkmatter.md`;
- GitHub Actions e scripts podem falhar ou duplicar contagem.

## 4. Regra de preservação histórica

Quando um caminho errado for corrigido:

1. criar o caminho canônico correto;
2. verificar que o conteúdo foi preservado;
3. atualizar links internos;
4. remover ou arquivar o caminho incorreto;
5. registrar a mudança em documento normativo;
6. atualizar inventário.

## 5. Contagem e inventário

Contagens devem sempre informar a categoria:

```text
tracked_files_total      = todos os arquivos rastreados pelo Git
cataloged_files          = arquivos processados pelo inventário
uncataloged_or_error     = arquivos que falharam ou foram ignorados
markdown_files           = arquivos .md detectados
line_count               = linhas de um arquivo específico
```

Números como `308`, `335`, `368`, `388` não devem ser comparados sem declarar se são linhas, arquivos Markdown, arquivos catalogados ou versões antigas do inventário.

## 6. Regra de commit

Toda normalização de nome deve ter commit próprio ou mensagem explícita contendo:

```text
Normalize filename
Fix inventory path
Update links after filename cleanup
```

---

*Nome limpo é caminho limpo; caminho limpo é prova melhor.*
