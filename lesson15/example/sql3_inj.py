#!/usr/bin/env python3
"""
SQL Инъекция: создание таблицы → уязвимый код → атака → защита
"""

import sqlite3
from contextlib import contextmanager

# 1. СОЗДАНИЕ ТАБЛИЦЫ И НАПОЛНЕНИЕ
@contextmanager
def get_db():
    conn = sqlite3.connect(':memory:')  # В памяти для демо
    try:
        yield conn
    finally:
        conn.close()

def create_users_table(conn):
    """Создаёт таблицу users с тестовыми данными"""
    cursor = conn.cursor()
    
    # Создаём таблицу
    cursor.execute('''
        CREATE TABLE users (
            id INTEGER PRIMARY KEY,
            username TEXT UNIQUE,
            password TEXT,
            role TEXT
        )
    ''')
    
    # Наполняем тестовыми пользователями
    users = [
        ('admin', 'admin123', 'administrator'),
        ('user1', 'pass123', 'user'),
        ('guest', 'guest', 'guest'),
    ]
    
    cursor.executemany(
        'INSERT INTO users (username, password, role) VALUES (?, ?, ?)', 
        users
    )
    
    conn.commit()
    print("✅ Таблица users создана с 3 пользователями")
    print("👑 admin:admin123 | 👤 user1:pass123 | 👤 guest:guest")

# 2. УЯЗВИМЫЙ КОД (конкатенация строк)
def vulnerable_login(conn, username, password):
    """❌ УЯЗВИМЫЙ! Конкатенация строк"""
    cursor = conn.cursor()
    
    # НЕБЕЗОПАСНО!
    query = f"""
        SELECT * FROM users 
        WHERE username='{username}' AND password='{password}'
    """
    
    print(f"🔴 Уязвимый запрос: {query}")
    cursor.execute(query)
    result = cursor.fetchone()
    
    if result:
        return f"✅ Логин: {result[1]} | Роль: {result[3]}"
    return "❌ Доступ запрещён"

# 3. БЕЗОПАСНЫЙ КОД (параметры)
def safe_login(conn, username, password):
    """✅ БЕЗОПАСНЫЙ! Параметризованный запрос"""
    cursor = conn.cursor()
    
    # ПАРАМЕТРЫ вместо конкатенации!
    query = """
        SELECT * FROM users 
        WHERE username=? AND password=?
    """
    
    print(f"🟢 Безопасный запрос: {query} (параметры: '{username}', '{password}')")
    cursor.execute(query, (username, password))
    result = cursor.fetchone()
    
    if result:
        return f"✅ Логин: {result[1]} | Роль: {result[3]}"
    return "❌ Доступ запрещён"

# 4. ДЕМО АТАКИ
def demo_attack():
    with get_db() as conn:
        create_users_table(conn)
        
        print("\n" + "="*60)
        print("📱 НОРМАЛЬНЫЙ ЛОГИН")
        print("="*60)
        
        # Нормальный логин
        print(vulnerable_login(conn, 'user1', 'pass123'))
        
        print("\n" + "="*60)
        print("💥 SQL ИНЪЕКЦИЯ")
        print("="*60)
        
        # ИНЪЕКЦИЯ: Обход авторизации
        payload = "admin' OR '1'='1' --"
        print(vulnerable_login(conn, payload, 'что угодно'))
        # Результат: ЛОГИН АДМИНОМ!
        
        print("\n" + "="*60)
        print("🛡️ БЕЗОПАСНЫЙ КОД")
        print("="*60)
        
        # Тот же payload на безопасном коде
        print(safe_login(conn, payload, 'что угодно'))
        # Результат: ❌ Доступ запрещён
        
        print("\n" + "="*60)
        print("💀 ОПАСНЫЕ ИНЪЕКЦИИ")
        print("="*60)
        
        # DROP TABLE (если бы была запись)
        drop_payload = "'; DROP TABLE users; --"
        print(f"🚨 Было бы: {drop_payload}")
        
        # UNION атака
        union_payload = "' UNION SELECT 'hacker', 'hacked', 'hacker' --"
        print(f"🚨 UNION: {union_payload}")

if __name__ == "__main__":
    demo_attack()
