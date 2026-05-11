from pathlib import Path

import duckdb
import pandas as pd


from src.logger import set_up_logger

logger = set_up_logger()

DATABASE_PATH = Path("database/restaurant_warehouse.duckdb")
RAW_DATA_PATH = Path("data/raw/restaurant_orders.csv")

def load_restaurant_data() -> None:

    logger.info("Starting restaurant data load process.")

    DATABASE_PATH.parent.mkdir(parents=True, exist_ok= True)

    df = pd.read_csv(RAW_DATA_PATH)

    logger.info(f"Loaded CSV with {len(df):,} rows.")

    conn = duckdb.connect(str(DATABASE_PATH))

    conn.execute("""
        CREATE OR REPLACE TABLE raw_orders AS
        SELECT * FROM df
    """)

    conn.close()

    logger.info("Raw restaurant data loaded successfully!")