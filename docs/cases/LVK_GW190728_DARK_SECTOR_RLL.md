# LVK/GW190728 como teste lateral do setor escuro no RLL

**Status:** Exploratório / Parcial real em preparação  
**Domínio:** cosmologia, objetos compactos, ondas gravitacionais  
**Modalidade:** gravitational waves / waveform residuals / dark-sector imprint  
**Caso-guia:** GW190728  
**Fonte de contexto:** MIT News, 2026-05-12; Physical Review Letters, 2026

---

## 1. Objetivo

Este documento registra uma nova trilha observacional lateral para o Relativity Living Light (RLL/MCRP): usar eventos de ondas gravitacionais de binários de buracos negros como teste de compatibilidade para possíveis assinaturas indiretas do setor escuro.

A motivação vem de um estudo associado ao MIT que propõe um método para procurar marcas de matéria escura em sinais de ondas gravitacionais, comparando modelos de fusão em vácuo contra modelos em ambiente de matéria escura.

O caso **GW190728** foi apontado como evento com possível preferência por um modelo contendo ambiente escuro, mas sem significância suficiente para declarar detecção.

---

## 2. Interpretação correta

Este caso **não confirma matéria escura** e **não confirma o RLL**.

A leitura correta é metodológica:

1. há uma nova forma de procurar assinaturas indiretas do setor escuro;
2. essas assinaturas podem aparecer como desvios sutis na forma de onda gravitacional;
3. a hipótese precisa ser testada contra múltiplos eventos LVK;
4. o resultado deve permanecer classificado como exploratório até validação estatística independente.

No RLL, esta trilha deve funcionar como teste de falsificabilidade e não como prova narrativa.

---

## 3. Ponte com o RLL

O RLL já organiza validação por camadas observacionais: expansão cósmica, CMB, BAO, supernovas, crescimento de estrutura, lentes gravitacionais, anomalias astrofísicas e casos locais.

A camada LVK adiciona um regime complementar:

```text
Cosmologia de fundo       -> H(z), BAO, SNe Ia, CMB
Crescimento de estrutura  -> fσ8, weak lensing, clusters
Astrofísica anômala       -> JWST, objetos compactos, stress tests
Ondas gravitacionais      -> h(t), fase, amplitude, residual de waveform
```

A hipótese operacional é simples:

```text
Se o setor escuro altera o ambiente dinâmico de binários compactos,
então parte dessa alteração pode aparecer como residual de forma de onda
quando se compara o modelo de vácuo contra modelos com acoplamento ambiental.
```

---

## 4. Relação com o núcleo conceitual do RLL

O RLL modela um componente efetivo de superposição/coerência com transição logística:

```math
f(z)=\frac{1}{1+\exp((z-z_t)/w_t)}
```

com interpretação de limites:

```text
f -> 1 : comportamento tipo energia escura efetiva
f -> 0 : comportamento tipo matéria efetiva
```

O estudo LVK/MIT não usa esse mecanismo diretamente. Ele trabalha com uma hipótese diferente, ligada a campos escalares leves e ambiente em torno de buracos negros.

Portanto, a ponte é de **método e observável**, não de identidade física imediata.

---

## 5. Observáveis mínimos para uma trilha RLL-LVK

Uma futura implementação quantitativa deve mapear:

1. **Forma de onda base:** `h_vac(t)` para binário de buracos negros em vácuo.
2. **Forma de onda alternativa:** `h_dark(t; θ_dark)` com parâmetros ambientais efetivos.
3. **Residual:**

```math
\Delta h(t)=h_{obs}(t)-h_{vac}(t)
```

4. **Deriva de fase:**

```math
\Delta \phi(t)=\phi_{obs}(t)-\phi_{vac}(t)
```

5. **Comparação estatística:** razão de evidência/Bayes factor entre modelo de vácuo e modelo com ambiente escuro.
6. **Critério de robustez:** repetição em múltiplos eventos, não dependência de um único candidato.

---

## 6. Critério de falsificabilidade

A trilha LVK só deve subir de status se cumprir etapas explícitas:

| Nível | Critério | Status |
|---|---|---|
| Sintético | Simulação interna de waveform modificada | permitido |
| Parcial real | Comparação com dados públicos LVK | em preparação |
| Real validado | múltiplos eventos, significância robusta, reprodução independente | não concluído |

Condição de rejeição:

```text
Se modelos de vácuo explicarem os eventos LVK sem ganho estatístico robusto
para ambiente escuro, a trilha LVK não deve ser usada como suporte empírico forte ao RLL.
```

---

## 7. Integração documental sugerida

Entrada sugerida para `data/observational_sources.yml`:

```yaml
  lvk_gw_dark_sector_2026:
    label: "LVK gravitational-wave dark-sector waveform screening"
    type: journal_and_public_data
    domain: compact_objects_cosmology
    modality: gravitational_waves
    release_status: exploratory
    language_scope: [en]
    url: "https://news.mit.edu/2026/new-way-spot-signs-dark-matter-0512"
    usage: "Waveform-residual stress test for possible dark-sector environments around black-hole binaries; not a confirmed detection."
```

---

## 8. Síntese

O caso GW190728 deve ser tratado como **sinal candidato**, não como evidência conclusiva.

Para o RLL, seu valor está em abrir uma quarta classe de validação:

```text
DESI / Pantheon+ / Planck  -> expansão e fundo cosmológico
Euclid / Rubin / lensing   -> crescimento e estrutura
JWST / anomalias           -> stress tests astrofísicos
LVK / GW residuals         -> campo forte e setor escuro local
```

**Conclusão:** a trilha LVK é coerente com a arquitetura de validação do RLL, desde que permaneça marcada como exploratória até que haja modelagem quantitativa, comparação com dados públicos e reprodução independente.

---

**RAFCODE-Φ / RLL-MCRP**  
`Ω = coerência máxima sem inflar evidência`  
`FIAT LUX · FIAT VERITAS`
