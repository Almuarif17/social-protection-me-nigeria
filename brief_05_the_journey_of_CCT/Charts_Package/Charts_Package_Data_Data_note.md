# Data

Four CSV files, one per chart in Brief 5. Every value is grounded in a named source in the brief's 26-source evidence matrix.

---

## The four CSVs

### `chart1_transfer_adequacy.csv`

Transfer size across CCT programmes in USD per household per month.

**Columns:**
- `programme` — programme name (e.g. Progresa, Bolsa Familia, NASSP-HUP).
- `country` — country name.
- `transfer_usd_month` — transfer value in USD per household per month.
- `pct_consumption` — transfer as percentage of beneficiary household consumption.
- `note` — source or context note explaining the figure.

Two rows for Nigeria's NASSP-HUP: one at appraisal (2016, USD 12.17 nominal) and one for 2026 real value (USD 3.50 after NBS Food CPI deflation).

### `chart2_coverage_share.csv`

Cash transfer coverage as share of national population across eleven programmes.

**Columns:**
- `programme` — programme name.
- `country` — country name.
- `households_millions` — number of beneficiary households in millions.
- `population_share_pct` — beneficiary share of national population, as a percentage.
- `note` — source or context note.

Two rows for Nigeria: `NASSP-HUP achieved` (1.8 million households, below 2 per cent) and `NASSP-SU target` (10.2 million households aspirational, roughly 10 per cent).

### `chart3_real_value_trajectory.csv`

Real transfer values in USD per household per month, 2016 to 2026, for five programmes.

**Columns:**
- `year` — calendar year, 2016 to 2026.
- `nassp_hup_nigeria` — Nigeria NASSP-HUP real value, deflated by NBS Food CPI.
- `ct_ovc_kenya` — Kenya CT-OVC, maintained through indexation.
- `bolsa_brazil` — Brazil Bolsa Familia basic benefit.
- `leap_ghana` — Ghana LEAP.
- `prospera_mexico` — Mexico Prospera (2019 discontinuity when AMLO replaced it).
- `adequacy_threshold` — the USD 20 reference line.

Values are estimates where indexation is not documented in the primary source.

### `chart5_outcome_hierarchy.csv`

CCT effect hierarchy by outcome domain. Basis for Chart 4 (file numbered `05_` for provenance; see the Charts_Package About file for the numbering note).

**Columns:**
- `outcome_domain` — one of Education access, Health utilization, Nutrition, Economic empowerment.
- `evidence_strength_score` — 1 to 4 scale used for bar length (4 strongest, 1 weakest).
- `effect_size_range` — plain-language summary of the documented effect size range.
- `replication_frequency` — how consistently the effect replicates across studies.
- `nigeria_targets_this` — yes / partial / no, indicating whether Nigeria's NASSP-HUP conditions on this domain.
- `note` — one-line synthesis of the domain finding.

---

## How to reuse the data

The CSVs are UTF-8 encoded and use standard comma delimiters. They open cleanly in pandas, Excel, Google Sheets, R, and Stata.

If you cite any figure from these CSVs, please reference the underlying source named in the brief's evidence matrix rather than the CSV itself. The CSV is a working file; the source is what carries the epistemic weight.

Released under Creative Commons Attribution 4.0 International (CC-BY 4.0) with attribution to the Brief 5 review.
