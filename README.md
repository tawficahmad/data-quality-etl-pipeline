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