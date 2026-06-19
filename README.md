# Social Protection M&E — Nigeria

**Independent Monitoring & Evaluation reviews of Nigerian social protection and human-capital programmes.**

Author: **Usman Almuarif Mashood**, Independent M&E Consultant — Public Administration (B.Sc., Ahmadu Bello University, Zaria). LinkedIn: [almuarifusman](https://linkedin.com/in/almuarifusman).

---

## Purpose of this repository

This repository is the public archive of a series of independent M&E reviews of Nigerian social protection and human-capital programmes. Each brief is published in full as a downloadable PDF and includes reproducible analysis code and data where applicable.

The series exists to do three things that the official Results Frameworks of large-scale donor-funded programmes in Nigeria often do not do well on their own:

1. **Document, in publicly accessible form, what the programmes actually committed to measure** — drawn directly from World Bank Project Appraisal Documents, Implementation Status Reports, government policy documents, and academic literature.
2. **Test those commitments against the public evidence of performance** — combining donor evaluation data, independent academic studies, civil-society monitoring, and where possible primary-data analysis of public-use datasets.
3. **Identify the structural blind spots in the Results Frameworks themselves** — the indicators that were never specified, the outcomes that are not tracked, and the gaps between what the programme says it will measure and what it actually measures.

Each brief is independent, evidence-anchored, and written with the conventions of the M&E profession in mind: methodology stated, sample sizes disclosed, limitations acknowledged, recommendations grounded in international benchmarks.

---

## Briefs in this series

### Brief 1 — National Social Safety Net Programme — Household Uplifting Programme (NASSP-HUP)

An independent M&E review of Nigeria's flagship federal Conditional Cash Transfer programme, operated by the National Cash Transfer Office under the National Social Investment Programmes Agency. The brief examines what the programme committed to measure, tests those commitments against available evidence, identifies measurement gaps, documents achievements, and recommends five new indicators.

- 📄 [Read the brief (PDF)](./brief_01_NASSP_HUP/brief_01_NASSP_HUP_Independent_M&E_Review.pdf)
- 🔗 [Published article on LinkedIn](https://www.linkedin.com/pulse/nigerias-nassp-hup-crossroads-independent-monitoring-evaluation-7vnee)

Method: Desk review of public sources. No primary-data analysis.

### Brief 2 — Adolescent Girls Initiative for Learning and Empowerment (AGILE)

A primary-data review of AGILE, Nigeria's $1.2 billion gender-focused secondary education programme co-funded by the World Bank's International Development Association. The brief analyses the World Bank's anonymised AGILE-IE Baseline Survey 2023 (8,223 girls, 8,007 caregivers, 270 schools across Kaduna, Kano, and Katsina) to identify four critical measurement gaps in the programme's Results Framework.

- 📄 [Read the brief (PDF)](./brief_02_AGILE/AGILE_Independent_ME_Review.pdf)
- 🐍 [Reproducible Colab notebook](./brief_02_AGILE/AGILE_Brief2_Analysis.ipynb)
- 📊 [Key findings numbers (CSV)](./brief_02_AGILE/key_findings_numbers.csv)
- 🖼️ [Charts](./brief_02_AGILE/)
- 📐 [LaTeX dashboard source](./brief_02_AGILE/AGILE_Brief2_Dashboard.tex) — Full 7-page visual summary dashboard (compile with XeLaTeX)
- 🔗 *LinkedIn article: forthcoming*

Method: Desk review of the AGILE document set + primary analysis of public-use World Bank microdata.

---

## Reproducibility

Where primary data is used, this repository contains the complete analytical pipeline: the Colab notebook, the variable list, the cleaned outputs, and the chart-generating code. Any reader who can access the underlying World Bank microdata can reproduce every number, table, and chart from first principles.

This repository does **not** redistribute restricted-use datasets. The World Bank Microdata terms of use require users to access data directly from the Library; the briefs cite the catalogue identifiers and the pathway to access.

---

## How to navigate
social-protection-me-nigeria/

├── README.md ← you are here

├── brief_01_NASSP_HUP/

│ ├── README.md

│ └── Independent_ME_Review.pdf

└── brief_02_AGILE/

│ ├── README.md

│ ├── AGILE_Independent_ME_Review.pdf

│ ├── AGILE_Brief2_Analysis.ipynb

│ ├── AGILE_Brief2_Dashboard.tex

│ ├── key_findings_numbers.csv

│ └── (chart PNGs)


---

## About the author

Usman Almuarif Mashood is an independent M&E consultant based in Nigeria, with applied training in Social and Behaviour Change (UNICEF, 2024), Disaster Risk Reduction and Climate Change Adaptation (IFRC, 2023), and Monitoring & Evaluation of education programmes (World Bank, 2022). He holds a B.Sc. in Public Administration from Ahmadu Bello University, Zaria, and is completing an MSc in Social Policy and Planning in Developing Countries (London School of Economics, 2026).

For collaboration, commissioned analysis, or speaking engagements, contact via [LinkedIn](https://linkedin.com/in/almuarifusman) or email: usmanmashoodalmuarif@gmail.com.

---

## Citation

If you cite a brief from this series, please use the format below, adapting the brief title and date as appropriate:

> Mashood, U. A. (2026). *Nigeria's NASSP-HUP at the Crossroads: An Independent Monitoring & Evaluation Review.* Social Protection M&E — Nigeria series, Brief 1. Available at: https://github.com/Almuarif17/social-protection-me-nigeria

## License

The briefs and analytical materials in this repository are released under the Creative Commons Attribution 4.0 International License (CC BY 4.0). You may use, share, adapt, and build upon them with attribution.
