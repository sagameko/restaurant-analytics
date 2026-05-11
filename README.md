![Python](https://img.shields.io/badge/Python-3.11-blue)
![dbt](https://img.shields.io/badge/dbt-Analytics-orange)
![DuckDB](https://img.shields.io/badge/DuckDB-Warehouse-yellow)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)
![CI](https://github.com/YOUR_USERNAME/YOUR_REPO/actions/workflows/restaurant_ci.yml/badge.svg)

# Restaurant Analytics Platform

A personal analytics engineering and business intelligence project built to improve my practical experience with data warehousing, dbt, machine learning, dashboard development, and modern data workflows.

The goal of this project is to simulate how restaurant operational data can be transformed into a structured analytics platform for reporting, performance tracking, and forecasting.

This project was designed based on real restaurant operations and business scenarios that I observed while working in the hospitality industry.

---

# Project Objectives

The project focuses on building a complete end-to-end analytics workflow including:

- raw data ingestion
- warehouse modeling
- dbt transformations
- star schema design
- analytics marts
- interactive dashboarding
- machine learning forecasting
- CI/CD automation

Rather than only building visual dashboards, the project aims to simulate a more realistic analytics engineering environment.

---

# Tech Stack

| Area | Technology |
|---|---|
| Programming | Python |
| Data Processing | Pandas |
| Warehouse | DuckDB |
| Transformation Layer | dbt |
| Dashboard | Streamlit |
| Machine Learning | Scikit-learn |
| Version Control | Git & GitHub |
| CI/CD | GitHub Actions |

---

# Project Architecture

```text
Synthetic Restaurant Data
            ↓
Python Data Ingestion
            ↓
DuckDB Warehouse
            ↓
dbt Transformations
            ↓
Star Schema Warehouse
            ↓
Analytics Marts
            ↓
Streamlit Dashboard
            ↓
Machine Learning Forecasting
            ↓
GitHub Actions CI/CD
```

---

# Warehouse Design

The warehouse follows a star schema design.

## Fact Table

### `fact_orders`

Contains restaurant transactional metrics including:
- revenue
- profit
- quantity sold
- pricing
- discount information

---

## Dimension Tables

### `dim_date`
Date hierarchy and calendar attributes.

### `dim_time`
Order hour and time period segmentation.

### `dim_menu_item`
Menu item and category information.

### `dim_staff`
Restaurant staff information.

### `dim_payment_method`
Payment method details.

### `dim_order_type`
Dine-in, takeaway, and delivery order classifications.

---

# Analytics Marts

## `mart_daily_sales`

Daily restaurant KPIs including:
- revenue
- profit
- total orders
- total items sold
- profit margin

---

## `mart_menu_performance`

Menu-level business performance including:
- top-selling items
- most profitable products
- category analysis

---

## `mart_staff_performance`

Staff-level metrics including:
- revenue handled
- order counts
- average order value

---

# Machine Learning Forecasting

The project includes a machine learning component for restaurant revenue forecasting.

A Random Forest Regressor model is trained using historical restaurant metrics to estimate future revenue based on:
- expected orders
- items sold
- seasonality
- day of week

The prediction system is integrated directly into the Streamlit dashboard.

---

# Dashboard Features

The Streamlit dashboard includes:

- executive KPI overview
- revenue trend analysis
- menu performance tracking
- staff performance analysis
- order type breakdown
- payment method analysis
- machine learning revenue prediction

---

# CI/CD

GitHub Actions is used to automatically validate the project on every push.

The workflow currently:
- installs dependencies
- generates synthetic restaurant data
- runs the ingestion pipeline
- executes dbt models
- runs dbt tests
- trains the machine learning model

This helps simulate a more production-style analytics engineering workflow.

---

# Project Structure

```text
restaurant-analytics/
│
├── .github/
│   └── workflows/
│       └── restaurant_ci.yml
│
├── app/
│   └── dashboard.py
│
├── data/
│   └── raw/
│
├── database/
│
├── dbt/
│   └── restaurant_analytics_dbt/
│
├── docs/
│   └── screenshots/
│
├── ml/
│   ├── models/
│   ├── predict.py
│   └── train_model.py
│
├── src/
│   ├── generate_data.py
│   ├── load.py
│   └── logger.py
│
├── testing/
│
├── main.py
├── requirements.txt
└── README.md
```

---

# Running The Project

## Clone Repository

```bash
git clone <repository-url>
cd restaurant-analytics
```

---

## Create Environment

```bash
conda create -n restaurant_analytics python=3.11
conda activate restaurant_analytics
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Generate Dataset

```bash
python src/generate_data.py
```

---

## Run Data Pipeline

```bash
python main.py
```

---

## Run dbt Models

```bash
cd dbt/restaurant_analytics_dbt

dbt run
dbt test
```

---

## Train Machine Learning Model

```bash
python ml/train_model.py
```

---

## Launch Dashboard

```bash
streamlit run app/dashboard.py
```

---

# Screenshots

Dashboard screenshots can be found in:

```text
docs/screenshots/
```

---

# What I Learned From This Project

Through this project I practiced:
- warehouse design
- dbt workflows
- analytics engineering concepts
- SQL modeling
- data quality testing
- CI/CD pipelines
- dashboard development
- machine learning integration
- project structuring for production-style workflows

The project also helped me better understand how business reporting systems are structured outside of notebook-based data science projects.

---

# Future Improvements

Potential future improvements include:
- Docker containerization
- cloud deployment
- Snowflake migration
- real restaurant POS integration
- customer segmentation models
- demand forecasting improvements
- automated reporting pipelines
- Power BI integration
