CREATE TABLE products (
	Product_ID serial primary key,
	Name varchar(100) not null,
	Sku_code char(8) unique not null,
	Price numeric(10, 2) check (Price>0),
	Stock_quantity int default 0 check (Stock_quantity>=0),
	Is_available boolean default true,
	Category text not null,
	Added_on date default current_date,
	Last_updated timestamp default now()
);

INSERT INTO products (Name, Sku_code, Price, Stock_quantity, Is_available, Category)
VALUES
('Wireless Mouse', 'WM123456', 599.00, 120, true, 'Electronics'),
('Bluetooth Headphones', 'BH789012', 1499.00, 75, true, 'Electronics'),
('Mechanical Keyboard', 'MK345678', 2999.00, 40, true, 'Electronics'),
('USB-C Charger 25W', 'UC901234', 899.00, 200, false, 'Accessories'),
('Laptop Stand', 'LS567890', 999.00, 55, true, 'Office Supplies'),
('Smart LED Bulb', 'SB432109', 499.00, 180, true, 'Home Automation'),
('Fitness Tracker Band', 'FT654321', 1999.00, 60, false, 'Wearables'),
('Gaming Monitor 27"', 'GM876543', 15999.00, 15, true, 'Electronics'),
('Portable SSD 1TB', 'PS109876', 6999.00, 25, true, 'Storage Devices'),
('Smartphone Case', 'SC210987', 299.00, 500, true, 'Accessories'),
('Noise Cancelling Earbuds', 'NE321098', 3499.00, 35, true, 'Electronics'),
('Wireless Router AX1500', 'WR432187', 2499.00, 28, true, 'Networking'),
('HDMI Cable 2m', 'HC543276', 249.00, 300, true, 'Accessories'),
('Electric Kettle', 'EK654365', 899.00, 70, true, 'Home Appliances'),
('Desk Lamp', 'DL765454', 699.00, 90, true, 'Home Decor'),
('USB Flash Drive 64GB', 'UF876543', 599.00, 150, true, 'Storage Devices'),
('Laptop Backpack', 'LB987632', 1499.00, 45, false, 'Travel Accessories'),
('Smartwatch', 'SW098721', 4999.00, 30, true, 'Wearables'),
('Bluetooth Speaker', 'BS123789', 1899.00, 55, true, 'Audio'),
('Power Bank 20000mAh', 'PB456912', 1599.00, 80, true, 'Accessories');

SELECT * FROM products;

DELETE FROM products;

SELECT Name, Price FROM products;

SELECT * FROM products WHERE Category='Electronics';

SELECT Category FROM products GROUP BY Category;

SELECT Category, COUNT(*) FROM products GROUP BY Category HAVING COUNT(*) > 1;

SELECT Name, Price FROM products ORDER BY Price ASC;

SELECT * FROM products LIMIT 3;

SELECT Name AS Item_Name, Price AS Item_Price FROM products;

SELECT DISTINCT Category FROM products;

SELECT * FROM products WHERE Category != 'Electronics';

SELECT * FROM products WHERE Price > 1000;

SELECT * FROM products WHERE Price < 1000;

SELECT * FROM products WHERE Price < 1000 and Category = 'Accessories';

SELECT * FROM products WHERE Price < 1000 and Price > 500;

SELECT * FROM products WHERE Price BETWEEN 700 AND 1000;

SELECT * FROM products WHERE Category = 'Accessories' OR Category = 'Home Appliances';

SELECT * FROM products WHERE Category IN ('Audio', 'Home Appliances', 'Travel Accessories');

SELECT * FROM products WHERE Sku_code LIKE 'W%';

SELECT * FROM products WHERE Sku_code LIKE '%123%';

SELECT * FROM products WHERE Sku_code LIKE '_B%';

SELECT * FROM products WHERE NOT Category = 'Electronics';

SELECT COUNT(Product_ID) FROM products;

SELECT SUM(Price) FROM products;

SELECT SUM(Price) FROM products WHERE Category = 'Electronics';

SELECT Category, SUM(Price) FROM products GROUP BY Category;

SELECT ROUND(AVG(Price), 2) FROM products;

SELECT MIN(Price) FROM products;

SELECT MAX(Price) FROM products;

SELECT Name, Price FROM products WHERE Price = (SELECT MIN(Price) FROM products);

SELECT Category, AVG(Price) AS Average_price FROM products WHERE Category IN ('Home Appliances', 'Accessories') GROUP BY Category;

SELECT Name, Stock_quantity FROM products WHERE Is_available = true AND Stock_quantity > 50 AND Price != 299;

SELECT Category, MAX(Price) AS Max_price FROM products GROUP BY Category;

SELECT DISTINCT UPPER(Category) AS Category_name FROM products ORDER BY Category_name DESC;

SELECT UPPER(Name) FROM products;

SELECT LOWER(Name) FROM products;

SELECT LENGTH(Name) FROM products;

SELECT SUBSTRING('Brother in arms', 1, 7);

SELECT Name, SUBSTRING(Sku_code, 1, 2) FROM products;

SELECT Name, LEFT(Sku_code, 2) FROM products;

SELECT Name, RIGHT(Sku_code, 6) FROM products;

SELECT CONCAT(Name, ' - ', Category) FROM products;

SELECT CONCAT_WS(' - ', Name, Category, Sku_code) FROM products;

SELECT TRIM(Name) FROM products;

SELECT REPLACE(Sku_code, LEFT(Sku_code, 2), 'GG') FROM products;



-- CASE
SELECT Name, Price,
CASE WHEN (Price > 1000) THEN 'Expensive'
     WHEN Price BETWEEN 500 AND 1000 THEN 'Moderate'
	 ELSE 'Cheap'
END AS Price_tag FROM products;

SELECT * FROM products;

ALTER TABLE products ADD COLUMN Price_tag TEXT;

UPDATE products
SET Price_tag = 
CASE WHEN (Price > 1000) THEN 'Expensive'
     WHEN Price BETWEEN 500 AND 1000 THEN 'Moderate'
	 ELSE 'Cheap'
END;

ALTER TABLE products ADD COLUMN Availability BOOLEAN;

UPDATE products
SET Availability = 
CASE WHEN Is_available = TRUE THEN 'In Stock'
     WHEN Is_available = FALSE THEN 'Out of Stock'
END;

ALTER TABLE products ALTER COLUMN Availability TYPE TEXT;

SELECT Stock_quantity,
CASE WHEN (Stock_quantity > 100) THEN 'High Stock'
     WHEN Stock_quantity BETWEEN 30 AND 100 THEN 'Medium Stock'
	 ELSE 'Low Stock'
END AS Stock_level FROM products;
