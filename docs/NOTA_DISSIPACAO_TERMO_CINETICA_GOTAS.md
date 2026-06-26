# Nota: Dissipacao termo-cinetica em gotas em queda

Status date: 2026-06-26  
Claim state: `COD/MODEL`, not validation  
Escopo: gota de chuva, arrasto, calor, movimento molecular, evaporacao e fronteira de claim.

## 1. Ideia central

Uma gota em queda nao deve ser descrita apenas pela forma externa. Ela tambem deve ser descrita por um balanco de energia na interface gota-ar.

Leitura fisica simples:

```text
queda -> velocidade relativa -> arrasto -> dissipacao -> calor local + turbulencia + oscilacao + evaporacao
```

O ponto correto e:

```text
se ha atrito ou arrasto, ha dissipacao de energia mecanica;
se ha dissipacao, parte dessa energia aparece como movimento molecular e calor;
se o corpo e liquido, a superficie tambem pode deformar, oscilar, trocar calor e evaporar.
```

## 2. Fronteira de claim

Esta nota nao afirma nova fisica fundamental.

Ela apenas organiza a descricao:

```text
gota de chuva = forma + camada-limite + tensao superficial + dissipacao termo-cinetica + evaporacao
```

Uso permitido:

```text
A gota em queda e um sistema interfacial deformavel; o arrasto redistribui energia mecanica em turbulencia, calor local, oscilacao da superficie e processos termicos.
```

Uso proibido sem medicao:

```text
A gota sempre aquece muito apenas por cair.
O atrito da gota prova uma nova lei fisica.
A forma da gota valida RLL cosmologico.
```

## 3. Balanco qualitativo

Quando a gota cai, a gravidade fornece energia ao movimento. O arrasto impede aceleracao indefinida. Ao se aproximar do regime de velocidade terminal, a energia que nao vira aumento de velocidade passa a ser redistribuida no sistema gota-ar.

Canais principais:

- movimento turbulento no ar;
- aquecimento viscoso local;
- oscilacao e deformacao da superficie;
- evaporacao;
- troca de calor entre gota e ar.

Claim boundary:

```text
O atrito gera calor, mas a temperatura final da gota depende tambem do ar, da umidade, da evaporacao, do tamanho da gota e do tempo de queda.
```

## 4. Descricao RAFAELIA

```text
psi: gota entra em queda
chi: ar mede a gota por pressao, arrasto e temperatura
rho: ruido aparece como turbulencia, calor local e oscilacao
Delta: a interface distribui energia entre forma, calor e evaporacao
Sigma: regime quase-estavel de queda
Omega: equilibrio dinamico entre movimento, forma e troca termica
```

## 5. Relacao com a borda multiescala

Esta nota complementa:

```text
docs/CONVERGENCIA_BORDA_MULTIESCALA_BIOMIMETICA.md
```

A ampliacao proposta e:

```text
Borda Multiescala -> Interface Termo-Cinetica -> Balanco Forma/Calor/Evaporacao
```

Assim, a gota nao e apenas um perfil aerodinamico. Ela e uma interface viva no sentido fisico: uma fronteira deformavel onde energia mecanica, calor, movimento molecular, evaporacao e forma se acoplam.

## 6. Fontes para leitura

- NASA GPM, `The Anatomy of a Raindrop`: https://gpm.nasa.gov/education/videos/anatomy-raindrop
- Loftus and Wordsworth, `The Physics of Falling Raindrops in Diverse Planetary Atmospheres`: https://arxiv.org/abs/2102.09570
- Wet-bulb temperature / evaporative cooling reference: https://en.wikipedia.org/wiki/Wet-bulb_temperature

## 7. Fechamento

Descricao defensavel:

> A gota em queda e um sistema interfacial deformavel. O arrasto nao apenas modela a forma; ele tambem participa de um balanco termo-cinetico, redistribuindo energia mecanica em turbulencia, calor local, oscilacao, evaporacao e troca termica. O conhecimento descritivo mais amplo nao e uma nova fisica, mas uma taxonomia melhor: forma e temperatura devem ser lidas juntas como efeitos de interface.

Retroalimentacao:

```text
F_ok: atrito/arrasto foi incorporado como dissipacao termo-cinetica.
F_gap: falta quantificar por tamanho, umidade, temperatura e velocidade.
F_next: criar plano de validacao com balanco energetico simples e tabela de regimes.
```
