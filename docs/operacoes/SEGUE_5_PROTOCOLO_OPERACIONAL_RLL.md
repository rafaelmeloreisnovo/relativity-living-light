# SEGUE 5 — Protocolo Operacional RLL

**Status:** protocolo operacional v0.1  
**Data:** 2026-06-16  
**Escopo:** modo de trabalho para cinco comandos consecutivos `Segue` no repositório Relativity Living Light.

---

## 1. Motivo

Este protocolo existe para evitar encaixe solto. Cada `Segue` deve trabalhar com ancoragem, leitura parcial honesta, claim_state, TOKEN_VAZIO e retroalimentacao coerente.

Regra central:

```text
Nao ler o material como hash generico.
Ler por ancora, dependencia, claim, codigo, dado e proximo passo.
```

A imagem do usuario e preservada assim:

```text
nao falar do vermelho generico;
procurar o espectro do vermelho registrado no material.
```

---

## 2. Invariante operacional

Cada ciclo `Segue` deve produzir:

1. `F_ok` — o que foi encontrado com ancora.
2. `F_gap` — o que ainda esta vazio, parcial ou nao lido.
3. `F_next` — uma acao pequena, executavel e reversivel.
4. `Claim boundary` — o que nao pode ser promovido.
5. `Parabola curta` — explicacao ludica sem substituir a prova.

---

## 3. Os cinco ciclos

### Segue 1 — Ancora Canonica

Objetivo: localizar o arquivo mais central para o tema atual.

Prioridade:

```text
docs/CANONICAL_SOURCES.md
docs/canonicos/00_COMO_LER.md
docs/canonicos/13_EPISTEMOLOGIA_RAFAELIA_RLL.md
docs/canonicos/14_MODELO_COSMOLOGICO_RLL.md
docs/canonicos/21_MODELO_VETORIAL_INFORMACIONAL.md
```

Saida esperada:

```text
qual arquivo ancora o tema;
qual arquivo nao deve ser usado como fonte primaria;
qual claim_state inicial usar.
```

### Segue 2 — Leitura por Dependencia

Objetivo: ler dependencias do arquivo central.

Ordem:

```text
norma -> epistemologia -> modelo -> schema -> codigo -> dados
```

Saida esperada:

```text
mapa de dependencias;
linhas ou trechos usados;
TOKEN_VAZIO para dependencia ausente.
```

### Segue 3 — Hotfix de Coerencia

Objetivo: corrigir apenas inconsistencias pequenas e bem ancoradas.

Exemplos:

```text
unidade fisica errada;
claim_state mais forte que o codigo permite;
entropia tratada como certeza absoluta;
metafora promovida como medida.
```

Saida esperada:

```text
patch pequeno;
sem reescrever teoria inteira;
sem criar claim novo sem referencia.
```

### Segue 4 — Integracao Transdisciplinar

Objetivo: conectar fisica, informacao, estatistica, codigo e parabola sem misturar niveis.

Tabela minima:

```text
metafora -> modelo -> variavel -> teste -> referencia -> claim_state
```

Saida esperada:

```text
ponte clara entre linguagens;
nenhum salto METAFORA -> CLAIM_ALLOWED;
registro de refs pendentes.
```

### Segue 5 — Sintese Omega

Objetivo: consolidar o ciclo em forma operacional e didatica.

Saida esperada:

```text
resumo tecnico;
R3;
parabola ludica;
proximo ciclo sugerido;
lista de arquivos tocados.
```

---

## 4. Regra de escrita GitHub

A escrita deve ser pequena, auditavel e reversivel.

Preferencia:

```text
1 arquivo pequeno por ciclo;
ou 1 hotfix pequeno em arquivo canonico;
ou 1 PR curto com descricao neutra.
```

Evitar:

```text
reescrever documento longo sem necessidade;
criar formula forte sem fonte;
remover contexto autoral;
substituir TOKEN_VAZIO por chute.
```

---

## 5. Parabola do carro e do arco circular

O trabalho e como dirigir num arco circular a noite.

O farol mostra apenas um trecho da curva. O motorista nao inventa o resto da estrada. Ele usa o trecho iluminado, o mapa, o painel, o som do motor e a memoria do caminho. Se a neblina aparece, ele nao acelera para fingir certeza; ele reduz, marca o vazio e segue com cuidado.

No RLL, cada `Segue` e um metro iluminado da curva:

```text
farol = evidencia
painel = metrica
mapa = referencia
motor = codigo
neblina = TOKEN_VAZIO
curva = verdade ainda nao totalmente observada
```

---

## 6. R3

```text
F_ok   = modo SEGUE 5 definido para continuidade operacional.
F_gap  = cada ciclo ainda depende de leitura real do tema solicitado.
F_next = usar o primeiro proximo `Segue` para aplicar o ciclo 1: ancora canonica.
```
