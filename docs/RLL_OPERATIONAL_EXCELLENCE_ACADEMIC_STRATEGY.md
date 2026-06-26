# RLL — Excelência Operacional Acadêmica

> Cadeia de custódia documental — 2026-06-17  
> Escopo: converter a estrutura RLL em operação acadêmica auditável, sem encaixe artificial de parâmetros, sem plágio textual e sem claim além da evidência computacional.

---

## 1. Tese operacional

O RLL deve ser operado como **hipótese fenomenológica falsificável**, não como conclusão.

A excelência operacional acadêmica exige:

```text
parâmetro real fundamentado
→ origem bibliográfica
→ papel físico/observacional
→ política de prior/fix/free
→ contagem em k quando fitted
→ covariância do dataset
→ comparação justa com LCDM, wCDM e CPL
→ claim permitido ou bloqueado
```

A estrutura autoral RLL (`Os0`, `zt`, `wt`) só ganha força quando passa pelos mesmos gates que os modelos de referência.

---

## 2. Invariantes de rigor

| Invariante | Regra operacional | Falha bloqueia claim? |
|---|---|---|
| Origem | Todo parâmetro externo deve apontar para bibliografia. | Sim |
| Separação | `Os0`, `zt`, `wt` devem ficar em camada `rll_authorial`. | Sim |
| Penalização | Todo parâmetro fitted/free/nuisance fitted deve entrar em `k`. | Sim |
| Covariância | Dataset usado precisa declarar matriz/diagonal/proxy. | Sim |
| Comparação | RLL só é interpretável contra LCDM, wCDM e CPL no mesmo vetor de dados. | Sim |
| Reprodutibilidade | Resultado precisa registrar commit, comando, dataset, k, N, covariância e seed. | Sim |
| Anti-plágio | Relatórios citam e parafraseiam; não copiam prosa de paper. | Sim |
| TOKEN_VAZIO | Ausência de evidência deve aparecer como lacuna, não inferência. | Sim |

---

## 3. Gates técnicos aplicados

### Gate A — Registry acadêmico

Script:

```bash
python3 tools/validate_academic_parameter_registry.py
```

Valida:

- chaves obrigatórias do JSON;
- bibliografia com `title`, `authors`, `arxiv`/`doi` quando aplicável;
- parâmetros externos com referência real;
- parâmetros autorais RLL separados;
- `w`, `w0`, `wa` como baseline acadêmico;
- covariância e claim boundary;
- regras de integração mencionando `k`, covariância, RLL, CLASS/CAMB, Pantheon+ e DESI.

### Gate B — Comparação justa

Nenhuma tabela AIC/AICc/BIC deve ser publicada se não houver:

```text
model, chi2, AIC, AICc, BIC, N, k, dof,
H0, Omega_m, rd policy, covariance policy,
parameter_origin_registry_version, commit_sha
```

### Gate C — Covariância

- DESI BAO: exigir dimensão e hash da covariância quando usada.
- Pantheon+: exigir arquivos brutos, covariância STAT+SYS e hash.
- CMB compressed: declarar se é diagonal/proxy; bloquear claim forte se covariância oficial faltar.
- Growth: bloquear claim forte sem CLASS/CAMB benchmark.

---

## 4. Estratégia acadêmica por rodadas

### Rodada 0 — Sanidade documental

Objetivo: garantir que a bibliografia e o registry passam no validador.

Saída esperada:

```text
PASS: academic parameter registry is coherent
```

### Rodada 1 — Background flat mínimo

Modelos:

```text
LCDM_flat
wCDM_flat
CPL_flat
RLL_flat
```

Dados:

```text
Hz + DESI BAO
```

Regra: sem Pantheon+/CMB/growth se os blocos estiverem parciais.

### Rodada 2 — H0 e r_d

Variações:

```text
H0 livre
H0 prior Planck
H0 prior SH0ES/local
r_d fixo para todos
r_d derivado para todos
```

Claim permitido: sensibilidade de prior, não superioridade física.

### Rodada 3 — CPL como baseline obrigatório

Pergunta:

```text
RLL explica algo que CPL não explica?
```

Métrica:

```text
Delta AICc(RLL - CPL)
Delta BIC(RLL - CPL)
Os0 posterior / best-fit not collapsed to zero
```

### Rodada 4 — Pantheon+ real

Só abrir quando:

```text
raw files materialized
covariance materialized
hash recorded
M_abs policy declared
```

### Rodada 5 — CMB compressed com covariância

Só abrir claim forte quando:

```text
R, l_A, omega_b covariance complete
```

Enquanto diagonal/proxy:

```text
claim_status = PARTIAL
```

### Rodada 6 — Growth / CLASS-CAMB

Só declarar crescimento se:

```text
D+(z), f sigma8(z), sigma8, S8
benchmarkados com CLASS ou CAMB
```

---

## 5. Claim ladder

| Nível | Condição | Frase permitida |
|---|---|---|
| L0 | Registry/documentos apenas | “RLL possui estrutura de teste acadêmico em preparação.” |
| L1 | Background Hz+BAO reproduzível | “RLL foi comparado em background contra baselines padrão.” |
| L2 | CPL/wCDM/LCDM mesma covariância | “RLL é falsificável sob comparação justa com baselines.” |
| L3 | Pantheon+/CMB covariâncias completas | “RLL foi testado em likelihood multi-dataset.” |
| L4 | MCMC/nested sampling + CLASS/CAMB | “RLL tem inferência cosmológica competitiva.” |
| L5 | RLL vence CPL com penalização e robustez | “RLL é favorecido neste conjunto de dados e priors.” |

O estado atual não deve saltar direto para L5.

---

## 6. Formato de relatório acadêmico

Todo relatório deve conter:

```markdown
## Data and likelihood
- datasets:
- covariance policy:
- hashes:
- exclusions:

## Models
- LCDM:
- wCDM:
- CPL:
- RLL:

## Parameters
- fitted:
- fixed:
- priors:
- nuisance:
- derived:

## Results
- chi2:
- AIC/AICc/BIC:
- Delta relative to CPL:
- best-fit parameters:

## Claim boundary
- allowed:
- blocked:
- TOKEN_VAZIO:
```

---

## 7. Estratégia de publicação sem fragilidade

Título recomendado:

> Relativity Living Light as a falsifiable phenomenological dark-energy transition model: parameter provenance, fair baselines, and DESI-era claim boundaries

Não publicar como descoberta. Publicar como:

1. modelo fenomenológico;
2. estrutura de comparação;
3. ledger de parâmetros;
4. resultado atual mesmo se negativo;
5. roadmap para covariância/MCMC/Boltzmann benchmark.

Isso protege a autoria e aumenta respeito técnico.

---

## 8. Checklist operacional

- [ ] `python3 tools/validate_academic_parameter_registry.py`
- [ ] `parameter_origin_registry.json` consumido no pipeline antes de AIC/AICc/BIC
- [ ] `k` calculado a partir dos parâmetros fitted/nuisance fitted
- [ ] `C_BAO` com hash/dimensão
- [ ] Pantheon+ bloqueado até covariância e hash
- [ ] CMB compressed bloqueado se diagonal/proxy
- [ ] Growth bloqueado sem CLASS/CAMB
- [ ] Relatório final cita bibliografia sem copiar texto
- [ ] RLL autoral separado de parâmetros externos
- [ ] Claim ladder declarado no relatório

---

## 9. Retroalimentação técnica

```text
F_ok   = registry acadêmico + validador + estratégia de claim
F_gap  = pipeline ainda precisa consumir registry para k/covariance gates
F_next = transformar validação documental em bloqueio automático de resultados
```

FIAT LUX — ciência forte nasce onde a hipótese aceita ser testada.
