import sqlite3

conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

# Создаем таблицу сотрудников
cursor.execute('''
CREATE TABLE Employee (
    EmployeeID INTEGER PRIMARY KEY,
    Name TEXT NOT NULL
)
''')

# Создаем таблицу деталей сотрудников (один к одному)
cursor.execute('''
CREATE TABLE EmployeeDetails (
    EmployeeID INTEGER PRIMARY KEY,
    Address TEXT,
    Phone TEXT,
    FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID)
)
''')

# Вставляем несколько сотрудников
cursor.executemany(
    "INSERT INTO Employee (EmployeeID, Name) VALUES (?, ?)",
    [
        (1, 'Alice'),
        (2, 'Bob'),
        (3, 'Carol'),
        (4, 'David'),
        (5, 'Eva')
    ]
)

# Вставляем детали сотрудников
cursor.executemany(
    "INSERT INTO EmployeeDetails (EmployeeID, Address, Phone) VALUES (?, ?, ?)",
    [
        (1, '123 Main St', '555-1234'),
        (2, '234 Maple Ave', '555-2345'),
        (3, '345 Oak Dr', '555-3456'),
        (4, '456 Pine Ln', '555-4567'),
        (5, '567 Cedar Rd', '555-5678')
    ]
)

conn.commit()



cursor.execute('''
SELECT e.EmployeeID, e.Name, d.Address, d.Phone
FROM Employee e
JOIN EmployeeDetails d ON e.EmployeeID = d.EmployeeID
ORDER BY e.EmployeeID
''')


results = cursor.fetchall()
for r in results:
    print(r)

conn.close()