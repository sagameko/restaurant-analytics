SELECT
    ROW_NUMBER() OVER (
        ORDER BY staff_name
    ) AS staff_key,

    staff_name

FROM (
    SELECT DISTINCT staff_name
    FROM {{ ref('stg_orders') }}
)