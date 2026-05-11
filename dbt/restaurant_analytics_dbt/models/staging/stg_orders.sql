SELECT
    order_id,

    CAST(order_datetime AS TIMESTAMP) AS order_timestamp,

    CAST(order_datetime AS DATE) AS order_date,

    EXTRACT(hour FROM CAST(order_datetime AS TIMESTAMP))
        AS order_hour,

    customer_name,

    menu_item,
    category,

    quantity,

    CAST(unit_price AS DOUBLE) AS unit_price,
    CAST(unit_cost AS DOUBLE) AS unit_cost,

    CAST(discount_rate AS DOUBLE)
        AS discount_rate,

    CAST(net_revenue AS DOUBLE)
        AS net_revenue,

    CAST(total_cost AS DOUBLE)
        AS total_cost,

    CAST(profit AS DOUBLE) AS profit,

    staff_name,
    payment_method,
    order_type

FROM raw_orders