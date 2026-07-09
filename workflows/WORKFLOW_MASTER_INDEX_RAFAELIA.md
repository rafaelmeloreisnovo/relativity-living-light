# WORKFLOW_MASTER_INDEX_RAFAELIA

> **Estado:** índice mestre operacional  
> **Data:** 2026-07-09  
> **Escopo:** RAFAELIA / RLL / Omega Kernel / Termux RAFCODEΦ / Vectras VM Android / ChipQuantum / corpus / agentes  
> **Princípio:** símbolo preservado, prova marcada, execução auditável.

---

## 0. Finalidade

Este documento consolida as sessões do workflow RAFAELIA como um índice mestre navegável.

Ele não substitui papers, código, issues, pull requests ou logs de execução. Sua função é ligar:

```text
sessão → camada → repositório → artefato → estado epistêmico → gate de prova → próxima ação
```

A regra de segurança epistemológica é:

```text
TOKEN_VAZIO > inferência sem origem verificável
```

---

## 1. Estados epistêmicos permitidos

| Estado | Uso |
|---|---|
| `VERIFIED` | Há arquivo, execução, teste, log, PR, dado ou referência auditável. |
| `PARTIAL` | Há implementação ou evidência parcial, mas ainda falta validação suficiente. |
| `DECLARED` | Foi afirmado em sessão ou documentação, mas ainda não foi comprovado no repositório. |
| `TOKEN_VAZIO` | Lacuna assumida; não inventar conclusão. |
| `CONTRADICTION` | Há conflito entre resultados, arquivos, versões ou interpretações. |
| `BLOCKED` | Depende de ambiente, permissão, dado, CI, runtime ou decisão externa. |

---

## 2. Invariante operacional

A invariante comum das sessões é:

```text
coerência verificável = símbolo preservado + prova registrada + execução auditável
```

Forma RAFAELIA:

```text
ψ → χ → ρ → Δ → Σ → Ω
```

Onde:

| Selo | Função operacional |
|---|---|
| `ψ` | intenção / pergunta-raiz |
| `χ` | observação / evidência coletada |
| `ρ` | ruído / lacuna / erro / contradição |
| `Δ` | transmutação ética em teste, correção ou marcação |
| `Σ` | memória coerente / documento / commit |
| `Ω` | fechamento provisório com próximo passo |

---

## 3. Mapa canônico dos blocos

| ID | Bloco | Função | Estado atual | Gate mínimo |
|---|---|---|---|---|
| `01` | RAFAELIA simbólica | Linguagem, ética, nomes, fórmulas e compressão simbólica | `PARTIAL` | Separar símbolo, definição, hipótese, experimento e prova |
| `02` | RLL científico | Cosmologia, falsificação, likelihood, MCMC, Bayes | `PARTIAL` | Rodar pipeline reprodutível com priors, evidência e relatório |
| `03` | Omega Kernel | C freestanding, matriz 10x10x10, sem malloc/heap/GC | `PARTIAL` | Testes determinísticos de boot, hash, checkpoint e rollback |
| `04` | Ω Governance Architecture | Schemas, auditoria, eventos, policy, rollback | `PARTIAL` | Validar schemas e conectar a registros de execução |
| `05` | Termux RAFCODEΦ | Runtime Android local, shell, pkg bridge, proot | `BLOCKED` | Resolver apt/dpkg real, permissões e bootstrap verificável |
| `06` | Vectras VM Android | VM/QEMU/proot/rootfs/UI Android | `BLOCKED` | Gate shell_ok→vm_boot_ok com logs reais |
| `07` | ChipQuantum geometria | √3/2, hexágono, projeções, docpapers | `DECLARED` | Formalizar definições antes de teoremas |
| `08` | RafaeliaEngine | Entropia, coerência, FAISS, drift, rollback | `PARTIAL` | Testes unitários, datasets pequenos e logs versionados |
| `09` | Middleware Android IA | WebView, bridge de prompt, frames seed | `PARTIAL` | Garantir limites: não intercepta rede nem respostas |
| `10` | CompiladorLowFala | VM simbólica, fala, bytecode, Escrituras | `DECLARED` | Especificar ISA mínima e parser demonstrável |
| `11` | Bare-metal Edge | Arduino/Raspberry, registradores, Timer, UART, SPI | `PARTIAL` | Exemplos reproduzíveis por placa e clock |
| `12` | Drive/corpus/memória | Corpus bruto, DBs, vetores, chunks | `PARTIAL` | Índice mestre, chunking auditável e checksums |
| `13` | GitHub/agentes/Codex | PRs, issues, CI, automação assistida | `VERIFIED` | Manter PRs pequenos, rastreáveis e revisáveis |

---

## 4. Workflow por camada

### 4.1 RAFAELIA simbólica

**Função:** preservar o núcleo de linguagem, ética e intenção do projeto.

**Contrato:**

```text
símbolo → definição → uso → teste → registro
```

**Não permitido:** transformar metáfora em fato sem prova.

**Próxima ação:** criar glossário vivo com termos como `TOKEN_VAZIO`, `ψχρΔΣΩ`, `Bitraf64`, `Φ_ethica`, `ZIPRAFΩ` e `RAFCODE-Φ`.

---

### 4.2 RLL científico

**Função:** tornar hipóteses cosmológicas falsificáveis.

**Gates mínimos:**

```text
data_ok
model_ok
priors_ok
likelihood_ok
mcmc_ok
bayes_ok
report_ok
reproducibility_ok
```

**Regra:** nenhuma conclusão de superioridade científica sem comparação contra baselines e evidência estatística.

**Próxima ação:** fechar pipeline com MCMC, Bayes factor, relatório final e contrato de falsificadores.

---

### 4.3 Omega Kernel

**Função:** núcleo determinístico de execução.

**Princípios:**

```text
no malloc
no heap
no GC
fixed memory
deterministic transforms
branchless where safe
checkpointable
rollbackable
audit-friendly
```

**Testes mínimos:**

```text
test_00_boot
test_01_matrix_init
test_02_no_malloc
test_03_checkpoint_hash
test_04_policy_reject
test_05_rollback
test_06_branchless_filter
test_07_serialization
test_08_determinism_seed
test_09_audit_record
```

**Próxima ação:** criar suíte mínima de testes C/host para Omega Kernel v3.

---

### 4.4 Ω Governance Architecture

**Função:** governar artefatos, eventos, relações, auditoria e estados epistêmicos.

**Gates:**

```text
schema_parse_ok
required_fields_ok
epistemic_state_ok
hash_ok
audit_record_ok
rollback_path_ok
```

**Próxima ação:** ligar schemas a validação local em CI.

---

### 4.5 Termux RAFCODEΦ

**Função:** chão Android local para execução.

**Gates reais:**

```text
shell_ok
prefix_ok
busybox_ok
pkg_ok
apt_ok
dpkg_ok
proot_ok
storage_ok
permission_ok
```

**Estado crítico:** `BLOCKED` enquanto o backend real de pacotes não estiver íntegro.

**Próxima ação:** criar script de diagnóstico único com saída JSON e classificação por gate.

---

### 4.6 Vectras VM Android

**Função:** VM Android via UI + shell + proot + QEMU + rootfs.

**Cadeia mínima:**

```text
UI Android
→ StartVM.env
→ MainStartVM.startNow
→ MainService
→ Terminal.executeShellCommand2
→ ProotCommandBuilder
→ proot
→ qemu-system-*
→ rootfs/image
→ VNC/SPICE/console
```

**Gates:**

```text
shell_ok
prefix_ok
qemu_ok
proot_ok
rootfs_ok
storage_ok
vnc_ok
vm_boot_ok
```

**Próxima ação:** criar matriz de falha por elo da cadeia.

---

### 4.7 ChipQuantum geometria

**Função:** formalizar intuições geométricas, especialmente `√3/2`, hexágono longo e projeções.

**Separação obrigatória:**

| Camada | Exemplo |
|---|---|
| definição | `√3/2` como altura do triângulo equilátero unitário |
| metáfora | fator de coerência/projeção |
| hipótese | ganho estrutural em varredura específica |
| experimento | script com métrica e baseline |
| teorema | somente com prova formal |

**Próxima ação:** criar documento `DEFINICOES_GEOMETRICAS_MINIMAS.md` antes de expandir alegações.

---

### 4.8 RafaeliaEngine

**Função:** motor experimental de coerência, memória, drift e rollback.

**Gates:**

```text
small_dataset_ok
embedding_ok
memory_write_ok
memory_recall_ok
rollback_ok
drift_metric_ok
history_csv_ok
plot_ok
```

**Próxima ação:** travar dataset mínimo reproduzível e testes de regressão.

---

### 4.9 Middleware Android IA

**Função:** enriquecer prompts em apps/WebView sem interceptar respostas.

**Limite ético/técnico:**

```text
não intercepta rede
não lê respostas privadas
não simula permissão inexistente
não promete automação sem runtime real
```

**Próxima ação:** documentar fronteiras e permissões explicitamente.

---

### 4.10 CompiladorLowFala

**Função:** transformar linguagem/fala em bytecode simbólico auditável.

**ISA mínima sugerida:**

```text
0x04 PUSH
0x10 BEGIN
0x11 CREATE
0xF0 LOGOS
0xFF SEAL
```

**Próxima ação:** criar parser mínimo com entrada textual e saída bytecode JSONL.

---

### 4.11 Bare-metal Edge

**Função:** levar RAFAELIA ao nível de registrador, clock, UART, SPI, ADC e GPIO.

**Gates:**

```text
board_ok
clock_ok
gpio_ok
timer_ok
uart_ok
spi_ok
adc_ok
build_ok
flash_or_sim_ok
```

**Próxima ação:** separar AVR, Raspberry/ARM e simulação host.

---

### 4.12 Drive/corpus/memória

**Função:** organizar corpus bruto, DBs, vetores e chunks.

**Gates:**

```text
inventory_ok
checksum_ok
chunking_ok
index_ok
sample_read_ok
privacy_ok
reproducibility_ok
```

**Próxima ação:** criar índice de datasets com tamanho, origem, hash, licença/privacidade e estado.

---

### 4.13 GitHub/agentes/Codex

**Função:** transformar sessões em PRs pequenos, auditáveis e reversíveis.

**Política operacional:**

```text
1 PR = 1 intenção principal
1 commit lógico por artefato ou grupo coeso
sem claims científicos sem teste
sem misturar kernel + paper + CI + corpus no mesmo PR sem necessidade
```

**Próxima ação:** manter este índice como ponto de entrada para novas branches.

---

## 5. Template obrigatório de encerramento de sessão

Cada sessão relevante deve produzir este bloco:

```text
[SESSÃO]
Nome:
Data:
Repositório:
Branch/PR:
Camada: simbólica | científica | runtime | kernel | docs | dados | hardware

[ENTRADA]
O que foi recebido:

[SAÍDA]
O que foi produzido:

[CLAIMS]
VERIFIED:
PARTIAL:
DECLARED:
TOKEN_VAZIO:
CONTRADICTION:
BLOCKED:

[ARTEFATOS]
Arquivos criados:
Arquivos alterados:
Testes/logs:

[PRÓXIMA AÇÃO]
1 ação concreta:
```

---

## 6. Ordem operacional recomendada

### P0 — estabilização

1. Manter este índice atualizado.
2. Criar ledger de `TOKEN_VAZIO`.
3. Criar mapa `repo → sessão → arquivo → teste`.
4. Criar gates Termux/Vectras.
5. Criar testes mínimos Omega Kernel.
6. Separar canônico, experimental, poético e legado.

### P1 — prova científica

1. RLL com MCMC.
2. Bayes factor.
3. Priors explícitos.
4. Likelihood auditável.
5. Falsificadores documentados.
6. Relatório final reproduzível.

### P2 — expansão controlada

1. ChipQuantum Docpapers.
2. CompiladorLowFala.
3. Middleware Android IA.
4. RAFAELIA Edge Node.
5. Geometria hexagonal avançada.

---

## 7. Critério de excelência operacional

Uma sessão só deve ser considerada operacionalmente excelente quando responder:

| Pergunta | Critério |
|---|---|
| Qual era o objetivo? | explícito |
| O que foi alterado? | arquivo/commit/PR |
| O que foi provado? | teste/log/evidência |
| O que ficou vazio? | `TOKEN_VAZIO` marcado |
| O que está bloqueado? | causa e gate |
| Qual é o próximo passo? | uma ação concreta |
| Pode ser reproduzido? | sim/não com instrução |

---

## 8. Fechamento

```text
RAFAELIA = Verbo simbólico
         ⊕ Kernel determinístico
         ⊕ Ciência falsificável
         ⊕ Android executável
         ⊕ Memória auditável
         ⊕ Ética por design
```

Este índice é o mapa de navegação.  
A execução real permanece nos arquivos, testes, logs, branches e pull requests.

**Retroalimentação:**

```text
F_ok   = workflow consolidado em blocos auditáveis
F_gap  = faltam ledgers e gates executáveis por camada
F_next = criar artefatos P0 pequenos e verificáveis
```
