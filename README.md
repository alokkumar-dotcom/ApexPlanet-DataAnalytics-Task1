# ApexPlanet Data Analytics Internship – Task 1
## Data Immersion & Data Wrangling using Python (Pandas)

## 📌 Project Overview

This project was completed as part of the **ApexPlanet Data Analytics Internship**.

The objective of Task 1 is to understand the provided sales dataset, assess its quality, identify data issues, clean and transform the data, and prepare it for further analysis.

---

# 📊 Dataset Information

- **Dataset Name:** ApexPlanet Sales Dataset
- **Total Records:** 1000
- **Total Columns:** 12

The dataset contains customer information, order details, product information, pricing, and sales transactions.

---

# 🎯 Objectives

- Understand the dataset structure
- Create a Data Dictionary
- Perform Data Quality Assessment
- Identify data quality issues
- Clean and transform the dataset
- Validate the cleaned dataset
- Prepare the data for Exploratory Data Analysis (EDA)

---

# 📁 Project Files

```
ApexPlanet-DataAnalytics-Task1/

├── ApexPlanet_DataAnalytics_Dataset.xlsx
├── cleaned_sales_dataset.xlsx
├── cleaned_sales_dataset.csv
├── clean_data.py
├── data_dictionary.md
├── data_quality_assessment.md
├── README.md
└── .gitignore
```

---

# 📖 Data Dictionary

A comprehensive Data Dictionary was created for every column in the dataset, including:

- Column Name
- Data Type
- Description
- Business Importance

This helps users understand the purpose and business relevance of each attribute.

---

# 🔍 Data Quality Assessment

The dataset was profiled to identify potential data quality issues.

## Checks Performed

- Missing Value Detection
- Duplicate Record Detection
- Data Type Verification
- Formatting Consistency Check
- Outlier Analysis
- Logical Validation

## Issues Identified

- 20 missing values in the **Age** column.
- 13 missing values in the **City** column.
- Duplicate **Order_ID** values detected.
- **Order_Date** stored as text format.
- No calculation errors found in **Total_Sales**.

---

# 🧹 Data Cleaning & Transformation

The following preprocessing steps were performed using **Python (Pandas)**:

- Filled missing **Age** values using the median age within each gender group.
- Replaced missing **City** values with `"Unknown"`.
- Converted **Order_Date** to datetime format.
- Standardized the date format.
- Resolved duplicate **Order_ID** values by creating unique identifiers.
- Added new features:
  - Order_Year
  - Order_Month
  - Age_Group
- Validated that:

```
Total_Sales = Quantity × Unit_Price
```

for all records.

---

# ✅ Data Validation

The cleaned dataset was validated to ensure:

- No missing values remain.
- Every **Order_ID** is unique.
- **Total_Sales** is correctly calculated.
- Date format is standardized.
- Dataset is ready for analysis.

---

# 🛠️ Technologies Used

- Python
- Pandas
- Microsoft Excel
- Git
- GitHub
- Visual Studio Code

---

# 📈 Project Outcome

After completing the data cleaning process:

- Dataset quality improved significantly.
- Missing values were handled.
- Duplicate order IDs were resolved.
- Date formats were standardized.
- New analytical features were created.
- The dataset is now ready for Exploratory Data Analysis (EDA) and Business Intelligence.

---

# 🚀 Future Work

The cleaned dataset will be used in **Task 2** for:

- Exploratory Data Analysis (EDA)
- Data Visualization
- Business Insights
- Dashboard Development

---

# 👨‍💻 Author

**Alok Kumar**

B.Tech in Computer Science & Engineering  
IIIT Kottayam

**GitHub:** https://github.com/alokkumar-dotcom

---

## ⭐ If you found this project useful, feel free to star the repository.
