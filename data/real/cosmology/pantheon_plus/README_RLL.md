# Pantheon+SH0ES official non-binary release files

This directory materializes selected **official** text/table files from the public
Pantheon+SH0ES `DataRelease` repository:

- source repository: <https://github.com/PantheonPlusSH0ES/DataRelease>
- materialized subset: `README.md`, Pantheon+ redshift/data tables, the
  `Pantheon+SH0ES.dat` distance table, and non-binary SH0ES calibration/result
  tables.
- excluded from git by policy: FITS files, `NewLCs.tar`, and the large
  covariance matrices (`Pantheon+SH0ES_STAT+SYS.cov`,
  `Pantheon+SH0ES_STATONLY.cov`). These are official release products but are
  intentionally not committed here because they are binary/heavy or too large for
  review diffs. Fetch them from the upstream repository when a full covariance
  likelihood is required.

`MANIFEST.json` records source URLs, sizes, and SHA256 checksums for every
materialized non-binary file.

Scientific boundary: these files establish source custody and ingestion
readiness only. Model-preference claims still require the appropriate likelihood,
covariance handling, and validation gates.
