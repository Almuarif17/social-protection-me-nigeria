# Social Protection M&E, Nigeria

Independent monitoring and evaluation reviews of Nigerian social protection and human capital programmes.

Author: **Usman Almuarif Mashood**, Independent Policy Researcher. Public Administration, Ahmadu Bello University, Zaria (B.Sc., Second Class Upper, CGPA 4.06/5.0). Reach me at [linkedin.com/in/almuarifusman](https://linkedin.com/in/almuarifusman) or usmanmashoodalmuarif@gmail.com.

---

## What this repository is

This is the public archive of an ongoing series of independent M&E reviews of Nigeria's largest social protection and human capital programmes. Each brief is published as a downloadable PDF and, where primary data is used, ships with the reproducible analysis code that produced its charts.

The series exists because Nigeria's flagship social investment programmes are large, expensive, and consequential, and yet a citizen or a policy officer trying to understand how any one of them is actually doing has to reconstruct the answer from scattered official statements, civil society reports, press investigations, and academic studies. No single public source pulls those threads together into a defensible programme review. These briefs do.

Three practical things guide the work:

1. **Document, in one accessible place, what each programme committed to measure.** Drawn from World Bank Project Appraisal Documents, Implementation Status Reports, government policy documents, and programme design frameworks.
2. **Test those commitments against public evidence of performance.** Donor evaluation data, independent academic studies, civil society monitoring, and where possible primary-data analysis of publicly available datasets.
3. **Name the structural blind spots in each Results Framework.** The indicators that were never specified, the outcomes that are not tracked, and the gaps between what a programme promises to achieve and what it actually measures.

Every brief follows the same discipline: methodology stated, sample sizes disclosed, limitations acknowledged, and recommendations grounded in the evidence the brief itself lays out. Where sources conflict, contradictions are named openly rather than reconciled.

---

## The briefs

### Brief 1, National Social Safety Net Programme, Household Uplifting Programme (NASSP-HUP)

An independent M&E review of Nigeria's flagship federal Conditional Cash Transfer programme, operated by the National Cash Transfer Office under NSIPA. The brief analyses the programme's performance against its official Results Framework, identifies gaps in the M&E architecture, and proposes five operational indicator recommendations.

- 📄 [Read the brief (PDF)](brief_01_NASSP_HUP/brief_01_NASSP_HUP_Independent_M&E_Review.pdf)
- 📁 [Folder contents](brief_01_NASSP_HUP)
- 🔗 [Published on LinkedIn](https://www.linkedin.com/pulse/nigerias-nassp-hup-crossroads-independent-monitoring-evaluation-7vnee)

Method: desk review of public sources. No primary-data analysis.

### Brief 2, Adolescent Girls Initiative for Learning and Empowerment (AGILE)

An independent M&E review of Nigeria's World Bank-financed adolescent girls education investment. The brief is built directly from the World Bank AGILE-IE Baseline Survey 2023 microdata, 8,223 adolescent girls, 8,007 caregivers, and 270 schools across Kaduna, Kano, and Katsina. Analysis in Python (pandas, NumPy, matplotlib, seaborn) via a fully reproducible Google Colab pipeline.

- 📄 [Read the brief (PDF)](brief_02_AGILE)
- 📁 [Folder contents](brief_02_AGILE)

Method: primary-data secondary analysis of World Bank Microdata Library ref NGA_2023_AGILE-IE_v01_M. 30-page brief, four publication-quality figures, 7-page landscape dashboard.

### Brief 3, National Home-Grown School Feeding Programme (NHGSFP)

An independent M&E review of Africa's largest school feeding initiative, built from 34 curated public sources covering 2016 to 2025. World Bank assessments, House Committee on Public Accounts hearings, ICPC fraud investigations, BudgIT fiscal tracking data, NBS Consumer Price Index series, peer-reviewed academic studies, and investigative journalism. Five publication-quality charts rendered from reconciled fiscal, reach, fraud, and cost-erosion data.

- 📄 [Read the full brief (PDF)](Brief%2003_HGSF/HGSF%20Reading%20and%20Summary)
- 📁 [Folder contents](Brief%2003_HGSF)
- 🔬 [Reproducible analysis pipeline (Quarto + CSVs)](Brief%2003_HGSF/R%20and%20Data%20Analysis)

Method: secondary analysis with reconciled budget arithmetic and NBS Food CPI–deflated cost-erosion analysis. No primary fieldwork.

### Brief 4, N-Power Programme

An independent M&E review of Nigeria's flagship graduate employment programme across its full ten-year arc, 2016 to 2026. Origin, performance, and reform options, built from a curated 30-source evidence matrix and covering the programme's launch in the 2016 recession, three enrolment batches through 2020, the January 2024 suspension, and the 2025 Renewed Hope reset.

- 📄 [Read the full brief (PDF)](brief_04_NPower/Brief%20Documents/NPower_Independent%20_M%26E%20Review.pdf)
- 📄 [Read the executive summary (PDF)](brief_04_NPower/Brief%20Documents/NPower_Independent_M%26E_Summary.pdf)
- 📁 [Folder contents](brief_04_NPower)
- 🔬 [Reproducible analysis (Python notebook + CSVs)](brief_04_NPower/Reproducible%20data%20Analysis)

Method: secondary analysis with NBS Food CPI–deflated stipend erosion, denominator-sensitive ghost-name adjustment (9–18% band), and Theory of Change measurement coverage audit. No primary fieldwork.

---

## How to use this repository

If you are a policy reader, open each brief's PDF directly. The executive summary at the front carries the full argument.

If you are a researcher, the source matrices and full-brief PDFs sit alongside each brief. Every figure cited has a traceable origin.

If you are a technical reviewer, the analysis folder under each brief contains the source files, the datasets, and the rendered outputs. Clone the repository, install the toolchain named in that brief's analysis README, and re-render every chart from source.

---

## Citation

If you cite any brief in academic or policy work, please reference:

> Mashood, U. A. (2026). *Independent M&E Reviews of Nigerian Social Investment Programmes.* GitHub repository: github.com/Almuarif17/social-protection-me-nigeria.

Add the brief number and programme name for individual briefs.

---

## Licence

Content is shared under Creative Commons Attribution 4.0 International (CC-BY 4.0). Free to share, adapt, and build upon with attribution.

---

## Contact

- Email: usmanmashoodalmuarif@gmail.com
- LinkedIn: [linkedin.com/in/almuarifusman](https://linkedin.com/in/almuarifusman)

Correction, contradiction, and triangulation are welcome, particularly from readers with access to primary data the public record does not contain.
