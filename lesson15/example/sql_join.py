
# INNER JOIN	Возвращает только те строки, которые имеют совпадения в обеих таблицах 
#               по условию соединения. Это наиболее часто используемый тип. 
#               Вернёт пересечение таблиц.
# LEFT JOIN (или LEFT OUTER JOIN)	Возвращает все строки из левой таблицы и совпадающие 
#               строки из правой. Если совпадений нет, в столбцах правой таблицы будут NULL.
# RIGHT JOIN (или RIGHT OUTER JOIN)	Возвращает все строки из правой таблицы и совпадающие 
#               из левой. Если совпадений нет, столбцы левой таблицы будут NULL.
# FULL JOIN (или FULL OUTER JOIN)	Возвращает все строки из обеих таблиц, объединяя совпадения, 
#               а для отсутствующих значений подставляет NULL. Покрывает все случаи с обеих сторон.
# CROSS JOIN	Выполняет декартово произведение таблиц — каждая строка первой таблицы соединяется 
#               с каждой строкой второй, без условия соединения.
# SELF JOIN	Соединение таблицы самой с собой, используется для сравнения строк внутри одной таблицы. 
#               Это способ использовать JOIN, когда обе таблицы — одна и та же.

# левая та таблица которая после FROM



import sqlite3

# Создаём соединение с БД в памяти (или укажите имя файла)
conn = sqlite3.connect(':memory:')
cur = conn.cursor()

# Создаём таблицы
cur.execute('''
CREATE TABLE employees (
  employee_id INTEGER PRIMARY KEY,
  name TEXT,
  department_id INTEGER
)
''')

cur.execute('''
CREATE TABLE departments (
  department_id INTEGER PRIMARY KEY,
  department_name TEXT
)
''')

# Вставляем данные в таблицы
cur.executemany('INSERT INTO employees VALUES (?, ?, ?)', [
    (1, 'Alice', 10),
    (2, 'Bob', 20),
    (3, 'Charlie', None),
    (4, 'David', 30)
])

cur.executemany('INSERT INTO departments VALUES (?, ?)', [
    (10, 'HR'),
    (20, 'Finance'),
    (40, 'Marketing')
])

conn.commit()

# 1. INNER JOIN — только сотрудники с существующим отделом defolt
print('INNER JOIN:')
cur.execute('''
SELECT e.name, d.department_name
FROM employees e
INNER JOIN departments d ON e.department_id = d.department_id
''')
for row in cur.fetchall():
    print(row)
# Вывод: ('Alice', 'HR'), ('Bob', 'Finance')

# 2. LEFT JOIN — все сотрудники + отделы или NULL, если отдела нет
print('\nLEFT JOIN:')
cur.execute('''
SELECT e.name, d.department_name
FROM employees e
LEFT JOIN departments d ON e.department_id = d.department_id
''')
for row in cur.fetchall():
    print(row)
# Вывод: ('Alice', 'HR'), ('Bob', 'Finance'), ('Charlie', None), ('David', None)

# 3. CROSS JOIN — декартово произведение сотрудников и отделов
print('\nCROSS JOIN:')
cur.execute('''
SELECT e.name, d.department_name
FROM employees e
CROSS JOIN departments d
''')
for row in cur.fetchall():
    print(row)
# Выведет все пары (4 сотрудников × 3 отдела = 12 рядов)

# 4. SELF JOIN — поиск сотрудников из одного отдела (кроме самого себя)
print('\nSELF JOIN (сотрудники в одном отделе):')
cur.execute('''
SELECT e1.name AS emp1, e2.name AS emp2, e1.department_id
FROM employees e1
INNER JOIN employees e2 
  ON e1.department_id = e2.department_id
  AND e1.employee_id != e2.employee_id
''')
for row in cur.fetchall():
    print(row)
# Вывод в нашем примере пустой, т.к. нет сотрудника с совпадающим department_id кроме себя

conn.close()
