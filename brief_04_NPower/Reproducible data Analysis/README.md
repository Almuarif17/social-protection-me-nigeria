# Reproducible Data Analysis

The complete analytical pipeline behind the three charts in the N-Power Brief 4 review. Anyone with Python and Jupyter can clone this folder, run the notebook, and regenerate every chart from source.

---

## What is in this folder

### 📓 Jupyter notebook

**File:** `NPower_Brief4_Charts.ipynb`

Four cells: one setup cell that loads libraries and defines the house style, and three chart cells (one per chart). Each chart cell reads its CSV, builds the chart, displays it inline, and saves a 300 DPI PNG to a `charts/` sub-folder created on first run.

The notebook is written to run identically in Jupyter Notebook, JupyterLab, VS Code's Jupyter extension, and Google Colab.

### 📊 Three source CSVs

**File:** `npower_budget_transparency.csv`

Yearly N-Power federal budget figures, 2016 to 2024. Columns:
- `year` — programme year.
- `value_naira_bn` — value in ₦ billion, or blank where no figure is disclosed.
- `category` — one of `N-Power verified`, `Ministry envelope`, or `Not disclosed`.
- `label` — the display label for the chart annotation.
- `source_note` — the source reference for the figure.

**File:** `npower_reach_verification.csv`

Reach claims and independent verification across batches and sub-strands. Columns:
- `batch_strand` — batch identifier (A, B, C Stream 1, C Stream 2, N-Teach cumulative, N-Health cumulative).
- `official_claim` — the federal claim figure.
- `verified_low`, `verified_high` — the independently verified range, if any exists.
- `verification_status` — plain-language status.
- `ghost_flag` — Y or N, whether ghost-name adjustment applies.
- `adverse_note` — the qualifying data point (arrears, disputes, etc.).
- `sources` — the source references.

**File:** `npower_stipend_real_value.csv`

Annual real-value calculation for the ₦30,000 stipend, 2016 to 2026. Columns:
- `year` — from 2016 base year through 2026.
- `nominal_stipend` — ₦30,000 flat across all years.
- `food_cpi_yoy_pct` — NBS Food CPI year-on-year percentage.
- `cumulative_deflator` — running product of `1 + food_cpi_yoy_pct/100`.
- `real_value_low`, `real_value_high` — the deflated real value band.
- `note` — source or contextual note.

---

## How to reproduce the charts

### Option 1, Google Colab (easiest, no setup)

1. Open Colab at [colab.research.google.com](https://colab.research.google.com).
2. File → Open notebook → GitHub tab → paste this repository URL and select `NPower_Brief4_Charts.ipynb`.
3. Upload the three CSVs to a `data/` sub-folder in the Colab session (drag and drop from the sidebar).
4. Run all cells.
5. Rendered PNGs will save to `charts/` in the Colab session; download them from the sidebar.

### Option 2, local Jupyter

1. Clone the repository, or download this folder.
2. Ensure Python 3.9 or later is installed.
3. Install dependencies: `pip install pandas matplotlib jupyter`
4. Open Jupyter: `jupyter notebook` (or use VS Code's Jupyter extension).
5. Open `NPower_Brief4_Charts.ipynb`.
6. Run the setup cell first, then each chart cell in order.

The notebook creates a `charts/` sub-folder on first run and writes the three PNGs there.

---

## Anchor sources

- **Budget figures:** BudgIT tracker (2020 to 2023) for ministry envelopes; TheCable (2019, 2021) for the 2016 N-Power-specific verified anchor of ~₦26.4bn.
- **Reach figures:** N-Power Information Guide (2017); NSIPA (2026); Premium Times (2019); Punch (2020); TheCable (2019, 2021); FIJ (2024); ANEEJ (2025); Osimen et al. (2025); Guardian Nigeria (2024).
- **Ghost-name adjustment:** TheCable (2019, 2021) undercover investigation; second list (D'Banj) reported 2021; individual cleared by ICPC in November 2023.
- **Stipend deflator:** NBS Consumer Price Index, Food sub-index (annual averages). Series re-based to 2024 = 100 by NBS in 2024, which introduces a level break the notebook flags in Chart 3.

---

## What the charts do not do

- They do not extrapolate beyond the source data. Where no figure exists, the chart shows an empty bar or annotation, not an interpolation.
- They do not claim causal attribution. Chart 2's verification band is arithmetic on documented ghost-name counts, not an audit.
- They do not smooth across the CPI base year revision. Chart 3 renders a re-basing sensitivity band rather than a single point value.

Full methodological notes are in Section 7 of the main brief.

---

## Licence

Data files and notebook are shared under Creative Commons Attribution 4.0 International (CC-BY 4.0). Free to reuse and adapt with attribution.

---

*Author: Usman Almuarif Mashood · Independent Policy Researcher · [github.com/Almuarif17](https://github.com/Almuarif17)*
