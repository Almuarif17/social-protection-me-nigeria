# Charts Package

Everything that goes with the four charts in Brief 5: the finished PNG files themselves, the analysis pipeline that generates them, and the source data that drives them. Standalone, 300 DPI, ready for reuse under CC-BY 4.0 with attribution.

---

## What is in this folder

Four PNG chart files sit at this level. Two sub-folders hold everything else.

### 📁 [Analysis](Analysis)

The reproducible pipeline plus the documents that explain how Brief 5 was built.

- Jupyter notebook (`Brief5_Charts.ipynb`) and standalone Python script (`brief5_charts.py`) that generate all four charts from the CSVs in the `Data` folder.
- The Brief 5 approach note (`Brief5_Approach_Note.pdf`) documenting the main objective, methodology (chronological country genealogy plus synthesis), the five-point country story frame, and the source discipline.
- The full 26-source evidence matrix (`Source Matrix extracted.pdf`) with every source, its citation, its section served, its country and programme, its findings, and its one-line contribution to the brief.

### 📁 [Data](Data)

The four source CSVs, one per chart. Every value is grounded in a named source in the evidence matrix. See the folder's own `Data_note.md` for column definitions.

---

## The four charts

### Chart 1, Transfer adequacy across CCT programmes

**File:** `01_transfer_adequacy.png`

*Transfer size across CCT programmes, USD per household per month, with the 20 per cent consumption adequacy threshold from Bastagli et al. (2016).*

Horizontal bar chart sorted by transfer size. Programmes at or above the adequacy threshold shown in amber. Programmes below the threshold shown in burnt orange. Nigeria's NASSP-HUP shown twice (nominal at appraisal and real 2026 value) and highlighted in red. The adequacy threshold sits as a vertical dashed reference line. The chart makes the adequacy failure visible in one image: Nigeria's real 2026 value of USD 3.50 sits an order of magnitude below the threshold.

Source: Brief 5 country sources (Bastagli et al. 2016; F1 Fiszbein and Schady 2009; F4a IEG 2024; UNICEF Transfer Project). Values are nominal at last documented year.

### Chart 2, Coverage as share of national population

**File:** `02_coverage_share.png`

*Cash transfer coverage as share of national population across eleven programmes.*

Horizontal bar chart sorted by population share. Nigeria shown twice: achieved coverage under the regular-CT programme (below 2 per cent, highlighted in red) and the NASSP-SU aspirational target (10 per cent, shown in amber outline). The chart places Nigeria's achieved position alongside Ghana and Kenya at the bottom of the distribution, while the aspirational target would bring it into the Latin American coverage range.

Source: Brief 5 country sources; F4a IEG 2024; F4b NASSP-SU PAD 2024. JSY shown as annual flow (one-time payment per delivery).

### Chart 3, Nigeria real-value trajectory versus comparators

**File:** `03_real_value_trajectory.png`

*Real-value trajectory of cash transfers 2016 to 2026, USD per household per month at 2016 base year.*

Line chart comparing five programmes' real transfer values over eleven years. Nigeria NASSP-HUP in thick red shows a monotone decline from USD 12.17 in 2016 to below USD 4 in 2026, unmatched by any comparator. Kenya CT-OVC maintains real value through indexation. Brazil's Bolsa Familia adjusted upward in 2023 under Lula's restructuring. Ghana's LEAP nominally quadrupled but only doubled in real terms. Mexico's Prospera was replaced by an unconditional pension in 2019. The adequacy threshold reference line sits at USD 20.

Source: Brief 5 country sources; NBS Food CPI; F4a IEG 2024; F4b NASSP-SU PAD 2024. Values estimated where indexation not documented.

### Chart 4, CCT effect hierarchy by outcome domain

**File:** `05_outcome_hierarchy.png`

*The four outcome domains ranked by evidence strength, effect size, and replication frequency, with an indicator showing which domains Nigeria targets.*

Horizontal bar chart with four rows. Education access and health utilization show the strongest evidence and largest effects (amber). Nutrition sits at moderate (burnt orange). Economic empowerment is the weakest domain (red): cash alone does not create sustained employment or exit from poverty. A right-side column indicates which domains Nigeria's NASSP-HUP formally targets. The chart shows Nigeria targets the two strongest-evidence domains, but the accompanying analysis in Section 10 documents that Nigeria operates below the conditions those domains require.

Source: Brief 5 Section 10 synthesis of Bastagli et al. 2016, Baird et al. 2011, and country-level evidence tabulated in the source matrix.

Note: the chart file is numbered `05` because in an earlier draft the outcome section was Section 10A and this was Chart 5. The section was promoted to Section 10 in the final draft. The chart is referred to as Chart 4 in the finished brief. The file name is preserved for provenance.

---

## How to regenerate

1. Open `Analysis/Brief5_Charts.ipynb` in Jupyter, JupyterLab, or Google Colab.
2. Run the setup cell to load libraries and define the house style.
3. Run each chart cell in order. Each cell reads its CSV from the `Data` folder, builds the chart, displays it inline, and saves the PNG.

Alternative: run `python Analysis/brief5_charts.py` from a terminal in the `Charts_Package` folder to regenerate all four charts in one go.

---

## Licence

Released under Creative Commons Attribution 4.0 International (CC-BY 4.0). Free to share, adapt, and build upon with attribution:

> Mashood, U. A. (2026). Brief 5 charts, from *The Journey of an Instrument: How Conditional Cash Transfer Design Travelled from Latin America to Nigeria, 1997 to 2026.* Social Protection M&E Nigeria series. github.com/Almuarif17/social-protection-me-nigeria
