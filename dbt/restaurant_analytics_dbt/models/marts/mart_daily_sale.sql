SELECT
    d.full_date,
    d.day_name,
    SUM(f.net_revenue) AS total_revenue,
    SUM(f.total_cost) AS total_cost,
    SUM(f.profit) AS total_profit,
    COUNT(DISTINCT f.order_id) AS total_orders,
    SUM(f.quantity) AS total_items_sold,
    SUM(f.profit) / NULLIF(SUM(f.net_revenue), 0) AS profit_margin
FROM {{ ref('fact_orders') }} f
LEFT JOIN {{ ref('dim_date') }} d
    ON f.date_key = d.date_key
GROUP BY 1, 2
ORDER BY 1