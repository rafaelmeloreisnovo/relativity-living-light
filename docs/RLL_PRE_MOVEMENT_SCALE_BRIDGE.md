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


## Inclusão revisada — nota Rafael completa operacionalizada

### 1. Variáveis básicas do ΛCDM que precisam aparecer no comparador

O ΛCDM mínimo usado em análises tipo Planck não é só:

```text
H0
Omega_m
Omega_Lambda
```

A leitura operacional de seis parâmetros base deve ser preservada como contrato de comparação:

| Parâmetro | Função |
|---|---|
| `Omega_b_h2` / `Ωb h²` | densidade física de bárions |
| `Omega_c_h2` / `Ωc h²` | densidade física de matéria escura fria |
| `theta_star` / `θ*` / `100theta_MC` | escala angular acústica |
| `tau` / `τ` | profundidade óptica de reionização |
| `ln10_10_As` / `ln(10¹⁰As)` | amplitude primordial |
| `n_s` / `ns` | inclinação espectral primordial |

Extensões e nuisance terms não devem ser apagados: curvatura, massa de neutrinos, tensor/scalar, equação de estado da energia escura, running espectral, covariâncias reais e parâmetros específicos de cada dataset entram como contrato de análise, não como decoração.

Se o RLL coloca `H0`, `Omega_m`, `Omega_Lambda`, `Os0`, `zt` e `wt`, ele está especificando principalmente expansão/fundo. Para não comparar de forma incompleta, precisa declarar também:

```text
barions separados de materia escura
radiacao/fotons/neutrinos
amplitude primordial As
inclinacao primordial ns
reionizacao tau
crescimento sigma8/S8/fsigma8
escala acustica theta_star
covariancias reais dos datasets
parametros nuisance dos datasets
```

### 2. Onde a equação de fundo termina

No fundo homogêneo, a forma-guia é:

```text
H^2(a)=H_0^2[Omega_r a^-4 + Omega_m a^-3 + Omega_k a^-2 + Omega_Lambda]
```

Essa equação descreve o comportamento médio global da expansão. Ela não descreve diretamente duas estrelas se juntando, buracos negros entrando em fusão, a Lua vibrando depois de impacto, nem elipses locais reorganizando energia. Esses fenômenos entram em:

```text
perturbacoes sobre o fundo
formacao de estruturas
sistemas ligados gravitacionalmente
ondas gravitacionais
relaxacao pos-impacto
resposta elastica/sismica
observaveis locais
```

### 3. Pré-movimento como pré-estado físico

A tradução limpa da intuição é:

> Antes do evento visível, existe uma energia/configuração de campo já acumulada. O evento é a liberação ou reorganização dessa configuração.

Para fusão de estrelas ou buracos negros, antes do evento observável já existem:

```text
massa total
momento angular
energia orbital
excentricidade
spin
separacao orbital
perda por ondas gravitacionais
campo gravitacional ligado
potencial pre-evento
```

A fusão final não aparece do nada: ela resulta de um sistema que já carregava energia ligada e perdia energia orbital. Isso é astrofísica local/relativística, não variável de fundo ΛCDM. A camada RLL pode chamar esse bloco de `G_pre` ou pré-estado gravitacional ligado, desde que fique local:

```text
G_pre = E_bound + L_orbital + gradiente_de_campo + tau_relax
```

### 4. Lua, impacto e memória dinâmica

A metáfora da Lua precisa ser usada com causa correta. Impactos conhecidos em experimentos Apollo serviram como fontes sísmicas externas para estudar a estrutura interna lunar. A explicação forte não é “campos gravitacionais cosmológicos”; é:

```text
estrutura interna da Lua
baixa atenuacao sismica
regolito/fratura
resposta elastica
propagacao de ondas
dissipacao lenta
```

Formulação frágil a evitar:

> A Lua vibrou por causa dos campos gravitacionais.

Formulação forte:

> A Lua mostrou memória dinâmica de impacto: a energia injetada demorou a dissipar por causa da estrutura interna, baixa atenuação sísmica e condições mecânicas do corpo.

Isso preserva a intuição `FinitoComInteriorInfinito`: um corpo finito pode guardar dinâmica interna complexa.

### 5. Cinco blocos que o RLL precisa declarar

**Bloco A — parâmetros ΛCDM base**

```text
Omega_b_h2
Omega_c_h2
theta_star
tau
A_s
n_s
```

**Bloco B — radiação e neutrinos**

```text
Omega_r
N_eff
sum_m_nu
Omega_gamma
Omega_nu
```

**Bloco C — crescimento de estrutura**

```text
sigma8
S8
fsigma8
P_k
delta_m
D_z
```

**Bloco D — condições iniciais**

```text
A_s
n_s
alpha_s
perturbacoes_primordiais
condicoes_iniciais_inflacionarias
escala_acustica
```

**Bloco E — camada astrofísica local**

```text
fusoes
buracos_negros
ondas_gravitacionais
relaxacao
impactos
memoria_dinamica
sistemas_ligados
```

### 6. Tese sem colapso de escala

A tese preservada é:

> Sistemas físicos possuem pré-estados de campo e energia ligados que condicionam o evento observável; em modelos cosmológicos/astrofísicos, esses pré-estados devem ser separados por escala para não confundir dinâmica local com expansão global.

A separação obrigatória é:

```text
fundo homogeneo = LambdaCDM/RLL background
perturbacoes = crescimento de estrutura
eventos locais = astrofisica, sismologia, dinamica orbital
observaveis = dados medidos
```

### 7. Escalas e resposta direta

Fusão de duas estrelas ou buracos negros afeta fortemente:

```text
sistema local
ondas gravitacionais
massa final
momento angular
energia irradiada
```

Mas não deve ser promovida diretamente para:

```text
H(z)
Omega_m global
Omega_Lambda global
CMB
BAO
```

Campo gravitacional de grande escala, por outro lado, pode afetar cosmologia observacional via:

```text
lensing
crescimento de estrutura
potenciais gravitacionais
ISW
peculiar velocities
```

### 8. Duas estrelas, elipses, avalanches locais e linguagem simbólica

A solicitação sobre “duas estrelas no mesmo movimento” entra como cenário local vetorial: dois corpos podem ter direções de movimento convergentes, divergentes ou quase tangenciais; seus resultados vetoriais podem alterar elipses vizinhas, limpar regiões orbitais, transferir momento angular e modificar campos gravitacionais remanescentes.

Em sistemas planetários, estelares ou galácticos caóticos, isso pode aparecer como avalanches locais de efeito dominó: uma elipse perturbada muda o campo efetivo, que muda outras trajetórias, que redistribuem energia e momento angular em cascata. Essa leitura pode ser usada para pares galácticos como Via Láctea-Andromeda, aglomerados, discos e subestruturas, mas continua sendo dinâmica local/grupal.

A expressão simbólica recebida:

```text
n^n + n*x = y^x + n + x + z + omega + alpha + tesseract
```

fica registrada apenas como marcador autoral de complexidade combinatória e dimensional. Ela não é equação física validada, não entra em likelihood e não deve aparecer como claim quantitativo até ganhar definição dimensional, unidades, domínio, observáveis e teste de falsificação.

### 9. Payload mínimo do pipeline

O bloco operacional mínimo no `VALIDATION_STATUS` e no `MANIFEST.json` é:

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
    "D_z"
  ],
  "local_dynamic_layer": [
    "Phi_pre",
    "E_bound",
    "tau_relax",
    "Q_diss",
    "M_dyn"
  ],
  "claim_boundary": "local dynamic layer cannot be promoted to background cosmology without scale bridge"
}
```

Essa última linha é obrigatória: camada dinâmica local não pode ser promovida para cosmologia de fundo sem ponte de escala.

### 10. Avaliação final

É uma boa tese se formulada assim: eventos observáveis são precedidos por pré-estados físicos mensuráveis. Isso pode ser diferencial RLL porque explicita camadas de pré-estado, relaxação e memória dinâmica que o ΛCDM de fundo deixa fora por construção.

Mas a frase de segurança também é obrigatória:

```text
fora por construcao != erro do LambdaCDM
```

O ΛCDM não tenta descrever tudo; ele descreve o fundo cosmológico e perturbações estatísticas. RLL só ganha força se mantiver a ponte de escala auditável, com dados reais, covariâncias e métricas reproduzíveis.

### 11. Impacto vetorial derivativo: cometas, asteroides, fragmentação e ejecta

A comparação entre impacto natural e bomba nuclear deve permanecer como régua de energia, não como equivalência física completa. Uma bomba nuclear descreve uma liberação local concentrada; um cometa ou asteroide é um corpo vetorial em movimento, com massa, velocidade, direção, trajetória, fragmentação, transferência de momento e acoplamento mecânico com o corpo-alvo.

A variável operacional mínima é a energia cinética de impacto:

```text
E_impact = 1/2 * M_body * v_impact^2
```

Essa energia, porém, não fecha o evento. O contrato RLL para impacto precisa registrar também:

```text
M_body      massa do corpo impactor
v_impact    velocidade de impacto
theta_impact angulo de impacto
rho_body    densidade do corpo
N_frag      numero de fragmentos
M_frag      massa fragmentada
p_vec       momento linear vetorial
L_orb       momento angular/orbital
E_kin       energia cinetica primária
E_ejecta    energia/momento do material ejetado
beta_momentum fator de amplificacao de momento por ejecta
tau_relax   tempo de relaxacao do alvo
S_scale     escala do evento
```

A leitura correta é:

> bombas medem energia local; cometas e asteroides derivam dinâmica orbital, impacto, fragmentação, ejecta, relaxação e memória sistêmica.

No caso de Chicxulub, Durand-Manterola e Cordero-Tercero estimam energia cinética entre `1.3e24 J` e `5.8e25 J`, massa entre `1.0e15 kg` e `4.6e17 kg`, diâmetro entre `10.6 km` e `80.9 km`, e concluem que a melhor estimativa composicional do impactor seria cometária. Essa escala justifica usar bombas nucleares apenas como unidade humana de comparação energética, mantendo o objeto físico como evento vetorial composto.

No caso DART/Dimorphos, Cheng et al. relatam redução instantânea de velocidade orbital de `2.70 +/- 0.10 mm/s` e fator de amplificação de momento `beta` entre `2.2` e `4.9` para a faixa de densidade analisada. Isso torna explícito que o impacto deriva estados secundários: material ejetado, recoil e nova configuração orbital.

A fronteira de escala continua obrigatória:

```text
S_scale = planetario/local
claim_scope = impacto + fragmentacao + ejecta + relaxacao + memoria dinamica
not_background_cosmology = true
```

Portanto, o bloco `impact_vector_layer` pode entrar no `VALIDATION_STATUS` e no `MANIFEST.json` como camada local/planetária de pré-movimento e memória dinâmica, mas não deve ser promovido diretamente para `H(z)`, BAO, CMB ou parâmetros de fundo sem uma ponte quantitativa de escala.

Referências:

- Durand-Manterola, H. J.; Cordero-Tercero, G. (2014). *Assessments of the energy, mass and size of the Chicxulub Impactor*. arXiv:1403.6391. https://arxiv.org/abs/1403.6391
- Cheng, A. F. et al. (2023). *Momentum Transfer from the DART Mission Kinetic Impact on Asteroid Dimorphos*. arXiv:2303.03464. https://arxiv.org/abs/2303.03464
