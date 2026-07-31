import pandas as pd

RAW_PATH = "/Users/alokkumar/Desktop/Apex Planet/Task 1/ApexPlanet_DataAnalytics_Dataset.xlsx"
OUT_CSV = "/Users/alokkumar/Desktop/Apex Planet/Task 1/cleaned_sales_dataset.csv"
OUT_XLSX = "/Users/alokkumar/Desktop/Apex Planet/Task 1/cleaned_sales_dataset.xlsx"


def load_data(path: str) -> pd.DataFrame:
    df = pd.read_excel(path, sheet_name="Sales_Dataset")
    return df


def fix_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    # Age: impute with median age within each Gender group
    df["Age"] = df.groupby("Gender")["Age"].transform(
        lambda s: s.fillna(s.median())
    )

    # City: too few missing (13) to safely infer -> explicit "Unknown" flag
    df["City"] = df["City"].fillna("Unknown")

    return df


def fix_duplicate_ids(df: pd.DataFrame) -> pd.DataFrame:
    # Keep the first occurrence of each Order_ID as-is.
    # For repeats, append a suffix so every row has a unique key.
    is_dupe = df.duplicated(subset="Order_ID", keep="first")
    dupe_counter = df.groupby("Order_ID").cumcount()  # 0,1,2... per Order_ID group

    df.loc[is_dupe, "Order_ID"] = (
        df.loc[is_dupe, "Order_ID"] + "-" + dupe_counter[is_dupe].astype(str)
    )
    return df


def standardize_dates(df: pd.DataFrame) -> pd.DataFrame:
    df["Order_Date"] = pd.to_datetime(df["Order_Date"], errors="coerce")
    return df


def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    df["Order_Year"] = df["Order_Date"].dt.year
    df["Order_Month"] = df["Order_Date"].dt.month_name()

    bins = [17, 25, 35, 45, 55, 65]
    labels = ["18-25", "26-35", "36-45", "46-55", "56-65"]
    df["Age_Group"] = pd.cut(df["Age"], bins=bins, labels=labels, include_lowest=True)

    return df


def run_quality_checks(df: pd.DataFrame) -> None:
    assert df["Order_ID"].is_unique, "Order_ID is still not unique!"
    assert df.isna().sum().sum() == 0, "Unexpected nulls remain after cleaning!"
    mismatch = (df["Quantity"] * df["Unit_Price"] - df["Total_Sales"]).abs() > 0.01
    assert mismatch.sum() == 0, "Total_Sales does not match Quantity * Unit_Price!"
    print("All quality checks passed.")


def main():
    df = load_data(RAW_PATH)
    print(f"Loaded {len(df)} rows, {len(df.columns)} columns")

    df = fix_missing_values(df)
    df = fix_duplicate_ids(df)
    df = standardize_dates(df)
    df = engineer_features(df)

    run_quality_checks(df)

    df["Order_Date"] = df["Order_Date"].dt.strftime("%Y-%m-%d")

    df.to_csv(OUT_CSV, index=False)
    df.to_excel(OUT_XLSX, index=False)
    print(f"Saved cleaned dataset to {OUT_CSV} and {OUT_XLSX}")


if __name__ == "__main__":
    main()
