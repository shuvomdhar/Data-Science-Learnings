SELECT * FROM products ;

CREATE VIEW available_fitness_products AS
SELECT product_id, name, price, stock_quantity
FROM products
WHERE category = 'Accessories' AND is_available = TRUE;

SELECT * FROM available_fitness_products ;

CREATE VIEW low_stock_products AS
SELECT name, category, stock_quantity
FROM products
WHERE stock_quantity < 30;

SELECT * FROM low_stock_products;

CREATE PROCEDURE add_product(
    p_name VARCHAR,
    p_sku CHAR(8),
    p_price NUMERIC,
    p_qty INT,
    p_category TEXT
)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO products(name, sku_code, price, stock_quantity, category)
    VALUES (p_name, p_sku, p_price, p_qty, p_category);

    RAISE NOTICE 'Product added successfully!';
END;
$$;

CALL add_product('Bottle', 'bo123467', 234.00, 45, 'Fitness');
