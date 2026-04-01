from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, Float, JSON
from sqlalchemy.dialects.postgresql import UUID, INET  # PostgreSQL
from sqlalchemy.orm import DeclarativeBase

from datetime import datetime, timezone

# смотрим как создаются модели в sqlalchemy (одна модель -> одна таблица)
# модель описывает структуру таблицы - ее поля и их типы данных

class Base(DeclarativeBase):
    pass

    
class User(Base):
    __tablename__ = 'users'
    
    # Основные поля
    id = Column(Integer, primary_key=True, autoincrement=True)
    
    uuid = Column(UUID(as_uuid=True), unique=True, nullable=False)  # UUID
    username = Column(String(50), unique=True, nullable=False)      # Строка
    email = Column(String(100), unique=True, nullable=False)        # Email
    full_name = Column(String(200))                                 # Полное имя
    
    # Числа
    age = Column(Integer)                       # Целое
    height = Column(Float)                      # Дробное
    salary = Column(Float, default=0.0)         # Деньги
    
    # Текст
    bio = Column(Text)                          # Длинный текст
    preferences = Column(JSON)                  # JSON (настройки)
    
    # Булевы
    is_active = Column(Boolean, default=True)   # Активен
    is_admin = Column(Boolean, default=False)   # Админ
    
    # Даты
    created_at = Column(DateTime, 
                       default=lambda: datetime.now(timezone.utc))
    last_login = Column(DateTime)               # Последний вход
    
    # Специальные (PostgreSQL)
    # ip_address = Column(INET)                   # IP адрес
    tags = Column(JSON)                         # Теги
    
    

'''
Столбец	    Тип SQLAlchemy	SQL тип	        Пример значения
id	        Integer	        INTEGER	        1
uuid	    UUID	        UUID	        550e8400-e29b...
username	String(50)	    VARCHAR(50)	    "vasya_dev"
age	        Integer	        INTEGER	        30
height	    Float	        FLOAT	        1.82
salary	    Float	        FLOAT	        150000.50
bio	        Text	        TEXT	        "Python dev..."
preferences	JSON	        JSONB	        {"theme": "dark"}
is_active	Boolean	        BOOLEAN	        true
created_at	DateTime	    TIMESTAMP	    2025-01-01 12:00
ip_address	INET	        INET	        "192.168.1.100"

'''


# в файлах типа models.py хранятся в основном модели данных
# код ниже по созданию таблиц и управлению данными обычно выносится в другие файлы

# Создание таблицы
from sqlalchemy import create_engine
import os

db_file = f"{os.path.dirname(__file__)}\\test3.db"
engine = create_engine(f'sqlite:///{db_file}')

Base.metadata.create_all(bind=engine) # создает в базе все таблицы наследованные от класса Base

    