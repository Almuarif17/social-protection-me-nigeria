# Social Protection M&E — Nigeria

**Independent Monitoring & Evaluation reviews of Nigerian social protection and human-capital programmes.**

Author: **Usman Almuarif Mashood**, Independent M&E Consultant — Public Administration (B.Sc., Ahmadu Bello University, Zaria). LinkedIn: [almuarifusman](https://linkedin.com/in/almuarifusman).

---

## Purpose of this repository

This repository is the public archive of a series of independent M&E reviews of Nigerian social protection and human-capital programmes. Each brief is published in full as a downloadable PDF and includes reproducible analysis code where primary data is used.

The series exists to do three things that the official Results Frameworks of large-scale donor-funded programmes in Nigeria often do not do well on their own:

1. **Document, in publicly accessible form, what the programmes actually committed to measure** — drawn directly from World Bank Project Appraisal Documents, Implementation Status Reports, government policy documents, and programme design frameworks.
2. **Test those commitments against the public evidence of performance** — combining donor evaluation data, independent academic studies, civil-society monitoring, and where possible primary-data analysis of publicly available datasets.
3. **Identify the structural blind spots in the Results Frameworks themselves** — the indicators that were never specified, the outcomes that are not tracked, and the gaps between what the programme promises to achieve and what it actually measures.

Each brief is independent, evidence-anchored, and written with the conventions of the M&E profession in mind: methodology stated, sample sizes disclosed, limitations acknowledged, recommendations grounded in evidence.

---

## Briefs in this series

### Brief 1 — National Social Safety Net Programme — Household Uplifting Programme (NASSP-HUP)

An independent M&E review of Nigeria's flagship federal Conditional Cash Transfer programme, operated by the National Cash Transfer Office under the National Social Investment Programmes Agency. The brief analyses the programme's performance against its official Results Framework, identifies gaps in the M&E architecture, and proposes five operational indicator recommendations.

- 📄 [Read the brief (PDF)](./brief_01_NASSP_HUP/brief_01_NASSP_HUP_Independent_M&E_Review.pdf)
- 📖 [Brief documentation & navigation](./brief_01_NASSP_HUP/)
- 🔗 [Published article on LinkedIn](https://www.linkedin.com/pulse/nigerias-nassp-hup-crossroads-independent-monitoring-evaluation-7vnee)

**Method:** Desk review of public sources. No primary-data analysis.

---

### Brief 2 — Adolescent Girls Initiative for Learning and Empowerment (AGILE)

A primary-data review of AGILE, Nigeria's $1.2 billion gender-focused secondary education programme co-funded by the World Bank's International Development Association. The brief analyses the World Bank's Baseline Survey microdata using reproducible Python code.

- 📄 [Read the brief (PDF)](./brief_02_AGILE/AGILE_Independent_ME_Review.pdf)
- 📖 [Brief documentation & navigation](./brief_02_AGILE/)
- 🐍 [Reproducible Colab notebook](./brief_02_AGILE/AGILE_Brief2_Analysis.ipynb)
- 📊 [Key findings numbers (CSV)](./brief_02_AGILE/key_findings_numbers.csv)
- 🖼️ [Charts](./brief_02_AGILE/)
- 📐 [LaTeX dashboard source](./brief_02_AGILE/AGILE_Brief2_Dashboard.tex) — Full 7-page visual summary dashboard (compile with XeLaTeX)

**Method:** Desk review of the AGILE document set + primary analysis of public-use World Bank microdata.

---

### Brief 3 — Home Grown School Feeding Programme (HGSF)

An independent M&E review of Nigeria's Home Grown School Feeding Programme (HGSF), the country's flagship school meals initiative. The brief examines budget trends, programme reach, cost-effectiveness, and governance outcomes using structured data analysis and reproducible R/Quarto code.

- 📄 [Read the brief (PDF)](./Brief%2003_HGSF/HGSF%20Reading%20and%20Summary/Evaluated_Home_Grown_School_Feeding_Programme%20(1).pdf)
- 📊 [Executive summary (PDF)](./Brief%2003_HGSF/HGSF%20Reading%20and%20Summary/NHGSFP_Executive_Summary_Final.pdf)
- 📖 [Brief documentation & navigation](./Brief%2003_HGSF/)
- 🔬 [Reproducible R/Quarto analysis](./Brief%2003_HGSF/R%20and%20Data%20Analysis/HGSF_Brief3_Analysis.qmd)
- 📊 [Data extraction tables (PDF)](./Brief%2003_HGSF/R%20and%20Data%20Analysis/HGSF_ME_Review_Structured_Extraction_Table.pdf)
- 🖼️ [Visualizations & charts](./Brief%2003_HGSF/IMAGES/)
- ✅ [Verified numbers & statistics](./Brief%2003_HGSF/R%20and%20Data%20Analysis/verified_numbers.md)

**Method:** Desk review of programme documents + primary analysis of structured programme data with reproducible R/Quarto pipeline.

---

## Quick Navigation by Brief

| Brief | Topic | Read | Docs | Code | Data |
|-------|-------|------|------|------|------|
| **1** | NASSP-HUP (Cash Transfers) | [PDF](./brief_01_NASSP_HUP/brief_01_NASSP_HUP_Independent_M&E_Review.pdf) | [📖](./brief_01_NASSP_HUP/) | Desk review | Public sources |
| **2** | AGILE (Education) | [PDF](./brief_02_AGILE/AGILE_Independent_ME_Review.pdf) | [📖](./brief_02_AGILE/) | [Notebook](./brief_02_AGILE/AGILE_Brief2_Analysis.ipynb) | WB Microdata |
| **3** | HGSF (School Meals) | [PDF](./Brief%2003_HGSF/HGSF%20Reading%20and%20Summary/Evaluated_Home_Grown_School_Feeding_Programme%20(1).pdf) | [📖](./Brief%2003_HGSF/) | [Quarto](./Brief%2003_HGSF/R%20and%20Data%20Analysis/HGSF_Brief3_Analysis.qmd) | Programme data |

---

## Reproducibility

Where primary data is used, this repository contains the complete analytical pipeline: the code (Colab notebook, Quarto script), the variable lists, the cleaned outputs, and the chart-generating code. Any reader with access to the same datasets can reproduce every figure.

This repository does **not** redistribute restricted-use datasets. The World Bank Microdata terms of use require users to access data directly from the Library; the briefs cite the catalogue identifiers and link to the data use agreement.

---

## How to navigate

```
social-protection-me-nigeria/
│
├── README.md ← you are here
│
├── brief_01_NASSP_HUP/
│   ├── README.md
│   ├── brief_01_NASSP_HUP_Independent_M&E_Review.pdf
│   └── (supporting materials)
│
├── brief_02_AGILE/
│   ├── README.md
│   ├── AGILE_Independent_ME_Review.pdf
│   ├── AGILE_Brief2_Analysis.ipynb
│   ├── AGILE_Brief2_Dashboard.tex
│   ├── key_findings_numbers.csv
│   └── (chart PNGs)
│
└── Brief 03_HGSF/
    ├── README.md
    │
    ├── IMAGES/
    │   ├── Image Note.md
    │   ├── 01_budget_trend.png
    │   ├── 02_reach_trend.png
    │   ├── 03_cost_per_meal.png
    │   ├── 03b_real_value_70_deflated.png
    │   └── 04_fraud_recovery.png
    │
    ├── HGSF Reading and Summary/
    │   ├── About Documentations.md
    │   ├── Evaluated_Home_Grown_School_Feeding_Programme (1).pdf
    │   └── NHGSFP_Executive_Summary_Final.pdf
    │
    └── R and Data Analysis/
        ├── Note on Analysis.md
        ├── HGSF_Brief3_Analysis.qmd
        ├── Feeding the Bet — HGSF Brief 3 Analysis.pdf
        ├── HGSF_ME_Review_Structured_Extraction_Table.pdf
        └── verified_numbers.md
```

---

## About the author

Usman Almuarif Mashood is an independent M&E consultant based in Nigeria, with applied training in Social and Behaviour Change (UNICEF, 2024), Disaster Risk Reduction and Climate Change Adaptation (UNDP DESINVENTAR, 2023), and MEAL Systems Design. His applied research focuses on programme performance, measurement architecture gaps, and the translation of results frameworks into actionable indicators.

For collaboration, commissioned analysis, or speaking engagements, contact via [LinkedIn](https://linkedin.com/in/almuarifusman) or email: usmanmashoodalmuarif@gmail.com.

---

## Citation

If you cite a brief from this series, please use the format below, adapting the brief title and date as appropriate:

> Mashood, U. A. (2026). *Nigeria's NASSP-HUP at the Crossroads: An Independent Monitoring & Evaluation Review.* Social Protection M&E — Nigeria series, Brief 1. Available at: https://github.com/Almuarif17/social-protection-me-nigeria/tree/main/brief_01_NASSP_HUP

or

> Mashood, U. A. (2026). *Feeding the Bet: An Independent Monitoring & Evaluation Review of Nigeria's Home Grown School Feeding Programme.* Social Protection M&E — Nigeria series, Brief 3. Available at: https://github.com/Almuarif17/social-protection-me-nigeria/tree/main/Brief%2003_HGSF

---

## License

The briefs and analytical materials in this repository are released under the Creative Commons Attribution 4.0 International License (CC BY 4.0). You may use, share, adapt, and build upon them with attribution.

```
CC BY 4.0: https://creativecommons.org/licenses/by/4.0/
```

---

**Last updated:** June 2026
