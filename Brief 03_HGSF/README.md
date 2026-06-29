# Brief 3 — National Home-Grown School Feeding Programme (NHGSFP) · Independent M&E Review

**An independent Monitoring & Evaluation review of Nigeria's National Home-Grown School Feeding Programme — Africa's largest school-feeding initiative.**

Author: Usman Almuarif Mashood · Independent M&E Researcher · Published June 2026

---

## What this brief is

The National Home-Grown School Feeding Programme (NHGSFP) is the Federal Government of Nigeria's commitment to providing one daily mid-day meal to pupils in Primary 1–3 across public primary schools nationwide. At its 2022 peak it claimed to feed nearly 10 million pupils across 53,000+ schools through 127,000 community cooks, at a fixed unit cost of ₦70 per child per meal.

This brief is the independent M&E specification for a verification system that should already exist. It examines the programme through five analytical lenses:

1. **What it committed to do** — the official five-pillar design and Results Framework architecture
2. **What the evidence shows** — performance against committed targets through programme data, donor assessments, audit reports, and independent academic studies
3. **Where the M&E framework falls short** — gaps in monitoring architecture and data availability
4. **What the programme has genuinely achieved** — documented successes in reach, enrolment, employment, and smallholder agriculture
5. **What should be added to the framework** — five operational, costed, time-bound recommendations

The brief draws on **34 curated public sources** spanning official government portals, World Bank and UN assessments, legislative oversight reports, ICPC fraud investigations, peer-reviewed academic studies, civic-data platforms (BudgIT), and investigative journalism (Punch, Premium Times, Vanguard, Guardian Nigeria, Tribune Online, The Cable, BusinessDay). Where sources conflict, the contradiction is **named** rather than resolved.

---

## How to navigate this brief

This folder is organised into three sections for different types of reader.

### 📚 [HGSF Reading and Summary](https://github.com/Almuarif17/social-protection-me-nigeria/tree/main/Brief%2003_HGSF/HGSF%20Reading%20and%20Summary) — Executive reports

The narrative outputs, in three reader-targeted formats:

- **Full Brief (22 pages)** — complete evaluation with methodology, four findings, five recommendations, limitations, and methodological caveats. Read this if you want the full argument.
- **Executive Summary (7 pages)** — the M&E-style condensed version. Read this if you have 10 minutes and want the spine of the analysis.
- **LinkedIn Dashboard (9 pages)** — the visual-first carousel with big typography, suited for phone scrolling and document-post sharing.

**[📖 View Reading and Summary documentation →](https://github.com/Almuarif17/social-protection-me-nigeria/blob/main/Brief%2003_HGSF/HGSF%20Reading%20and%20Summary/About%20Documentations.md)**

### 📊 [IMAGES](https://github.com/Almuarif17/social-protection-me-nigeria/tree/main/Brief%2003_HGSF/IMAGES) — Publication-quality charts

Five standalone PNG charts at 300 DPI, ready for citation, reuse, or republication under CC-BY:

- `01_budget_trend.png` — Annual federal allocation, 2018–2023
- `02_reach_trend.png` — Federal pupil-reach claims, 2017–2025 (peak, suspension, pilot relaunch)
- `03_cost_per_meal.png` — Where ₦70 actually goes (food vs. overhead breakdown)
- `03b_real_value_70_deflated.png` — Real-terms purchasing power of ₦70/meal, NBS Food CPI deflated, 2016–2025
- `04_fraud_recovery.png` — Documented fraud incidents vs. NSIPA recovery action, log scale, 2019–2025

**[📖 View IMAGES documentation →](https://github.com/Almuarif17/social-protection-me-nigeria/blob/main/Brief%2003_HGSF/IMAGES/Image%20Note.md)**

### 🔬 [R and Data Analysis](https://github.com/Almuarif17/social-protection-me-nigeria/tree/main/Brief%2003_HGSF/R%20and%20Data%20Analysis) — Reproducible analytical pipeline

The full technical layer. Anyone with R + Quarto + tidyverse can clone this repository and re-render every chart and every page from source:

- `HGSF_Brief3_Analysis.qmd` — the Quarto source file (analysis + prose in one)
- `Feeding the Bet — HGSF Brief 3 Analysis.pdf` — the rendered analytical output
- `HGSF_ME_Review_Structured_Extraction_Table.pdf` — the full 34-source extraction matrix with author, date, source type, URL, programme element, indicators, quantitative findings, qualitative themes, and gap assessment per row
- Five source CSVs — `hgsf_budget_series.csv`, `hgsf_reach_claims.csv`, `hgsf_cost_per_meal.csv`, `hgsf_real_value_70naira.csv`, `hgsf_fraud_timeline.csv`

**[📖 View analysis documentation →](https://github.com/Almuarif17/social-protection-me-nigeria/blob/main/Brief%2003_HGSF/R%20and%20Data%20Analysis/Note%20on%20Analysis.md)**

---

## Headline findings

**Finding 1 — The budget arithmetic that does not reconcile.** Component years disclosed (₦63.2bn + ₦32.2bn + ₦124.4bn) sum to ₦219.8bn, not the stated cumulative ₦186bn. A ₦33.8 billion discrepancy has never been publicly reconciled. Only ₦64bn of the ₦186bn reached direct feeding.

**Finding 2 — The ₦70 question.** The unit cost was set at ₦70 in 2016 and held there until the 2024 suspension. The ₦100 rate approved in 2022 was never implemented. NBS Food CPI–deflated, ₦70 in 2025 retains the food-purchasing power of approximately ₦11 in 2016 terms — less than one-sixth of its launch value.

**Finding 3 — Three orders of magnitude.** Documented fraud incidents (₦40m + ₦68m Kogi 2019; ₦2.67bn COVID-period allegation 2020) are dwarfed by the ₦30 billion+ NSIPA recovery action of December 2025.

**Finding 4 — The measurement blind spot.** No public NHGSFP dashboard exists. No quarterly state-level delivery record has been published since 2020. WFP School Meals Coalition (2023) records 10 million pupils receiving meals; the World Bank / NASSCO (2025) review states the programme has not delivered benefits since 2023. Two reputable bodies, the same year, irreconcilable on the basic question of whether the programme exists.

---

## Five recommendations

1. **Public quarterly dashboard** — NSIPA + FME, feasible in 90 days, no legislation required.
2. **Independent verification budget line** — ≥1% of NHGSFP annual budget for accredited CSO verification, 2027 appropriation.
3. **Biometric cook registry** — NIN-anchored, NSIPA + NIMC, pilot 10,000 cooks across 2 states within 180 days.
4. **Automatic unit-cost review trigger** — legislated, NBS Food CPI ≥25% movement compels rate review within 60 days; include in the 2026 Finance Act.
5. **State co-financing readiness audit** — NSIPA + State MoEs, scores published for 12 pilot states within 6 months.

---

## Methodological note

Secondary analysis of 34 publicly available sources. No primary fieldwork. Where sources conflict, contradictions are named rather than resolved. Inflation deflation uses NBS Food CPI annual averages indexed to 2016. Currency conversion for WFP figures uses the CBN 2023 annual average rate of approximately ₦750/$. Readers seeking primary data are directed to the CGIAR/IFPRI Osun State baseline study and the ANEEJ/NSIO Social Protection Baseline Report.

---

## Citation

> Mashood, U. A. (2026). *Feeding the Bet: An Independent M&E Review of Nigeria's Home-Grown School Feeding Programme, 2016–2025.* Brief 3 of the Independent M&E Reviews of Nigerian Social Investment Programmes. GitHub: github.com/Almuarif17/social-protection-me-nigeria.

---

## Licence

Content is shared under Creative Commons Attribution 4.0 International (CC-BY 4.0).

---

## Contact

Usman Almuarif Mashood · Independent M&E Researcher · usmanmashoodalmuarif@gmail.com · [linkedin.com/in/almuarifusman](https://linkedin.com/in/almuarifusman)
