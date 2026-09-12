import pandas as pd
from pathlib import Path
from datetime import datetime
from sqlalchemy import create_engine, text
from urllib.parse import quote_plus

# ============================================================
# NexaRetail Sales Analytics ETL Pipeline
# Raw CSV -> Cleaning/Validation -> SQL Server
# ============================================================

print("=" * 60)
print("NexaRetail Sales Analytics Pipeline Started")
print("=" * 60)

# 1. PROJECT PATHS
BASE_DIR = Path(__file__).resolve().parent
RAW_FILE = BASE_DIR / "sales_data_raw.csv"
CLEAN_FILE = BASE_DIR / "sales_data_cleaned.csv"
REJECTED_DATE_FILE = BASE_DIR / "rejected_order_dates.csv"
REJECTED_QUANTITY_FILE = BASE_DIR / "rejected_quantity_records.csv"
LOG_DIR = BASE_DIR / "logs"
LOG_DIR.mkdir(exist_ok=True)

run_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
LOG_FILE = LOG_DIR / f"etl_{run_time}.log"

# 2. SIMPLE LOGGING
def log(message=""):
    print(message)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(str(message) + "\n")

# 3. CHECK RAW FILE
if not RAW_FILE.exists():
    log(f"ERROR: Raw file not found: {RAW_FILE}")
    raise FileNotFoundError(f"Raw file not found: {RAW_FILE}")

try:
    # 4. LOAD RAW DATA
    sales_01 = pd.read_csv(RAW_FILE)

    log("Raw data loaded successfully")
    log(f"Rows: {len(sales_01)}")
    log(f"Columns: {len(sales_01.columns)}")

    required_columns = [
        "Order_ID", "Order_Date", "Ship_Date", "Customer_ID",
        "Segment", "Region", "State", "City", "Category",
        "Sub_Category", "Quantity", "Unit_Price", "Discount",
        "Sales", "Profit"
    ]

    missing_columns = [
        col for col in required_columns
        if col not in sales_01.columns
    ]

    if missing_columns:
        log(f"ERROR: Required columns missing: {missing_columns}")
        raise ValueError(
            f"Required columns missing from CSV: {missing_columns}"
        )

    # 5. DATA QUALITY CHECK
    log("\nDATA QUALITY CHECK")
    log("------------------")
    log("Missing values:")
    log(sales_01.isnull().sum().to_string())
    log(f"\nDuplicate rows: {sales_01.duplicated().sum()}")

    # 6. REMOVE EXACT DUPLICATES
    log("\nDATA CLEANING")
    log("-------------")

    before_duplicates = len(sales_01)
    sales_clean = sales_01.drop_duplicates().copy()
    after_duplicates = len(sales_clean)

    log(
        f"Duplicate rows removed: "
        f"{before_duplicates - after_duplicates}"
    )
    log(f"Rows after removing duplicates: {after_duplicates}")

    # 7. REMOVE ROWS WITH MISSING SALES
    before_sales_missing = len(sales_clean)
    sales_clean = sales_clean.dropna(subset=["Sales"]).copy()
    after_sales_missing = len(sales_clean)

    log(
        f"Missing Sales rows removed: "
        f"{before_sales_missing - after_sales_missing}"
    )
    log(f"Rows after handling missing Sales: {after_sales_missing}")

    # 8. CONVERT DATE COLUMNS
    log("\nDATE PROCESSING")
    log("---------------")

    sales_clean["Order_Date"] = pd.to_datetime(
        sales_clean["Order_Date"],
        format="mixed",
        dayfirst=True,
        errors="coerce"
    ).dt.date

    sales_clean["Ship_Date"] = pd.to_datetime(
        sales_clean["Ship_Date"],
        format="mixed",
        dayfirst=True,
        errors="coerce"
    ).dt.date

    log("Date columns converted successfully")

    # 9. HANDLE INVALID ORDER DATES
    invalid_order_dates = sales_clean[
        sales_clean["Order_Date"].isna()
    ].copy()

    invalid_order_dates.to_csv(
        REJECTED_DATE_FILE,
        index=False
    )

    sales_clean = sales_clean.dropna(
        subset=["Order_Date"]
    ).copy()

    log("\nDATE VALIDATION")
    log("----------------")
    log(f"Invalid Order Dates: {len(invalid_order_dates)}")
    log(f"Invalid Ship Dates: {sales_clean['Ship_Date'].isna().sum()}")
    log(
        f"Rejected Order Date records saved: "
        f"{len(invalid_order_dates)}"
    )
    log(f"Rows after removing invalid Order Dates: {len(sales_clean)}")

    # 10. HANDLE INVALID QUANTITY
    log("\nQUANTITY VALIDATION")
    log("-------------------")

    invalid_quantity = sales_clean[
        sales_clean["Quantity"] < 0
    ].copy()

    invalid_quantity.to_csv(
        REJECTED_QUANTITY_FILE,
        index=False
    )

    log(f"Negative Quantity records: {len(invalid_quantity)}")

    sales_clean = sales_clean[
        sales_clean["Quantity"] >= 0
    ].copy()

    log(
        f"Rows after removing invalid quantities: "
        f"{len(sales_clean)}"
    )

    # 11. BUSINESS VALIDATION
    log("\nBUSINESS VALIDATION")
    log("-------------------")

    negative_quantity = (sales_clean["Quantity"] < 0).sum()
    log(f"Negative Quantity remaining: {negative_quantity}")

    if negative_quantity == 0:
        log("Quantity check: PASS")
    else:
        log("Quantity check: FAIL")

    invalid_discount = (
        (sales_clean["Discount"] < 0) |
        (sales_clean["Discount"] > 1)
    ).sum()

    log(f"Invalid Discount remaining: {invalid_discount}")

    if invalid_discount == 0:
        log("Discount check: PASS")
    else:
        log("Discount check: FAIL")

    invalid_sales = sales_clean[
        sales_clean["Sales"] < 0
    ].copy()

    log(f"Negative Sales records: {len(invalid_sales)}")

    if len(invalid_sales) == 0:
        log("Sales check: PASS")
    else:
        log("Sales check: FAIL")

    # Negative Profit is allowed because it represents a loss.
    loss_records = sales_clean[
        sales_clean["Profit"] < 0
    ].copy()

    log(f"Loss-making records: {len(loss_records)}")
    log("Profit check: PASS (negative Profit represents a loss)")

    # 12. FINAL DATA VALIDATION
    log("\nFINAL DATA VALIDATION")
    log("---------------------")

    remaining_missing = sales_clean.isnull().sum().sum()
    remaining_duplicates = sales_clean.duplicated().sum()
    invalid_ship_dates = sales_clean["Ship_Date"].isna().sum()

    log(f"Final rows: {len(sales_clean)}")
    log(f"Missing values: {remaining_missing}")
    log(f"Duplicate rows: {remaining_duplicates}")
    log(f"Invalid Ship Dates: {invalid_ship_dates}")

    validation_passed = (
        remaining_missing == 0
        and remaining_duplicates == 0
        and negative_quantity == 0
        and invalid_discount == 0
        and len(invalid_sales) == 0
        and invalid_ship_dates == 0
    )

    if not validation_passed:
        log("Final validation: FAIL")
        log(
            "SQL Server was NOT changed because the new data "
            "failed validation."
        )
        raise ValueError(
            "Final validation failed. Existing SQL Server data "
            "was left unchanged."
        )

    log("Final validation: PASS")

    # 13. SAVE FINAL CLEAN DATA
    sales_clean.to_csv(
        CLEAN_FILE,
        index=False
    )

    log("\nCleaned data saved successfully")
    log(f"Cleaned file: {CLEAN_FILE}")
    log(f"Clean rows: {len(sales_clean)}")

    # 14. SQL SERVER CONNECTION
    log("\nSQL SERVER CONNECTION")
    log("---------------------")

    server = "localhost"
    database = "SalesAnalytics"

    connection_string = (
        "DRIVER={ODBC Driver 18 for SQL Server};"
        "SERVER=localhost;"
        "DATABASE=SalesAnalytics;"
        "Trusted_Connection=yes;"
        "TrustServerCertificate=yes;"
    )

    engine = create_engine(
        "mssql+pyodbc:///?odbc_connect=" +
        quote_plus(connection_string)
    )

    log("SQL Server connection created successfully")

    # 15. REPLACE SQL DATA SAFELY
    log("\nLOADING DATA INTO SQL SERVER")
    log("----------------------------")

    # DELETE + INSERT are in one transaction.
    # If the insert fails, the DELETE is rolled back.
    with engine.begin() as connection:
        connection.execute(text("DELETE FROM dbo.Sales"))
        log("Previous SQL data cleared")

        sales_clean.to_sql(
            name="Sales",
            con=connection,
            schema="dbo",
            if_exists="append",
            index=False
        )

        log("New cleaned data inserted")

    # 16. SQL SERVER VALIDATION
    log("\nSQL SERVER VALIDATION")
    log("---------------------")

    with engine.connect() as connection:
        result = connection.execute(
            text("SELECT COUNT(*) FROM dbo.Sales")
        )
        sql_rows = result.fetchone()[0]

    expected_rows = len(sales_clean)

    log(f"Rows in SQL Server: {sql_rows}")
    log(f"Expected rows: {expected_rows}")

    if sql_rows == expected_rows:
        log("Row count check: PASS")
    else:
        log("Row count check: FAIL")
        raise ValueError(
            "SQL Server row count does not match expected row count."
        )

    # 17. SUCCESS
    log("\n" + "=" * 60)
    log("NexaRetail ETL COMPLETED SUCCESSFULLY")
    log("=" * 60)
    log(f"Final rows loaded: {expected_rows}")
    log(f"Log file: {LOG_FILE}")

except Exception as e:
    log("\n" + "=" * 60)
    log("NexaRetail ETL FAILED")
    log("=" * 60)
    log(f"Error: {e}")
    log(f"Log file: {LOG_FILE}")
    raise
