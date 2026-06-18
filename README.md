# Social Protection M&E — Nigeria

**Independent Monitoring & Evaluation reviews of Nigerian social protection and human-capital programmes.**

Author: **Usman Almuarif Mashood**, Independent M&E Consultant — Public Administration (B.Sc., Ahmadu Bello University, Zaria). LinkedIn: [almuarifusman](https://linkedin.com/in/almuarifusman).

---

## Purpose of this repository

This repository is the public archive of a series of independent M&E reviews of Nigerian social protection and human-capital programmes. Each brief is published in full as a downloadable PDF and is supported, where primary microdata is available, by a fully reproducible Python analysis pipeline.

The series exists to do three things that the official Results Frameworks of large-scale donor-funded programmes in Nigeria often do not do well on their own:

1. **Document, in publicly accessible form, what the programmes actually committed to measure** — drawn directly from World Bank Project Appraisal Documents, Implementation Status Reports, government policy frameworks, and civic accountability reporting.
2. **Test those commitments against the public evidence of performance** — combining donor evaluation data, independent academic studies, civil-society monitoring, and where possible primary-data analysis of anonymised survey microdata.
3. **Identify the structural blind spots in the Results Frameworks themselves** — the indicators that were never specified, the outcomes that are not tracked, and the gaps between what the programme is built to deliver and what its measurement architecture allows it to demonstrate.

Each brief is independent, evidence-anchored, and written with the conventions of the M&E profession in mind: methodology stated, sample sizes disclosed, limitations acknowledged, recommendations operational rather than aspirational.

---

## Briefs in this series

### Brief 1 — National Social Safety Net Programme — Household Uplifting Programme (NASSP-HUP)

An independent M&E review of Nigeria's flagship federal Conditional Cash Transfer programme, operated by the National Cash Transfer Office under the National Social Investment Programmes Agency. The brief examines the programme's stated development objective, the indicators committed in the 2016 World Bank Project Appraisal Document, the publicly available evidence of performance through the 2019 Implementation Status Report, and the systemic gaps documented by BudgIT, the House of Representatives ₦30 billion recovery investigation, and the January 2024 Presidential Panel suspension.

- 📄 [Read the brief (PDF)](./brief_01_NASSP_HUP/Independent_ME_Review.pdf)
- 🔗 [Published article on LinkedIn](https://www.linkedin.com/pulse/nigerias-nassp-hup-crossroads-independent-monitoring-evaluation-7vnee)

Method: Desk review of public sources. No primary-data analysis.

### Brief 2 — Adolescent Girls Initiative for Learning and Empowerment (AGILE)

A primary-data review of AGILE, Nigeria's $1.2 billion gender-focused secondary education programme co-funded by the World Bank's International Development Association. The brief analyses the World Bank's anonymised AGILE-IE Baseline Survey 2023 (8,223 adolescent girls, 8,007 caregivers, 270 school principals across Kaduna, Kano, and Katsina) and identifies four measurement gaps in the official Results Framework: prior digital exposure, caregiver educational aspirations, household food security as a poverty-targeting verification measure, and classroom seating adequacy as the binding infrastructure constraint.

- 📄 [Read the brief (PDF)](./brief_02_AGILE/AGILE_Independent_ME_Review.pdf)
- 🐍 [Reproducible Colab notebook](./brief_02_AGILE/AGILE_Brief2_Analysis.ipynb)
- 📊 [Key findings numbers (CSV)](./brief_02_AGILE/key_findings_numbers.csv)
- 🖼️ [Charts](./brief_02_AGILE/)
- 🔗 *LinkedIn article: forthcoming*

Method: Desk review of the AGILE document set + primary analysis of public-use World Bank microdata.

---

## Reproducibility

Where primary data is used, this repository contains the complete analytical pipeline: the Colab notebook, the variable list, the cleaned outputs, and the chart-generating code. Any reader who can download the public-use dataset from the original source (e.g. the World Bank Microdata Library, with free registration) can re-run the entire analysis end-to-end and verify every number in the brief.

This repository does **not** redistribute restricted-use datasets. The World Bank Microdata terms of use require users to access data directly from the Library; the briefs cite the catalogue identifiers and explain the registration path.

---

## How to navigate
social-protection-me-nigeria/
├── README.md ← you are here
├── brief_01_NASSP_HUP/
│ ├── README.md
│ └── Independent_ME_Review.pdf
└── brief_02_AGILE/
├── README.md
├── AGILE_Independent_ME_Review.pdf
├── AGILE_Brief2_Analysis.ipynb
├── key_findings_numbers.csv
└── (chart PNGs)


---

## About the author

Usman Almuarif Mashood is an independent M&E consultant based in Nigeria, with applied training in Social and Behaviour Change (UNICEF, 2024), Disaster Risk Reduction and Climate Change Adaptation (UNSSC & UNDRR, 2023), Data Science and Python (Tech Sphere Academy, 2026), and AI Career Essentials (ALX Africa, 2024). His undergraduate thesis at Ahmadu Bello University evaluated the impact of Conditional Cash Transfers on women's economic empowerment and poverty reduction in Nigeria — the analytical foundation on which this M&E series builds.

For collaboration, commissioned analysis, or speaking engagements, contact via [LinkedIn](https://linkedin.com/in/almuarifusman) or email: usmanmashoodalmuarif@gmail.com.

---

## Citation

If you cite a brief from this series, please use the format below, adapting the brief title and date as appropriate:

> Mashood, U. A. (2026). *Nigeria's NASSP-HUP at the Crossroads: An Independent Monitoring & Evaluation Review.* Social Protection M&E — Nigeria series, Brief 1. Available at: https://github.com/Almuarif17/social-protection-me-nigeria

## License

The briefs and analytical materials in this repository are released under the Creative Commons Attribution 4.0 International License (CC BY 4.0). You may use, share, adapt, and build upon them with attribution.
