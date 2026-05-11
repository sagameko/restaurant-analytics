SELECT
    m.menu_item,
    m.category,
    SUM(f.quantity) AS total_quantity_sold,
    SUM(f.net_revenue) AS total_revenue,
    SUM(f.total_cost) AS total_cost,
    SUM(f.profit) AS total_profit,
    SUM(f.profit) / NULLIF(SUM(f.net_revenue), 0) AS profit_margin,
    COUNT(DISTINCT f.order_id) AS total_orders
FROM {{ ref('fact_orders') }} f
LEFT JOIN {{ ref('dim_menu_item') }} m
    ON f.menu_item_key = m.menu_item_key
GROUP BY 1, 2
ORDER BY total_revenue DESC