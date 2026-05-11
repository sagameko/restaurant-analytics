SELECT
    ROW_NUMBER() OVER (
        ORDER BY menu_item, category
    ) AS menu_item_key,

    menu_item,
    category

FROM (
    SELECT DISTINCT
        menu_item,
        category
    FROM {{ ref('stg_orders') }}
)