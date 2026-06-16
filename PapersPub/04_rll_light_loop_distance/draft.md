# RLL Light-Loop Distance: Propagação da Luz, Densidade de Acoplamento e Limites de Claim

**Status:** `draft_paper_v0.1`  
**Repositório:** `instituto-Rafael/relativity-living-light`  
**Trilha:** `PapersPub/04_rll_light_loop_distance`  
**Preparado em:** `2026-06-16`  
**Autor/Instituição:** Instituto Rafael / Rafael Melo Reis  
**Claim boundary:** este documento não afirma que fótons perdem energia por distância no vácuo ideal. Ele separa física padrão, analogia RLL, hipótese operacional e lacunas bibliográficas.

---

## 1. Pergunta de origem

A pergunta de origem foi:

```text
No RLL, a distância da luz vai perdendo a capacidade dos loops, tendo dispersão.
Seria uma raiz quadrada a cada metro? Como funciona isso no vácuo?
```

Este documento organiza a pergunta sem plágio e sem overclaim.

A formulação segura é:

```text
A luz no vácuo ideal não perde energia por atrito ou cansaço do fóton.
O que decai com a distância é a densidade de energia/acoplamento observável,
por geometria, difração, divergência de feixe ou perda de coerência operacional.
```

---

## 2. Encaixe no RLL

Dentro do RLL, esta peça deve ser tratada como:

```text
CONCEPT_000003 = Light-Loop Coupling Capacity
FORMULA_000002 = C_loop(r)
CLAIM_STATE = HIPOTESE + SOURCE_LINKED_PARTIAL
```

Não deve ser tratada como:

```text
CLAIM_ALLOWED: luz perde energia intrínseca por metro no vácuo
```

A expressão “capacidade dos loops” pode ser definida como uma grandeza RLL de acoplamento, não como propriedade física já estabelecida do fóton:

```text
C_loop = capacidade de reentrada, acoplamento, coerência ou utilidade do sinal no modelo RLL
```

---

## 3. Física padrão mínima

### 3.1 Fonte pontual isotrópica

Para uma fonte pontual isotrópica ideal, a potência se espalha por uma esfera de área:

```text
A(r) = 4πr²
```

Logo, a irradiância/intensidade cai como:

```text
I(r) = P / (4πr²)
```

Então:

```text
I(r) ∝ 1/r²
```

A amplitude/campo associado escala como a raiz da intensidade:

```text
A_field(r) ∝ √I(r) ∝ 1/r
```

Portanto, se RLL chamar `C_loop` de intensidade, a escala natural é `1/r²`; se chamar de amplitude/acoplamento de campo, a escala natural é `1/r`.

---

## 4. Onde a raiz quadrada entra

A raiz quadrada aparece porque intensidade é proporcional ao quadrado da amplitude:

```text
I ∝ |A|²
A ∝ √I
```

Assim, não é correto afirmar sem definição:

```text
A luz perde raiz quadrada a cada metro.
```

A formulação correta é:

```text
A amplitude de uma onda esférica ideal cai como 1/r,
que é a raiz quadrada da queda de intensidade 1/r².
```

---

## 5. Feixes gaussianos e distância de Rayleigh

Se a luz for tratada como feixe colimado/laser, a lei esférica simples não é suficiente. Um feixe gaussiano em propagação livre possui raio:

```text
w(z) = w0 × √(1 + (z/zR)²)
```

Onde:

```text
zR = πw0² / λ
```

No comprimento de Rayleigh, a área do feixe dobra e o raio aumenta por `√2`.

Isso é o melhor encaixe para uma intuição de “raiz” ligada a distância, mas ela se refere à abertura do feixe, não à perda de energia intrínseca do fóton.

---

## 6. Dispersão no vácuo

No vácuo ideal clássico, ondas eletromagnéticas possuem relação linear:

```text
ω = c k
```

Isso implica velocidade de fase e grupo iguais a `c`, sem dependência da frequência no modelo clássico. Logo, não há dispersão material no vácuo ideal.

A palavra “dispersão” no RLL deve ser usada com cuidado:

| Uso | Estado |
|---|---|
| espalhamento geométrico | permitido |
| divergência/difração de feixe | permitido |
| dispersão material no vácuo ideal | bloqueado |
| perda de coerência operacional | hipótese RLL |
| fóton cansado por distância | bloqueado |

---

## 7. Fórmulas RLL propostas

### 7.1 Versão amplitude

```text
C_loop_amp(r) = C0 / r
```

Uso:

```text
quando C_loop mede acoplamento de campo, amplitude, coerência linear ou capacidade de reentrada por frente de onda.
```

### 7.2 Versão intensidade

```text
C_loop_int(r) = C0 / r²
```

Uso:

```text
quando C_loop mede energia por área, irradiância, potência recebida ou densidade de sinal.
```

### 7.3 Versão gaussiana

```text
C_loop_gauss(z) = C0 / [1 + (z/zR)²]
```

Uso:

```text
quando C_loop mede intensidade no eixo de um feixe gaussiano ideal.
```

### 7.4 Versão raiz operacional

```text
C_loop_sqrt(z) = C0 / √(1 + (z/zR)²)
```

Uso:

```text
quando C_loop mede amplitude/confinamento proporcional ao inverso do raio gaussiano.
```

---

## 8. Anti-plágio e autoria

O RLL não deve apresentar como descoberta própria:

- lei do inverso do quadrado;
- amplitude como raiz da intensidade;
- feixe gaussiano;
- comprimento de Rayleigh;
- relação de dispersão `ω=ck` no vácuo;
- informação de Shannon;
- máquina de Turing;
- neurônio lógico de McCulloch-Pitts;
- história de cartões perfurados ou armazenamento magnético;
- numerologias históricas como Pakua, base 60 suméria ou zero.

O que pode ser autoral é a **conexão RLL**:

```text
C_loop como grandeza de acoplamento/coerência/reentrada do sinal no modelo RLL.
```

E a pergunta nova:

```text
Qual escala física conhecida serve como melhor analogia para a perda de capacidade de loop RLL?
```

---

## 9. Relações autorais e paralelos existentes

RLL deve procurar paralelos em:

| Área | Referências-base |
|---|---|
| óptica geométrica/onda | inverso do quadrado, ondas esféricas, Gaussian beam, Rayleigh range |
| informação | Shannon, entropia, bits, canal, ruído |
| computação | Turing, Church-Turing, cartões perfurados, estados discretos |
| redes neurais | McCulloch-Pitts, limiar lógico, neurônio artificial |
| simbologia histórica | Pakua, base 60, zero, dedos/membros, combinatória simbólica |

A relação entre esses campos é permitida como síntese autoral somente quando marcada como síntese, não como origem histórica.

---

## 10. Claim matrix

| Claim | Estado | Correção |
|---|---|---|
| “No vácuo, fóton perde energia por metro” | `CLAIM_BLOCKED` | não afirmar |
| “Irradiância de fonte pontual cai como 1/r²” | `SOURCE_LINKED` | citar inverso do quadrado |
| “Amplitude associada cai como 1/r” | `SOURCE_LINKED` | derivar de I ∝ A² |
| “Raiz aparece na abertura gaussiana” | `SOURCE_LINKED` | citar Gaussian beam/Rayleigh |
| “RLL loop capacity pode ser acoplamento/coerência” | `HIPOTESE` | definir variável e testar |
| “Pakua/base 60 provam RLL” | `CLAIM_BLOCKED` | só analogia histórica/simbólica |
| “Qualquer coisa pode ser descrita matematicamente” | `PHILOSOPHICAL_CLAIM` | não tratar como prova universal |

---

## 11. Próximos passos técnicos

1. Definir formalmente `C_loop`.
2. Escolher se `C_loop` mede intensidade, amplitude, coerência, probabilidade ou acoplamento.
3. Criar simulação simples comparando `1/r`, `1/r²` e modelo gaussiano.
4. Registrar unidades físicas.
5. Criar `FORMULA_000002` no registry.
6. Incluir referências bibliográficas em `references.md`.
7. Só promover claim depois de método e teste.

---

## 12. R3

```text
F_ok   = hipótese RLL encaixada sem plagiar física existente.
F_gap  = C_loop ainda precisa definição operacional, unidade e teste.
F_next = criar simulação mínima e matriz claim→referência→fórmula.
```
