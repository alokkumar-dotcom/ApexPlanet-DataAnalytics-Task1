# Data Dictionary — ApexPlanet Sales Dataset

**Source file:** `ApexPlanet_DataAnalytics_Dataset.xlsx` (sheet: `Sales_Dataset`)
**Rows:** 1,000 | **Columns:** 12
**Grain:** One row = one line-item sales order

| Column | Type | Description | Business Relevance |
|---|---|---|---|
| `Order_ID` | Text (string) | Unique identifier for each order (e.g. `ORD100002`) | Primary key for tracking individual transactions |
| `Order_Date` | Date | Date the order was placed | Enables trend, seasonality, and time-series analysis |
| `Customer_ID` | Text (string) | Unique identifier for each customer (e.g. `CUST5529`) | Links orders to customers for repeat-purchase / retention analysis |
| `Customer_Name` | Text (string) | Customer's display name | Identification; not used for analytics (low cardinality value) |
| `Age` | Numeric (float) | Customer's age in years | Enables demographic segmentation |
| `Gender` | Categorical | `Male` / `Female` | Demographic segmentation, targeted marketing |
| `City` | Categorical | Customer's city (e.g. Bengaluru, Delhi, Mumbai) | Regional sales performance and market expansion analysis |
| `Product` | Categorical | Product purchased (e.g. Rice, Book, Laptop) | Product-level performance tracking |
| `Category` | Categorical | Product category (e.g. Grocery, Electronics, Fashion) | Category-level trends, cross-sell analysis |
| `Quantity` | Numeric (integer) | Number of units purchased | Volume analysis, demand forecasting |
| `Unit_Price` | Numeric (float) | Price per unit (₹) | Pricing analysis, margin studies |
| `Total_Sales` | Numeric (float) | `Quantity × Unit_Price` | Core revenue metric — used in nearly every downstream KPI |

**Derived columns added during cleaning (see cleaning script):**

| Column | Type | Description |
|---|---|---|
| `Order_Year` | Integer | Year extracted from `Order_Date` |
| `Order_Month` | Text | Month name extracted from `Order_Date` |
| `Age_Group` | Categorical | Age bucketed into `18-25`, `26-35`, `36-45`, `46-55`, `56-65` |
