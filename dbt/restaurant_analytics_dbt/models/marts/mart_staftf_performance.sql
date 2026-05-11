SELECT
    s.staff_name,
    SUM(f.net_revenue) AS total_revenue,
    SUM(f.profit) AS total_profit,
    COUNT(DISTINCT f.order_id) AS total_orders,
    SUM(f.quantity) AS total_items_sold,
    SUM(f.net_revenue) / NULLIF(COUNT(DISTINCT f.order_id), 0) AS average_order_value
FROM {{ ref('fact_orders') }} f
LEFT JOIN {{ ref('dim_staff') }} s
    ON f.staff_key = s.staff_key
GROUP BY 1
ORDER BY total_revenue DESC