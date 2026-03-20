# Синглтон (Singleton) - один из порождающих паттернов 
# гарантирует, что у класса есть только один экземпляр, 
# и предоставляет глобальную точку доступа к этому экземпляру.



# с помощью метаклассa
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            # Создаём новый экземпляр, если его ещё нет
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]
    
    # __call__ у метаклассов отвечает за создание экземпляра класса (то есть вызывается при создании объекта через MyClass()).
    # type — встроенный метакласс — реализует __call__, который вызывает __new__ и __init__ для создания и инициализации экземпляра.


class SingletonClass(metaclass=SingletonMeta):
    def __init__(self, value):
        self.value = value

# Проверка
obj1 = SingletonClass(10)
obj2 = SingletonClass(20)

print(obj1.value)  # 10
print(obj2.value)  # 10 — obj2 это тот же объект, что и obj1
print(obj1 is obj2)  # True


# -----------------------------------------------------------
print('-'*20)


# без Матакласса
class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, value):
        print(1)
        self.value = value

obj1 = Singleton(10)
obj2 = Singleton(20)

print(obj1.value)  # 20 — __init__ вызывается каждый раз, поэтому значение обновилось
print(obj1 is obj2)  # True


