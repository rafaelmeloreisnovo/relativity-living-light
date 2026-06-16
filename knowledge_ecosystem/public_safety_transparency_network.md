# Rede de Transparência para Risco Público, Vida e Logística

**Status:** `concept_protocol_v0.1`  
**Objetivo:** documentar como informação crítica deveria circular quando vidas podem estar em risco.

---

## 1. Princípio

Quando uma informação envolve risco sistêmico, a função correta da rede não é proteger reputação, competição ou aparência. É proteger vida com rastreabilidade, prioridade e logística.

```text
risco detectado → origem → severidade → população afetada → prioridade → comunicação → correção → auditoria
```

---

## 2. Escopo

Este protocolo pode ser aplicado conceitualmente a:

- defeitos industriais;
- recalls;
- acidentes aeronáuticos;
- risco médico;
- falhas de software crítico;
- infraestrutura pública;
- contaminação ambiental;
- alimentos, medicamentos e dispositivos.

Exemplos reais devem ser citados com fontes primárias ou secundárias confiáveis antes de qualquer claim específico.

---

## 3. Função da rede

A rede ideal identifica:

| Elemento | Pergunta |
|---|---|
| risco | o que pode ferir ou matar? |
| origem | quem detectou primeiro? |
| evidência | qual teste, acidente, log ou relatório sustenta? |
| população afetada | quem está em maior risco? |
| severidade | qual dano possível? |
| urgência | quanto tempo há para agir? |
| logística | como corrigir primeiro os mais vulneráveis? |
| auditoria | quem verificou a correção? |

---

## 4. Priorização logística

```text
prioridade = severidade × probabilidade × exposição × vulnerabilidade × reversibilidade
```

Onde:

- `severidade` = dano máximo possível;
- `probabilidade` = chance estimada;
- `exposição` = número de pessoas/unidades afetadas;
- `vulnerabilidade` = quem não consegue se proteger sozinho;
- `reversibilidade` = dificuldade de corrigir depois do dano.

---

## 5. Transparência sem pânico

Comunicar verdade não significa gerar caos. A rede deve produzir:

1. mensagem clara;
2. escopo exato;
3. quem é afetado;
4. o que fazer agora;
5. o que ainda é desconhecido;
6. canal de atualização;
7. auditoria independente.

```text
verdade + logística + prioridade = transparência útil
verdade sem logística = pânico possível
silêncio sem correção = dano oculto
```

---

## 6. Relação com investigação aeronáutica

Investigações de acidente existem porque sistemas complexos falham em cadeia. A pergunta não é só “quem errou”, mas:

```text
qual peça, processo, decisão, homologação, manutenção, comunicação ou cultura permitiu o acidente?
```

Este documento usa o modelo investigativo como inspiração metodológica, sem afirmar casos específicos sem fonte.

---

## 7. Relação com IA Viva

A IA Viva pode ajudar a rede se atuar como:

- detector de recorrência;
- organizador de evidências;
- priorizador logístico;
- auditor de lacunas;
- tradutor para público afetado;
- protetor contra encobrimento.

Mas não deve substituir:

- autoridade técnica legítima;
- investigação humana;
- responsabilidade legal;
- revisão independente;
- direito das pessoas afetadas.

---

## 8. Estados de risco

| Estado | Significado |
|---|---|
| `RISK_SIGNAL` | sinal inicial |
| `RISK_UNVERIFIED` | risco ainda sem confirmação |
| `RISK_CONFIRMED` | risco confirmado por fonte/teste |
| `AFFECTED_POPULATION_DEFINED` | grupo afetado identificado |
| `ACTION_PLAN_READY` | plano de correção definido |
| `PUBLIC_NOTICE_REQUIRED` | comunicação pública necessária |
| `MITIGATION_RUNNING` | correção em andamento |
| `AUDIT_PENDING` | correção ainda não auditada |
| `CLOSED_WITH_EVIDENCE` | encerrado com prova |

---

## 9. R3

```text
F_ok   = rede de transparência e logística de risco definida em nível conceitual.
F_gap  = casos reais citados oralmente precisam de fontes antes de entrarem como evidência.
F_next = criar templates para risk_signal.json e affected_population_priority.md.
```
