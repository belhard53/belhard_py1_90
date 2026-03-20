# ООП


# абстракция
    # Сокрытие сложных деталей реализации, показ только необходимого интерфейса. 
    # Выделение главных характеристик объекта, игнорируя второстепенные.
# наследование
    # Создание новых классов на основе существующих с получением их свойств и методов. 
    # Повторное использование кода через иерархию "родитель-дочерний".
# полиморфизм
    # Возможность использовать один интерфейс для разных типов объектов. Один метод ведёт 
    # себя по-разному в зависимости от типа объекта (переопределение, перегрузка)
# инкапсуляция
    # Объединение данных и методов в классе + сокрытие внутренней реализации. 
    # Доступ к данным только через публичные методы (геттеры/сеттеры).

# -------------------------------------------------------------
# наследование

# class A:
#     a1 = 3
#     a2 = 2
    
        
    
#     def __init__(self, a):
#         self.ao = 3
#         self.ao2 = 4
        
#     def m1(self):
#         print(1111)
        
        
# a = A(1)

# print(a.a1, a.ao)

# class B(A):
#     b1 = 1
    
#     def __init__(self, a, b):
#         super().__init__(a)
#         self.bo = b
        

# class C(A):
#     c1 = 1

# class D(C):
#     d1 = 1

# class E:
#     e1 = 1
#     a1 = 2
    
#     def __init__(self):
#         self.eo = 4 
    
# class F(E, A):    
#     f1 = 1

#     def __init__(self, a):
#         E.__init__(self)
#         A.__init__(self, a)
#         self.fo = 5
    
# b = B(1, 2)
# c = C(1)
# d = D(1)
# f = F(1)

# print(b.__dict__, b.ao2, b.bo)
# print(c.a1, c.c1, c.ao, c.ao2)
# print(d.ao2, d.c1, d.d1)
# print(f.a1, f.e1, f.f1, f.ao2)

# f.m1()

# print(dir(f))    

# class User:        
#     def __init__(self, name, age=0):
#         self.name = name
#         self.age = age
        
# class Admin(User):    
#     def __init__(self, name, password): 
#         super().__init__(name)       
#         self.pas = password
    
#     def kill_user(self):
#         pass
        
# user1 = User("Vasya")
# admin1 = Admin('Dima', "1234")

# -----
# пример наследования класса из другой библиотеки

# from turtle import *
# # t = Turtle()
# class Turtle2(Turtle):
#     def __init__(self, shape = "turtle", color_='red', x=100, y=100):
#         super().__init__(shape=shape)
#         self.color(color_)
#         self.goto(x, y)
    
#     def goto100(self):
#         pass      
    
# t = Turtle2(color_="blue", x=200, y=200)   
# t.goto100()      
# mainloop()

    

# ----------
# полиморфизм

# from typing import Any

# # наследуемся от пайтоновского класса list и переопределим его метод append
# class List2(list):
#     #   еще пример как у наследника добавить новые методы
#     def slice(self, n):
#         for i in range(n):
#             self.insert(0, self.pop())
            
#     def append(self, object):
#         # super().append(object)
#         # super().append(object)
#         # super().insert(0, object)
#         self.insert(0, object)
#         # return super().append(object)

# a = List2()
# a += [1, 2, 3, 4, 5]
# a.append(6)
# # a.slice(1)
# print(a)
# print(type(a))
# print(issubclass(List2, list))
# print(11111, isinstance(a, list))
# print(type(a) == list)




# ------------------------------------------
# инкапсуляция

# class User:
#     __age: int = 13 # private - защищенное свойство можно использовать только внутри класса
#     _activ: bool = True # protect - тоже но доступно через наследование
    
#     def __init__(self, age):
#         self.__age = age
        
        
#     @staticmethod
#     def __check_age(age):
#         return age >= 14        

#     @property # геттер
#     def age(self):        
#         return self.__age
    
#     @age.setter
#     def age(self, val): # сеттер
#         if self.__check_age(val):
#             self.__age = val
#         else:
#             raise ValueError ("Возраст меньше 14")
        
        
#     def __met1(self):
#         print(123)


#     def print_age(self):
#         print(self.__age)
        
    
            
# user = User(21)        
# print(user.age)
# user.age = 11
# print(user.age)
# # print(user.__age)
# # user.__age = 18
# # print(user.__age)
# user.print_age()



# --------------------------------        

# "Если крякает как утка и выглядит как утка — это утка!"
# НЕ проверяем тип → проверяем поведение (наличие методов/атрибутов).    
    
    
# class A:
#     def foo1(self):
#         print(1)
#     def __len__(self):
#         return 1
    
# class B:
#     def foo1(self):
#         print(2)
#     def __len__(self):
#         return 2
    
# def f1(obj):
#     obj.foo1()

# a = A()
# b = B()

# # a.foo1()
# # b.foo1()    

# f1(a)
# f1(b)

# l = [A(), B(), A(), "sas"]
# print(list(map(len, l)))
# for obj in l:
#     try:
#         obj.foo1()
#     except:
#         print('err')

# ---------------------------------------

# # абстрактные классы 
# # только для наследования
# # Классы, которые нельзя инстанцировать(создать объект) напрямую — служат базой для наследования. 
# # содержат общую реализацию + абстрактные методы (без тела), которые обязаны реализовать наследники.
# # реализует шаблон поведения для группы классов

# from abc import ABC, abstractmethod

# class Basic(ABC):
#     __slots__ = ['a','b']
    
#     @abstractmethod # только для перезаписывания
#     def foo1(self):
#         print(1) # для примера обычно тут pass

#     def foo2(self): 
#         print(3)

# class Child(Basic):   
#     pass 
#     def foo1(self): # должен быть обязательно
#         super().foo1()
#         print(2)
        
# a = Child()
# a.foo1()


# ----------------------------------------
# декораторы класса

# def class_decorator(cls):
#     attrs = dict(a=1, b=2, c=3)

#     for attr, val in attrs.items():
#         setattr(cls, attr, val) 
#     return cls

# @class_decorator
# class A:    
#     def a():
#         print(1)
        
        
# a = A()    
# print(a.a, a.b)	
# print(a.__dict__)

# -------------------------------------

# ---------------------------------------------
# from dataclasses import dataclass
# from typing import Any

# # @dataclass(frozen=True)
# @dataclass
# class User:
#     # получаем упрощенную запись класса
#     # с реализованными методами __init__, __repr__, __str__ и __eq__
         
#     # аннотации типов обязательны
#     name:str
#     age:int
#     a: Any
    
# user = User('Alex', 33, 1)
# user.age = 20


# users = [
#     user,
#     User("Max", 20, '1'),
#     User("Djo", 20, True)
# ]

# print(user)
# for user in users:
#     print(user)
#     # user.send_email()


# ---------------------------------

# Метакласс — это класс, который управляет созданием и поведением других классов


# Метакласс — это класс для классов.
# Позволяет контролировать и изменять процесс создания классов.
# Используется для автоматизации, проверки и модификации классов при их определении.
# Создаётся путём наследования от type и переопределения методов __new__ и/или __init__.

# создать класс
# type(
#     name  (str)   — ИМЯ класса
#     bases (tuple) — БАЗОВЫЕ классы (наследование)
#     dict  (dict)  — ПРОСТРАНСТВО ИМЁН (методы, атрибуты)
# )


# User  = type("User", (), {'name':"123", 'age':0})
# user = User()
# print(user.name)



# # --

# class UpperAttrMeta(type):
#     def __new__(cls, name, bases, attrs):
#         uppercase_attrs = {
#             key.upper() if not key.startswith('__') else key: val
#             for key, val in attrs.items()
#         } 
#         return super().__new__(cls, name, bases, uppercase_attrs)

# class SimpleClass(metaclass=UpperAttrMeta):
#     attr1 = "value1"
#     attr2 = "value2"

# print(hasattr(SimpleClass, 'attr1'))  # False
# print(hasattr(SimpleClass, 'ATTR1'))  # True



# print('-'*20)

# # перехват инит
# class Meta(type):
#     def __init__(cls, name, bases, attrs):
#         print(f"Инициализация класса {name} метаклассом")
#         super().__init__(name, bases, attrs)
#         cls.custom_attr = "Добавлено метаклассом"

# class MyClass(metaclass=Meta):
#     def __init__(self, value):
#         print(f"Инициализация экземпляра MyClass с value = {value}")
#         self.value = value

# # Создание экземпляра класса
# obj = MyClass(42)
# print(obj.value)          # 42
# print(obj.custom_attr)  # Добавлено метаклассом
# print(obj.__dict__)


# добавление атрибута не в класс а в объект
# class Meta(type):
#     def __new__(cls, name, bases, attrs):
#         # Сохраняем оригинальный __init__, если он есть
#         original_init = attrs.get('__init__')

#         # Определяем новый __init__
#         def __init__(self, *args, **kwargs):
#             # Добавляем атрибут в экземпляр
#             self.meta_attr = 'Добавлено метаклассом'
#             # Вызываем оригинальный __init__, если он был
#             if original_init:
#                 original_init(self, *args, **kwargs)

#         # Заменяем __init__ в атрибутах класса
#         attrs['__init__'] = __init__

#         # Создаём класс с изменёнными атрибутами
#         return super().__new__(cls, name, bases, attrs)

# class MyClass(metaclass=Meta):
#     def __init__(self, value):
#         self.value = value

# obj = MyClass(10)
# print(obj.value)      # 10
# print(obj.meta_attr)  # Добавлено метаклассом
# print(obj.__dict__)
