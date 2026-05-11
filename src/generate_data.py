from pathlib import Path
import random
from datetime import datetime, timedelta

import pandas as pd
from faker import Faker


fake = Faker()

RAW_DATA_PATH = Path("data/raw/restaurant_orders.csv")


MENU_ITEMS = [
    ("Pho Bo", "Main", 16.50, 6.50),
    ("Pho Ga", "Main", 15.50, 6.00),
    ("Bun Bo Hue", "Main", 17.50, 7.00),
    ("Banh Mi Pork", "Main", 11.50, 4.00),
    ("Rice Paper Rolls", "Starter", 9.50, 3.00),
    ("Spring Rolls", "Starter", 10.50, 3.50),
    ("Com Tam", "Main", 18.50, 7.50),
    ("Vietnamese Iced Coffee", "Drink", 6.50, 1.50),
    ("Lemon Iced Tea", "Drink", 5.50, 1.20),
    ("Coke", "Drink", 4.50, 1.00),
]

STAFF = ["Jack", "Anna", "Minh", "Linh", "David"]
PAYMENT_METHODS = ["Card", "Cash", "Online"]
ORDER_TYPES = ["Dine-in", "Takeaway", "Delivery"]


def generate_orders(num_orders: int = 5000) -> pd.DataFrame:
    rows = []

    start_date = datetime(2024, 1, 1)
    end_date = datetime(2024, 12, 31)
    total_days = (end_date - start_date).days

    for order_id in range(1, num_orders + 1):
        order_datetime = start_date + timedelta(
            days=random.randint(0, total_days),
            hours=random.randint(10, 21),
            minutes=random.randint(0, 59),
        )

        item_name, category, unit_price, unit_cost = random.choice(MENU_ITEMS)
        quantity = random.choices([1, 2, 3, 4], weights=[60, 25, 10, 5])[0]
        discount = random.choice([0, 0, 0, 0.05, 0.10])

        gross_revenue = unit_price * quantity
        discount_amount = gross_revenue * discount
        net_revenue = gross_revenue - discount_amount
        total_cost = unit_cost * quantity
        profit = net_revenue - total_cost

        rows.append({
            "order_id": order_id,
            "order_datetime": order_datetime,
            "customer_name": fake.first_name(),
            "menu_item": item_name,
            "category": category,
            "quantity": quantity,
            "unit_price": unit_price,
            "unit_cost": unit_cost,
            "discount_rate": discount,
            "net_revenue": round(net_revenue, 2),
            "total_cost": round(total_cost, 2),
            "profit": round(profit, 2),
            "staff_name": random.choice(STAFF),
            "payment_method": random.choice(PAYMENT_METHODS),
            "order_type": random.choice(ORDER_TYPES),
        })

    return pd.DataFrame(rows)


def main() -> None:
    RAW_DATA_PATH.parent.mkdir(parents=True, exist_ok=True)

    df = generate_orders()
    df.to_csv(RAW_DATA_PATH, index=False)

    print(f"Generated dataset: {RAW_DATA_PATH}")
    print(f"Rows: {len(df):,}")


if __name__ == "__main__":
    main()