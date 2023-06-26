-- Tworzenie tabeli "Customers"
CREATE TABLE Customers (
    CustomerID INTEGER PRIMARY KEY,
    FirstName TEXT,
    LastName TEXT,
    Email TEXT
);

-- Tworzenie tabeli "Orders"
CREATE TABLE Orders (
    OrderID INTEGER PRIMARY KEY,
    CustomerID INTEGER,
    OrderDate TEXT,
    TotalAmount REAL,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

-- Wstawianie danych do tabeli "Customers"
INSERT INTO Customers (CustomerID, FirstName, LastName, Email)
VALUES (1, 'John', 'Doe', 'john.doe@example.com');

INSERT INTO Customers (CustomerID, FirstName, LastName, Email)
VALUES (2, 'Jane', 'Smith', 'jane.smith@example.com');

-- Wstawianie danych do tabeli "Orders"
INSERT INTO Orders (OrderID, CustomerID, OrderDate, TotalAmount)
VALUES (1, 1, '2023-06-26', 100.00);

INSERT INTO Orders (OrderID, CustomerID, OrderDate, TotalAmount)
VALUES (2, 2, '2023-06-27', 150.00);

-- Pobieranie danych z tabeli "Customers"
SELECT * FROM Customers;

-- Pobieranie danych z tabeli "Orders"
SELECT * FROM Orders;
