# CODEX CONTINUA — RLL Claim Boundary

Status: guia operacional para Codex/agentes.
Data de referência: 2026-06-22.
Escopo: continuar o RLL com rigor de falsificabilidade, sem transformar resultado parcial em vitória física.

## 1. Regra de claim

O RLL deve preservar a separação entre:

- hipótese dinâmica;
- pipeline computacional;
- resultado estatístico;
- interpretação física;
- claim público permitido.

Se um resultado não passa os critérios de comparação, o status correto é candidato sob avaliação, não confirmação.

## 2. Sequência `continua`

```text
1. Ler README.md, docs/RLL_TRACEABILITY_MAP.md e resultados atuais.
2. Identificar o menor limite de claim ainda aberto.
3. Se houver resultado real, comparar com LCDM, wCDM, CPL e RLL.
4. Registrar deltas de chi2, AIC, AICc e BIC.
5. Manter claim_allowed=false se algum critério bloquear superioridade.
6. Criar ou atualizar diagnóstico, não propaganda.
7. Commitar pequeno.
8. Responder F_ok, F_gap, F_next.
```

## 3. Estados permitidos

| Estado | Significado |
|---|---|
| `VERIFIED_RESULT` | resultado reproduzido e registrado |
| `CANDIDATE_MODEL` | hipótese testável ainda não vencedora |
| `CLAIM_BLOCKED` | métricas atuais impedem claim forte |
| `TOKEN_VAZIO` | evidência ainda não localizada |
| `NEEDS_RERUN` | resultado existe, mas precisa repetição robusta |

## 4. Prioridades

1. Reexecutar ou documentar robustez do `joint_real_likelihood`.
2. Aumentar iterações/seeds quando ambiente permitir.
3. Separar aproximação interna de backend físico completo.
4. Criar tabela paper-ready com limites honestos.
5. Conectar novas evidências externas apenas como motivação, não prova.

## 5. Formulação segura

Permitido:

```text
RLL é um candidato de cosmologia dinâmica sob avaliação com dados reais.
```

Bloqueado sem novos resultados:

```text
RLL venceu LCDM/CPL.
RLL confirma a natureza física da energia escura.
RLL possui superioridade estatística consolidada.
```

## 6. Retroalimentação

```text
F_ok: resultado ou limite mais claro.
F_gap: métrica, backend ou dataset ainda faltante.
F_next: próxima repetição, tabela ou diagnóstico.
```
