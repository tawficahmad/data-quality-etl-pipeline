import pandas as pd
import os
from datetime import datetime

print("=" * 60)
print("ETL PIPELINE — PLANNING APPLICATIONS DATA")
print(f"Run time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("=" * 60)

# --------------------------------------------------------
# STEP 1 — EXTRACT
# --------------------------------------------------------
print("\n[1/3] Extracting data...")

raw_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data', 'planning_applications.csv')
print(f"Looking for file at: {raw_path}")
df = pd.read_csv(raw_path, encoding='latin1', skiprows=3)

print(f"Rows extracted: {len(df):,}")
print(f"Columns extracted: {len(df.columns)}")

# --------------------------------------------------------
# STEP 2 — TRANSFORM
# --------------------------------------------------------
print("\n[2/3] Transforming data...")

cols = [
    'Region',
    'LPANM',
    'Quarter',
    'Applications received',
    'Applications decided',
    'Applications withdrawn',
    'Enforcement notices issued',
    'F_Year'
]

df = df[cols]
df.columns = [
    'region',
    'local_authority',
    'quarter',
    'apps_received',
    'apps_decided',
    'apps_withdrawn',
    'enforcement_notices',
    'year'
]

numeric_cols = ['apps_received', 'apps_decided', 'apps_withdrawn', 'enforcement_notices']
df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors='coerce')

df['year_clean'] = df['year'].str.split('-').str[0].astype(int)

df['region'] = df['region'].str.strip().str.title()
df['local_authority'] = df['local_authority'].str.strip().str.title()
df['quarter'] = df['quarter'].str.strip()

df = df.drop_duplicates()

df = df[df['year_clean'] >= 1996]

print(f"Rows after transformation: {len(df):,}")
print(f"Duplicate rows removed: {df.duplicated().sum()}")

# --------------------------------------------------------
# STEP 3 — LOAD
# --------------------------------------------------------
print("\n[3/3] Loading cleaned data...")

os.makedirs('../outputs', exist_ok=True)
output_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'outputs', 'planning_applications_clean.csv')
df.to_csv(output_path, index=False)

print(f"Clean data saved to: {output_path}")
print("\nETL pipeline completed successfully.")