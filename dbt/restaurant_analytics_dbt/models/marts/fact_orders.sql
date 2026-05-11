SELECT
    o.order_id,

    d.date_key,
    t.time_key,
    m.menu_item_key,
    s.staff_key,
    p.payment_method_key,
    ot.order_type_key,

    o.quantity,
    o.unit_price,
    o.unit_cost,

    o.discount_rate,

    o.net_revenue,
    o.total_cost,
    o.profit

FROM {{ ref('stg_orders') }} o

LEFT JOIN {{ ref('dim_date') }} d
    ON o.order_date = d.full_date

LEFT JOIN {{ ref('dim_time') }} t
    ON o.order_hour = t.order_hour

LEFT JOIN {{ ref('dim_menu_item') }} m
    ON o.menu_item = m.menu_item
   AND o.category = m.category

LEFT JOIN {{ ref('dim_staff') }} s
    ON o.staff_name = s.staff_name

LEFT JOIN {{ ref('dim_payment_method') }} p
    ON o.payment_method = p.payment_method

LEFT JOIN {{ ref('dim_order_type') }} ot
    ON o.order_type = ot.order_type