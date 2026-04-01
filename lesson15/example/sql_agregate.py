import sqlite3

# Создаём и подключаемся к базе в памяти
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

# Создаём таблицу sales
cursor.execute('''
CREATE TABLE sales (
    sale_id INTEGER PRIMARY KEY,
    product_id INTEGER,
    quantity INTEGER,
    price REAL,
    sale_date TEXT
)
''')

# Вставляем несколько строк (примерные данные)
sales_data = [
    (1, 1, 10, 5.0, '2025-07-01'),
    (2, 2, 5, 10.0, '2025-07-02'),
    (3, 1, 15, 5.0, '2025-07-03'),
    (4, 3, 8, 7.5, '2025-07-04'),
    (5, 2, 12, 10.0, '2025-07-05')
]
cursor.executemany('INSERT INTO sales VALUES (?, ?, ?, ?, ?)', sales_data)
conn.commit()

# cursor.execute("""
# SELECT sale_date, product_id, min(price), max(price)
# FROM sales
# GROUP BY sale_date, product_id
# """)


# cursor.execute("""
# SELECT  sale_date, product_id, min(price), max(price)
# FROM sales
# GROUP BY sale_date, product_id
# HAVING min(price) < 7
# """)

cursor.execute('''
SELECT
    product_id,
    SUM(quantity) AS total_quantity,
    SUM(quantity * price) AS total_revenue,
    AVG(quantity * price) AS average_revenue_per_sale,
    MIN(quantity) AS min_quantity,
    MAX(quantity) AS max_quantity,
    COUNT(*) AS sales_count
FROM sales
GROUP BY product_id
ORDER BY product_id;
''')






# Вывод результата
rows = cursor.fetchall()
print(f"{'ProductID':>9} | {'TotalQty':>8} | {'TotalRevenue':>12} | {'AvgRevenue':>11} | {'MinQty':>6} | {'MaxQty':>6} | {'SalesCount':>10}")
print('-'*76)
for row in rows:
    print(f"{row[0]:9d} | {row[1]:8d} | {row[2]:12.2f} | {row[3]:11.2f} | {row[4]:6d} | {row[5]:6d} | {row[6]:10d}")

conn.close()


rows = cursor.fetchall()
for row in rows:
    print(row)