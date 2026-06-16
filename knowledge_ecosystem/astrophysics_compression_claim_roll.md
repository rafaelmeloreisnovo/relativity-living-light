# Rol de Informações — Astrofísica de Compressão

**Status:** `claim_roll_v0.1`  
**Data:** `2026-06-16`  
**Relacionado:** `PapersPub/05_compression_astrophysics_claims/*`

---

## 1. Propósito

Registrar cada informação da hipótese oral como item auditável:

```text
observação → domínio → fonte → estado → correção → próximo passo
```

---

## 2. Rol principal

| ID | Informação | Domínio | Estado | Correção científica | Próximo passo |
|---|---|---|---|---|---|
| `ASTRO_COMP_001` | corpos maiores tendem a acumular voláteis/gás | exoplanetas | `SOURCE_LINKED` | tendência, não regra absoluta | citar Rogers/Seager/Fortney |
| `ASTRO_COMP_002` | planeta rochoso pode passar para regime mini-Netuno/gasoso | exoplanetas | `SOURCE_LINKED` | usar massa-raio-densidade | criar tabela de regimes |
| `ASTRO_COMP_003` | hidrogênio pode virar sólido sob pressão/temperatura adequadas | alta pressão | `SOURCE_LINKED` | depende de fase P-T | citar hidrogênio sólido/metálico |
| `ASTRO_COMP_004` | hidrogênio metálico em gigantes gasosos | planetas gigantes | `REF_REQUIRED_STRONGER` | provável em interiores, mas exige fonte específica | buscar revisão sobre Júpiter/Saturno |
| `ASTRO_COMP_005` | massa crítica para fusão de deutério perto de 13 M_J | anãs marrons | `SOURCE_LINKED` | regra prática, não corte universal | citar Spiegel/Bodenheimer |
| `ASTRO_COMP_006` | fusão sustentada de hidrogênio exige ~0.075–0.08 M☉ | estrelas | `SOURCE_LINKED_PARTIAL` | precisa referência estelar formal | buscar livro/revisão |
| `ASTRO_COMP_007` | fissão e fusão coexistem como motores principais de estrelas | física nuclear estelar | `CLAIM_BLOCKED_AS_PRIMARY` | fusão domina; fissão não é motor comum | revisar contextos raros |
| `ASTRO_COMP_008` | ignição estelar por compressão gravitacional | evolução estelar | `SOURCE_LINKED` | gravidade → pressão/temperatura → fusão | citar Kippenhahn/Woosley |
| `ASTRO_COMP_009` | uma subpartícula atravessa estrutura e acende estrela | hipótese/metáfora RLL | `METAFORA_OR_HIPOTESE` | física padrão não usa causa única assim | definir como analogia de gatilho |
| `ASTRO_COMP_010` | átomos não se tocam classicamente | mecânica quântica | `SOURCE_LINKED_PARTIAL` | usar campos, estados, Pauli | buscar fonte didática forte |
| `ASTRO_COMP_011` | pressão de degenerescência segura remanescentes compactos | astrofísica compacta | `SOURCE_LINKED` | até limites de massa | citar TOV/Pauli |
| `ASTRO_COMP_012` | buraco negro por colapso quando suporte interno falha | relatividade/astrofísica | `SOURCE_LINKED` | não é apenas estrela que atrai matéria | citar Oppenheimer-Snyder/Woosley/Heger |
| `ASTRO_COMP_013` | estrela atrai matéria esgotada e vira buraco negro | analogia incompleta | `CLAIM_REVISED` | acreção aumenta massa; colapso depende de suporte/limite | reescrever como colapso + acreção |
| `ASTRO_COMP_014` | compressão máxima organiza regime de matéria | RLL/conceito | `HIPOTESE` | precisa variável e teste | criar `Regime(M,P,T,rho,comp)` |
| `ASTRO_COMP_015` | tensão de partículas é liberada por fusão | física estelar/RLL | `SOURCE_LINKED_PARTIAL` | fusão libera energia por diferença de energia de ligação; não falar só “tensão” | citar energia de ligação nuclear |

---

## 3. Estados de promoção

```text
METAFORA_OR_HIPOTESE → SOURCE_LINKED → METHOD_DEFINED → MODEL_TESTED → CLAIM_ALLOWED
```

Bloqueios:

```text
CLAIM_BLOCKED_AS_PRIMARY
CLAIM_REVISED
REF_REQUIRED_STRONGER
TOKEN_VAZIO_REFERENCE
```

---

## 4. Síntese RLL segura

```text
A compressão gravitacional organiza transições de regime da matéria.
O RLL pode estudar essas transições como linguagem de acoplamento, tensão e forma,
mas deve preservar física conhecida: massa, pressão, temperatura, densidade,
composição, fusão, degenerescência e colapso.
```

---

## 5. R3

```text
F_ok   = rol de informações criado e separado por estado.
F_gap  = faltam fontes específicas para hidrogênio metálico planetário, Pauli didático e limite de hydrogen burning.
F_next = buscar fontes e criar simulação conceitual de regimes M/P/T/rho.
```
