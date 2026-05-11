from pathlib import Path

import joblib
import pandas as pd


MODEL_PATH = Path(
    "ml/models/revenue_forecast_model.pkl"
)


def predict_revenue(
    day_of_week: int,
    month: int,
    day: int,
    total_orders: int,
    total_items_sold: int
) -> float:

    model = joblib.load(MODEL_PATH)

    input_df = pd.DataFrame([{
        "day_of_week": day_of_week,
        "month": month,
        "day": day,
        "total_orders": total_orders,
        "total_items_sold": total_items_sold
    }])

    prediction = model.predict(input_df)[0]

    return round(prediction, 2)