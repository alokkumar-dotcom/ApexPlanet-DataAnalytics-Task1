# Data Quality Assessment — ApexPlanet Sales Dataset

## 1. Missing Values
| Column | Missing Count | % of Rows | Action |
|---|---|---|---|
| `Age` | 20 | 2.0% | Impute with median age, grouped by `Gender` |
| `City` | 13 | 1.3% | Fill with `"Unknown"` (too few to safely impute a real city) |
| All other columns | 0 | 0% | No action needed |

## 2. Duplicates
- **Full-row duplicates:** 0
- **Duplicate `Order_ID` values:** 8 IDs are reused across 9 rows total (e.g. `ORD100050` appears
  9 times with 9 *different* customers, dates, and products). This breaks the primary-key
  assumption on `Order_ID` and would cause row loss in any `JOIN`/`VLOOKUP` on that field.
  **Action:** regenerate a unique ID for the duplicate rows (keep the first occurrence as-is).

## 3. Formatting Consistency
- `Order_Date` is stored as text in the source file rather than a true date type.
  **Action:** convert to `datetime`, standardize output as `YYYY-MM-DD`.
- Categorical fields (`Gender`, `City`, `Product`, `Category`) were checked for casing/spelling
  inconsistencies (e.g. `"bengaluru"` vs `"Bengaluru"`, trailing spaces) — **none found**, values
  are already clean and consistent.

## 4. Outlier / Range Checks
| Column | Min | Max | Assessment |
|---|---|---|---|
| `Age` | 18 | 65 | Reasonable adult customer range, no outliers |
| `Quantity` | 1 | 10 | Reasonable order-line range, no outliers |
| `Unit_Price` | ₹145.78 | ₹49,997.53 | Wide range expected (Grocery vs Electronics/Furniture), no impossible values (no zero/negative) |
| `Total_Sales` | — | — | Verified `Total_Sales = Quantity × Unit_Price` holds for **all 1,000 rows** — no calculation errors |

## 5. Referential/Logical Checks
- No negative or zero values in `Quantity`, `Unit_Price`, or `Total_Sales`.
- `Order_Date` values all fall within a sensible business window (Jan 2025–Jan 2026).

## Summary
Overall the dataset is fairly clean. The two issues requiring real cleaning work are the
**missing values in `Age`/`City`** and the **duplicate `Order_ID`s**. Everything else needed only
type standardization and light feature engineering.
