# Proveniência dos dados externos RLL

Status: registro leve de hashes disponíveis no repositório em 2026-07-01. Arquivos grandes excluídos do Git devem ser baixados novamente das URLs oficiais antes de qualquer submissão.

## DESI DR2 / BAO

| Artefato local | URL/referência oficial registrada | SHA256 | Status |
|---|---|---|---|
| `data/real/cosmology/desi_bao_dr2_cobaya/desi_gaussian_bao_ALL_GCcomb_mean.tsv` | `https://arxiv.org/abs/2503.14738` / release DESI DR2 BAO registrada no repositório | `138f09ca5d08506c1a45c4a1c50773f98b257e6b8981d95546e1fd5fbfee4ebc` | materializado leve |
| `data/real/cosmology/desi_bao_dr2_cobaya/desi_gaussian_bao_ALL_GCcomb_cov.tsv` | `https://arxiv.org/abs/2503.14738` / release DESI DR2 BAO registrada no repositório | `1d40b03d7ded75b609e2c1a38aacfa1b5eeff4795f2e8600b13e73fa2b1bee73` | materializado leve |
| `data/real/BAO_data_real.csv` | compilação operacional do repositório | `1decb159dd8c276e356e1f2ca45028da0079302a0b7b279797d8e40aab0c9527` | usado no gate |

## Pantheon+ / SH0ES

Fonte oficial registrada: `https://github.com/PantheonPlusSH0ES/DataRelease`.

| Arquivo oficial selecionado | URL | SHA256 |
|---|---|---|
| `Pantheon+_Data/4_DISTANCES_AND_COVAR/Pantheon+SH0ES.dat` | `https://raw.githubusercontent.com/PantheonPlusSH0ES/DataRelease/main/Pantheon+_Data/4_DISTANCES_AND_COVAR/Pantheon+SH0ES.dat` | `1cb0fc379ef066afdc2ffd1857681cc478024570d8a3eba284fb645775198cf8` |
| `Pantheon+_Data/1_DATA/all_redshifts_PVs.csv` | `https://raw.githubusercontent.com/PantheonPlusSH0ES/DataRelease/main/Pantheon+_Data/1_DATA/all_redshifts_PVs.csv` | `06641b9d3a54fc8ad1ce5a58dd11c6dce84af37e2f312326d2be0ca881a37d8a` |
| `README.md` | `https://raw.githubusercontent.com/PantheonPlusSH0ES/DataRelease/main/README.md` | `aebbe5d60292a548f008173b122073622f1f1c113af65ee988d29c53f51aa677` |

## Planck

| Artefato local | Referência | SHA256 | Status |
|---|---|---|---|
| `data/real/CMB_shift_real.json` | Planck 2018 VI, shift/ruler operacional local | `f658dafa16b57a4522bdf59c243d8693e20efe9936e2815720fed7ed6d637cdc` | usado no gate |

## H(z)

| Artefato local | Referência | SHA256 | Status |
|---|---|---|---|
| `data/real/Hz_data_real.csv` | compilação observacional operacional do repositório | `1194fe2066dc3d92b4870cfb03d2cdbe2a316deae2e1355943f7f2ccca6d52b6` | usado no gate |

## Token Vazio

`[VAZIO]`: hashes dos binários/covariâncias completos não versionados de Pantheon+ e Planck devem ser recalculados no ambiente de submissão após download oficial completo.
