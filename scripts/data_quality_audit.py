import pandas as pd
import os
from datetime import datetime

print("=" * 60)
print("DATA QUALITY AUDIT — PLANNING APPLICATIONS")
print(f"Run time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("=" * 60)

clean_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'outputs', 'planning_applications_clean.csv')
df = pd.read_csv(clean_path)

print(f"\nDataset: {len(df):,} rows x {len(df.columns)} columns")

print("\n--- 1. MISSING VALUES ---")
missing = df.isnull().sum()
missing_pct = (missing / len(df) * 100).round(2)
missing_report = pd.DataFrame({'missing_count': missing, 'missing_pct': missing_pct})
missing_report = missing_report[missing_report['missing_count'] > 0]
if missing_report.empty:
    print("No missing values found.")
else:
    print(missing_report)

print("\n--- 2. DUPLICATE ROWS ---")
dupes = df.duplicated().sum()
print(f"Duplicate rows: {dupes}")

print("\n--- 3. YEAR RANGE ---")
print(f"Earliest year: {df['year_clean'].min()}")
print(f"Latest year: {df['year_clean'].max()}")
print(f"Total years covered: {df['year_clean'].nunique()}")

print("\n--- 4. NEGATIVE VALUES CHECK ---")
numeric_cols = ['apps_received', 'apps_decided', 'apps_withdrawn', 'enforcement_notices']
for col in numeric_cols:
    negatives = (df[col] < 0).sum()
    print(f"{col}: {negatives} negative values")

print("\n--- 5. DECISIONS EXCEEDING APPLICATIONS RECEIVED ---")
anomalies = df[df['apps_decided'] > df['apps_received'] * 1.5]
print(f"Rows where decisions exceed 150% of applications received: {len(anomalies):,}")

print("\n--- 6. REGION COVERAGE ---")
print(f"Unique regions: {df['region'].nunique()}")
print(df['region'].value_counts())

print("\n--- 7. LOCAL AUTHORITY COVERAGE ---")
print(f"Unique local authorities: {df['local_authority'].nunique()}")

print("\n--- 8. SUMMARY ---")
total_checks = 6
issues = 0
if not missing_report.empty:
    issues += 1
if dupes > 0:
    issues += 1
if len(anomalies) > 0:
    issues += 1
print(f"Checks run: {total_checks}")
print(f"Issues flagged: {issues}")
print(f"Data quality status: {'⚠ REVIEW NEEDED' if issues > 0 else '✓ PASSED'}")

print("\nAudit completed.")

audit_output = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'outputs', 'data_quality_report.txt')

with open(audit_output, 'w') as f:
    f.write("DATA QUALITY AUDIT REPORT\n")
    f.write(f"Run time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    f.write("=" * 60 + "\n")
    f.write(f"Total rows: {len(df):,}\n")
    f.write(f"Missing values:\n{missing_report.to_string()}\n")
    f.write(f"Duplicate rows: {dupes}\n")
    f.write(f"Anomalies (decisions > 150% received): {len(anomalies):,}\n")
    f.write(f"Checks run: {total_checks}\n")
    f.write(f"Issues flagged: {issues}\n")
    f.write(f"Status: {'REVIEW NEEDED' if issues > 0 else 'PASSED'}\n")

print(f"\nAudit report saved to: {audit_output}")