# ApexPlanet Data Analytics Internship – Task 1
## Data Immersion & Data Wrangling

### Overview
This project is part of the ApexPlanet Data Analytics Internship. The objective of Task 1 is to understand the dataset, assess its quality, clean the data, and prepare it for further analysis.

---

## Dataset Information

- **Dataset:** ApexPlanet Sales Dataset
- **Rows:** 1000
- **Columns:** 12

The dataset contains customer orders, product details, sales information, and customer demographics.

---

## Objectives

- Understand the dataset
- Create a Data Dictionary
- Perform Data Quality Assessment
- Clean and transform the dataset
- Validate data quality
- Prepare the dataset for Exploratory Data Analysis (EDA)

---

## Files Included

- `ApexPlanet_DataAnalytics_Dataset.xlsx` – Original dataset
- `cleaned_sales_dataset.xlsx` – Cleaned dataset (Excel)
- `cleaned_sales_dataset.csv` – Cleaned dataset (CSV)
- `clean_data.py` – Python script for data cleaning
- `data_dictionary.md` – Data dictionary
- `data_quality_assessment.md` – Data quality assessment report

---

## Data Quality Assessment

The following checks were performed:

- Missing value detection
- Duplicate record detection
- Data type verification
- Formatting consistency check
- Outlier analysis
- Logical validation of sales values

### Issues Identified

- Missing values in **Age**
- Missing values in **City**
- Duplicate **Order_ID** values
- Order_Date stored as text format

---

## Data Cleaning Performed

- Filled missing **Age** values using the median age within each gender group.
- Filled missing **City** values with **"Unknown"**.
- Converted **Order_Date** to a standard datetime format.
- Fixed duplicate **Order_ID** values.
- Added new columns:
  - Order_Year
  - Order_Month
  - Age_Group
- Verified that:

```
Total_Sales = Quantity × Unit_Price
```

for every record.

---

## Technologies Used

- Python
- Pandas
- Microsoft Excel
- Git
- GitHub

---

## Project Structure

```
ApexPlanet-DataAnalytics-Task1/
│
├── ApexPlanet_DataAnalytics_Dataset.xlsx
├── cleaned_sales_dataset.xlsx
├── cleaned_sales_dataset.csv
├── clean_data.py
├── data_dictionary.md
├── data_quality_assessment.md
└── README.md
```

---

## Outcome

The dataset has been successfully cleaned, validated, and prepared for further analysis. It is now ready for Exploratory Data Analysis (EDA) and Business Intelligence tasks.

---

## Author

**Alok Kumar**

B.Tech Computer Science & Engineering  
IIIT Kottayam

GitHub: https://github.com/alokkumar-dotcom
