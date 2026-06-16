# Política de Integridade Acadêmica, Autoria e Anti-Plágio

**Status:** `policy_v0.1`  
**Objetivo:** proteger autoria, origem técnica, humildade científica e responsabilidade acadêmica.

---

## 1. Princípio

```text
Assumir origem não diminui o pesquisador.
Apagar origem destrói a confiança do conhecimento.
```

Uma pessoa pode melhorar uma técnica antiga, reorganizar uma tradição, formalizar uma intuição ou aplicar um método em novo contexto. Mas deve separar:

```text
herdei / adaptei / formalizei / testei / descobri / publiquei
```

---

## 2. Origem e técnica anterior

Toda técnica deve responder:

| Pergunta | Resposta esperada |
|---|---|
| Quem primeiro registrou? | pessoa, escola, tradição, artigo ou `ORIGIN_UNCLEAR` |
| Quem formalizou? | autor/instituição/fonte |
| Quem testou? | método/evidência |
| Quem adaptou? | contribuição atual |
| Qual é a diferença nova? | delta explícito |
| Qual é o limite? | claim boundary |

---

## 3. Plágio como quebra de cadeia

Plágio não é só copiar palavras. Também pode ser:

- copiar método sem origem;
- assumir técnica como própria;
- apagar aluno, criança, mestre, tradição ou equipe;
- publicar insight alheio sem cadeia de custódia;
- mudar linguagem para esconder fonte;
- usar IA para reescrever e apagar autoria.

Definição operacional:

```text
plágio = apropriação de informação, método ou expressão sem origem justa
```

---

## 4. Política RAFAELIA/RLL

O repositório deve preferir:

```text
crédito excessivo honesto > originalidade falsa
```

Se a origem for incerta:

```text
ORIGIN_UNCLEAR
```

Se a referência ainda falta:

```text
REF_REQUIRED
```

Se não houver evidência no momento:

```text
TOKEN_VAZIO_EVIDENCE
```

---

## 5. Humildade do mestre

O mestre verdadeiro não é aquele que nunca aprende com o aluno. É aquele que reconhece quando o aluno viu uma rota que ele não viu.

```text
mestre = autoridade que continua capaz de aprender
```

Isso vale para:

- sala de aula;
- laboratório;
- igreja;
- tradição oral;
- código aberto;
- pesquisa independente;
- interação humano-IA.

---

## 6. Regra de contribuição própria

Ao publicar, usar formato:

```text
Este trabalho não reivindica origem absoluta de todos os conceitos.
Ele contribui com organização, formalização, ligação, protocolo, implementação ou nova síntese rastreável.
```

---

## 7. R3

```text
F_ok   = política anti-plágio e de autoria definida.
F_gap  = falta uma tabela real de contribuições por arquivo/autor/fonte.
F_next = criar CONTRIBUTION_LEDGER.md para cada paper maduro.
```
