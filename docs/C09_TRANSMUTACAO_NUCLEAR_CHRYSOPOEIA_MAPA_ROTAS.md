# C09 — Transmutação nuclear / chrysopoeia via nêutrons de fusão

Status date: 2026-06-26

## Propósito

Este documento registra a nona convergência candidata (`C09`) do mapa RAFAELIA/RLL:

```text
transmutação nuclear real -> reorganização de núcleo -> rota material verificável -> claim gate
```

A nota nasce de uma matéria popular sobre mercúrio virando ouro em contexto de fusão nuclear, mas usa como núcleo técnico fontes primárias/preprints e separa claramente:

```text
notícia -> preprint -> mecanismo nuclear -> simulação -> pendência experimental -> claim boundary
```

## Fonte de gatilho

- Click Petróleo e Gás. Matéria popular enviada pelo usuário: `mercurio virando ouro... neutrons de tokamak... ouro-197 estavel`.
- Uso permitido: gatilho de triagem e leitura pública.
- Uso proibido: usar matéria popular como prova técnica.

## Fontes técnicas mínimas

- Rutkowski, A., Harter, J., & Parisi, J. (2025). *Scalable Chrysopoeia via (n,2n) Reactions Driven by Deuterium-Tritium Fusion Neutrons*. arXiv:2507.13461. https://arxiv.org/abs/2507.13461
- Parisi, J. F., & Azad, J. (2026). *Self-subsidizing Mercury Remediation with Fusion Reactors*. arXiv:2604.02590. https://arxiv.org/abs/2604.02590
- Parisi, J. F., Rutkowski, A., Harter, J., Schwartz, J. A., & Chen, S. (2025). *Production of High-Specific-Activity Radioisotopes Using High-Energy Fusion Neutrons*. arXiv:2511.02814. https://arxiv.org/abs/2511.02814

Observação: as fontes arXiv devem ser tratadas como preprints até revisão independente/peer review e reprodução externa.

## Mecanismo físico normalizado

A rota nuclear principal proposta é:

```text
D-T fusion -> fast 14 MeV neutrons -> 198Hg(n,2n)197Hg -> 197Au stable
```

Em forma curta:

```text
198Hg + n_fast -> 197Hg + 2n
197Hg -> 197Au + decay
```

A tese técnica do preprint de 2025 é que uma camada de blanket especializada poderia usar nêutrons rápidos de uma plasma D-T para produzir `197Au` a partir de `198Hg`, mantendo compatibilidade com funções de blanket, multiplicação de nêutrons e ciclo de trítio.

## O que é real, o que é hipótese, o que é pendência

| Item | Estado | Observação |
|---|---|---|
| Transmutação nuclear existe | `[E]` | mudança de elemento por reação nuclear é física estabelecida |
| Ouro-197 é o isótopo estável de ouro | `[E]` | alvo correto para ouro materialmente utilizável |
| `198Hg(n,2n)197Hg -> 197Au` | `[E][H]` | rota nuclear plausível; exige modelagem de seção de choque, fluxo e produtos colaterais |
| Produção em escala de toneladas | `[H][M]` | depende de simulação de blanket, fluxo de nêutrons, materiais e economia |
| Não prejudicar energia/trítio | `[H][M]` | precisa reprodução independente em códigos neutronics e engenharia de blanket |
| Ouro comercial limpo | `[H][M]` | exige separação química, decaimento, gestão radiológica e certificação |
| Validação de RLL/RAFAELIA | `[VAZIO]` | não valida cosmologia nem teoria autoral |

## Por que C09 é independente de C01..C08

C01 tratava de rigidez emergente e dissipação em transições de fase.

C09 trata de outro regime:

```text
não é só fase;
não é só analogia;
é mudança de identidade nuclear por canal energético específico.
```

A convergência útil para RAFAELIA/RLL está no padrão de engenharia epistemológica:

```text
forma simbólica antiga
  -> impossibilidade química
  -> possibilidade nuclear restrita
  -> simulação moderna
  -> pendência experimental
  -> claim boundary
```

Isto conversa diretamente com a regra:

```text
ruído histórico / mito / linguagem simbólica
  -> extração técnica
  -> mecanismo verificável
  -> rota de validação
  -> TOKEN_VAZIO quando faltar prova
```

## Mapa de rotas

### Rota A — Física nuclear

```text
isótopo alvo -> reação nuclear -> seção de choque -> espectro de nêutrons -> taxa de produção -> produtos colaterais
```

Pendências:

- confirmar bases de dados nucleares usadas para `198Hg(n,2n)`;
- reproduzir taxa de produção em código independente;
- mapear todos os isótopos de Hg presentes em mercúrio natural;
- estimar radioisótopos de Au/Hg/Tl/Pt gerados;
- separar `197Au` de contaminantes radioativos.

### Rota B — Engenharia de blanket / tokamak

```text
plasma D-T -> fluxo 14 MeV -> blanket -> multiplicador de nêutrons -> breeding de trítio -> remoção térmica
```

Pendências:

- compatibilidade com razão de reprodução de trítio;
- compatibilidade térmica e corrosiva do mercúrio;
- segurança de inventário de mercúrio;
- dano por nêutrons em materiais estruturais;
- manutenção remota e blindagem.

### Rota C — Economia / regulação

```text
produção estimada -> pureza -> tempo de resfriamento -> certificação -> mercado -> risco regulatório
```

Pendências:

- custo de enriquecimento/separação de `198Hg`;
- custo de armazenamento radiológico;
- aceitação de ouro produzido em ambiente nuclear;
- impacto no mercado de ouro;
- licenças para mercúrio e material ativado.

### Rota D — Remediação ambiental

```text
mercúrio poluente -> captura -> transmutação -> ouro estável -> remoção permanente do risco químico
```

Pendências:

- logística de coleta global de mercúrio;
- balanço de risco ambiental antes/depois;
- comprovar que a rota reduz risco líquido;
- evitar incentivo perverso à produção extra de mercúrio.

### Rota E — Arquitetura informacional RAFAELIA

```text
notícia ruidosa -> fonte primária -> mecanismo -> matriz de pendências -> claim_state
```

Tradução:

```text
linguagem simbólica antiga = entrada bruta
mecanismo nuclear = extração técnica
simulação = hipótese operacional
reprodução independente = possível promoção
lacuna = TOKEN_VAZIO
```

## Mapa de pendências

| Pendência | Tipo | Status atual | Saída correta |
|---|---|---|---|
| peer review do preprint | científica | pendente | não promover escala industrial |
| reprodução neutronics | técnica | pendente | script/código/fonte/resultado |
| dados de seção de choque | nuclear | pendente | tabela e referência primária |
| espectro real de nêutrons | engenharia | pendente | modelo de blanket reproduzível |
| impurezas radioativas | segurança | pendente | decay chain + storage time |
| integração com trítio | fusão | pendente | TBR validado |
| viabilidade econômica | econômica | pendente | CAPEX/OPEX + sensibilidade |
| relação com RLL | epistemológica | indireta | apenas analogia metodológica |

## Claim boundary

Permitido:

```text
A transmutação de elementos é fisicamente possível por reações nucleares.
O preprint propõe produzir Au-197 a partir de Hg-198 usando nêutrons rápidos de fusão D-T.
A proposta é uma C09 candidata por representar passagem de símbolo histórico para rota técnica verificável.
```

Proibido:

```text
RLL provou transmutação nuclear.
RAFAELIA prevê ouro de tokamak.
A matéria popular confirma a teoria.
C09 fecha o sistema.
```

## Síntese RAFAELIA

```text
C09 = alquimia sem fantasia:
    símbolo antigo preservado,
    química impossível separada,
    física nuclear reconhecida,
    engenharia pendente marcada,
    claim boundary obedecido.
```

Em termos de redução de incoerência:

```text
mito -> notícia -> preprint -> mecanismo -> pendência -> rota -> teste -> claim/TOKEN_VAZIO
```

## Próxima ação recomendada

1. Inserir C09 no registro mestre de convergências.
2. Tratar C09 como `candidate_active`, não como validada.
3. Criar um script futuro para catálogo de fontes externas (`data/rll_latentes/observations.yml` ou equivalente).
4. Não misturar C09 com validação cosmológica RLL.
5. Usar C09 como exemplo de metodologia: transformar ruído semântico em rota técnica auditável.
