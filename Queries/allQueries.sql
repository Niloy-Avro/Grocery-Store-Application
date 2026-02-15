CREATE DATABASE GroceryStore;
USE GroceryStore;
-- creating products table
CREATE TABLE products (
	product_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    uom_id INT,
    price_per_unit DECIMAL(10, 2) NOT NULL
);

-- entering product without mentioning ID
INSERT INTO products (name, uom_id, price_per_unit) VALUES
('Rice', 2, 45.50),
('Sugar', 2, 42.00),
('Milk', 1, 28.00),
('Salt', 3, 1.20);
-- entering product mentioning ID
INSERT INTO products VALUES(5, 'Rice', 2, 45.50);
INSERT INTO products VALUES(6, 'Peanut', 2, 45.50);
INSERT INTO products VALUES(7, 'Chocolate', 1, 12.50);
INSERT INTO products VALUES(8, 'Flower', 1, 5.50);
INSERT INTO products VALUES(9, 'Brown Sugar', 2, 50.50);

SET SQL_SAFE_UPDATES = 0;
UPDATE products 
SET name = 'Milk Packet'
WHERE name = 'Milk'; 
SET SQL_SAFE_UPDATES = 1;

SELECT * FROM PRODUCTS;

-- creating uom table
CREATE TABLE uom (
	uom_id INT PRIMARY KEY AUTO_INCREMENT,
    uom_name VARCHAR(45) NOT NULL
);
INSERT INTO uom (uom_name) VALUES -- as uom_id is autoIncrement
('each piece'),
('kg'),
('gram');

SELECT * FROM uom;

-- making the uom_id of products table foreign key 
ALTER TABLE products
ADD CONSTRAINT fk_uom_id
FOREIGN KEY (uom_id)
REFERENCES uom(uom_id);

SELECT * FROM products;

-- creating order table
CREATE TABLE orders (
 order_id INT PRIMARY KEY AUTO_INCREMENT,
 customer_name VARCHAR(100) NOT NULL,
 total DECIMAL(10,2) NOT NULL,
 dateTime DATETIME DEFAULT CURRENT_TIMESTAMP
);

SELECT * FROM orders;

-- creating order_details table
CREATE TABLE order_details (
	order_id INT NOT NULL ,
    product_id INT NOT NULL,
    quantity DECIMAL(10, 2) NOT NULL,
    total_price DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (order_id, product_id),
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
	FOREIGN KEY (product_id) REFERENCES products(product_id)
);

SELECT * FROM order_details;

