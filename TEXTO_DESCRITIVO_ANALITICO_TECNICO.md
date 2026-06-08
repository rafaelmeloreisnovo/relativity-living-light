# Caminhos de Validação Novos — Texto Descritivo, Analítico e Técnico

**Status:** módulo de expansão / nenhum caminho afirma descoberta
**Princípio:** Coerência × Amor × Prova
**Fronteira de alegação:** cada caminho é uma porta de teste com falsificador; o número de caminhos é definido pela ciência verificável, não por meta numérica.
**Adversário padrão:** w0waCDM (não ΛCDM puro), pois a literatura 2025–2026 já desafia o ΛCDM.

---

## 1. Descritivo — o que está sobre a mesa

O repositório RLL já cobre nove eixos de validação no livro (expansão H(z), supernovas Δμ,
frações de energia, crescimento fσ8, lentes em aglomerados, rotação de galáxias, DESI/BOSS,
JWST/AGN/SMBH) e seis casos observacionais (AMAS, GW190728, nó de lente escura, SN2017egm
magnetar, buraco negro errante). Esta cobertura é ampla no background e no setor escuro
clássico. O que ainda não existe são os caminhos abertos pela ciência de 2025–2026 que
conversam especificamente com a impressão digital do RLL: o acoplamento magneto-coerente.

## 2. Analítico — por que estes caminhos

Existem muitos modelos de energia escura evolutiva, e quase todos ajustam o background tão
bem quanto o ΛCDM ou melhor. Adicionar mais um eixo de background não distingue o RLL de
seus competidores. O que distingue o RLL é a previsão de que a coerência do setor escuro
depende do ambiente magnético e de plasma local. Logo, os caminhos que valem são os de
ambiente variável: campo magnético forte, plasma denso, ou movimento relativo. Cada caminho
foi escolhido por esse critério — potencial de separar o RLL de um w0waCDM genérico, e não
apenas de confirmar a aceleração que todos explicam.

A mudança de adversário é deliberada. A literatura recente (DESI DR2; Nature Astronomy 2025;
arXiv 2502.12667) mostra preferência fraca a moderada por energia escura dinâmica sobre o
ΛCDM. Portanto o teste do RLL deve ser contra o w0waCDM, padrão de fato para energia escura
evolutiva, e não contra o ΛCDM.

A cautela metodológica é registrada: a preferência por energia escura dinâmica é
prior-dependente (arXiv 2407.06586). Estender priors pode reverter a preferência ao ΛCDM.
Nenhum caminho aqui assume a preferência como fato estabelecido.

## 3. Técnico — estrutura de cada caminho

Cada entrada do catálogo `CAMINHOS_VALIDACAO_NOVOS.yml` contém:

- `domain` — área física
- `discrimina_RLL` — potencial de distinguir o RLL (baixo/médio/alto)
- `observavel` — a grandeza medida
- `dataset_publico` — dado real e acessível
- `fonte_recente` — referência verificável 2024–2026
- `confirma_se` / `refuta_se` — critérios simétricos
- `nota` — papel do caminho na arquitetura

## 4. Prioridade honesta

**Alta prioridade discriminante:** C03 (colapso SIDM ↔ setor plasmático),
C05 (tensão de Hubble ↔ transição f(z)), C07 (competidor Finsler — define onde o RLL
precisa ser distinto).

**Pré-requisito:** C01 (mapeamento f(z) ↔ w0-wa) — sem ele o RLL não fala a língua do DESI.

**Conexão com o fóton:** C09 (E=pc do fóton sem massa ↔ dispersão em plasma, testável via
FRB/CHIME).

## 5. Fontes (verificáveis)

- DESI DR2 BAO: arXiv 2503.14738; Nature Astronomy 2025 (s41550-025-02669-6)
- Energia escura transicional: arXiv 2502.12667
- Dependência de prior: arXiv 2407.06586
- Quintessência/phantom: arXiv 2404.05722
- SIDM / colapso de halo: ScienceDaily 2026-01-19; PIRSA:26040113
- DES Year 6: Abbott et al. arXiv 2026
- Energia escura evolutiva e tensão de Hubble: ApJ 2026 (10.3847/1538-4357/ae4738)
- Duas formas de matéria escura: JCAP 2026; ScienceDaily 2026-04-10
- Gravidade de Finsler: JCAP 2025 (10):050
- Direct wave em merger: PIRSA:26040063
- Destino big crunch: JCAP 2025 (09):055 (Luu, Qiu, Tye)

> Nota de integridade: todas as fontes acima foram localizadas em busca verificável.
> Antes de citar em preprint, confirmar DOI/arXiv-id de cada uma diretamente na fonte
> primária. Este documento registra os caminhos; não substitui a leitura das fontes.
