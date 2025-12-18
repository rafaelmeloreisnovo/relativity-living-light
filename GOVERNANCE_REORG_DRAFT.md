governanca e goverbanca
# Repository Audit & Governance Draft Plan (DRAFT)
_Scope: non-destructive reorganization, governance cleanup, and reproducibility scaffolding. No files were moved or altered._

## A. Repository Audit (Inventory & Classification)
- **Root**: `README.md` (manifesto/symbolic), `README_MASTER.md` (navigation), `REFORM_LOG.md`, `RESUMO_REFORMA.md`, `SECURITY_SUMMARY.md`, `LICENSE.md` (RAFCODE-𝚽, non-OSI), `requirements.txt`.
- **Docs (`/docs`)**: mixture of scientific (e.g., `Conclusion.md`, `Structure.md`, `RelativityLivingLight_arXiv.tex/.pdf`, `ARTICLE_ANALYSIS_SUMMARY.md`, `ANALISE_ARTIGO_NATURE_PT.md`) and symbolic/manifesto content (`MANIFESTO.md`, `MAPA_RAFAELIA_TOTAL.md`, `SUPREMO UNIFICADO.md`, `IMPACT_REPORT_MULTI.md`, `New theory and beyond.md`, numeric series in `/docs/numeros_rafaelianos`). Patches and snippets (`README_patch_unified_PT_EN_v3/v4.md`, `README_snippet.md`, etc.) mix scientific explanation and narrative.
- **Data (`/data`)**:
  - Notebooks: `Hz_superposicao.ipynb`, `ciencia_Hz_superposicao*.ipynb`, `density_decomp.ipynb`, `rotation_model.ipynb`.
  - CSV/JSON: `posterior_unified_synth*.csv` (synthetic posterior), `relativity_living_light_models.csv`, `unified_entropy_margin_10_12.csv`, `zenodo.json`, `CITATION.cff` (CC-BY-SA-4.0, v4.0, author Rafael Melo Reis).
  - Bundles: `RelativityLivingLight_v4_bundle.zip` and `relativity_bundle_results.zip` (both contain README_patch_v4, unified_* plots, posterior CSV, mock fits, posteriors, synthetic_posterior_summary.json).
  - Mock/derived data: `posterior_unified_synth (1|2).csv`, `posterior_unified_synth.csv` appear synthetic; no observational provenance documented.
- **Figures (`/figs`)**: scientific plots (unified_* plots, post_* posterior grids, rotation/lensing demos), mock fits (`mock_H_fit*.png`, `mock_SN_fit*.png`), screenshots/photos (`IMG_*`, `Screenshot_*`), science visuals (`ciencia_hz_superposicao*.png`, `density_evolution_sup*.png`).
- **Governance files**: only `LICENSE.md` (custom), `SECURITY_SUMMARY.md`; `CITATION.cff` lives under `/data`; no NOTICE/manifest; no OSI/CC split licensing.
- **Placeholders/empty**: none found; all files non-empty based on listings.

## B. Gaps & Risks
- **Licensing ambiguity**: Custom RAFCODE-𝚽 license is non-OSI and asserts supra-constitutional terms; `data/CITATION.cff` lists CC-BY-SA-4.0, conflicting/unclear for code vs text vs data. No standard code license or CC license for docs; no NOTICE.
- **Governance coverage**: Missing root `CITATION.cff`, `NOTICE`, and a manifest of artifacts/hashes; zenodo.json exists but is not referenced; requirements lack pinning.
- **Reproducibility**: No runbook, seeds, or config files; notebooks have docstrings but no environment lockfile; synthetic/mock datasets (`posterior_unified_synth*`, bundle contents) are not labeled as synthetic in-file; no separation of observational vs synthetic.
- **Mixed scopes**: Scientific notebooks/data co-located with symbolic/manifesto texts; screenshots mixed with scientific plots; zip bundles duplicate files without checksums.
- **Ethical/attribution risk**: Third-party plots or images (screenshots, photos) not attributed; license terms for figures unspecified.
- **Latent/underdocumented**: `requirements.txt` minimal but not referenced in docs; bundles include `synthetic_posterior_summary.json` not surfaced in docs.

## C. Proposed Restructure (Logical Plan — no moves executed)
```
/                      (keep root manifest/README)
├── governance/        (new)
│   ├── LICENSE.md                # keep RAFCODE as declaration
│   ├── LICENSE_CODE_MIT.md       # standard OSI license for code/notebooks
│   ├── LICENSE_DOC_CC-BY-4.0.md  # CC-BY for text/figures unless otherwise noted
│   ├── NOTICE.md                 # attributions, data/figure sources
│   ├── CITATION.cff              # root citation (mirrors data/ version)
│   └── manifest.json             # hashes, provenance, synthetic flags
├── docs/
│   ├── symbolic_manifesto/   # MANIFESTO, MAPA*, SUPREMO*, RAFAELIA, numerology
│   ├── scientific_core/      # Conclusion, Structure, arXiv tex/pdf, ANALISE_*, ARTICLE_* 
│   ├── readme_patches/       # README_patch_unified_PT_EN_v3/v4, README_snippet*
│   ├── logs_summaries/       # REFORM_LOG.md, RESUMO_REFORMA.md, SECURITY_SUMMARY.md
│   └── references/           # REFERENCES.md, More.md, Others*, RESULTS/IMPACT
├── data/
│   ├── synthetic/            # posterior_unified_synth*.csv, synthetic_posterior_summary.json
│   ├── derived/              # relativity_living_light_models.csv, unified_entropy_margin_10_12.csv
│   ├── bundles/              # RelativityLivingLight_v4_bundle.zip, relativity_bundle_results.zip
│   ├── notebooks/            # *.ipynb
│   └── metadata/             # zenodo.json, CITATION.cff (if kept as copy)
├── figs/
│   ├── scientific/           # unified_*, post_*, rotcurve_*, cluster_lensing_*
│   ├── mock_demo/            # mock_* fits, demo curves
│   └── screenshots/          # IMG_*, Screenshot_*
└── configs/                  # proposed configs (seeds, data paths)
```
_Logical moves only; history-preserving moves to be performed in a future PR after approval._

## D. Governance Fix (Non-Destructive Proposals)
Files to add (contents below; do not delete existing `LICENSE.md`):

<details>
<summary>LICENSE_CODE_MIT.md</summary>

```
MIT License

Copyright (c) 2025 Rafael Melo Reis

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
</details>

<details>
<summary>LICENSE_DOC_CC-BY-4.0.md</summary>

```
Creative Commons Attribution 4.0 International (CC BY 4.0)

This repository's textual, visual, and non-code creative works are licensed
under CC BY 4.0 unless otherwise noted. You are free to share and adapt with
attribution. Full legal text: https://creativecommons.org/licenses/by/4.0/legalcode

Attribution: © 2025 Rafael Melo Reis (∆RafaelVerboΩ).
```
</details>

<details>
<summary>CITATION.cff (root)</summary>

```
cff-version: 1.2.0
title: "Relativity Living Light"
message: "If you use this work, please cite it as below."
authors:
  - family-names: "Melo Reis"
    given-names: "Rafael"
    orcid: "https://orcid.org/0000-0000-0000-0000"
doi: 10.5281/zenodo.17187966
license: CC-BY-SA-4.0
version: "v4.0"
date-released: 2025-09-24
repository-code: "https://github.com/instituto-Rafael/relativity-living-light"
```
</details>

_Note: license set to CC-BY-SA-4.0 to mirror current `data/CITATION.cff`; adjust if the project adopts a different canonical doc/figure license (e.g., CC-BY-4.0). ORCID should use the canonical format `0000-0000-0000-0000` (or `https://orcid.org/0000-0000-0000-0000`)._

<details>
<summary>NOTICE.md</summary>

```
Relativity Living Light — NOTICE

- Original manifesto and symbolic content © 2025 Rafael Melo Reis (RAFCODE-𝚽 declaration retained).
- Code/notebooks: MIT License (see LICENSE_CODE_MIT.md).
- Text and figures: CC BY 4.0 unless a file states otherwise.
- Third-party assets: cite sources for screenshots/photos if external; mark internal captures as project-owned.
- Data: synthetic/model outputs (`posterior_unified_synth*.csv`, bundle contents) — not observational data.
```
</details>

<details>
<summary>manifest.json (template)</summary>

```json
{
  "version": "0.1.0-draft",
  "generated": "2025-12-18",
  "artifacts": [
    {"path": "data/posterior_unified_synth.csv", "type": "synthetic-posterior", "sha256": "<fill>", "source": "model sampling", "notes": "synthetic"},
    {"path": "data/relativity_living_light_models.csv", "type": "derived-grid", "sha256": "<fill>", "source": "model grid"},
    {"path": "data/unified_entropy_margin_10_12.csv", "type": "derived-band", "sha256": "<fill>", "source": "entropy margin"},
    {"path": "data/RelativityLivingLight_v4_bundle.zip", "type": "bundle", "sha256": "<fill>", "contents": ["unified_* plots", "posterior_unified_synth.csv", "synthetic_posterior_summary.json"]},
    {"path": "data/relativity_bundle_results.zip", "type": "bundle", "sha256": "<fill>", "contents": ["unified_* plots", "posterior_unified_synth.csv"]},
    {"path": "figs/unified_H_ratio.png", "type": "figure", "sha256": "<fill>", "source": "model output"}
  ],
  "licenses": {
    "code": "MIT",
    "docs": "CC-BY-4.0",
    "declaration": "RAFCODE-𝚽 (kept as author declaration)"
  },
  "provenance": {
    "datasets": [],
    "synthetic": ["posterior_unified_synth*.csv", "bundle posterior files"]
  }
}
```
</details>

_Guidance: replace `<fill>` with SHA256 values via `sha256sum <path>` (e.g., `sha256sum data/posterior_unified_synth.csv`) or Python (`python -c "import hashlib, pathlib; print(hashlib.sha256(pathlib.Path('data/posterior_unified_synth.csv').read_bytes()).hexdigest())"`), and revise license/provenance fields once a final governance decision is made._

## E. Reproducibility Plan
- **Data labeling**: Mark `posterior_unified_synth*.csv`, `synthetic_posterior_summary.json`, bundle posterior outputs as synthetic; distinguish any future observational references in `data/metadata/`.
- **Configs**: Add `configs/default.yaml` with seeds, data paths, model parameters (`Omega_s0`, `z_t`, `w_t`, `Omega_B0`, `Omega_P0`), and paths to CSVs/figures.
- **Environment**: Pin `requirements.txt` to exact versions (switch current `>=` to `==`) and provide `python -m venv .venv && pip install -r requirements.txt`; optionally generate a lock via `pip freeze > requirements-lock.txt` or use pip-tools (`pip install pip-tools && pip-compile requirements.in`).
- **Pipelines (skeleton)**:
  1. `make prepare` → create `.venv`, install deps.
  2. `make reproduce` → run notebooks headlessly (papermill) to regenerate CSVs/figures from synthetic data.
  3. `make validate` → checksum compare against `manifest.json`; flag drift.
- **Separation of concerns**:
  - **Model consistency demo**: regenerate synthetic posteriors, mock fits, unified_* plots from notebooks using seeds in configs.
  - **Observational validation (future)**: add external dataset references (BAO/SNe/rotation curves) with provenance URLs; keep in `data/raw/observational/` and cite in `NOTICE`.
- **Provenance**: Add note in notebooks headers linking to `manifest.json`; record random seeds per run.

## F. Draft Pull Request (to open as DRAFT)
**Title:** DRAFT: Repository audit, governance alignment, and reorg plan  

**Description:**
- Provide a consolidated audit of content types and governance gaps.
- Propose non-destructive folder reorganization separating symbolic, scientific, and experimental layers.
- Introduce draft governance artifacts (MIT for code, CC-BY for text/figures, NOTICE, root CITATION, manifest template) while retaining RAFCODE declaration.
- Outline reproducibility steps and synthetic-data labeling.

**Checklist:**
- [ ] Add governance drafts (MIT, CC-BY, NOTICE, root CITATION, manifest template) under `governance/`.
- [ ] Document proposed folder tree and file moves (no content deletions).
- [ ] Label synthetic/mock data and update notebook headers to point to manifest.
- [ ] Add configs/default.yaml with seeds/paths; pin requirements.
- [ ] Validate notebooks headlessly (optional) or record skipped reason.

**Testing:** Not run (pytest unavailable/not listed). Suggested checks for this repo: headless notebook execution (papermill), data/manifest checksum validation, and simple integrity asserts on CSVs.

## G. Commit Plan (ordered, future work)
1. `docs: add governance audit and restructure plan (draft)` — add this plan file and summarize inventory/gaps.
2. `chore: add governance drafts (MIT, CC-BY, NOTICE, manifest, citation)` — add governance folder with proposed files; no existing license removed.
3. `docs: document reproducibility setup` — add configs template, update notebooks README pointers, and note synthetic data labeling.

## H. Notes on Validation
- Attempted `python -m pytest` → failed because `pytest` is not installed (no tests discovered). No further execution performed to keep repository unchanged.
