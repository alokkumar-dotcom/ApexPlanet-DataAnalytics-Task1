# 📊 ApexPlanet Data Analytics Internship – Task 1

## Data Cleaning & Preparation using Python (Pandas)

## 📌 Project Overview

This project was completed as part of the **ApexPlanet Data Analytics Internship**.

The objective of **Task 1** was to understand the provided sales dataset, assess its quality, identify data quality issues, clean and transform the data, and prepare it for further analysis.

---

## 📊 Dataset Information

**Dataset Name:** ApexPlanet Sales Dataset

- **Total Records:** 1,000
- **Total Columns:** 12

The dataset contains customer information, order details, product information, pricing, and sales transaction data.

---

## 🎯 Objectives

- Understand the dataset structure
- Create a Data Dictionary
- Perform Data Quality Assessment
- Identify data quality issues
- Clean and transform the dataset
- Validate the cleaned dataset
- Prepare the data for Exploratory Data Analysis (EDA)

---

## 📁 Project Structure

```text
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

## 📖 Data Dictionary

A comprehensive **Data Dictionary** was created for every column in the dataset, including:

- Column Name
- Data Type
- Description
- Business Importance

This documentation helps users understand the purpose and business relevance of every attribute in the dataset.

---

## 🔍 Data Quality Assessment

The dataset was profiled to identify potential data quality issues before analysis.

### Checks Performed

- Missing Value Detection
- Duplicate Record Detection
- Data Type Verification
- Formatting Consistency Check
- Outlier Analysis
- Logical Validation

### Issues Identified

- 20 missing values in the **Age** column
- 13 missing values in the **City** column
- Duplicate **Order_ID** values detected
- **Order_Date** stored as text instead of datetime
- No calculation errors found in **Total_Sales**

---

## 🧹 Data Cleaning & Transformation

The following preprocessing steps were performed using **Python (Pandas)**:

- Filled missing **Age** values using the median age within each gender group.
- Replaced missing **City** values with **"Unknown"**.
- Converted **Order_Date** to datetime format.
- Standardized the date format.
- Resolved duplicate **Order_ID** values by creating unique identifiers.
- Created additional analytical features:
  - Order_Year
  - Order_Month
  - Age_Group

Validated that:

```text
Total_Sales = Quantity × Unit_Price
```

for every record.

---

## ✅ Data Validation

The cleaned dataset was validated to ensure:

- No missing values remain.
- Every **Order_ID** is unique.
- **Total_Sales** is correctly calculated.
- Date formats are standardized.
- The dataset is ready for further analysis.

---

## 🛠️ Technologies Used

- Python
- Pandas
- Microsoft Excel
- Git
- GitHub
- Visual Studio Code

---

## 📈 Project Outcome

After completing the data cleaning process:

- Improved overall dataset quality.
- Handled all missing values.
- Resolved duplicate order IDs.
- Standardized date formats.
- Created new analytical features.
- Prepared the dataset for Exploratory Data Analysis (EDA) and Business Intelligence.

---

## 🚀 Future Work

The cleaned dataset will be used in **Task 2** for:

- Exploratory Data Analysis (EDA)
- Data Visualization
- Business Insights
- Interactive Dashboard Development

---

## 👨‍💻 Author

**Alok Kumar**

**B.Tech – Computer Science & Engineering**

**Indian Institute of Information Technology (IIIT) Kottayam**

🔗 **GitHub:** https://github.com/alokkumar-dotcom

🔗 **LinkedIn:** https://www.linkedin.com/in/alok-kumar-b19a2835b/

---

⭐ If you found this project useful, consider starring the repository and exploring the remaining internship projects in this series.
