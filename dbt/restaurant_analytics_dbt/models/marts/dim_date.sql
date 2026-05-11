SELECT
    ROW_NUMBER() OVER (
        ORDER BY order_date
    ) AS date_key,

    order_date AS full_date,

    EXTRACT(year FROM order_date) AS year,
    EXTRACT(month FROM order_date) AS month,
    EXTRACT(day FROM order_date) AS day,
    DAYNAME(order_date) AS day_name,

    DATE_TRUNC('month', order_date)
        AS month_start

FROM (
    SELECT DISTINCT order_date
    FROM {{ ref('stg_orders') }}
)