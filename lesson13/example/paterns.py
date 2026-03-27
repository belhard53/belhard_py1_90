# Паттерны проектирования — это проверенные решения типичных задач программирования, которые помогают делать код гибким, масштабируемым и понятным. Их обычно делят на три группы:
    # Порождающие паттерны — управляют созданием объектов (например, Синглтон, Абстрактная фабрика, Строитель, Фабричный метод, Прототип).
    # Структурные паттерны — определяют удобные способы организации классов и объектов для упрощения взаимодействия (например, Адаптер, Мост, Компоновщик, Декоратор, Фасад, Легковес, Заместитель).
    # Поведенческие паттерны — описывают способы взаимодействия между объектами (например, Цепочка обязанностей, Команда, Итератор, Посредник, Снимок, Наблюдатель, Состояние, Стратегия, Шаблонный метод, Посетитель).
    
    
# наиболее частые примеры

"""
Порождающие | Структурные | Поведенческие
Singleton   | Decorator   | Observer
Factory     | Adapter     | Strategy
"""

from abc import ABC, abstractmethod
from functools import wraps

# ========================================
# ПОРОЖДАЮЩИЙ: SINGLETON (Одиночка)
# Гарантирует единственный экземпляр класса
# ========================================
class Singleton:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

db = Singleton()
print(id(db))  # Один и тот же ID

# ========================================
# ПОРОЖДАЮЩИЙ: FACTORY METHOD (Фабричный метод)
# Создает объекты без указания конкретного класса
# ========================================
class Animal(ABC):
    @abstractmethod
    def speak(self): pass

class Dog(Animal):
    def speak(self): return "Гав!"

class Cat(Animal):
    def speak(self): return "Мяу!"

class AnimalFactory:
    @staticmethod
    def create(type: str) -> Animal:
        if type == "dog": return Dog()
        if type == "cat": return Cat()
        raise ValueError("Неизвестный тип")

dog = AnimalFactory.create("dog")
print(dog.speak())  # Гав!

# ========================================
# СТРУКТУРНЫЙ: FACADE (Фасад) 
# Упрощает интерфейс сложной подсистемы
# ========================================
class CPU: 
    def process(self): 
        return "CPU работает"
    
class Memory: 
    def load(self): 
        return "Память загружена"
    
class Disk: 
    def read(self): 
        return "Диск прочитан"

class ComputerFacade:
    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.disk = Disk()
    
    def start(self):
        return [self.disk.read(), self.memory.load(), self.cpu.process()]

pc = ComputerFacade()
print(pc.start())  # ['Диск прочитан', 'Память загружена', 'CPU работает']

# ========================================
# СТРУКТУРНЫЙ: ADAPTER (Адаптер)
# Позволяет несовместимым интерфейсам работать вместе
# ========================================
class OldPrinter:
    def print_old(self, text): 
        return f"OLD: {text.upper()}"

class NewPrinter:
    def print_new(self, text): 
        return f"NEW: {text.lower()}"

class PrinterAdapter:
    def __init__(self, old_printer: OldPrinter):
        self.old = old_printer
    
    def print_new(self, text):        
        return self.old.print_old(text)

old = OldPrinter()
adapter = PrinterAdapter(old)
print(adapter.print_new("hello"))  # OLD: HELLO

# ========================================
# ПОВЕДЕНЧЕСКИЙ: OBSERVER (Наблюдатель)
# Рассылка изменений множеству подписчиков
# ========================================
class Subject:
    def __init__(self):
        self._observers = []
    
    def attach(self, observer):
        self._observers.append(observer)
    
    def detach(self, observer):
        self._observers.remove(observer)
    
    def notify(self, message):
        for obs in self._observers:
            obs.update(message)

class Observer:
    def __init__(self, name):
        self.name = name
    
    def update(self, message):
        print(f"{self.name} получил: {message}")

news = Subject()
bob = Observer("Боб")
alice = Observer("Алиса")

news.attach(bob)
news.attach(alice)
news.notify("Новость!")  # Боб получил: Новость! / Алиса получила: Новость!

# ========================================
# ПОВЕДЕНЧЕСКИЙ: STRATEGY (Стратегия)
# Выбор алгоритма во время выполнения
# ========================================
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount): pass

class CardPayment(PaymentStrategy):
    def pay(self, amount): return f"Оплата картой: {amount}₽"

class CashPayment(PaymentStrategy):
    def pay(self, amount): return f"Наличные: {amount}₽"

class Order:
    def __init__(self, strategy: PaymentStrategy):
        self.strategy = strategy
    
    def pay(self, amount):
        return self.strategy.pay(amount)

order1 = Order(CardPayment())
order2 = Order(CashPayment())

print(order1.pay(1000))  # Оплата картой: 1000₽
print(order2.pay(1000))  # Наличные: 1000₽
