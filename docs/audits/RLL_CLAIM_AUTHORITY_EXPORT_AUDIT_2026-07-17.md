# Auditoria do Export de Autoridade RLL

Data: `2026-07-17`  
Branch: `docs/rll-claim-authority-export-20260717`  
Estado: `IMPLEMENTED_NOT_MERGED / claim_allowed=false`

## O que foi gravado

- export machine-readable dos estados de claim RLL;
- preservação do resultado computacional registrado em `20260709-132833-utc`;
- distinção entre resultado local, superioridade ampla e confirmação física;
- validador fail-closed;
- workflow com checksum e artifact.

## Leitura permitida

```text
A execução registrada comparou os modelos presentes no JSON de entrada.
Na métrica BIC daquele artefato, CPL venceu e o relatório marcou RLL_PERDE.
```

## Leituras bloqueadas

```text
RLL perdeu universalmente.
CPL é a teoria verdadeira.
RLL foi confirmado fisicamente.
RLL é estatisticamente superior em geral.
Uma execução substitui replicação, revisão e novos dados.
```

## Limitações preservadas

- `source_ref=main` ainda não é pin imutável de commit;
- o blob SHA protege o conteúdo dos arquivos citados, mas não substitui um manifesto assinado;
- novas execuções podem alterar o estado, desde que preservem a história;
- consumidores precisam registrar `STALE_CONSUMER` quando ficarem atrás do produtor;
- esta mudança não executa likelihood, MCMC ou comparação nova.

## Critério de promoção

```text
CI PASS
pin por commit/tag
checksum do export
sincronização no consumidor
revisão do escopo/not_claimed
claim_allowed permanece false para verdade física
```

## Resultado

O RLL passa a oferecer uma primeira interface explícita de produtor de claims. Ela permite consumo rastreável sem transformar um README interpretativo em autoridade científica paralela.
