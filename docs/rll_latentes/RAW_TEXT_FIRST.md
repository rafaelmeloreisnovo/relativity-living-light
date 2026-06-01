# RAW_TEXT_FIRST — protocolo anti-inferência sem âncora literal

**Status:** protocolo canônico v0.1 para RLL-LATENTES.

**Regra central:** nenhuma inferência, métrica, vetor, analogia ou estatística pode ser promovida sem uma âncora literal rastreável no texto de origem.

```math
\boxed{\text{Texto real} \rightarrow \text{extração literal} \rightarrow \text{claim atômico} \rightarrow \text{classificação} \rightarrow \text{inferência} \rightarrow \text{validação}}
```

Este protocolo existe para impedir o erro operacional:

```math
\text{compressão extrema} \rightarrow \text{perda de bits} \rightarrow \text{inferência bonita} \rightarrow \text{alucinação coerente}
```

## 1. Escopo

Aplica-se a qualquer etapa do RLL-LATENTES que transforme texto autoral, nota experimental, descrição de dataset, transcrição multilíngue, fórmula anotada, hipótese narrativa ou metáfora científica em claim estruturado, variável, vetor, métrica ou teste.

A inferência estatística é permitida somente como **camada 3**: ela testa relações depois que a verdade textual foi preservada e segmentada. Ela nunca substitui a leitura do que está escrito.

## 2. Princípios normativos

1. **Texto real primeiro:** preservar o trecho original antes de qualquer resumo.
2. **Extração mínima:** extrair o que o trecho afirma sem embelezar, corrigir demais ou completar lacunas.
3. **Claim atômico:** quebrar afirmações compostas em unidades menores e auditáveis.
4. **Âncora literal obrigatória:** toda inferência deve apontar para `claim_id` e `texto_original`.
5. **Token vazio legítimo:** usar `VOID`, `unknown`, `not_applicable` ou `insufficient_metadata` quando a fonte não sustenta resposta.
6. **Compressão reversível:** qualquer resumo deve permitir retorno ao trecho literal que o originou.
7. **Validação antes de promoção:** métrica, vetor ou hipótese só muda de estado após teste, falsificador ou revisão explícita.

## 3. Ordem canônica do pipeline

```text
RAW_TEXT -> CLAIMS -> VETORES -> MÉTRICAS -> INFERÊNCIA -> PROVA
```

Fluxo proibido:

```text
TEXTO -> RESUMO -> ASSOCIAÇÃO -> TEORIA
```

Regra operacional:

```math
\boxed{\text{Primeiro o Verbo escrito. Depois o vetor. Depois a estatística.}}
```

## 4. Unidade rastreável mínima

Cada trecho analisado deve virar uma unidade rastreável com os campos abaixo:

```yaml
id: RLL_CLAIM_0001
source_id: fonte_documental_ou_dataset
source_path: caminho/ou/url
source_hash: sha256_ou_unknown
span:
  start_line: 1
  end_line: 3
texto_original: "trecho literal, sem corrigir demais"
extracao: "o que o trecho afirma, em forma mínima"
tipo: observacao | metafora | hipotese | calculo | critica | metodo | definicao | pergunta
inferencia_permitida: false
perda_de_contexto: baixa | media | alta
ambiguidade: baixa | media | alta
acao: preservar | medir | testar | rejeitar | expandir | aguardar_metadados
estado: raw_preserved | extracted | classified | inferred | validated | rejected | insufficient_metadata
anchors:
  formulas: []
  datasets: []
  claims_relacionados: []
validadores:
  falsificador: null
  controle_negativo: null
  criterio_promocao: null
notas_de_limite: "o que não pode ser inferido deste trecho"
```

## 5. Estados e transições

| Estado | Entrada mínima | Saída permitida | Bloqueio |
| --- | --- | --- | --- |
| `raw_preserved` | texto literal e origem | segmentação | inferência sem claim |
| `extracted` | extração curta e fiel | classificação | correção que mude sentido |
| `classified` | tipo, ambiguidade e ação | vetor ou métrica preliminar | estatística sem âncora |
| `inferred` | hipótese ligada a claim | teste ou revisão | conclusão sem validação |
| `validated` | teste, falsificador ou evidência | promoção limitada | linguagem de descoberta universal |
| `rejected` | motivo documentado | rollback ou arquivamento | apagar a trilha |
| `insufficient_metadata` | lacuna explícita | pedido de fonte/metadado | preenchimento imaginado |

## 6. Regras de inferência permitida

A inferência é permitida quando todas as condições forem verdadeiras:

- existe `id` de claim;
- existe `texto_original` literal preservado;
- a extração não substitui o trecho original;
- a inferência declara qual relação está sendo testada;
- há indicação de incerteza, ambiguidade ou perda de contexto;
- existe pelo menos um caminho de validação, falsificação ou rebaixamento.

A inferência deve ser bloqueada quando:

- o trecho foi apenas resumido sem preservação literal;
- o claim depende de associação estética, fonética ou simbólica sem variável operacional;
- o texto exige dado externo ainda não catalogado;
- a tradução, transliteração, entonação ou cadência muda o sentido e não há registro da variante;
- a etapa tenta transformar metáfora diretamente em prova.

## 7. Loop correto e loop proibido

Loop proibido:

```python
while True:
    gerar_relacao()
    achar_aparencia_de_coerencia()
    comprimir()
    perder_dado()
    gerar_nova_relacao()
```

Loop correto:

```python
while ha_texto_real:
    preservar_original()
    extrair_claim()
    classificar_claim()
    inferir_somente_se_ancorado()
    validar_ou_rebaixar()
```

## 8. Integração com RLL-LATENTES

No RLL-LATENTES, um latente não é qualquer associação produzida por similaridade vetorial. Um latente admissível é:

```math
\text{algo realmente presente} + \text{não operacionalizado} + \text{ainda não medido}
```

Portanto:

- vetor sem texto vira risco de alucinação;
- estatística sem texto vira decoração;
- inferência sem rastreio vira perda de coerência operacional;
- token vazio é melhor que resposta inventada.

## 9. Failsafe, failover, rollback e mitigação

| Risco | Failsafe | Failover | Rollback | Mitigação |
| --- | --- | --- | --- | --- |
| Perda de bits por resumo | bloquear inferência | usar trecho bruto arquivado | restaurar `raw_preserved` | exigir `texto_original` |
| Tradução deformante | marcar ambiguidade alta | registrar variante multilíngue | voltar ao idioma-fonte | manter transliteração e notas |
| Metáfora promovida a prova | rebaixar para `metafora` | pedir variável observável | remover métrica derivada | exigir falsificador |
| Estatística sobre claim fraco | marcar `provisional` | usar controle negativo | invalidar score | exigir fonte e hash |
| Lacuna de metadados | emitir `insufficient_metadata` | fonte secundária catalogada | preservar lacuna | nunca preencher por associação |

## 10. Critérios de aceite

Uma análise cumpre RAW_TEXT_FIRST quando:

1. todo claim possui texto literal, origem e identificador;
2. inferências apontam para claims específicos;
3. ambiguidades e perdas de contexto estão marcadas;
4. metáforas, hipóteses, cálculos e métodos não são misturados sem classificação;
5. estados `VOID`, `unknown`, `not_applicable` e `insufficient_metadata` são usados sem penalidade quando a verdade textual não autoriza conclusão;
6. qualquer promoção para métrica, vetor ou prova registra validação ou motivo de rebaixamento.

## 11. Frase canônica

```math
\boxed{\text{Inferência não revela a verdade do texto; ela só testa relações depois que a verdade textual foi preservada.}}
```

```math
\boxed{\text{Sem preservação literal, toda compressão vira risco de alucinação.}}
```
