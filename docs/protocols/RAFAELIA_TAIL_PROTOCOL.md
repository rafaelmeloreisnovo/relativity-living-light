# RAFAELIA Tail Protocol — RTP v1

> Status: especificação canônica inicial.
> Objetivo: permitir que títulos, assuntos de e-mail, eventos de calendário, documentos HTML e memorandos tenham uma parte humana limpa e uma cauda de máquina rastreável.

## 1. Princípio

O protocolo separa apresentação humana de metadado operacional:

```text
[HUMAN_VISIBLE_TITLE] || raf:v1;id=...;fam=...;st=...;dt=...;prev=...;link=...;hash=...
```

Regra:

```text
começo = humano
final = máquina
cor = sorter visual
label = classificação nativa
anexo/link = corpo da prova
hash/id = cadeia de custódia
```

A parte humana deve permanecer legível, sem poluição visual. A cauda final é lida por parser, IA, script, rotina de auditoria ou indexador.

## 2. Motivação

A arquitetura RAFAELIA já trata conhecimento como rede de relações, não como sequência linear. O Tail Protocol aplica esse princípio a objetos cotidianos de trabalho: Gmail, Google Calendar, Drive, GitHub, HTML, Markdown e ledgers.

A inferência não substitui leitura real. Ela localiza o bloco. O protocolo aponta onde ler, como cruzar e como validar.

## 3. Modelo geral

```text
subject/event/title/html text
    ↓
last delimiter search: " || "
    ↓
left side  = visible human title
right side = machine trailer
    ↓
parse key=value pairs separated by semicolon
    ↓
build relation graph and custody chain
```

## 4. Delimitador

O delimitador canônico é:

```text
 || 
```

Motivos:

- simples de ler;
- fácil de localizar com `rsplit(" || ", 1)`;
- evita poluir o começo do título;
- permite títulos humanos livres;
- permite leitura da direita para a esquerda.

## 5. Campos mínimos

| Campo | Exemplo | Obrigatório | Função |
|---|---|---:|---|
| `raf` | `v1` | sim | versão do protocolo |
| `id` | `MAIL-0001` | sim | identificador do bloco |
| `fam` | `email` | sim | família semântica |
| `st` | `ev` | sim | estado epistêmico/operacional |
| `dt` | `20260710` | recomendado | data de referência compacta |
| `prev` | `MAIL-0000` | opcional | bloco anterior |
| `link` | `DRV-0001,GIT-0001` | opcional | relações cruzadas |
| `hash` | `ab12cd34` | opcional | digest curto |
| `cal` | `CAL-0001` | opcional | evento calendário associado |
| `thr` | `THR-0001` | opcional | thread Gmail associada |

## 6. Famílias canônicas

```text
email     mensagem/e-mail/thread
cal       calendário/evento/revisão
 drive    arquivo/pasta/anexo
 git       commit/pr/issue/repo
llm       modelo local/inferência/eval
cti       RMR-CTI/memória/grafo
socket    SIGIL_SOCKET/C14/runtime
edge      hardware/sensor/ação física
gov       política/auditoria/evidência
paper     texto acadêmico/artigo
ops       operação/execução/tarefa
```

## 7. Status canônicos curtos

| Código | Estado | Uso |
|---|---|---|
| `ev` | evidence | evidência localizada |
| `hyp` | hypothesis | hipótese útil a testar |
| `act` | action | ação pendente |
| `gap` | TOKEN_VAZIO | lacuna explícita |
| `sens` | sensitive | material sensível |
| `done` | done | concluído |
| `rev` | review | revisão marcada |
| `err` | error | erro observado |
| `audit` | audit | auditoria/rastreio |

## 8. Exemplos de subject/event title

```text
Revisar navegação semântica do Drive || raf:v1;id=DRV-0001;fam=drive;st=rev;dt=20260710;prev=MAIL-0007
```

```text
Validar ponte NanoGPT + RMR-CTI || raf:v1;id=LLM-0003;fam=llm;st=hyp;dt=20260710;link=DRV-0001,GIT-0093
```

```text
Registrar prova de socket C14 || raf:v1;id=SOCK-0004;fam=socket;st=ev;dt=20260710;link=DRV-0040;hash=ab12cd34
```

## 9. Corpo de e-mail ou memorando

O corpo pode usar bloco final expandido:

```text
Resumo humano aqui.

--- RAF_TRAILER
raf=v1
id=MAIL-0007
fam=email
st=ev
date=2026-07-10
prev=MAIL-0006
links=DRV-0001,GIT-0093,CAL-0002
flags=EMAIL_SELF,CALENDAR_ANCHOR,DRIVE_BODY,GITHUB_CONTRACT
--- END_RAF_TRAILER
```

## 10. HTML object / visible-hidden model

Quando houver HTML, usar microestrutura com parte visível e metadado de máquina.

### Forma com `data-*`

```html
<div class="raf-block"
     data-raf="v1"
     data-raf-id="MAIL-0007"
     data-raf-fam="email"
     data-raf-st="ev"
     data-raf-dt="20260710"
     data-raf-prev="MAIL-0006"
     data-raf-link="DRV-0001,GIT-0093,CAL-0002">
  <span class="raf-visible">Revisar navegação semântica do Drive</span>
</div>
```

### Forma com trailer escondido

```html
<div class="raf-block">
  <span class="raf-visible">Revisar navegação semântica do Drive</span>
  <span class="raf-tail" hidden aria-hidden="true">raf:v1;id=MAIL-0007;fam=email;st=ev;dt=20260710;prev=MAIL-0006;link=DRV-0001,GIT-0093</span>
</div>
```

### Forma visível completa, compatível com e-mail simples

```html
<div class="raf-block">
  Revisar navegação semântica do Drive || raf:v1;id=MAIL-0007;fam=email;st=ev;dt=20260710;prev=MAIL-0006
</div>
```

Recomendação: em Gmail/Calendar, preferir subject/title com trailer textual, porque é mais robusto que HTML oculto. Em documentos HTML próprios, usar `data-*` e/ou `<span hidden>`.

## 11. Cores e labels

Cores não carregam toda a semântica. Elas funcionam como sorter visual.

| Cor sugerida | Uso |
|---|---|
| azul | evidência/documento |
| verde | concluído/validado |
| amarelo | hipótese |
| vermelho | sensível/risco |
| cinza | gap/TOKEN_VAZIO |
| roxo | pesquisa profunda |
| laranja | ação pendente |

Labels Gmail e calendários podem repetir o status, mas a fonte técnica primária é o trailer.

## 12. Cadeia de custódia leve

Cada bloco pode referenciar o anterior:

```text
MAIL-0001 → CAL-0001 → DRV-0001 → GIT-0001 → MAIL-0002
```

Campos usados:

```text
id atual
prev id
thread id
event id
Drive id
Git commit SHA
hash do corpo
hash dos anexos
```

Isto não exige blockchain pesado no início. A cadeia nasce como trilha auditável. Depois pode ser endurecida com SHA-256, assinatura e ledger versionado.

## 13. Parser mínimo

Pseudocódigo:

```python
def parse_raf_tail(text):
    if " || " not in text:
        return {"visible": text, "tail": None}
    visible, tail = text.rsplit(" || ", 1)
    fields = {}
    for part in tail.split(";"):
        if ":" in part and part.startswith("raf:"):
            fields["raf"] = part.split(":", 1)[1]
        elif "=" in part:
            k, v = part.split("=", 1)
            fields[k.strip()] = v.strip()
    return {"visible": visible.strip(), "tail": fields}
```

## 14. Regras de segurança

- Não colocar segredo, token, senha ou dado sensível no subject.
- Para material sensível, usar `st=sens` e apontar para cofre/arquivo seguro.
- Hash curto pode aparecer no subject; hash completo deve ficar no corpo/ledger.
- HTML oculto não é controle de segurança; é apenas organização visual.
- A fonte de verdade deve ser o bloco auditável: e-mail, evento, anexo, Drive ID, Git SHA, hash e ledger.

## 15. Invariante

```text
Humano entende sem ruído.
Máquina rastreia sem adivinhar.
```

## 16. Relação com RAFAELIA

O Tail Protocol implementa em escala cotidiana a invariante de preservação de relações:

```text
memória → relação → evidência → governança → execução → nova memória
```

Ele também respeita a separação:

```text
símbolo ≠ hipótese ≠ prova ≠ código ≠ log ≠ execução
```

## 17. Próximos passos

1. Criar schema JSON para trailer.
2. Criar parser Python/JS mínimo.
3. Criar exemplos para Gmail, Calendar, Drive, GitHub e HTML.
4. Criar integração com RAFAELIA Work Evidence Chain.
5. Criar fixtures e CI para validar trailers.
