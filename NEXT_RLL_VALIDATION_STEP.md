# Próximo salto RLL

Objetivo:
Executar validação real mínima Pantheon+ com baseline ΛCDM equivalente.

Requisitos:
1. Baixar Pantheon+ de fonte oficial.
2. Registrar provenance manifest:
   - URL
   - versão/tag
   - data UTC
   - SHA256
   - tamanho
   - licença/termos
3. Rodar:
   python scripts/verify_pantheon_inputs.py --json
   python -m rll.cli preflight-real --json
   python -m rll.cli run --data real --model both --with-covariance
4. Gerar:
   results/real_validation_report.json
   results/model_comparison_table.md
5. Incluir:
   - χ²
   - AIC
   - BIC
   - número de parâmetros
   - dataset usado
   - tolerância de rerun
6. Só depois disso permitir qualquer claim parcial sobre desempenho.
