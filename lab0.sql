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
