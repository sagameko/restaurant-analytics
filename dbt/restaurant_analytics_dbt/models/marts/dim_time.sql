SELECT
    ROW_NUMBER() OVER (
        ORDER BY order_hour
    ) AS time_key,

    order_hour,

    CASE
        WHEN order_hour < 12 THEN 'Morning'
        WHEN order_hour < 17 THEN 'Afternoon'
        ELSE 'Evening'
    END AS time_period

FROM (
    SELECT DISTINCT order_hour
    FROM {{ ref('stg_orders') }}
)