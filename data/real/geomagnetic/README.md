# data/real/geomagnetic

Status: **Parcial real em preparação**.

## Registro de cadeia de custódia (preencher por dataset)
Para cada fonte utilizada, registrar:
- Fonte institucional;
- Versão/edição;
- URL e/ou DOI;
- Licença de uso;
- Data de acesso (UTC);
- Hash SHA-256 do arquivo bruto;
- Método de download (API/script/manual);
- Script de processamento aplicado.

## Fontes previstas
- IGRF14.
- WMM2025.
- ESA Swarm (2014–2025).

## Template mínimo por entrada
```yaml
source: ""
version: ""
url_or_doi: ""
license: ""
accessed_at_utc: "YYYY-MM-DDTHH:MM:SSZ"
sha256: ""
download_method: ""
processing_script: ""
notes: ""
```

## Observações
- Não promover status para validação real completa sem hashes e scripts reproduzíveis.
- Relacionar cada conjunto com hipótese, dado, modelo e métrica do pipeline geomagnético.
