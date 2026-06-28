# Brief 3 — Home Grown School Feeding Programme (HGSF) Independent M&E Review

**An independent Monitoring & Evaluation review of Nigeria's Home Grown School Feeding Programme (HGSF), the country's flagship school meals initiative.**

Author: Usman Almuarif Mashood · Published June 2026

---

## What this brief is

The Home Grown School Feeding Programme (HGSF) is Nigeria's commitment to providing nutritious meals to schoolchildren across public primary schools. This independent M&E review examines the programme through multiple analytical lenses:

1. **What it committed to do** — the official objectives and Results Framework indicators
2. **What the evidence shows** — performance against committed targets through programme data and independent evaluations
3. **Where the M&E framework falls short** — gaps in the monitoring architecture and data availability
4. **What the programme has achieved** — documented successes in reach, beneficiary outcomes, and implementation
5. **What should be added to the Results Framework** — specific, operational indicator recommendations

---

## How to navigate this brief

This folder is organized into three main sections for different types of users:

### 📊 **IMAGES** — Visualizations and Charts
Contains 5 key visualization files showing:
- Budget trends over time
- Programme reach and beneficiary expansion
- Cost per meal analysis
- Real value (inflation-adjusted) cost trends
- Fraud recovery and audit findings

**[📖 View IMAGES documentation](./IMAGES/Image%20Note.md)**

### 📚 **HGSF Reading and Summary** — Executive Reports
Contains two comprehensive evaluation documents:
- **Evaluated_Home_Grown_School_Feeding_Programme (1).pdf** — Full evaluation report with detailed methodology and findings
- **NHGSFP_Executive_Summary_Final.pdf** — Executive summary for quick reference

**[📖 View Reading and Summary documentation](./HGSF%20Reading%20and%20Summary/About%20Documentations.md)**

### 🔬 **R and Data Analysis** — Technical Analysis
Contains the reproducible analysis pipeline:
- **HGSF_Brief3_Analysis.qmd** — Quarto R script with complete analysis workflow
- **Feeding the Bet — HGSF Brief 3 Analysis.pdf** — Rendered analysis output
- **HGSF_ME_Review_Structured_Extraction_Table.pdf** — Data extraction and summary tables
- **verified_numbers.md** — Validated key figures and statistics

**[📖 View Analysis documentation](./R%20and%20Data%20Analysis/Note%20on%20Analysis.md)**

---

## Quick Start by Use Case

### For Decision-Makers & Policy Stakeholders
1. Start with: **NHGSFP_Executive_Summary_Final.pdf**
2. Review: **IMAGES folder** for key trends
3. Reference: **verified_numbers.md** for specific statistics

### For Researchers & Analysts
1. Read: **Evaluated_Home_Grown_School_Feeding_Programme (1).pdf** for methodology
2. Review: **HGSF_Brief3_Analysis.qmd** for reproducible analysis code
3. Check: **HGSF_ME_Review_Structured_Extraction_Table.pdf** for data structure

### For Reproducibility
1. Navigate to: **R and Data Analysis** folder
2. Review: **Note on Analysis.md** for instructions
3. Execute: `quarto render HGSF_Brief3_Analysis.qmd` to regenerate outputs

---

## Methodology

This brief combines:
- **Desk review** of public programme documents and reports
- **Primary data analysis** where datasets are publicly available
- **Structured data extraction** into standardized M&E tables
- **Cross-validation** of figures across multiple sources
- **R/Quarto reproducible analysis** for transparency and verifiability

All analysis is transparent, documented, and reproducible through the scripts and tables in the R and Data Analysis folder.

---

## Key Findings Overview

### Budget Analysis
See: **01_budget_trend.png**

### Programme Reach
See: **02_reach_trend.png**

### Cost Efficiency
See: **03_cost_per_meal.png** and **03b_real_value_70_deflated.png** (inflation-adjusted)

### Governance & Accountability
See: **04_fraud_recovery.png**

---

## Reproducibility & Transparency

Where primary data is used, this folder contains:
- ✅ Complete analytical pipeline (Quarto script)
- ✅ Variable lists and data documentation
- ✅ Cleaned outputs and processed datasets
- ✅ Chart-generating code
- ✅ Methodology documentation

All figures in **verified_numbers.md** have been cross-checked against source data.

---

## Folder Structure

```
Brief 03_HGSF/
├── README.md ← you are here
│
├── IMAGES/
│   ├── 01_budget_trend.png
│   ├── 02_reach_trend.png
│   ├── 03_cost_per_meal.png
│   ├── 03b_real_value_70_deflated.png
│   ├── 04_fraud_recovery.png
│   └── Image Note.md
│
├── HGSF Reading and Summary/
│   ├── Evaluated_Home_Grown_School_Feeding_Programme (1).pdf
│   ├── NHGSFP_Executive_Summary_Final.pdf
│   └── About Documentations.md
│
└── R and Data Analysis/
    ├── HGSF_Brief3_Analysis.qmd
    ├── Feeding the Bet — HGSF Brief 3 Analysis.pdf
    ├── HGSF_ME_Review_Structured_Extraction_Table.pdf
    ├── verified_numbers.md
    └── Note on Analysis.md
```

---

## Citation

If you cite this brief, please use:

> Mashood, U. A. (2026). *Feeding the Bet: An Independent Monitoring & Evaluation Review of Nigeria's Home Grown School Feeding Programme.* Social Protection M&E — Nigeria series, Brief 3. Available at: https://github.com/Almuarif17/social-protection-me-nigeria/tree/main/Brief%2003_HGSF

---

## License

All materials in this folder are released under the Creative Commons Attribution 4.0 International License (CC BY 4.0). You are free to use, share, adapt, and build upon these materials with attribution.

---

## Questions or Feedback?

For questions about:
- **The analysis methodology** → Review the Quarto script in R and Data Analysis
- **Specific findings** → Check verified_numbers.md
- **Data sources** → See citations in the main evaluation PDF
- **Using the materials** → This README and the three folder-level documentation files (Image Note.md, About Documentations.md, Note on Analysis.md)

---

**Back to main repository:** [Social Protection M&E — Nigeria](https://github.com/Almuarif17/social-protection-me-nigeria)
