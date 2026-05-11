from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]

if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

import duckdb
import pandas as pd
import streamlit as st

from ml.predict import predict_revenue


# =========================
# Page config
# =========================

st.set_page_config(
    page_title="Restaurant Analytics",
    layout="wide"
)


# =========================
# Database connection
# =========================

DATABASE_PATH = Path(
    "database/restaurant_warehouse.duckdb"
)

conn = duckdb.connect(str(DATABASE_PATH))


# =========================
# Load warehouse marts
# =========================

daily_sales_df = conn.execute("""
    SELECT *
    FROM mart_daily_sale
""").df()

menu_df = conn.execute("""
    SELECT *
    FROM mart_menu_performance
""").df()

staff_df = conn.execute("""
    SELECT *
    FROM mart_staftf_performance
""").df()

order_type_df = conn.execute("""
    SELECT
        ot.order_type,
        SUM(f.net_revenue) AS total_revenue,
        COUNT(*) AS total_orders
    FROM fact_orders f
    LEFT JOIN dim_order_type ot
        ON f.order_type_key = ot.order_type_key
    GROUP BY 1
    ORDER BY total_revenue DESC
""").df()

payment_df = conn.execute("""
    SELECT
        p.payment_method,
        SUM(f.net_revenue) AS total_revenue,
        COUNT(*) AS total_orders
    FROM fact_orders f
    LEFT JOIN dim_payment_method p
        ON f.payment_method_key = p.payment_method_key
    GROUP BY 1
    ORDER BY total_revenue DESC
""").df()


# =========================
# Dashboard title
# =========================

st.title("Restaurant Analytics Dashboard")


# =========================
# KPI section
# =========================

total_revenue = daily_sales_df[
    "total_revenue"
].sum()

total_profit = daily_sales_df[
    "total_profit"
].sum()

total_orders = daily_sales_df[
    "total_orders"
].sum()

profit_margin = (
    total_profit / total_revenue
) * 100


col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Revenue",
    f"${total_revenue:,.2f}"
)

col2.metric(
    "Total Profit",
    f"${total_profit:,.2f}"
)

col3.metric(
    "Total Orders",
    f"{int(total_orders):,}"
)

col4.metric(
    "Profit Margin",
    f"{profit_margin:.2f}%"
)


st.divider()


# =========================
# Daily revenue trend
# =========================

st.subheader("Daily Revenue Trend")

daily_chart = daily_sales_df.set_index(
    "full_date"
)["total_revenue"]

st.line_chart(daily_chart)


# =========================
# Menu performance
# =========================

st.subheader("Top Menu Items")

top_menu_df = menu_df.head(10)

st.dataframe(
    top_menu_df,
    use_container_width=True
)

menu_chart_df = top_menu_df.set_index(
    "menu_item"
)["total_revenue"]

st.bar_chart(menu_chart_df)


# =========================
# Staff performance
# =========================

st.subheader("Staff Performance")

st.dataframe(
    staff_df,
    use_container_width=True
)

staff_chart_df = staff_df.set_index(
    "staff_name"
)["total_revenue"]

st.bar_chart(staff_chart_df)


# =========================
# Order type breakdown
# =========================

st.subheader("Order Type Breakdown")

col5, col6 = st.columns(2)

with col5:
    st.dataframe(
        order_type_df,
        use_container_width=True
    )

with col6:
    order_type_chart = order_type_df.set_index(
        "order_type"
    )["total_revenue"]

    st.bar_chart(order_type_chart)


# =========================
# Payment method breakdown
# =========================

st.subheader("Payment Method Breakdown")

col7, col8 = st.columns(2)

with col7:
    st.dataframe(
        payment_df,
        use_container_width=True
    )

with col8:
    payment_chart = payment_df.set_index(
        "payment_method"
    )["total_revenue"]

    st.bar_chart(payment_chart)

# =========================
# Revenue Forecasting
# =========================

st.divider()

st.subheader("Revenue Forecast Prediction")

col9, col10 = st.columns(2)

with col9:

    forecast_day = st.slider(
        "Day of Month",
        1,
        31,
        15
    )

    forecast_month = st.selectbox(
        "Month",
        list(range(1, 13)),
        index=5
    )

    forecast_day_of_week = st.selectbox(
        "Day of Week",
        {
            0: "Monday",
            1: "Tuesday",
            2: "Wednesday",
            3: "Thursday",
            4: "Friday",
            5: "Saturday",
            6: "Sunday"
        }
    )

with col10:

    forecast_orders = st.slider(
        "Expected Orders",
        20,
        300,
        100
    )

    forecast_items = st.slider(
        "Expected Items Sold",
        20,
        600,
        200
    )

    prediction = predict_revenue(
        day_of_week=forecast_day_of_week,
        month=forecast_month,
        day=forecast_day,
        total_orders=forecast_orders,
        total_items_sold=forecast_items
    )

    st.metric(
        "Predicted Revenue",
        f"${prediction:,.2f}"
    )


conn.close()