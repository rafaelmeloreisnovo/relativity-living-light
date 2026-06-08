# RLL Pre-Movement Scale Bridge

## Clean architectural placement

Rafael, sim — essa intuição tem valor, mas precisa ficar no lugar certo da arquitetura. O que aqui é chamado de **pré-movimento** não é uma variável padrão de fundo do ΛCDM, como `H0`, `Omega_m` ou `Omega_Lambda`. Ele é melhor tratado como uma camada de **condições iniciais, energia ligada, perturbações locais, memória dinâmica e relaxação**.

Em linguagem operacional: **não falta uma variável única do ΛCDM; falta explicitar a camada física entre o campo cosmológico médio e os eventos astrofísicos locais**.

Essa camada pode ser real e mensurável, mas não substitui o ΛCDM de fundo. Ela entra como perturbação, crescimento de estrutura, sistemas ligados, fusões, ondas gravitacionais, relaxação, resposta elástica/sísmica e observáveis locais.

## Baseline ΛCDM/RLL que não deve ser misturado

O comparador ΛCDM mínimo usado em análises cosmológicas completas não deve ser reduzido apenas a:

```text
H0
Omega_m
Omega_Lambda
```

O checklist operacional precisa manter separados:

```text
Omega_b_h2
Omega_c_h2
theta_star ou 100theta_MC
tau
ln10_10_As
n_s
Omega_r
N_eff
sum_m_nu
sigma8
S8
fsigma8
D_z
P_k
covariancias reais
parametros nuisance dos datasets
```

Se RLL usa `H0`, `Omega_m`, `Omega_Lambda`, `Os0`, `zt` e `wt`, ele está mexendo no setor de expansão/fundo. A comparação fica incompleta se não declarar o que acontece com bárions, matéria escura fria, radiação, neutrinos, amplitude primordial, inclinação primordial, reionização, crescimento e covariâncias.

## Equação de fundo e limite de escala

No nível de fundo, a expansão homogênea é representada por uma forma como:

```text
H^2(a) = H0^2 [Omega_r a^-4 + Omega_m a^-3 + Omega_k a^-2 + Omega_Lambda]
```

Essa equação não descreve diretamente duas estrelas convergindo, um buraco negro entrando em ringdown, a Lua reverberando após impacto ou órbitas locais reorganizando energia. Esses fenômenos pertencem a outra camada:

```text
perturbacoes sobre o fundo
formacao de estruturas
sistemas ligados gravitacionalmente
ondas gravitacionais
fusoes e perdas orbitais
relaxacao pos-impacto
resposta elastica/sismica
```

## Definição RLL de pré-movimento

A formulação forte é:

> Todo evento observável possui um pré-estado físico mensurável; modelos que ignoram essa camada podem acertar o fundo médio, mas perder a dinâmica de transição, relaxação e memória local.

No vocabulário RLL, esse pré-estado deve ser indexado por escala:

```text
cosmologica
galactica
estelar
planetaria/sismica
local
```

O erro a evitar é transformar a camada local em parâmetro universal sem ponte de escala.

## Duas estrelas, elipses e campos remanescentes

Para o caso de duas estrelas, dois buracos negros ou dois corpos massivos em movimento convergente, o pré-movimento não é místico nem global: ele é o estado vetorial e energético antes da fusão. Antes do evento visível já existem:

```text
massa total
vetores de velocidade convergentes ou divergentes
momento angular orbital
energia orbital ligada
excentricidade
spin
separacao orbital
perda de energia por ondas gravitacionais
potencial gravitacional remanescente
```

Em sistemas com múltiplas órbitas, outras elipses podem ser perturbadas por marés, ressonâncias, encontros próximos, limpeza dinâmica de vizinhança orbital, ejeções e redistribuição de momento angular. O efeito pode formar uma cascata local: um evento altera o campo, o campo altera trajetórias vizinhas, e trajetórias vizinhas reorganizam novas regiões de estabilidade.

Essa linguagem conversa com agrupamentos estelares, sistemas planetários, discos, pares galácticos e ambientes caóticos. Porém a regra permanece: **efeito dominó local não vira parâmetro de fundo cosmológico sem uma ponte quantitativa de escala**.

## Galáxias, Andromeda e Via Láctea

Em escala galáctica, pares como Via Láctea e Andromeda devem ser tratados como dinâmica local/grupal dentro do universo em expansão, não como mudança direta de `H(z)` global. A camada útil para RLL é:

```text
potenciais gravitacionais locais
velocidades peculiares
momento angular de halos
relaxacao dinamica
mergers hierarquicos
memoria de campo em estruturas ligadas
```

Isso permite estudar convergência vetorial, redistribuição de energia, campos remanescentes e cascatas de interação sem confundir grupo local com cosmologia homogênea.

## Termos operacionais sugeridos

```json
{
  "background_parameters": [
    "H0",
    "Omega_m",
    "Omega_Lambda",
    "Omega_b_h2",
    "Omega_c_h2",
    "theta_star",
    "tau",
    "ln10_10_As",
    "n_s"
  ],
  "growth_parameters": [
    "sigma8",
    "S8",
    "fsigma8",
    "D_z",
    "P_k"
  ],
  "local_dynamic_layer": [
    "Phi_pre",
    "E_bound",
    "tau_relax",
    "Q_diss",
    "M_dyn",
    "L_orbital",
    "spin",
    "eccentricity",
    "separation_orbital",
    "gravitational_wave_loss"
  ],
  "claim_boundary": "local dynamic layer cannot be promoted to background cosmology without scale bridge"
}
```

## Tese consolidada

RLL pode explicitar camadas de pré-estado, relaxação e memória dinâmica que o ΛCDM de fundo deixa fora por construção. Isso não é erro do ΛCDM: o ΛCDM de fundo não tenta descrever cada evento local. A contribuição RLL só fica forte quando preserva a separação:

```text
fundo homogeneo = ΛCDM/RLL background
perturbacoes = crescimento de estrutura
eventos locais = astrofisica, sismologia, dinamica orbital
observaveis = dados medidos
```
