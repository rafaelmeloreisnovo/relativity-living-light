# RLL — Estrada Canônica de Execução

**Status:** rota operacional canônica para continuidade do repositório `relativity-living-light`.  
**Regra-raiz:** avançar em documentação, auditoria, organização, testes leves e planejamento reprodutível sem travar em pergunta a cada etapa.  
**Regra de proteção:** pedir confirmação apenas quando a ação alterar dado bruto, fórmula, claim científico, resultado canônico, saída estrutural nova fora do escopo ou qualquer decisão irreversível.

---

## 1. Intenção

Este documento transforma a análise do repositório em estrada executável. A função da estrada é impedir que cada próxima ação dependa de nova pergunta quando a direção já é clara.

A estrada preserva quatro princípios:

1. **Não inventar resultado.**
2. **Não alterar dado bruto sem autorização explícita.**
3. **Não declarar vitória científica sem gate estatístico e observacional.**
4. **Converter lacuna em `TOKEN_VAZIO` rastreável.**

A estrada permite agir em:

- documentação;
- auditoria;
- inventário;
- organização de rotas;
- criação de checklists;
- leitura de PRs e artefatos;
- classificação fato / hipótese / lacuna / risco / próximo teste;
- preparação de pipelines e planos de execução;
- criação de arquivos Markdown/YAML/TSV de governança.

---

## 2. Autorização operacional padrão

Quando uma análise produzir um próximo ato óbvio e seguro, este próximo ato deve ser considerado autorizado dentro do escopo abaixo.

### Autorizado sem nova pergunta

| Tipo de ação | Permitido | Observação |
|---|---:|---|
| Criar documentação explicativa | sim | desde que não altere claims científicos |
| Criar roadmap/checklist/ledger | sim | deve marcar lacunas como `TOKEN_VAZIO` |
| Criar arquivos de auditoria | sim | sem modificar dados brutos |
| Organizar caminhos de execução | sim | sem alterar fórmula/modelo |
| Adicionar plano de testes | sim | plano, não resultado inventado |
| Registrar fatos de PRs/commits | sim | com linguagem conservadora |
| Criar issue/PR/documento de acompanhamento | sim | se for documentação/governança |
| Corrigir links/documentação | sim | sem mudança científica |
| Escrever síntese acadêmica conservadora | sim | sem overclaim |

### Exige confirmação explícita

| Tipo de ação | Motivo |
|---|---|
| Alterar `data/real/**` | dado observacional bruto é fonte de prova |
| Alterar fórmula cosmológica | muda o objeto científico |
| Alterar parâmetros canônicos | pode gerar posterior/post-hoc fitting |
| Sobrescrever `results/**` canônicos | pode apagar rastreabilidade |
| Mudar `claim_allowed=false` para `true` | exige gates completos |
| Declarar RLL confirmado/vencedor | exige validação robusta |
| Criar saída estrutural externa ao repo | altera forma de entrega |
| Executar ação irreversível | risco de perda de trilha |

---

## 3. Mapa da estrada

```text
ψ intenção
  ↓
χ observar repositório / PR / arquivo / resultado
  ↓
ρ separar ruído, erro, lacuna e fato
  ↓
Δ transmutar em ledger, rota, teste ou doc
  ↓
Σ gravar memória coerente no repositório
  ↓
Ω proteger claim e preparar próximo ato
  ↓
ψ próxima execução
```

A estrada é cíclica. Cada análise deve terminar com:

```text
R3 = <F_ok, F_gap, F_next>
```

- `F_ok`: o que já é sustentado.
- `F_gap`: o que ainda não é sustentado.
- `F_next`: o próximo ato seguro.

---

## 4. As sete rotas do RLL

### Rota 1 — Verdade computacional

**Pergunta:** o que o código realmente calcula?

Saídas:

- funções implementadas;
- scripts executáveis;
- testes existentes;
- resultados materializados;
- dependências ausentes;
- `TOKEN_VAZIO_BACKEND` quando faltar motor externo.

Critério de avanço:

- `py_compile` documentado;
- testes mínimos definidos;
- ausência de inferência não rastreada.

---

### Rota 2 — Dados reais e proveniência

**Pergunta:** qual dado é real, qual é sintético, qual é parcial?

Saídas:

- manifesto de fontes;
- hashes;
- rota real/sintética;
- campos `dataset_type`;
- fronteira de claim.

Critério de avanço:

- dado real deve ter origem, hash ou razão de materialização manual;
- dado sintético nunca sustenta claim científico externo.

---

### Rota 3 — Comparação cosmológica justa

**Pergunta:** RLL foi comparado contra adversários adequados?

Baselines obrigatórios:

- `LCDM`;
- `wCDM`;
- `CPL/w0waCDM`;
- `RLL`.

Métricas obrigatórias:

- `chi2`;
- `AIC`;
- `AICc`;
- `BIC`;
- `N`;
- `k`;
- deltas contra LCDM e CPL.

Critério de avanço:

- nunca comparar apenas com LCDM quando CPL existir;
- nunca ocultar penalização por parâmetros extras.

---

### Rota 4 — Robustez estatística

**Pergunta:** o resultado é estável ou é apenas smoke test?

Degraus:

1. smoke test: `maxiter=3`;
2. robust fit: `maxiter>=100`, seeds múltiplas;
3. deep fit: `maxiter>=1000`, MCMC ou nested sampling;
4. posterior/evidência;
5. ablação por bloco de dados.

Critério de avanço:

- resultado com `maxiter=3` deve ser rotulado como smoke/sanity;
- claim forte exige robustez e repetição.

---

### Rota 5 — Falsificabilidade

**Pergunta:** o que derruba, limita ou enfraquece o RLL?

Registrar sempre:

- condição de falha;
- teste mínimo;
- dataset necessário;
- risco se inventar;
- decisão conservadora.

Exemplos:

- `Os0=0.0` recorrente em fits robustos;
- piora persistente de AIC/AICc/BIC;
- incapacidade de competir contra CPL;
- ausência de covariância oficial;
- crescimento sem CLASS/CAMB;
- Pantheon+ incompleto.

---

### Rota 6 — Publicação acadêmica

**Pergunta:** qual frase pode ser publicada sem overclaim?

Permitido hoje:

> O RLL é uma hipótese cosmológica fenomenológica testável com pipeline reprodutível em desenvolvimento, comparada contra LCDM, wCDM e CPL, mantendo gates conservadores de claim.

Proibido hoje:

> RLL está confirmado.

> RLL vence a cosmologia padrão.

> RLL resolve energia escura, H0 ou S8.

Próxima forma publicável:

> Apresentamos o framework RLL e um pipeline reprodutível de comparação observacional. Em execuções preliminares, CPL/w0waCDM é favorecido; RLL permanece candidato testável, com claims fortes bloqueados até fits robustos e datasets/covariâncias completos.

---

### Rota 7 — Valor e aplicação

**Pergunta:** onde está o valor real do repositório?

Valor atual:

- autoria rastreável;
- governança de hipótese;
- pipeline científico;
- metodologia de lacunas;
- estrutura de auditoria;
- base para artigo, apresentação, grants, laboratório e parceria.

Valor ainda não permitido:

- modelo cosmológico comprovado;
- produto científico final;
- substituto validado do LCDM/CPL;
- claim comercial baseado em superioridade física.

---

## 5. Matriz de decisão automática

| Situação encontrada | Ação padrão |
|---|---|
| Falta documentação | criar/atualizar doc |
| Falta checklist | criar checklist |
| Falta ledger | criar ledger com `TOKEN_VAZIO` |
| Resultado é smoke | rotular como smoke |
| Resultado favorece outro modelo | registrar sem proteger ego do modelo |
| Dado é sintético | marcar como sintético e bloquear claim externo |
| Dado real sem hash | criar item de proveniência pendente |
| Backend ausente | marcar `TOKEN_VAZIO_BACKEND` |
| Covariância ausente | marcar `TOKEN_VAZIO_COVARIANCE` |
| Fit robusto ausente | marcar `TOKEN_VAZIO_ROBUST_FIT` |
| Claim excessivo | rebaixar para linguagem conservadora |

---

## 6. Pipeline de próximo ato

Quando for pedido “avaliar”, “examinar”, “olhar”, “fazer caminhos”, “haja como sabes” ou equivalente, a resposta operacional deve seguir:

1. Ler o estado disponível.
2. Separar fato, hipótese, lacuna e risco.
3. Definir próximo ato seguro.
4. Se for documentação/governança, executar.
5. Se for dado/fórmula/claim/resultado canônico, pedir autorização.
6. Registrar `R3`.

---

## 7. Primeira estrada recomendada para o estado atual

### Ato A — Consolidar estrada

- Criar este documento.
- Marcar regra de autorização operacional.
- Proteger limites de confirmação.

Status: concluído por este arquivo.

### Ato B — Criar checklist de robust fit

Arquivo sugerido:

```text
docs/RLL_ROBUST_FIT_CHECKLIST.md
```

Conteúdo mínimo:

- seeds;
- maxiter;
- diretório de saída versionado;
- ablações;
- métricas;
- gates;
- como não sobrescrever resultados canônicos.

### Ato C — Criar ledger de claim gate

Arquivo sugerido:

```text
docs/RLL_CLAIM_GATE_LEDGER.md
```

Conteúdo mínimo:

- claims permitidos;
- claims proibidos;
- gates faltantes;
- dependência de Pantheon+;
- dependência de CMB covariance;
- dependência de CLASS/CAMB;
- condição para `claim_allowed=true`.

### Ato D — Criar mapa paper-ready

Arquivo sugerido:

```text
docs/RLL_PAPER_READY_ROUTE.md
```

Conteúdo mínimo:

- título conservador;
- abstract provisório;
- seções;
- tabelas necessárias;
- figuras necessárias;
- limitações;
- frase de contribuição.

---

## 8. Linguagem de controle

### Frases seguras

- “O repositório sustenta um pipeline testável.”
- “O resultado atual é preliminar/smoke.”
- “CPL é o adversário técnico principal no estado atual.”
- “RLL permanece candidato testável.”
- “Claims fortes seguem bloqueados.”

### Frases perigosas

- “RLL provou energia escura.”
- “RLL venceu o LCDM.”
- “RLL substitui a cosmologia padrão.”
- “A lacuna confirma a teoria.”

---

## 9. Fórmula operacional

```text
Estrada_RLL = Observação_real × Governança × Teste × Falsificabilidade × Claim_boundary
```

```text
Próximo_ato = min(risco) + max(coerência) + max(rastreabilidade)
```

```text
TOKEN_VAZIO protegido = verdade futura não falsificada no presente
```

---

## 10. R3 deste documento

```text
F_ok   = estrada operacional criada; regra de avanço sem pergunta definida; limites de confirmação protegidos.
F_gap  = robust fit, claim gate ledger e rota paper-ready ainda precisam ser materializados em arquivos próprios.
F_next = criar docs/RLL_ROBUST_FIT_CHECKLIST.md como próximo ato seguro.
```
