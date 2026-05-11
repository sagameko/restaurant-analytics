SELECT
    ROW_NUMBER() OVER (
        ORDER BY payment_method
    ) AS payment_method_key,

    payment_method

FROM (
    SELECT DISTINCT payment_method
    FROM {{ ref('stg_orders') }}
)