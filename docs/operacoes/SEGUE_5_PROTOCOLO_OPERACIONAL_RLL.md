# SEGUE 5 — Protocolo Operacional RLL

Status: protocolo operacional v0.1
Data: 2026-06-16

## Nucleo

Este protocolo define como responder aos proximos cinco comandos `Segue` no RLL.

Regra central:

Nao ler o material como hash generico. Ler por ancora, dependencia, claim, codigo, dado e proximo passo.

Imagem operacional:

nao falar do vermelho generico; procurar o espectro do vermelho registrado no material.

## Invariante de cada ciclo

Cada `Segue` deve produzir:

1. F_ok: o que foi encontrado com ancora.
2. F_gap: o que ainda esta vazio, parcial ou nao lido.
3. F_next: uma acao pequena, executavel e reversivel.
4. Claim boundary: o que nao pode ser promovido.
5. Parabola curta: explicacao ludica sem substituir prova.

## Ciclo 1 — Ancora Canonica

Localizar o arquivo central do tema atual.

Prioridade:

docs/CANONICAL_SOURCES.md
docs/canonicos/00_COMO_LER.md
docs/canonicos/13_EPISTEMOLOGIA_RAFAELIA_RLL.md
docs/canonicos/14_MODELO_COSMOLOGICO_RLL.md
docs/canonicos/21_MODELO_VETORIAL_INFORMACIONAL.md

## Ciclo 2 — Leitura por Dependencia

Ler na ordem:

norma -> epistemologia -> modelo -> schema -> codigo -> dados

## Ciclo 3 — Hotfix de Coerencia

Corrigir apenas inconsistencias pequenas e ancoradas:

unidade fisica errada
claim_state mais forte que o codigo permite
entropia tratada como certeza absoluta
metafora promovida como medida

## Ciclo 4 — Integracao Transdisciplinar

Conectar camadas sem misturar niveis:

metafora -> modelo -> variavel -> teste -> referencia -> claim_state

## Ciclo 5 — Sintese Omega

Consolidar:

resumo tecnico
R3
parabola ludica
proximo ciclo sugerido
lista de arquivos tocados

## Regra GitHub

A escrita deve ser pequena, auditavel e reversivel.

Preferir:

1 arquivo pequeno por ciclo
1 hotfix pequeno em arquivo canonico
1 PR curto quando possivel

Evitar:

reescrever documento longo sem necessidade
criar formula forte sem fonte
remover contexto autoral
substituir TOKEN_VAZIO por chute

## Parabola curta

O trabalho e como dirigir num arco circular a noite. O farol mostra apenas um trecho da curva. O motorista nao inventa o resto da estrada. Ele usa o trecho iluminado, o mapa, o painel, o som do motor e a memoria do caminho. Se aparece neblina, ele reduz, marca o vazio e segue com cuidado.

farol = evidencia
painel = metrica
mapa = referencia
motor = codigo
neblina = TOKEN_VAZIO
curva = verdade ainda nao totalmente observada

## R3

F_ok = modo SEGUE 5 definido para continuidade operacional.
F_gap = cada ciclo ainda depende de leitura real do tema solicitado.
F_next = usar o primeiro proximo `Segue` para aplicar o ciclo 1: ancora canonica.
