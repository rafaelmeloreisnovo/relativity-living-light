# Exemplos Citados — Registro com Referência Necessária

**Status:** `examples_registry_v0.1`  
**Objetivo:** preservar sinais e exemplos sem transformá-los em claims fortes antes da origem.

---

## 1. Política

Este arquivo registra exemplos mencionados como matéria polimática. Eles servem para orientar pesquisa, documentação e busca de fonte.

```text
exemplo oral ≠ evidência final
exemplo oral = pista de busca + domínio + claim boundary
```

---

## 2. Registro de exemplos

| ID | Exemplo/tema | Domínio principal | Uso conceitual | Estado |
|---|---|---|---|---|
| `EX_REF_001` | material acadêmico sobre chia, nutrição humana/animal e origem cultural | nutrição / agronomia / etnobotânica | mostrar material conceitual sustentado por bibliografia | `REF_REQUIRED` |
| `EX_REF_002` | origem histórica da cesariana e atribuições culturais/etimológicas | história da medicina | mostrar importância de origem técnica e autoria histórica | `ORIGIN_UNCLEAR`, `REF_REQUIRED` |
| `EX_REF_003` | técnica que permanece mesmo quando o nome original é esquecido | história / epistemologia | separar autoria nominal de continuidade técnica | `HIPOTESE_CONCEITUAL` |
| `EX_REF_004` | casos de plágio acadêmico e perda de legitimidade profissional | ética acadêmica / direito | demonstrar gravidade de apropriação de autoria | `REF_REQUIRED` |
| `EX_REF_005` | defeitos industriais/recalls envolvendo risco à vida | segurança pública / engenharia | rede de transparência e priorização logística | `REF_REQUIRED` |
| `EX_REF_006` | investigação pós-acidente aeronáutico | segurança / engenharia de sistemas | aprender com falhas em sistemas complexos | `REF_REQUIRED` |
| `EX_REF_007` | percepção de cor, nomes culturais e ilusão visual | neurociência / filosofia da linguagem / óptica | mostrar diferença entre medição e experiência | `REF_REQUIRED` |
| `EX_REF_008` | sensores animais: infravermelho, ecolocalização, linha lateral, magnetorrecepção, sensibilidade elétrica | biologia sensorial | mostrar que o humano padrão não esgota canais do real | `REF_REQUIRED` |
| `EX_REF_009` | campo elétrico/magnético em organismos e possíveis interações | biofísica | mapear limites entre medição convencional e hipótese | `REF_REQUIRED`, `CLAIM_BLOCKED` |
| `EX_REF_010` | bactérias, adaptação energética, ambientes extremos e radiação | microbiologia / astrobiologia | vida como exploração de gradientes de energia | `REF_REQUIRED` |
| `EX_REF_011` | fontes hidrotermais, quimiossíntese e ecossistemas extremos | biologia / geologia | ecossistema complexo sustentado por energia não solar direta | `REF_REQUIRED` |
| `EX_REF_012` | hemoglobina/hemocianina e transporte de gases em linhagens distintas | biologia comparada | diversidade de soluções biológicas | `REF_REQUIRED` |
| `EX_REF_013` | excesso de substâncias comuns podendo causar dano | medicina / toxicologia | dose, tempo e contexto como variáveis críticas | `REF_REQUIRED`, `MEDICAL_CAUTION` |
| `EX_REF_014` | hemorragia, sede, hemostasia e risco de conduta incorreta | medicina / emergência | separar intuição de protocolo médico | `REF_REQUIRED`, `MEDICAL_CAUTION`, `CLAIM_BLOCKED` |

---

## 3. Como promover um exemplo

Para promover `REF_REQUIRED` para `SOURCE_LINKED`:

1. encontrar fonte primária ou secundária confiável;
2. registrar citação completa;
3. marcar data de acesso;
4. resumir sem copiar demais;
5. separar o que a fonte diz do que o projeto infere;
6. atualizar claim state.

---

## 4. Linguagem segura

Permitido:

```text
O exemplo foi citado como pista conceitual e exige referência antes de claim empírico.
```

Proibido:

```text
O exemplo prova a teoria.
```

---

## 5. R3

```text
F_ok   = exemplos preservados sem overclaim.
F_gap  = falta buscar e anexar fontes confiáveis.
F_next = abrir tarefa de pesquisa bibliográfica por EX_REF_ID.
```
