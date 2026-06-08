# Data Quality & ETL Pipeline

A project that demonstrates how to build a simple ETL pipeline and run a data quality audit on local government planning data.

What this project covers

- Extracting raw data from a CSV source
- Transforming it — cleaning, standardising and restructuring
- Loading it into a clean output ready for analysis
- Running a structured data quality audit across key dimensions

Why this matters

Bad data leads to bad decisions. A BI team that doesn't audit its data regularly will eventually produce reports that stakeholders can't trust. This project documents a repeatable process for catching and flagging data quality issues before they reach a dashboard or report.

Tools

- Python and Pandas — ETL scripting and data quality checks
- SQL — validation queries
- Markdown — audit documentation

Structure

    data/       raw input data
    scripts/    ETL and data quality Python scripts
    outputs/    cleaned data and audit reports
    docs/       process documentation

Results

Running the full pipeline produces two outputs:

- `outputs/planning_applications_clean.csv` — cleaned dataset 
  ready for analysis or Power BI import
- `outputs/data_quality_report.txt` — audit summary with issues flagged

Data quality summary

| Check | Result |
|-------|--------|
| Missing values | Minor — 56 missing decisions (0.13%) |
| Duplicate rows | None |
| Negative values | None |
| Decision anomalies | 237 rows flagged for review |
| Coverage | 30 years, 10 regions, 462 local authorities |

Full process documented in [docs/etl_process.md](docs/etl_process.md)

How to run

```
python scripts/etl_pipeline.py
python scripts/data_quality_audit.py
```