# ETL Process & Data Quality Documentation

## Overview

This document describes the ETL pipeline and data quality audit 
process built for the UK government planning applications dataset. 
The process runs in two stages — first cleaning and restructuring 
the raw data, then auditing it for quality issues before it reaches 
any report or dashboard.

## Why this matters

Raw government datasets are rarely ready to analyse straight away. 
They arrive with inconsistent formatting, mixed data types, redundant 
columns and occasional anomalies. Running a structured ETL and audit 
process means any downstream analysis is built on data you can 
actually trust.

## Stage 1 — ETL Pipeline (`etl_pipeline.py`)

### Extract
Reads the raw CSV file published by the Department for Levelling Up, 
Housing and Communities. The file contains 93 columns and over 42,000 
rows covering all English local authorities from 1996 to 2025.

### Transform
- Selects the 8 columns relevant to the analysis
- Renames columns to clean, consistent lowercase names
- Converts numeric columns from text to numbers
- Extracts a clean 4-digit year from the inconsistent government 
  year format (e.g. `2023-24` → `2023`)
- Strips whitespace and standardises text formatting
- Removes duplicate rows

### Load
Saves the cleaned dataset to `outputs/planning_applications_clean.csv` 
— ready for analysis or import into a BI tool like Power BI.

### Results
- Raw dataset: 42,241 rows, 93 columns
- Clean dataset: 42,226 rows, 9 columns
- Rows removed: 15 duplicates
- Columns removed: 84 unnecessary columns

## Stage 2 — Data Quality Audit (`data_quality_audit.py`)

Runs 6 checks against the cleaned dataset and produces a summary 
report saved to `outputs/data_quality_report.txt`.

| Check | Result |
|-------|--------|
| Missing values | Minor — 56 missing decisions (0.13%) |
| Duplicate rows | None found |
| Year range | 1996 to 2025 — 30 years covered |
| Negative values | None found |
| Decision anomalies | 237 rows where decisions exceed 150% of applications received |
| Region coverage | 10 regions, 462 local authorities |

## Known Issues

**Decision anomalies (237 rows)**
These are rows where the number of decisions made exceeds 150% of 
applications received in the same period. This is likely due to 
councils clearing backlogs from previous quarters — decisions made 
in one period on applications received in an earlier one. These rows 
are flagged but not removed as they represent legitimate activity.

**Missing decisions (56 rows)**
A small number of rows have no decision count recorded. These 
represent 0.13% of the dataset and are unlikely to materially 
affect any analysis.

## How to run

From the project root directory:
python scripts/etl_pipeline.py
python scripts/data_quality_audit.py
Outputs will appear in the `outputs/` folder.
