# RLL Source State Lookback

Status: draft_track_v0.1
Data: 2026-06-16
Tema: sinal observado agora, fonte no passado e estado atual incerto.

## Nucleo

O sinal observado e registro de um evento passado, nao garantia do estado presente da fonte.

No RLL:

Observed_Signal(t0) = Source_State(te) + Propagation(te_to_t0) + Instrument_Model(t0)

Onde:
- te = tempo de emissao
- t0 = tempo de observacao
- Source_State(te) = estado da fonte quando emitiu
- Source_State(t0) = estado atual estimado ou desconhecido
- Propagation = expansao, redshift, absorcao, lenteamento e selecao

## Estados possiveis

SOURCE_STABLE
SOURCE_DIMMED
SOURCE_BRIGHTENED
SOURCE_OBSCURED
SOURCE_QUENCHED
SOURCE_MERGED
SOURCE_COMPACT_REMNANT
SOURCE_ACCRETING
SOURCE_OFF_CENTER_OR_WANDERING
SOURCE_UNKNOWN

## Claim boundary

Nao afirmar que a fonte ainda existe igual apenas porque seu sinal chegou.
Nao afirmar estado atual sem modelo ou novas observacoes.
Preservar TOKEN_VAZIO quando o estado atual nao puder ser inferido.

## Ponte RLL

compressao energia -> emissao transiente -> propagacao cosmologica -> observacao -> inferencia -> lacuna auditavel
