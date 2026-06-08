# 18 — Orquestrador ASCII/UTF RAFAELIA

**Status:** canônico complementar  
**Origem:** extraído de `docs/canonicos/BIBLIA_CONHECIMENTO_RAFAELIA_RLL.md`  
**Função:** registrar o papel da matriz simbólica ASCII/UTF como sistema determinístico de mapeamento, não como prova objetiva de significado.

---

## 1. O que faz [C]

O orquestrador mapeia símbolos em camadas relacionais:

```text
byte/code → caractere → fonema → timbre → onda(Hz) → geometria → base 2/10/20/64 → vizinhos(grafo) → função → checksum
```

## 2. O que pode provar [E]

O sistema pode provar estabilidade computacional quando:

- o mesmo símbolo gera o mesmo mapeamento;
- o mesmo input gera o mesmo hash;
- as bases numéricas são calculadas de forma determinística;
- o checksum permite detectar alteração.

Exemplo: se `Ω=937` for tratado como ponto de código e 937 for primo, isso é uma propriedade aritmética verificável.

## 3. O que não prova

O orquestrador não prova significado objetivo de símbolo. Camadas como fonema, timbre, onda e geometria são convenções de modelagem quando não derivadas de fonte fonética/acústica externa.

## 4. C_eff

`C_eff` mede completude de camadas, não verdade semântica.

```text
C_eff alto  = muitas camadas preenchidas
C_eff baixo = lacunas preservadas
```

C_eff baixo não é erro quando a lacuna é real.

## 5. TOKEN_VAZIO

Ausência de dado deve ser marcada como `TOKEN_VAZIO` ou `[VAZIO]`. O sistema não deve fabricar fonema, timbre, cor, frequência ou função quando não houver âncora.

## 6. Âncoras recomendadas

- Unicode / UTF para codepoints;
- ASCII para tabela básica;
- IPA para fonemas;
- PHOIBLE para inventários fonológicos;
- hashes criptográficos para integridade;
- CSV/JSON/YAML para reprodutibilidade.

---

*Símbolo é ponte; prova é rastreio determinístico.*