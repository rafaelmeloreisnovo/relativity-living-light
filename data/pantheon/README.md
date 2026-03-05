# Pantheon+ inputs (offline-ready placeholder)

Coloque aqui os arquivos oficiais do Pantheon+ para ativar o estágio observacional completo:

- `lcparam_full_long_zhel.txt` (obrigatório)
- `sys_full_long.txt` (opcional, recomendado para covariância total)

Fonte oficial:
- https://github.com/PantheonPlusSH0ES/DataRelease

## Execução

Com os arquivos presentes:

```bash
python docs/panteon_likelihood.py
```

Sem os arquivos, o pipeline deve falhar com mensagem explícita de ingestão pendente.
