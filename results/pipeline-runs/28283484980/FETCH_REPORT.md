# FETCH_REPORT

mode: `full`
- igrf14: fetched
- wmm2025: fetched
- omni: fetched
- nmdb: fetched
- desi: manual_materialization_required
  - reason: DESI bulk data are large and should be selected from the data portal before materialization.
- pantheon: fetched
- planck: manual_materialization_required
  - reason: Planck archive products are large and product-specific; select products in ESA PLA before download.
- spenvis_reference: manual_materialization_required
  - reason: SPENVIS workflows require portal/session configuration before exporting data.