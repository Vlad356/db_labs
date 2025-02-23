-- 1. Створення таблиці Products
CREATE TABLE Products (
    product_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    category VARCHAR(100) NOT NULL,
    price DECIMAL(10, 2) NOT NULL
);

-- 2. Створення таблиці Customers
CREATE TABLE Customers (
    customer_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    city VARCHAR(100) NOT NULL
);

-- 3. Створення таблиці Orders
CREATE TABLE Orders (
    order_id SERIAL PRIMARY KEY,
    customer_id INT,
    product_id INT,
    quantity INT NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id),
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
);



-- Заповнення таблиці Customers
INSERT INTO Customers (name, city) VALUES
('John Doe', 'New York'),
('Jane Smith', 'Los Angeles'),
('Bob Johnson', 'New York'),
('Alice Brown', 'Los Angeles');

-- Заповнення таблиці Products
INSERT INTO Products (name, category, price) VALUES
('Laptop', 'Electronics', 699.99),
('Smartphone', 'Electronics', 209.99),
('Headphones', 'Electronics', 190.00),
('Mouse', 'Electronics', 29.99),
('Keyboard', 'Electronics', 49.99);

-- Заповнення таблиці Orders
INSERT INTO Orders (customer_id, product_id, quantity) VALUES
(1, 1, 2),  -- John Doe купив Laptop (2 шт.)
(1, 2, 1),  -- John Doe купив Smartphone (1 шт.)
(2, 1, 1),  -- Jane Smith купила Laptop (1 шт.)
(3, 3, 3),  -- Jane Smith купила Smartphone (2 шт.)
(2, 2, 2);  -- Bob Johnson купив Headphones (3 шт.)

/* Tests(1)
SELECT 
    p.category,
    COUNT(o.order_id) as total_orders,
    SUM(o.quantity) as total_quantity,
    ROUND(AVG(p.price * o.quantity), 2) as avg_order_value
FROM Products p
JOIN Orders o ON p.product_id = o.product_id
GROUP BY p.category;

/* Очікуваний результат:
category    | total_orders | total_quantity | avg_order_value
Electronics | 5           | 9              | 659.99
*/

-- 2. Перетин таблиці з собою
-- Запит 2: Знайти пари клієнтів з одного міста
SELECT 
    c1.name as customer1,
    c2.name as customer2,
    c1.city
FROM Customers c1
JOIN Customers c2 ON c1.city = c2.city AND c1.customer_id < c2.customer_id;

/* Очікуваний результат:
customer1   | customer2    | city
(якщо є клієнти з одного міста, вони будуть показані попарно)
на ваш вибір 2 строчки
*/

-- 3. Різні типи JOIN
-- Запит 3: Показати всі продукти та їх замовлення (включаючи ті, що не мають замовлень)
SELECT 
    p.name as product_name,
    COALESCE(COUNT(o.order_id), 0) as orders_count,
    COALESCE(SUM(o.quantity), 0) as total_quantity
FROM Products p
LEFT JOIN Orders o ON p.product_id = o.product_id
GROUP BY p.name;

/* Очікуваний результат:
product_name | orders_count | total_quantity
Laptop      | 2           | 3
Smartphone  | 2           | 3
Headphones  | 1           | 3
Mouse       | 0           | 0
Keyboard    | 0           | 0
*/

-- Запит 4: Повне об'єднання клієнтів та їх замовлень
SELECT 
    c.name,
    o.order_id,
    p.name as product_name,
    o.quantity
FROM Customers c
LEFT JOIN Orders o ON c.customer_id = o.customer_id
LEFT JOIN Products p ON o.product_id = p.product_id
UNION ALL
SELECT 
    c.name,
    o.order_id,
    p.name as product_name,
    o.quantity
FROM Orders o
RIGHT JOIN Customers c ON c.customer_id = o.customer_id
RIGHT JOIN Products p ON o.product_id = p.product_id
WHERE c.customer_id IS NULL;

/* Очікуваний результат:
name        | order_id | product_name | quantity
John Doe    | 1        | Laptop      | 2
John Doe    | 2        | Smartphone  | 1
Jane Smith  | 3        | Laptop      | 1
Jane Smith  | 5        | Smartphone  | 2
Bob Johnson | 4        | Headphones  | 3
NULL        | NULL     | Keyboard    | NULL
NULL        | NULL     | Mouse       | NULL
*/

