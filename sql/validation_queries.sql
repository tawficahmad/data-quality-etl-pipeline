-- ============================================================
-- DATA QUALITY VALIDATION QUERIES
-- Planning Applications Dataset
-- ============================================================


-- ------------------------------------------------------------
-- 1. CHECK FOR MISSING VALUES
-- ------------------------------------------------------------
SELECT
    SUM(CASE WHEN apps_received IS NULL THEN 1 ELSE 0 END) AS missing_received,
    SUM(CASE WHEN apps_decided IS NULL THEN 1 ELSE 0 END) AS missing_decided,
    SUM(CASE WHEN apps_withdrawn IS NULL THEN 1 ELSE 0 END) AS missing_withdrawn,
    SUM(CASE WHEN enforcement_notices IS NULL THEN 1 ELSE 0 END) AS missing_enforcement
FROM planning_applications_clean;


-- ------------------------------------------------------------
-- 2. CHECK FOR DUPLICATE ROWS
-- ------------------------------------------------------------
SELECT
    local_authority,
    quarter,
    year,
    COUNT(*) AS row_count
FROM planning_applications_clean
GROUP BY local_authority, quarter, year
HAVING COUNT(*) > 1
ORDER BY row_count DESC;


-- ------------------------------------------------------------
-- 3. CHECK FOR NEGATIVE VALUES
-- ------------------------------------------------------------
SELECT *
FROM planning_applications_clean
WHERE apps_received < 0
   OR apps_decided < 0
   OR apps_withdrawn < 0
   OR enforcement_notices < 0;


-- ------------------------------------------------------------
-- 4. FLAG ANOMALIES — DECISIONS EXCEEDING APPLICATIONS
-- ------------------------------------------------------------
SELECT
    local_authority,
    year_clean,
    apps_received,
    apps_decided,
    ROUND((apps_decided * 100.0 / NULLIF(apps_received, 0)), 1) AS decision_rate_pct
FROM planning_applications_clean
WHERE apps_decided > apps_received * 1.5
ORDER BY decision_rate_pct DESC;


-- ------------------------------------------------------------
-- 5. YEAR RANGE CHECK
-- ------------------------------------------------------------
SELECT
    MIN(year_clean) AS earliest_year,
    MAX(year_clean) AS latest_year,
    COUNT(DISTINCT year_clean) AS total_years
FROM planning_applications_clean;


-- ------------------------------------------------------------
-- 6. REGION COMPLETENESS CHECK
-- ------------------------------------------------------------
SELECT
    region,
    COUNT(DISTINCT local_authority) AS authority_count,
    COUNT(*) AS total_rows,
    SUM(CASE WHEN apps_received IS NULL THEN 1 ELSE 0 END) AS missing_values
FROM planning_applications_clean
GROUP BY region
ORDER BY total_rows DESC;