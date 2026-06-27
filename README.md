# NorthWind-Finance
Northwind Trading Co. FP&amp;A build on Fabric: automate a manual Excel month-end A ~12k-line GL plus monthly budget and rolling forecast (FY24–25, 7 depts, 3 regions) that reconcile  actual net profit £9.6m vs £9.6m budget (+0.5%). Medallion to a Direct Lake model feeding PowerBI: budget-vs-actual waterfall, variance matrix and P&amp;L, RLS by department.


# Northwind Trading Co. — Synthetic FP&A Dataset

**Purpose:** A clean, internally-consistent finance dataset for a Microsoft Fabric / Power BI budget-vs-actual showcase. Actuals, Budget and Forecast share the same dimensional keys and reconcile, so variance analysis ties out.

**Company:** Northwind Trading Co. (fictional) · **Currency:** GBP · **Period:** FY2024–FY2025 (calendar fiscal year, 24 months) · **Generated:** synthetically, fully reproducible via `generate_finance_data.py`.

**Sign convention (P&L):** Revenue is positive, expenses are negative, so `SUM(Amount)` gives net profit. Contra-revenue (returns & discounts) is negative.

---

## Tables

### fact_gl_actuals.csv — transaction-level General Ledger (≈12,000 rows)
Grain: one journal line. Aggregates up to the monthly Budget/Forecast grain.
| Column | Description |
|--------|-------------|
| JournalID | Unique journal line ID |
| Date | Posting date (within FY2024–FY2025) |
| AccountNo / AccountName / AccountType | Chart-of-accounts reference |
| Department | Owning department |
| Region | UK / Europe / North America |
| Amount | Signed GBP (revenue +, expense −) |
| Currency | GBP |
| Description | Source narrative (e.g. Customer invoice, Payroll run) |

### fact_budget.csv — monthly plan (1,512 rows)
Grain: Month × Account × Department × Region.
| Column | Description |
|--------|-------------|
| Month, FiscalYear, FiscalQuarter | Period |
| AccountNo / AccountName / AccountType | Account |
| Department, Region | Keys |
| BudgetAmount | Planned GBP (same sign convention) |

### fact_forecast.csv — rolling reforecast (1,512 rows)
Same grain as budget. "As-of" July 2025: past months equal actuals, future months are budget adjusted by a forecast bias. Use to show Actual vs Budget vs Forecast across the timeline.

### dim_date.csv — daily calendar (731 rows)
Date, DateKey, Year, Quarter, MonthNo, MonthName, MonthYear, FiscalYear. Mark as the date table in Power BI.

### dim_account.csv — Chart of Accounts (15 rows)
AccountNo, AccountName, AccountType (Revenue / Contra Revenue / COGS / Operating Expense), Statement, OwningDept.

### dim_department.csv — 7 departments
Sales, Marketing, R&D, Operations, Finance, HR, IT.

### dim_region.csv — 3 regions
UK, Europe, North America (with plan weight). Use for row-level security.

---

## Suggested Power BI star schema
- Facts: `fact_gl_actuals`, `fact_budget`, `fact_forecast`.
- Dimensions: `dim_date` (on Date / MonthYear), `dim_account` (AccountNo), `dim_department` (Department), `dim_region` (Region).
- Core DAX: Total Actual = `SUM(fact_gl_actuals[Amount])`; Total Budget; Variance = Actual − Budget; Variance % ; plus `SAMEPERIODLASTYEAR` and `TOTALYTD` time-intelligence.
- Built-in realism: Marketing systematically overspends, R&D underspends, revenue ran ahead of plan in FY2024 and slightly behind in FY2025 — so the variance story is non-trivial.

## Notes
- This is 100% synthetic data — no confidentiality concerns, safe for a public portfolio.
- Regenerate or rescale anytime by editing the assumptions block in `generate_finance_data.py` (a nice "I built the data engineering too" talking point).
