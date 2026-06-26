# Registro de convergências independentes RAFAELIA/RLL

Status date: 2026-06-26

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

## Escala 3 -> 8 -> 8+1

```text
3 convergências      -> hat-trick mínimo: merece nota técnica e rastreio.
8 convergências      -> matriz de recorrência: merece registro mestre e claim gate dedicado.
8 + 1 identificador  -> oito eixos externos mais C09 reservado; não é nona prova.
```

Interpretação matemática controlada:

```text
8 eixos externos -> matriz 8x8 de cruzamentos potenciais.
+1 reservado     -> C09 permanece protegido para fóton/plasma já usado no repositório.
```

Portanto, a passagem de oito eixos para um identificador reservado não autoriza linguagem de prova. Ela aumenta disciplina de namespace e rastreabilidade.

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

## Matriz de oito convergências externas

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

## Identificador reservado fora da contagem externa

| ID | Uso reservado | Motivo | Gate obrigatório |
|---|---|---|---|
| C09 | fóton/plasma | já usado no repositório como `C09_photon_massless_dispersion` | não reutilizar C09 para convergências externas |

## Convergências externas fora da série Cxx

| ID externo | Eixo | Padrão observado | Tradução RAFAELIA/RLL | Regime atual | Gate obrigatório |
|---|---|---|---|---|---|
| CONV-NUC-01 | Transmutação nuclear / chrysopoeia por nêutrons de fusão | símbolo histórico de transmutação encontra rota nuclear restrita via `198Hg(n,2n)197Hg -> 197Au` em preprint de fusão | mito/notícia -> preprint -> mecanismo -> pendência -> rota -> teste/TOKEN_VAZIO | `[E][C][H][M]` | tratar como candidata ativa; exige peer review, reprodução neutronics, segurança radiológica e separação química |

## Regra de elevação

A elevação não deve ser escrita como vitória automática. Ela abre um regime de organização, mas não autoriza colisão de identificadores.

```text
C01..C08    = eight_external_convergence_axes
C09         = reserved_internal_photon_plasma_identifier
CONV-NUC-01 = external_convergence_candidate
```

Critério de saída para CONV-NUC-01:

```text
se CONV-NUC-01 for reproduzida -> criar pipeline/teste;
se CONV-NUC-01 for refutada -> registrar falha e manter histórico;
se CONV-NUC-01 ficar sem validação -> manter como hipótese operacional;
se CONV-NUC-01 for usada como prova de RLL -> bloquear por claim boundary.
```

Documento específico:

```text
docs/CONVERGENCIA_NUCLEAR_CHRYSOPOEIA_MAPA_ROTAS.md
```

## Cubo e fatorial: uso permitido da metáfora

A metáfora do cubo/fatorial é permitida apenas como linguagem de complexidade combinatória e deve explicitar o conjunto contado:

```text
8^3 = 512 tríades ordenadas possíveis entre os oito eixos externos
8! = 40320 ordens possíveis entre os oito eixos externos
```

O identificador C09 não entra nessa contagem externa. Ele é uma reserva de namespace para preservar rastreabilidade com o caminho fóton/plasma já existente.

Esses números não são evidência física. Eles indicam que, ao crescer o número de eixos, cresce também o risco de combinações espúrias. Por isso, a matriz precisa de gate, não de entusiasmo solto.

## Frase canônica curta

> O projeto registra convergências independentes como pistas estruturadas. A presença de múltiplas convergências aumenta a relevância heurística e a prioridade de validação, mas não promove automaticamente hipóteses a resultados. Cada eixo precisa atravessar fonte, artefato, métrica e claim boundary.

## Anti-claim obrigatório

Não escrever:

```text
oito convergências ou um C09 reservado provam RAFAELIA/RLL
```

Escrever:

```text
oito eixos de convergência externa justificam uma matriz formal de validação e priorização experimental; C09 fica reservado ao caminho fóton/plasma.
```

## Próximos passos

1. Preencher cada eixo com fontes primárias ou artefatos internos.
2. Separar eixos redundantes de eixos realmente independentes.
3. Criar notas específicas apenas para convergências com fonte e extração técnica.
4. Vincular cada eixo ao claim boundary e ao pipeline quando houver métrica.
5. Manter C09 reservado ao caminho fóton/plasma e CONV-NUC-01 como `candidate_active` externa até reprodução independente ou refutação técnica.
