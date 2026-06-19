# Brief 2 — AGILE Independent M&E Review

**A primary-data Monitoring & Evaluation review of Nigeria's Adolescent Girls Initiative for Learning and Empowerment (AGILE), drawing on the World Bank's anonymised AGILE-IE Baseline Survey 2023.**

Author: Usman Almuarif Mashood · Published June 2026

---

## What this brief is

AGILE is the largest gender-focused education investment in West African history. Co-financed by the World Bank's International Development Association under Projects P170664 (2020, $500m) and P179281 (2023, $700m), it targets 8.6 million adolescent girls across 18 Nigerian states, with a cumulative disbursement of $368.87m as of June 2025.

This brief takes the AGILE-IE Baseline Survey 2023 — a World Bank-collected dataset of 8,223 adolescent girls, 8,007 caregivers, and 270 school principals across Kaduna, Kano, and Katsina — and examines it for four specific measurement gaps: gaps where the programme's official Results Framework does not measure what determines whether outputs convert into outcomes.

The four findings:

1. **The digital-literacy floor.** Across the three surveyed states, only 17% of SS1 girls have ever used a mobile phone independently, 6% have used a smartphone, and under 1% have ever touched a computer. Yet the Results Framework counts digital-literacy trainees without a baseline on prior exposure.
2. **The caregiver aspiration gradient.** Caregiver educational aspirations for daughters drop sharply moving north across the three states: 73% of Kaduna caregivers aspire to bachelor's-level or higher, vs. 32% in Katsina. Yet the Results Framework has no baseline aspiration measure against which to evaluate social-norm change.
3. **Household food insecurity.** 21% of households in the sample skipped meals in the past seven days, rising to 27% in Katsina. The Results Framework includes no food-security indicator to verify that financial incentives reach the most vulnerable households.
4. **The school-seating gap.** While 95% of surveyed schools have toilets and 92% have water and blackboards, only 26% have sufficient classroom seats for their enrolled SS1 cohort. The official infrastructure indicators count classrooms built, not seats provided.

The brief closes with five specific, operational indicator recommendations that AGILE should incorporate into its Results Framework before the midline survey.

---

## Files in this folder

- 📄 **[AGILE_Independent_ME_Review.pdf](./AGILE_Independent_ME_Review.pdf)** — the full 30-page brief
- 📐 **[AGILE_Brief2_Dashboard.tex](./AGILE_Brief2_Dashboard.tex)** — LaTeX source for a 7-page visual-summary dashboard (compile with XeLaTeX to produce a professional landscape PDF)
- 🐍 **[AGILE_Brief2_Analysis.ipynb](./AGILE_Brief2_Analysis.ipynb)** — fully reproducible Google Colab notebook generating every chart and table in the brief
- 📊 **[key_findings_numbers.csv](./key_findings_numbers.csv)** — 83 rows of analysis-tagged, state-disaggregated percentages — the underlying numbers for every chart and table
- 🖼️ **Chart PNGs** — the four publication-quality figures used in Section 4:
  - `01_digital_literacy_floor.png`
  - `02_caregiver_aspiration_gradient.png`
  - `03_food_insecurity.png`
  - `04_school_infrastructure.png`

---

## How to reproduce the analysis

1. Download the AGILE-IE Baseline Survey 2023 (catalogue identifier `NGA_2023_AGILE-IE_v01_M`) from the World Bank Microdata Library at https://microdata.worldbank.org/index.php/catalog/6239. Free registration required; all terms are standard World Bank microdata terms.
2. Download the three CSVs (`adolescent_survey_anon.csv`, `caregiver_survey_anon.csv`, `school_survey_anon.csv`) and the questionnaires & codebook from the same catalogue entry.
3. Open `AGILE_Brief2_Analysis.ipynb` in Google Colab.
4. Run Cell 1 to set up the environment and libraries.
5. Run Cell 2; when the upload prompt appears, select all three CSVs at once.
6. Run Cells 3 through 9 in sequence. The notebook will load the data, verify row and column counts against the published metadata, perform the four analyses, generate the four PNG charts, export the findings CSV, and create a summary stats table.

The notebook was developed and tested on Google Colab (Python 3.10, pandas 2.x, NumPy 1.26, Matplotlib 3.8). It runs end-to-end in under five minutes on a free Colab runtime.

---

## Compiling the LaTeX Dashboard

To compile the `AGILE_Brief2_Dashboard.tex` file to PDF:

**On your local machine (if you have a LaTeX installation):**
```bash
xelatex AGILE_Brief2_Dashboard.tex
```

**Online (no installation needed):**
- Upload the `.tex` file to [Overleaf](https://www.overleaf.com/) or another online LaTeX editor
- Ensure the compiler is set to **XeLaTeX** (not pdfLaTeX)
- Click "Recompile" to generate the PDF

The dashboard will produce a 7-page landscape PDF with the brief's title, timeline, key achievements, methodology, four findings, and recommendations.

---

## Data source — citation and terms

> Chang, W., Gulesci, S., Hailemichael, A. H., Rouanet, L., Mohammed, A. G., & Jagun, F. A. (2024). Nigeria — Adolescent Girls Initiative for Learning and Empowerment: Impact Evaluation of a Safe Learning Environment and Social Norm Change. World Bank, Poverty and Equity Global Practice. [Microdata catalogue: NGA_2023_AGILE-IE_v01_M](https://microdata.worldbank.org/index.php/catalog/6239)

The dataset is public-use and anonymised. Personally identifying fields (school names, GPS coordinates, supervisor names, applicant names) are replaced with "Removed for publication" in the public catalogue.

This repository does **not** redistribute the dataset. Readers wishing to reproduce or extend the analysis must download the data themselves from the World Bank Microdata Library under the terms of use.

---

## Methodology and limitations

The brief is a cross-sectional descriptive analysis of baseline data. It establishes pre-intervention starting conditions across three of seven original AGILE states and identifies measurement gaps in the official Results Framework.

Specific limitations stated in the brief's Methodology section:

- The data is baseline only. Findings characterise programme readiness and household context, not programme effect.
- The sample is restricted to SS1 girls enrolled in 270 selected schools. Out-of-school adolescents are not represented.
- Three of seven original AGILE states are surveyed. The 2023 Additional Financing expanded the programme to eleven additional states; those states are not in the analysis.
- All measures are self-reported via CAPI interview, with the usual social-desirability caveats around sensitive items.

---

## A future Brief in this series

Brief 3 of this series will turn to learning outcomes and the measurement of academic performance among enrolled SS1 girls at baseline, drawing on the AGILE-IE Baseline Survey's reading-assessment module and comparative analysis with Nigeria's national learning assessments.
