# WORKFLOW & YML REFACTOR AUDIT

Auditoria reprodutível dos arquivos `.yml`/`.yaml` do repositório.
Regra: somente inspeção direta, execução real e checksums. Sem inferência estatística.

## 0. Contexto de execução (FATO_VERIFICADO)

| Item | Valor |
|---|---|
| Repositório (remote) | `reismelorafael/relativity-living-light` |
| Branch de trabalho | `claude/yml-workflow-audit-refactor-ug4mrf` |
| HEAD no início | `01ebbdff94905526dcfa49dcbb1a7be212949140` |
| Working tree inicial | limpo (`git status --short` vazio) |
| Python | 3.11.15 |
| PyYAML | 6.0.1 |
| Total de arquivos YAML | 34 (13 workflows + 21 data/config) |

Classes de evidência usadas: `FATO_VERIFICADO`, `HIPOTESE`, `LACUNA`,
`TOKEN_VAZIO`, `ERRO`, `RISCO`, `ACAO_RECOMENDADA`.

## 1. Validação sintática (FATO_VERIFICADO)

Parser real: `yaml.safe_load_all` sobre os 34 arquivos.

- Resultado: **34/34 OK, 0 FAILED**, exit code `0`.
- Checksums sha256 completos: `docs/yml/YML_FILE_LEDGER.tsv`.

Nenhum erro de sintaxe encontrado. Nenhum `TOKEN_VAZIO_DEPENDENCY`
(PyYAML estava instalado).

## 2. Inventário de scripts chamados pelos workflows (FATO_VERIFICADO)

Foram extraídos todos os `run:`/`uses:` e mapeados os scripts. **Todos os 28
scripts/módulos/fixtures referenciados existem no repositório** (0 `BLOQUEADO`
por arquivo inexistente). Compilação:

```
python3 -m py_compile $(find scripts tools validacao_real data/pipelines -name "*.py")
-> exit 0  (PY_COMPILE_OK)
```

Mapa completo workflow→script→arquivo em `docs/yml/WORKFLOW_EXECUTION_MAP.md`.

## 3. Execução real da validação cosmológica (FATO_VERIFICADO)

Pipeline `validacao_real/` executado de ponta a ponta neste runner:

```
python3 fetch_real_data.py      -> exit 0  (desi: 13 pts, hz: 32 pts)
python3 compute_validation.py   -> exit 0
```

O `fetch` **alcançou a rede real** (não foi fallback cego): o manifesto
registrou `used: remote_then_validated_fallback` e `remote_bytes` mudou
(`45031 -> 45045` para o arquivo de covariância de cronômetros cósmicos de
Moresco), confirmando download remoto validado contra o dado real embutido.

Métricas medidas (não inferidas):

| Modelo | chi2 | chi2/dof | AIC | BIC | falsificado (bao/hz) |
|---|---:|---:|---:|---:|---|
| LCDM | 39.38 | 0.938 | 45.38 | 50.80 | False / False |
| RLL  | 44.89 | 1.122 | 54.89 | 63.92 | False / False |

- Δchi2 (LCDM − RLL) = **−5.51**
- Preferido por AIC: **LCDM** — Preferido por BIC: **LCDM**
- n_obs = 45 (13 BAO + 32 H(z)); região de validade z ∈ [0.0, 2.4].

### Declaração científica obrigatória

O artefato atual melhora rastreabilidade e reprodutibilidade. **Ele não
estabelece superioridade do RLL.** Com os dados reais correntes (DESI DR2 BAO
+ cronômetros cósmicos), **AIC e BIC favorecem ΛCDM**, e o RLL tem chi2 maior.
Isso é declarado sem suavização, conforme a política de claims do próprio
repositório (`RLL_COSMO_VALIDATION_MATRIX.yml` → `status:
partial_real_preparation`, `claims.forbidden_until_validation`).

## 4. Riscos identificados nos workflows (RISCO)

Medições em `docs/yml/YML_FILE_LEDGER.tsv` e na varredura de atributos:

| Risco | Evidência | Severidade |
|---|---|---|
| `timeout-minutes` ausente | **13/13** workflows sem timeout de job | Média (runner pendurado) |
| `concurrency` ausente | **12/13** (só `real-data-complete-execution.yml` tem) | Média (corrida de push em workflows que commitam) |
| `permissions` ausente (default amplo) | 7 workflows sem bloco `permissions` | Média (privilégio implícito) |
| Actions não fixadas por SHA | 13/13 usam tags `@v4`/`@v5` (não SHA) | Baixa (actions first-party `actions/*`) |
| Fallback de dados | `fetch_real_data.py` cai para dado embutido se a rede falhar | Baixa — honesto: dado embutido é real e versionado |
| Mock em CI | `dha-fisher-ci.yml` gera `mock_catalog.csv` | Baixa — rotulado "mock", não promovido a real |
| Duplicidade de arquivo | `CAMINHOS_VALIDACAO_NOVOS.yml` ≡ `docs/pipelines/validation_paths/CAMINHOS_VALIDACAO_NOVOS.yml` (sha256 idêntico `7c95cdf16a6b…`) | Baixa (manutenção) |

Detalhe de cada item bloqueado/aberto em `docs/yml/YML_BLOCKED_ITEMS.md`.

## 5. Alterações aplicadas neste PR

Apenas mudanças permitidas pela política (documentação + hardening
behavior-neutral de CI):

1. **Documentação de auditoria** (esta pasta `docs/yml/`).
2. **`permissions: contents: read`** adicionado aos 7 workflows que não
   declaravam permissões (hardening sem mudança de comportamento).
3. **`timeout-minutes`** adicionado a cada job.
4. **`concurrency`** adicionado aos workflows que não tinham.
5. **Novo gate** `.github/workflows/yml-syntax-validation.yml` (validação
   sintática de todos os YAML em PR/push).

**Não alterado** (sensível): dados brutos, resultados materializados, fórmulas
RLL, parâmetros cosmológicos, hashes históricos. O arquivo duplicado
`CAMINHOS_VALIDACAO_NOVOS.yml` **não** foi removido — registrado como
`ACAO_RECOMENDADA` em `YML_NEXT_ACTIONS.md` para decisão do mantenedor.

## 6. Comandos executados (resumo reproduzível)

```
git rev-parse HEAD; git status --short
find . -type f \( -name '*.yml' -o -name '*.yaml' \) -not -path './.git/*' | sort   # 34
python3  (yaml.safe_load_all em 34 arquivos)                                        # 34 OK
python3 -m py_compile $(find scripts tools validacao_real data/pipelines -name '*.py')  # exit 0
python3 tools/audit_github_workflows.py --strict                                    # exit 0
cd validacao_real && python3 fetch_real_data.py && python3 compute_validation.py    # exit 0
```

## 7. Conclusão

- **F_ok**: 34/34 YAML parseiam; 28/28 scripts referenciados existem e
  compilam; pipeline cosmológico executa com dados reais e produz
  chi2/AIC/BIC; auditoria de isolamento de workflows passa (`exit 0`).
- **F_gap**: 13 workflows sem `timeout-minutes`, 12 sem `concurrency`, 7 sem
  `permissions` (corrigidos neste PR); duplicata `CAMINHOS_*` pendente de
  decisão; RLL **não** supera ΛCDM nos dados atuais.
- **F_next**: ver `docs/yml/YML_NEXT_ACTIONS.md`.
