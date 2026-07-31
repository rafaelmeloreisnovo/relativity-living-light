# Metodologia Coerente RLL

**Estado:** CANÔNICO OPERACIONAL — `claim_allowed=false`  
**Escopo:** dados observacionais reais, topologia estrutural do conhecimento e fronteira de claims do projeto Relativity Living Light (RLL).  
**Manifesto associado:** `data/manifests/dados_reais_fundamentais_v1.json`

> Este documento governa como os dados entram, são verificados, atravessam a inferência e podem — ou não — sustentar claims. Materialização, hash correto e execução de código são condições necessárias, mas não equivalem a validação científica da RLL.

## 1. Catálogo de dados reais fundamentais

A fonte operacional de verdade é o manifesto `data/manifests/dados_reais_fundamentais_v1.json`, em conjunto com `data/real/cosmology/real_cosmology_inputs.yml`, os snapshots `data/failsafe/*_FROZEN.json` e os arquivos materializados em `data/real/`.

| ID canônico | Observável | Caminho local | n | Estado |
|---|---|---|---:|---|
| `real_hz` | H(z), cosmic chronometers | `data/real/Hz_data_real.csv` | 33 | VERIFIED |
| `real_bao_legacy` | BAO legacy BOSS/DESI | `data/real/BAO_data_real.csv` | 10 | VERIFIED |
| `real_desi_dr2_bao` | DESI DR2 BAO | `data/real/cosmology/desi_dr2_bao_primary_points.csv` | 13 | VERIFIED |
| `real_fsigma8` | fσ8/RSD | `data/real/cosmology/fsigma8_growth_real.csv` | 17 | VERIFIED |
| `real_cmb_shift` | CMB shift comprimido | `data/real/CMB_shift_real.json` | 2 escalares principais | VERIFIED |
| `real_pantheon_plus_shoes` | Pantheon+SH0ES | `data/real/cosmology/pantheon_plus/MANIFEST.json` | ~1700 declarado | PARTIAL |

Para cada dataset, a identidade mínima é:

```text
(dataset_id, local_path, sha256, source_ref, n_obs, epistemic_state)
```

O SHA-256 identifica o conteúdo materializado. Ele não autentica sozinho a publicação científica, não resolve licenças e não demonstra adequação do modelo. A proveniência deve incluir fonte primária, política de erro/covariância, consumidor do pipeline e snapshot failsafe quando existente.

## 2. Pipeline de análise

A cadeia canônica é:

```text
Fonte primária
  → materialização local
  → SHA-256 + contrato de colunas
  → pré-processamento determinístico
  → observável teórico do modelo
  → resíduo e verossimilhança
  → comparação ΛCDM/wCDM/CPL/RLL
  → falsificadores e controles negativos
  → gate de claim
  → receipt append-only
```

### 2.1 Ingestão

1. Resolver o `dataset_id` no manifesto fundamental.
2. Exigir `local_path` existente e não vazio.
3. Recalcular SHA-256 e comparar com o valor congelado.
4. Validar esquema, colunas, tipos, ordem em redshift, incertezas positivas e política de duplicatas.
5. Bloquear promoção quando houver fixture sintética, arquivo ausente ou hash divergente.

### 2.2 Pré-processamento

O pré-processamento deve ser explícito e reproduzível: ordenação, seleção, normalização, tratamento de duplicatas e transformação de observáveis precisam aparecer em receipt. Nenhum valor observado pode ser ajustado manualmente para favorecer um modelo.

### 2.3 Verossimilhança

Para resíduos vetoriais `r = d - m(θ)`, a forma canônica é:

```text
χ²(θ) = rᵀ C⁻¹ r
```

Quando a covariância completa não estiver disponível, o uso diagonal deve ser declarado como aproximação e o dataset não pode ser descrito como likelihood completa. A matriz deve ser simétrica, finita e positiva definida ou ter regularização documentada.

### 2.4 Comparação de modelos

A avaliação deve incluir, no mínimo:

- χ² total e por bloco observacional;
- número de parâmetros livres `k` e observações `n`;
- `AIC = χ² + 2k`;
- `BIC = χ² + k ln(n)`;
- limite nulo exato da RLL para ΛCDM;
- diagnóstico de resíduos, estabilidade e sensibilidade;
- comparação com ΛCDM e, quando aplicável, wCDM/CPL;
- holdout ou posterior independente para qualquer claim preditivo.

### 2.5 Gate de claims

O gate padrão permanece fechado:

```text
claim_allowed=false
```

A abertura exige simultaneamente: proveniência completa, hashes verificados, likelihood adequada, baseline competitivo, falsificadores executados, incerteza reportada, replicação e revisão humana. O validador `tools/validate_schemas_claim_boundary.py` continua sendo uma barreira estrutural, não uma certificação científica.

## 3. Cadeia epistêmica

Estados operacionais:

```text
TOKEN_VAZIO
  → DECLARED
  → MATERIALIZED
  → HASH_VERIFIED
  → VERIFIED
  → EVIDENCED
  → CLAIM_ALLOWED
```

Regras:

1. `VERIFIED` significa que identidade, estrutura e verificações declaradas passaram; não significa que a RLL foi confirmada.
2. `PARTIAL` preserva o objeto utilizável sem ocultar covariância, licença, metadado ou integração ausente.
3. `TOKEN_VAZIO` é um estado auditável com `required_for` e `fill_path`; nunca deve ser preenchido por inferência silenciosa.
4. Toda mudança de estado deve produzir evento append-only com timestamp, hash de entrada, hash de saída, comando e resultado.
5. A promoção final depende de evidência externa e falsificação; execução local isolada não autoriza claim cosmológico.

Invariante de fronteira:

```text
Dado bruto ≠ dado verificado ≠ evidência ≠ claim
```

## 4. Protocolo de falsificação

A metodologia conecta-se ao `ROADMAP_FALSIFICADORES`, à matriz `RLL_FALSEABILITY_MATRIX.md` e aos nós de lacuna da floresta.

Um teste RLL deve declarar antes da execução:

- hipótese e limite nulo;
- observáveis capazes de refutá-la;
- baseline e priors;
- função de verossimilhança;
- covariância e sistemáticas;
- critério de falha e critério de saída;
- conjunto de treino, calibração e holdout, quando houver ML;
- regra que impede reinterpretação posterior do limiar.

Falsificadores mínimos para a cosmologia de fundo:

1. recuperação numérica de ΛCDM quando `Ωs0=ΩB0=ΩP0=0`;
2. consistência de H(z), BAO, CMB shift e fσ8 em análise conjunta;
3. penalização por complexidade via AIC/BIC e, quando disponível, evidência Bayesiana;
4. estabilidade sob remoção de um bloco observacional;
5. validação Pantheon+ com covariância completa antes de qualquer claim SNe;
6. cadeias MCMC/Cobaya posteriores reproduzíveis antes de intervalos finais.

Resultado incompatível deve ser registrado como `REFUTADO`, `BLOCKED` ou `TOKEN_VAZIO`, sem apagar o histórico.

## 5. Conexão com a topologia de conhecimento

`data/knowledge_forest/rll_route_forest_blueprint.json` representa a metodologia como duas árvores adicionais:

- `T-REAL-DATA`: proveniência, identidade, materialização e estado dos datasets;
- `T-METHODOLOGY`: ingestão, likelihood, seleção de modelos, falsificação e gate de claims.

As árvores conectam-se a `T-SCIENCE` sem transformar dataset em conclusão. Cada nó possui um vetor operacional 7D:

| Direção | Região | Pergunta de controle |
|---|---|---|
| D1 | Proveniência | De onde veio e qual sua cadeia de custódia? |
| D2 | Coerência semântica | O observável e o estado epistêmico são inequívocos? |
| D3 | Integridade dimensional | Unidades, domínios, transformações e covariâncias são válidos? |
| D4 | Execução | Existe código, gate e receipt reproduzível? |
| D5 | Memória temporal | Há precedência, supersessão e histórico append-only? |
| D6 | Direitos e segurança | Licença, privacidade e autorização estão registradas? |
| D7 | Evidência e falsificação | Qual teste pode contradizer o claim? |

Os vetores são coordenadas de roteamento operacional; não são embeddings aprendidos nem estados físicos. Uma rota `partial_resolution` reduz uma lacuna, mas não a fecha automaticamente.

## 6. Limitações atuais e próximos passos

Os seguintes vazios permanecem explícitos:

1. **Pantheon+ likelihood completa:** a covariância grande não acompanha integralmente o Git; integrar via caminho reproduzível, verificar hash e executar likelihood SNe.
2. **Cadeias MCMC/Cobaya:** materializar configuração, seeds, chains, diagnósticos de convergência e posterior independente.
3. **DESI DR2 covariance audit:** distinguir claramente matriz completa, resumo de covariância e aproximação diagonal em cada execução.
4. **Memória temporal:** ligar receipts científicos ao ledger append-only com precedência e invalidação.
5. **Licenças de datasets:** consolidar direitos de redistribuição e citação por dataset.
6. **Replicação externa:** repetir o pipeline em ambiente independente e publicar artefatos suficientes para revisão.

Próximo gate verificável:

```text
python tools/validate_fundamental_real_data_topology.py --write-receipt artifacts/fundamental-real-data-topology/receipt.json
```

O gate deve falhar em qualquer hash divergente, dataset sintético no perfil fundamental, equação crítica ausente, nó/rota ausente ou promoção indevida de `claim_allowed`.
