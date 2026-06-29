# Social Protection M&E — Nigeria

**Independent Monitoring & Evaluation reviews of Nigerian social protection and human-capital programmes.**

Author: **Usman Almuarif Mashood**, Independent M&E Researcher — Public Administration (B.Sc., Ahmadu Bello University, Zaria, Second Class Upper, CGPA 4.06/5.0). LinkedIn: [almuarifusman](https://linkedin.com/in/almuarifusman) · Email: usmanmashoodalmuarif@gmail.com

---

## Purpose of this repository

This repository is the public archive of a series of independent M&E reviews of Nigerian social protection and human-capital programmes. Each brief is published as a downloadable PDF and includes reproducible analysis code where primary data is used.

The series exists to do three things that the official Results Frameworks of large-scale donor-funded programmes in Nigeria often do not do well on their own:

1. **Document, in publicly accessible form, what the programmes actually committed to measure** — drawn directly from World Bank Project Appraisal Documents, Implementation Status Reports, government policy documents, and programme design frameworks.
2. **Test those commitments against the public evidence of performance** — combining donor evaluation data, independent academic studies, civil-society monitoring, and where possible primary-data analysis of publicly available datasets.
3. **Identify the structural blind spots in the Results Frameworks themselves** — the indicators that were never specified, the outcomes that are not tracked, and the gaps between what the programme promises to achieve and what it actually measures.

Each brief is independent, evidence-anchored, and written with the conventions of the M&E profession in mind: methodology stated, sample sizes disclosed, limitations acknowledged, recommendations grounded in evidence.

---

## Briefs in this series

### Brief 1 — National Social Safety Net Programme — Household Uplifting Programme (NASSP-HUP)

An independent M&E review of Nigeria's flagship federal Conditional Cash Transfer programme, operated by the National Cash Transfer Office under the National Social Investment Programmes Agency. The brief analyses the programme's performance against its official Results Framework, identifies gaps in the M&E architecture, and proposes five operational indicator recommendations.

- 📄 [Read the brief (PDF)](https://github.com/Almuarif17/social-protection-me-nigeria/blob/main/brief_01_NASSP_HUP/brief_01_NASSP_HUP_Independent_M&E_Review.pdf)
- 📖 [Brief documentation & navigation](https://github.com/Almuarif17/social-protection-me-nigeria/blob/main/brief_01_NASSP_HUP)
- 🔗 [Published article on LinkedIn](https://www.linkedin.com/pulse/nigerias-nassp-hup-crossroads-independent-monitoring-evaluation-7vnee)

**Method:** Desk review of public sources. No primary-data analysis.

---

### Brief 2 — Adolescent Girls Initiative for Learning and Empowerment (AGILE)

An independent M&E review of Nigeria's flagship World Bank–financed adolescent-girls education investment. The brief is built directly from the World Bank AGILE-IE Baseline Survey 2023 microdata — 8,223 adolescent girls, 8,007 caregivers, and 270 schools across Kaduna, Kano, and Katsina — analysed using Python (pandas, NumPy, matplotlib, seaborn) in a fully reproducible Google Colab pipeline.

- 📄 [Read the brief (PDF)](https://github.com/Almuarif17/social-protection-me-nigeria/tree/main/brief_02_AGILE)
- 📖 [Brief documentation & navigation](https://github.com/Almuarif17/social-protection-me-nigeria/tree/main/brief_02_AGILE)

**Method:** Primary-data secondary analysis using World Bank Microdata Library (ref NGA_2023_AGILE-IE_v01_M). 30-page brief, four publication-quality figures, 7-page landscape dashboard.

---

### Brief 3 — National Home-Grown School Feeding Programme (NHGSFP)

An independent M&E review of Africa's largest school-feeding initiative. Built from 34 publicly available sources covering 2016–2025 — World Bank assessments, House Committee on Public Accounts hearings, ICPC fraud investigations, BudgIT fiscal-tracking data, NBS Consumer Price Index series, peer-reviewed academic studies, and investigative journalism. Five publication-quality charts rendered in R + Quarto from reconciled fiscal, reach, fraud, and cost-erosion data.

- 📄 [Read the full brief (PDF)](https://github.com/Almuarif17/social-protection-me-nigeria/tree/main/Brief%2003_HGSF/HGSF%20Reading%20and%20Summary)
- 📖 [Brief documentation & navigation](https://github.com/Almuarif17/social-protection-me-nigeria/tree/main/Brief%2003_HGSF)
- 🔬 [Reproducible analysis pipeline (Quarto + CSVs)](https://github.com/Almuarif17/social-protection-me-nigeria/tree/main/Brief%2003_HGSF/R%20and%20Data%20Analysis)

**Method:** Secondary analysis of 34 curated public sources, with reconciled budget arithmetic and NBS Food CPI–deflated cost-erosion analysis. No primary fieldwork. Five charts built from project-built CSVs; full R + Quarto pipeline reproducible end-to-end.

---

## How to use this repository

- **If you are a policy reader:** open each brief's PDF directly. The executive summary at the front carries the full argument.
- **If you are a researcher:** the source pack and structured extraction matrix for each brief sit alongside the brief PDF. Every figure cited has a traceable origin.
- **If you are a technical reviewer:** the `R and Data Analysis/` folder under Brief 3 contains the `.qmd` source, the CSV datasets, and the rendered output. Clone the repo, install R + Quarto + tidyverse, and re-render the entire analysis from source.

---

## Citation

If you cite any brief in academic or policy work, please reference:

> Mashood, U. A. (2026). *Independent M&E Reviews of Nigerian Social Investment Programmes.* GitHub repository: github.com/Almuarif17/social-protection-me-nigeria.

For individual briefs, add the brief number and programme name.

---

## Licence

Content is shared under Creative Commons Attribution 4.0 International (CC-BY 4.0) — free to share, adapt, and build upon with attribution.

---

## Contact

- **Email:** usmanmashoodalmuarif@gmail.com
- **LinkedIn:** [linkedin.com/in/almuarifusman](https://linkedin.com/in/almuarifusman)

Correction, contradiction, and triangulation welcome — particularly from readers with access to primary data the public record does not contain.
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
