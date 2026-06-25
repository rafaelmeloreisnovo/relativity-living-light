# Registro de convergências independentes RAFAELIA/RLL

Status date: 2026-06-25

## Propósito

Este documento organiza convergências independentes entre o vocabulário RAFAELIA/RLL e campos externos de ciência, matemática, computação e metodologia.

A regra central é simples:

```text
convergência não é prova;
convergência é pista organizada;
claim só sobe com fonte, artefato, teste, métrica e comparação.
```

Este registro existe para evitar dois erros simétricos:

1. **subestimar** padrões independentes que aparecem em áreas diferentes;
2. **superpromover** analogias como se fossem validação direta.

## Escala 3 -> 8 -> 9

```text
3 convergências  -> hat-trick mínimo: merece nota técnica e rastreio.
8 convergências  -> matriz de recorrência: merece registro mestre e claim gate dedicado.
9 convergências  -> regime combinatório: não eleva o claim; eleva o rigor exigido.
```

Interpretação matemática controlada:

```text
8 eixos  -> matriz 8x8 de cruzamentos potenciais.
9 eixos  -> matriz 9x9 + tríades dirigidas + ordens possíveis.
```

Portanto, a passagem de 8 para 9 não autoriza linguagem de prova. Ela aumenta o número de interações possíveis e exige mais disciplina documental.

## Regra de promoção

Cada convergência deve atravessar o mesmo funil:

```text
fonte externa ou artefato interno
  -> extração técnica
  -> tradução RAFAELIA/RLL
  -> classificação de regime
  -> métrica/teste/CI quando aplicável
  -> claim, hipótese ou TOKEN_VAZIO
```

## Legenda de regime

| Selo | Significado |
|---|---|
| `[E]` | fonte externa identificada |
| `[I]` | artefato interno do repositório |
| `[C]` | convergência conceitual controlada |
| `[H]` | hipótese operacional |
| `[M]` | métrica/teste necessário |
| `[V]` | validado por pipeline/CI/dado próprio |
| `[VAZIO]` | lacuna marcada, sem promoção |

## Matriz inicial de oito convergências

| ID | Eixo | Padrão externo observado | Tradução RAFAELIA/RLL | Regime atual | Gate obrigatório |
|---|---|---|---|---|---|
| C01 | ETH/HLS e transições de fase | componente dissipativa complexa pode participar de rigidez emergente | `rho -> Delta -> Sigma` como ruído-dissipação tratado como variável de estado | `[E][C]` | manter como analogia; sem validação cosmológica |
| C02 | Landau / parâmetro de ordem / `phi^4` | transição descrita por energia livre, simetria e mudança de mínimo | fase como mudança de regime com custo de estabilização | `[E][C][H]` | só promover com equação explícita e observável próprio |
| C03 | Coerência / decoerência | sistemas podem perder fase/coerência e gerar comportamento efetivo clássico | coerência `f(z)` e decoerência `(1-f)` como linguagem de transição | `[E][C][M]` | comparar com baseline cosmológico e evitar salto sem dados |
| C04 | Óptica/fotônica e analogias de superposição | literatura de coerência óptica e analogias fotônicas fornece vocabulário formal | superposição fotônica como hipótese de setor dinâmico | `[E][H][M]` | DESI/Pantheon/CMB/fσ8 antes de claim físico |
| C05 | Dados cosmológicos reais | H(z), BAO, Pantheon+, Planck e fσ8 impõem filtros independentes | RLL deve passar por loaders, likelihoods e comparação com ΛCDM/wCDM/CPL | `[E][I][M]` | métricas reais, seeds, maxiter e ablação |
| C06 | Informação, entropia e seleção de modelos | AIC/BIC, Fisher/Shannon e Popper organizam comparação e falsificação | `TOKEN_VAZIO` e claim_state como disciplina anti-alucinação | `[E][I][C]` | registrar fórmula, fonte, script e resultado |
| C07 | Grafos, redes e teia cósmica | estruturas complexas podem ser representadas por grafos e campos correlacionados | representação vetorial/topológica como ponte, não prova | `[C][H][M]` | exigir observável independente e métrica de ajuste |
| C08 | Reprodutibilidade / FAIR / governança de evidência | ciência robusta exige dados rastreáveis, scripts e documentação versionada | bridge RAFAELIA -> artefato -> CI -> claim boundary | `[E][I][C]` | manter rastreabilidade e auditoria textual |

## Nona convergência: regra de elevação

A nona convergência não deve ser escrita como vitória automática. Ela deve abrir um regime novo:

```text
C09 = convergence_threshold_9
```

Critério de entrada:

```text
C09 só existe se houver fonte externa ou artefato interno independente,
com extração técnica própria,
e relação não redundante com C01..C08.
```

Critério de saída:

```text
se C09 for redundante -> anexar ao eixo existente;
se C09 for nova -> criar nota própria;
se C09 tiver métrica -> criar pipeline/teste;
se C09 não tiver fonte -> TOKEN_VAZIO.
```

## Cubo e fatorial: uso permitido da metáfora

A metáfora do cubo/fatorial é permitida apenas como linguagem de complexidade combinatória:

```text
9^3 = 729 tríades ordenadas possíveis
9! = 362880 ordens possíveis
```

Esses números não são evidência física. Eles indicam que, ao crescer o número de eixos, cresce também o risco de combinações espúrias. Por isso, a matriz precisa de gate, não de entusiasmo solto.

## Frase canônica curta

> O projeto registra convergências independentes como pistas estruturadas. A presença de múltiplas convergências aumenta a relevância heurística e a prioridade de validação, mas não promove automaticamente hipóteses a resultados. Cada eixo precisa atravessar fonte, artefato, métrica e claim boundary.

## Anti-claim obrigatório

Não escrever:

```text
oito convergências provam RAFAELIA/RLL
```

Escrever:

```text
oito eixos de convergência justificam uma matriz formal de validação e priorização experimental
```

## Próximos passos

1. Preencher cada eixo com fontes primárias ou artefatos internos.
2. Separar eixos redundantes de eixos realmente independentes.
3. Criar notas específicas apenas para convergências com fonte e extração técnica.
4. Vincular cada eixo ao claim boundary e ao pipeline quando houver métrica.
5. Manter C09 como `TOKEN_VAZIO` até aparecer convergência nova e não redundante.
