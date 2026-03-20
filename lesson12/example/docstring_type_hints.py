from typing import Union, Any

#-------------- type hints - тайпхинтинг
# def f2(a:Union[int, float], b: str, c: list[Union[int, float]]) -> bool:


def f2(a: int | float, b: str, c: list[int | float], e: Any) -> bool:
    print(a)


f2("1", "H", [1, 2])


def foo(a: list, *args: str | int, **kwargs: int) -> tuple[bool]:
    print(a)
    print(args)
    print(kwargs)
    return True, False


numbers: list[int] = [1, 2, 3, 4]

data: dict[str, dict[str, str]] = {
    "name": {"min": "Alex"}
}



# --------------------------------------
# docstring

def f1(a:int, b:list) -> list:
    """
    Функция для .....
    """
    pass

def rotate(objs: list[Any], n: int) -> list[Any]:
    """Rotate list

    :param objs: list for rotate
    :param n: step
    :return: rotated list
    """
    for _ in range(abs(n)):
        if n > 0:
            objs.insert(0, objs.pop(-1))
        else:
            objs.append(objs.pop(0))
    return objs

def multiply(a: int, b: int) -> int:
    """Произведение 2 целых чисел

    :param a: Первый множитель
    :type a: int
    :param b: Второй множитель
    :type b: int
    :return: Результат произведения
    :rtype: int
    :raise TypeError: если один из множителей не число
    
    """
    return a * b

f1(1, 2)
rotate([1,2,3,4,5], 2)
multiply(2,3)
    
    
    
# --------------------------
    
class Person:
    """
    Класс для представления человека.

    :param name: Имя человека.
    :type name: str
    :param age: Возраст человека.
    :type age: int
    """

    def __init__(self, name, age):
        self.name = name
        self.age = age    
    
    
class Person:
    """
    Класс для представления человека.

    Атрибуты:
        name (str): Имя человека.
        age (int): Возраст человека.

    Методы:
        greet(): Выводит приветствие с именем человека.
    """

    def __init__(self, name, age):
        """
        Инициализация экземпляра Person.

        Args:
            name (str): Имя человека.
            age (int): Возраст человека.
        """
        self.name = name
        self.age = age

    def greet(self):
        """Выводит приветствие с именем человека."""
        print(f"Привет, меня зовут {self.name} и мне {self.age} лет.")    

open()