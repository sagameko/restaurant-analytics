from pathlib import Path

import duckdb
import joblib
import pandas as pd

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split


# =========================
# Paths
# =========================

DATABASE_PATH = Path(
    "database/restaurant_warehouse.duckdb"
)

MODEL_PATH = Path(
    "ml/models/revenue_forecast_model.pkl"
)


# =========================
# Load data
# =========================

conn = duckdb.connect(str(DATABASE_PATH))

df = conn.execute("""
    SELECT *
    FROM mart_daily_sale
""").df()

conn.close()


# =========================
# Feature engineering
# =========================

df["full_date"] = pd.to_datetime(
    df["full_date"]
)

df["day_of_week"] = (
    df["full_date"]
    .dt.dayofweek
)

df["month"] = (
    df["full_date"]
    .dt.month
)

df["day"] = (
    df["full_date"]
    .dt.day
)


# =========================
# Features & target
# =========================

X = df[
    [
        "day_of_week",
        "month",
        "day",
        "total_orders",
        "total_items_sold"
    ]
]

y = df["total_revenue"]


# =========================
# Train/test split
# =========================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# =========================
# Train model
# =========================

model = RandomForestRegressor(
    n_estimators=200,
)

model.fit(X_train, y_train)


# =========================
# Evaluation
# =========================

predictions = model.predict(X_test)

mae = mean_absolute_error(
    y_test,
    predictions
)

print("\nModel Evaluation")
print("-" * 30)
print(f"Mean Absolute Error: ${mae:,.2f}")


# =========================
# Save model
# =========================

MODEL_PATH.parent.mkdir(
    parents=True,
    exist_ok=True
)

joblib.dump(model, MODEL_PATH)

print(f"\nModel saved to:")
print(MODEL_PATH)