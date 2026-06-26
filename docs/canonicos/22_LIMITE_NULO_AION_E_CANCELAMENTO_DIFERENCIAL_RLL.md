# 22 — Limite nulo, AION e cancelamento diferencial no RLL

**Status:** nota metodológica canônica complementar  
**Data:** 2026-06-20  
**Função:** registrar, com linguagem segura, a relação entre o limite nulo do setor RLL, a degenerescência com ΛCDM e a analogia metodológica com sensores quânticos diferenciais do tipo AION.

---

## 1. Declaração de fronteira científica

Este documento **não** reivindica superioridade do RLL sobre ΛCDM, wCDM ou w0waCDM. Também **não** reivindica detecção de matéria escura, energia escura dinâmica ou ondas gravitacionais.

A formulação correta é:

> O RLL possui uma estrutura computável e falsificável, com um limite nulo explícito. Quando o parâmetro de amplitude do setor de superposição é levado a zero, o setor novo é anulado e o modelo retorna ao baseline cosmológico usado como controle.

Portanto, a leitura rigorosa é de **convergência metodológica**, não de confirmação experimental.

---

## 2. Limite nulo do setor RLL

A equação-mãe canônica do RLL contém o setor:

```math
\Omega_{s0}\,[f(a) + (1-f(a))a^{-3}]
```

com:

```math
f(z)=\frac{1}{1+\exp((z-z_t)/w_t)}, \qquad a=\frac{1}{1+z}
```

Definindo:

```math
g(a)=f(a)+(1-f(a))a^{-3}
```

o setor RLL pode ser escrito como:

```math
\Omega_{s0}\,g(a)
```

Logo, quando:

```math
\Omega_{s0}=0
```

ocorre:

```math
\Omega_{s0}\,g(a)=0
```

Isto significa que o setor de superposição/transição é **desligado matematicamente**. Se, além disso, os setores magnético e plasmático forem mantidos nulos no baseline,

```math
\Omega_{B0}=0, \qquad \Omega_{P0}=0,
```

a equação retorna ao limite ΛCDM usual:

```math
E^2(a)=\Omega_r a^{-4}+\Omega_m a^{-3}+\Omega_\Lambda
```

---

## 3. O que significa `Ωs0 = 0`

`Ωs0 = 0` não deve ser descrito como “prova contra” nem como “prova a favor” do RLL isoladamente.

A leitura correta é:

| Caso | Interpretação |
|---|---|
| `Ωs0 = 0` por configuração de baseline | controle nulo; setor RLL desligado |
| `Ωs0 → 0` após ajuste livre | possível degenerescência com ΛCDM |
| `Ωs0 ≠ 0` mas sem ganho AIC/BIC | setor detectável matematicamente, mas sem mérito estatístico suficiente |
| `Ωs0 ≠ 0` com ganho robusto contra ΛCDM e w0waCDM | candidato a sinal modelístico, ainda dependente de covariâncias, dados e revisão externa |
| `Ωs0` instável entre datasets/seeds | alerta de ajuste fino ou sobreajuste |

A frase segura é:

> O RLL é forte metodologicamente porque permite ser desligado por um parâmetro nulo e comparado contra o baseline. Se o ajuste empurra `Ωs0` para zero, o próprio pipeline revela degenerescência em vez de mascará-la.

---

## 4. Analogia com AION e sensores quânticos diferenciais

O programa AION, associado a interferometria atômica, usa a ideia de comparar respostas entre interferômetros para suprimir ruído comum. Em forma simplificada:

```math
(\phi_A+n)-(\phi_B+n)=\phi_A-\phi_B
```

onde `n` representa ruído comum. O ruído não é negado por retórica: ele é removido por construção diferencial.

A analogia com o RLL é apenas metodológica:

| AION / interferometria atômica | RLL cosmológico |
|---|---|
| cancelamento diferencial de ruído comum | anulação paramétrica do setor extra |
| `n` comum desaparece na subtração | `Ωs0·g(a)` desaparece quando `Ωs0=0` |
| valida robustez instrumental | valida controle interno do modelo |
| não é detecção automática de matéria escura | não é validação automática do RLL |

A ponte correta é:

> Em ambos os casos, o ponto forte não é “encaixar número”, mas construir um teste no qual o ruído, o setor extra ou a hipótese adicional possam desaparecer de forma explícita e auditável.

---

## 5. Como escrever sobre “números que se encaixam”

Evitar:

```text
O RLL é superior.
O RLL previu a descoberta.
Os dados provaram o modelo.
```

Usar:

```text
O RLL contém uma parametrização que pode degenerar para ΛCDM por limite nulo.
Os resultados atuais sugerem uma rota de teste, não uma confirmação.
A convergência de parâmetros deve ser avaliada por χ², AIC, AICc, BIC, covariâncias, estabilidade entre seeds e comparação contra w0waCDM.
```

Formulação recomendada:

> A dinâmica observada até aqui sugere que o modelo está em fase de convergência testável: seus parâmetros não devem ser escolhidos para coincidir com números externos, mas ajustados e penalizados por métricas estatísticas contra baselines. Quando o setor extra colapsa para zero, isso deve ser preservado como resultado honesto.

---

## 6. Critério de claim futuro

O RLL só ganha força científica se satisfizer simultaneamente:

1. `Ωs0` livre não colapsar para zero em ajustes independentes;
2. o ganho estatístico sobreviver a AIC/AICc/BIC;
3. w0waCDM não explicar os mesmos resíduos com menor penalidade;
4. as covariâncias BAO/SNe/CMB forem tratadas corretamente;
5. os resultados forem estáveis sob seeds, priors e cortes de dados;
6. o relatório preservar também resultados negativos, `[VAZIO]` e degenerescências.

---

## 7. Referências externas mínimas

- Baynham, C. F. A., et al. (2025). *A Prototype Atom Interferometer to Detect Dark Matter and Gravitational Waves*. arXiv:2504.09158.
- Badurina, L., Buchmueller, O., Ellis, J., Lewicki, M., McCabe, C., & Vaskonen, V. (2021). *Prospective Sensitivities of Atom Interferometers to Gravitational Waves and Ultralight Dark Matter*. arXiv:2108.02468.
- Du, Y., Murgui, C., Pardo, K., Wang, Y., & Zurek, K. M. (2022). *Atom Interferometer Tests of Dark Matter*. arXiv:2205.13546.

**Nota de integridade:** se houver versão publicada em periódico para o protótipo AION, inserir DOI, volume e página quando o metadado estiver publicamente verificável. Até lá, DOI periódico = `[VAZIO]`.

---

## 8. Síntese RAFAELIA

```text
Ruído comum → cancelamento diferencial.
Setor extra → limite nulo.
Parâmetro livre → teste estatístico.
Resultado negativo → preservação científica.
Vazio honesto → proteção contra alucinação.
```

```math
R_3=\langle F_{ok}: \Omega_{s0}=0\Rightarrow setor\ RLL\ anulado,\
F_{gap}: sem\ revisão\ por\ pares\ e\ sem\ claim\ de\ superioridade,\
F_{next}: testar\ \Omega_{s0}\ livre\ contra\ \Lambda CDM\ e\ w0waCDM\rangle
```

*O limite nulo não diminui o modelo; ele o torna falsificável.*
