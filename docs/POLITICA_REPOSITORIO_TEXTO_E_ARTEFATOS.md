# Política do Repositório — Texto e Artefatos

**Status:** oficial (normativa)  
**Escopo:** todo o repositório Git (core), incluindo `README.md`, `docs/`, `data/`, `results/`, `src/` e scripts versionados.

---

## 1) Regra normativa de formatos no core

### 1.1 Permitido no core

No núcleo do repositório (core), é **permitido versionar**:

- arquivos textuais e documentação: `.md`, `.csv`, `.json`, `.tex`;
- código-fonte e scripts reprodutíveis (por exemplo: `.py`, `.sh`, `.c`, `.S`, `.java`), desde que auditáveis por diff textual;
- metadados e manifests textuais (ex.: checksums, índices e inventários em Markdown/CSV/JSON).

### 1.2 Proibido no core

No core, é **proibido versionar como prática padrão**:

- compactados: `.zip`;
- documentos binários: `.pdf`;
- imagens raster: `.png`, `.jpg`, `.jpeg`;
- notebooks: `.ipynb`;
- demais binários/opacos que não sejam auditáveis por diff textual.

> Racional: reduzir acoplamento de artefatos pesados/opacos no histórico Git e priorizar rastreabilidade textual e reprodutibilidade.

---

## 2) Exceções explícitas e prazo de migração

Exceções só são válidas quando **explicitamente registradas** com justificativa técnica e plano de saída.

Cada exceção deve declarar, no mínimo:

1. artefato e caminho;
2. motivo da permanência temporária;
3. responsável;
4. destino externo (Release/Zenodo);
5. hash SHA-256;
6. **prazo de migração**.

### 2.1 Janela padrão de migração

- Prazo padrão máximo: **30 dias corridos** a partir do registro da exceção.
- Prorrogação: apenas com novo registro explícito, justificativa e novo prazo.

### 2.2 Registro mínimo recomendado

Modelo em tabela (pode ficar em documento de governança):

| Artefato | Justificativa | Responsável | Destino externo | SHA-256 | Prazo de migração | Status |
|---|---|---|---|---|---|---|
| `data/exemplo.zip` | compatibilidade transitória | @owner | GitHub Release vX.Y.Z | `<hash>` | AAAA-MM-DD | aberto |

---

## 3) Como publicar artefatos externos

Artefatos binários e pacotes devem ser publicados fora do core, preferencialmente em **GitHub Releases** e/ou **Zenodo**.

### 3.1 Canais oficiais

- **GitHub Releases:** distribuição operacional por versão/tag.
- **Zenodo:** arquivamento científico com DOI e versionamento citable.

### 3.2 Convenção de nomes

Formato recomendado:

`rll-<componente>-v<MAJOR>.<MINOR>.<PATCH>-<AAAA-MM-DD>.<ext>`

Exemplos:

- `rll-results-v1.4.0-2026-02-25.zip`
- `rll-figures-v1.4.0-2026-02-25.pdf`

### 3.3 Integridade (hash SHA-256)

Para cada artefato publicado externamente:

1. gerar hash SHA-256;
2. registrar hash no release notes e/ou manifesto textual no repositório;
3. validar hash após upload/download.

Exemplo de comando:

```bash
sha256sum rll-results-v1.4.0-2026-02-25.zip
```

### 3.4 Versionamento

- Adotar SemVer para lotes versionáveis (`vMAJOR.MINOR.PATCH`).
- Associar cada artefato a uma tag Git.
- Registrar changelog mínimo (o que mudou, compatibilidade, data).

---

## 4) Inventários históricos

Documentos como `docs/ZIP_CONTENT_INDEX.md` e índices equivalentes são classificados como:

- **inventário histórico de rastreabilidade**; e
- **não recomendação de armazenamento de binários no core**.

Esses inventários existem para auditoria, legado e migração controlada.

---

## 5) Fonte oficial e precedência

Esta política é a **fonte oficial** para decisões sobre armazenamento de texto e artefatos no repositório core.

Em caso de conflito entre documentos de apoio, esta política prevalece para:

- aceitação/rejeição de formatos no core;
- uso de exceções;
- fluxo de publicação externa.
