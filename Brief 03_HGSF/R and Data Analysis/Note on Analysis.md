# Note on Analysis - R and Data Analysis

## Overview
This folder contains the technical analysis materials for the Home Grown School Feeding Programme (HGSF) Brief 3 evaluation. It includes reproducible analysis scripts, detailed data extraction tables, and processed findings. All analysis is conducted using R/Quarto for transparency and reproducibility.

## Contents

### HGSF_Brief3_Analysis.qmd
**Type:** Quarto (R Markdown) script  
**Description:** Primary reproducible analysis script  
**Purpose:** Contains all R code, analysis steps, and explanatory text for generating findings  
**What it includes:**
- Data import and cleaning procedures
- Statistical analysis and calculations
- Chart and visualization generation
- Interpretation and narrative

**How to Use:**
1. Ensure R and Quarto are installed on your system
2. Open the file in RStudio or any text editor
3. Execute with `quarto render HGSF_Brief3_Analysis.qmd` to regenerate all outputs
4. Modify parameters or data inputs to conduct sensitivity analyses
5. Review code comments for methodological explanations

### Feeding the Bet — HGSF Brief 3 Analysis.pdf
**Type:** Rendered HTML/PDF output from Quarto script  
**Description:** Complete analysis report with visualizations and interpretations  
**Purpose:** Final formatted output showing analysis results and supporting narrative  
**What it includes:**
- Detailed analysis process and findings
- Embedded charts and tables
- Statistical results and interpretations
- Conclusions and key takeaways

**How to Use:**
- Read as a standalone report for technical understanding
- Share with data analysts and researchers
- Reference for methodological approaches
- Compare outputs when re-running analysis

### HGSF_ME_Review_Structured_Extraction_Table.pdf
**Type:** Data extraction and summary table  
**Description:** Structured table extracting key metrics and findings  
**Purpose:** Serves as a data repository and quick-reference for important numerical findings  
**What it includes:**
- Key programme metrics and indicators
- Extracted data from various sources
- Aggregated findings in tabular format
- Raw numbers supporting analysis claims

**How to Use:**
- Reference for specific figures and statistics
- Data source for cross-tabulations
- Input for secondary analyses
- Basis for visualizations in the IMAGES folder

### verified_numbers.md
**Type:** Markdown document  
**Description:** List of key verified and validated numbers from the analysis  
**Purpose:** Quality assurance document listing confirmed figures from the evaluation  
**What it includes:**
- Critical programme metrics with verification status
- Numbers used in executive summaries and briefings
- Sources and validation methods
- Rationale for specific figures

**How to Use:**
- Check before using numbers in presentations or reports
- Understand data limitations and caveats
- Trace back to source documents and analysis
- Ensure accuracy in external communications

## Reproducibility and Data Science Best Practices

### For Researchers & Analysts
1. **Start with:** HGSF_Brief3_Analysis.qmd for the complete analysis workflow
2. **Reference:** HGSF_ME_Review_Structured_Extraction_Table.pdf for data structure
3. **Validate:** verified_numbers.md to confirm key figures
4. **Output:** Feeding the Bet PDF for presentation-ready results

### To Reproduce or Modify Analysis
```bash
# Ensure dependencies are installed
# Run in R console or terminal:
quarto render HGSF_Brief3_Analysis.qmd
```

### Data Quality Notes
- All figures in verified_numbers.md have been cross-checked against source data
- Inflation adjustments use 2007 as base year (see image 03b_real_value_70_deflated.png)
- For questions on specific calculations, review relevant sections in the Quarto script

## Related Resources
- **Visualizations:** See `IMAGES` folder for charts referenced in analysis
- **Reports:** See `HGSF Reading and Summary` folder for executive summaries
- **Raw Data:** Original datasets available in parent repository sections

## Technical Requirements
- **R Version:** 4.0 or higher
- **Quarto:** Latest version
- **Key Packages:** tidyverse, ggplot2, knitr (see imports in .qmd file)

## Questions or Issues?
If you need to:
- **Reproduce the analysis:** Use the Quarto script with updated data
- **Understand specific findings:** Check the commented code in the .qmd file
- **Validate numbers:** Cross-reference with verified_numbers.md
- **Modify visualizations:** Edit ggplot2 code in the Quarto script
