import sqlite3

conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

# Таблица отделов
cursor.execute('''
CREATE TABLE Department (
    DepartmentID INTEGER PRIMARY KEY,
    Name TEXT NOT NULL
)
''')

# Таблица сотрудников с внешним ключом на отдел
cursor.execute('''
CREATE TABLE Employee (
    EmployeeID INTEGER PRIMARY KEY,
    Name TEXT NOT NULL,
    DepartmentID INTEGER,
    FOREIGN KEY (DepartmentID) REFERENCES Department(DepartmentID)
)
''')

# Вставляем отделы
cursor.executemany(
    "INSERT INTO Department (DepartmentID, Name) VALUES (?, ?)",
    [
        (1, 'HR'),
        (2, 'Finance'),
        (3, 'IT'),
        (4, 'Marketing')
    ]
)

# Вставляем сотрудников с привязкой к отделам
cursor.executemany(
    "INSERT INTO Employee (EmployeeID, Name, DepartmentID) VALUES (?, ?, ?)",
    [
        (1, 'Bob', 1),
        (2, 'Carol', 1),
        (3, 'Dave', 2),
        (4, 'Eva', 3),
        (5, 'Frank', 3),
        (6, 'Grace', 4),
        (7, 'Hank', 4)
    ]
)

conn.commit()


cursor.execute('''
SELECT e.EmployeeID, e.Name, d.Name AS DepartmentName
FROM Employee e
JOIN Department d ON e.DepartmentID = d.DepartmentID
ORDER BY d.DepartmentID, e.EmployeeID
''')

results = cursor.fetchall()
for r in results:
    print(r)

conn.close()