SELECT
    ROW_NUMBER() OVER (
        ORDER BY order_type
    ) AS order_type_key,

    order_type

FROM (
    SELECT DISTINCT order_type
    FROM {{ ref('stg_orders') }}
)