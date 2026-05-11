from pathlib import Path

import duckdb
import pandas as pd

from src.logger import set_up_logger


logger = set_up_logger()

DATABASE_PATH = Path("database/restaurant_warehouse.duckdb")
RAW_DATA_PATH = Path("data/raw/restaurant_orders.csv")

def load_restaurant_data() -> None:
    logger.info("Starting restaurant data load process.")

    if not RAW_DATA_PATH.exists():
        raise FileNotFoundError(f"Missing raw data file: {RAW_DATA_PATH}")

    DATABASE_PATH.parent.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(RAW_DATA_PATH)

    logger.info(f"Loaded CSV with {len(df):,} rows.")

    conn = duckdb.connect(str(DATABASE_PATH))

    conn.execute("""
        CREATE TABLE IF NOT EXISTS raw_orders AS
        SELECT *
        FROM df
        WHERE 1 = 0
    """)

    existing_order_ids = conn.execute("""
        SELECT order_id
        FROM raw_orders
    """).df()

    if not existing_order_ids.empty:
        existing_ids = set(existing_order_ids["order_id"])
        df_new = df[~df["order_id"].isin(existing_ids)]
    else:
        df_new = df

    if df_new.empty:
        logger.info("No new restaurant orders found.")
    else:
        conn.execute("""
            INSERT INTO raw_orders
            SELECT *
            FROM df_new
        """)

        logger.info(f"Inserted {len(df_new):,} new rows into raw_orders.")

    total_rows = conn.execute("""
        SELECT COUNT(*)
        FROM raw_orders
    """).fetchone()[0]

    logger.info(f"raw_orders now contains {total_rows:,} rows.")

    conn.close()


if __name__ == "__main__":
    load_restaurant_data()