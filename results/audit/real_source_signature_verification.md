# Real source signature verification

- Sources verified: 6
- Sources needing review/failover: 1
- Fetch limit per URL: 65536 bytes

| dataset_id | status | status_code | local_path | source_url |
| --- | --- | --- | --- | --- |
| real_hz | source_verified | 206 | data/real/Hz_data_real.csv | https://arxiv.org/abs/2205.05701 |
| real_desi_dr2_bao | source_verified | 206 | data/real/cosmology/desi_dr2_bao_primary_points.csv | https://arxiv.org/abs/2503.14738 |
| real_desi_dr2_bao_supplement | source_verified | 200 | data/real/cosmology/desi_dr2_bao_covariance_summary.csv | https://zenodo.org/records/16644577 |
| real_fsigma8_6dfgs_anchor | source_verified | 206 | data/real/cosmology/fsigma8_growth_real.csv | https://arxiv.org/abs/1204.4725 |
| real_fsigma8_compilation | source_needs_review | 403 | data/real/cosmology/fsigma8_growth_real.csv | https://academic.oup.com/mnras/article-abstract/452/3/2930/1750209 |
| real_cmb_shift | source_verified | 206 | data/real/CMB_shift_real.json | https://arxiv.org/abs/1807.06209 |
| real_cmb_shift_covariance | source_verified | 206 | data/real/CMB_shift_real.json | https://arxiv.org/abs/1808.05724 |

## Failsafe

If a source is blocked or a required term is absent, keep the committed local file, mark the row as needing review, and do not fabricate replacement data.
