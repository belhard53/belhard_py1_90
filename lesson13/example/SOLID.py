# SOLID-принципы Дяди Боба(автор — Роберт К.Мартин) расшифровываются следующим образом:

# S – Принцип единственной ответственности (Single Responsibility Principle),
# O – Принцип открытости/закрытости (Open‐Closed Principle),
# L – Принцип подстановки Барбары Лисков (Liskov Substitution Principle),
# I – Принцип разделения интерфейсов (Interface Segregation Principle),
# D – Принцип инверсии зависимостей (Dependency Inversion Principle).




# Почему SOLID важен
#     Облегчает сопровождение и развитие кода
#     Повышает читаемость и повторное использование компонентов
#     Снижает количество ошибок при изменениях
#     Упрощает тестирование и внедрение новых функций

# SOLID — это не догма, а набор рекомендаций. 
#     Их разумное применение помогает создавать качественный, 
#     поддерживаемый и масштабируемый код



# --------------------------------

# 1 Принцип единственной ответственности (Single Responsibility Principle - SRP)
# Суть: Каждый класс или модуль должен отвечать только за одну задачу 
#       и иметь единственную причину для изменения.
# Преимущества: Повышает читаемость, облегчает тестирование и сопровождение


class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def save(self):
        # Логика сохранения пользователя в базе данных
        pass

    def send_email(self, message):
        # Логика отправки электронной почты пользователю
        pass

    def generate_report(self):
        # Логика генерации отчета пользователя
        pass
    
'''
Проблема: Класс User выполняет слишком много задач: управляет данными 
пользователя, сохраняет их, отправляет электронную почту и генерирует отчеты. 
Если потребуется изменить логику отправки электронной почты, 
это затронет класс User, даже если изменения не связаны с данными пользователя.
'''    


class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

class UserRepository:
    def save(self, user):
        # Логика сохранения пользователя в базе данных
        pass

class EmailSender:
    def send_email(self, user, message):
        # Логика отправки электронной почты пользователю
        pass

class ReportGenerator:
    def generate_report(self, user):
        # Логика генерации отчета пользователя
        pass
    
'''
Преимущества: Каждый класс отвечает за свою конкретную задачу: User управляет данными 
пользователя, UserRepository отвечает за сохранение данных, EmailSender — 
за отправку писем, а ReportGenerator — за генерацию отчетов.

'''    

# ---------------------------------

# ===========================================================    
# 2. Принцип открытости/закрытости (Open/Closed Principle - OCP)

# Суть: Классы должны быть открыты для расширения 
#       (можно добавлять новую функциональность), 
#       но закрыты для изменения (существующий код не должен меняться).
# Преимущества: Упрощает добавление новых возможностей 
#       без риска сломать старый код



class Shape:
    def __init__(self, type, width=None, height=None, radius=None):
        self.type = type
        self.width = width
        self.height = height
        self.radius = radius

    def calculate_area(self):
        if self.type == 'rectangle':
            return self.width * self.height
        elif self.type == 'circle':
            return 3.14 * self.radius ** 2

'''
Проблема: Каждый раз, когда добавляется новая фигура, необходимо 
изменять метод calculate_area. Это может привести к ошибкам и усложняет 
тестирование. Класс Shape не закрыт для модификации.
'''



from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius ** 2        


    
'''
Преимущества: Классы Rectangle и Circle могут быть расширены для добавления новых фигур 
без изменения существующего кода.
'''


# ====================================
# 3. Принцип подстановки Лисков (Liskov Substitution Principle - LSP)    
# Суть: Любой экземпляр подкласса должен корректно заменять 
#       экземпляр суперкласса, не нарушая логику программы.
# Преимущества: Позволяет использовать наследование без 
#       ожидаемых ошибок и нарушений логики    


#  Функции, которые используют базовый тип, должны иметь возможность использовать подтипы этого типа, не зная об этом




class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

class Square(Rectangle):
    def set_width(self, width):
        self.width = width
        self.height = width  # Стороны квадрата должны быть равны

    def set_height(self, height):
        self.width = height  # Стороны квадрата должны быть равны
        self.height = height    


''''
Проблема: Если использовать Square вместо Rectangle, 
поведение может быть непредсказуемым. Например, 
если задать ширину и высоту квадрата разными значениями, 
логика работы нарушится. Square не является полноценной заменой Rectangle.
'''        
        
        

# -------------------------------
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height        

class Square(Rectangle):
    def __init__(self, size):
        super().__init__(size, size)    \
            
    def set_width(self, width):
        self.width = width
        self.height = width  # Стороны квадрата должны быть равны

    def set_height(self, height):
        self.width = height  # Стороны квадрата должны быть равны
        self.height = height            
    
'''''
Преимущества: Класс Square корректно наследует от Rectangle, и обе фигуры могут 
быть использованы в одной функции без нарушения логики.

'''        


# ==================================================================
# 4. Принцип разделения интерфейса (Interface Segregation Principle - ISP)
# Суть: Не заставляйте клиентов реализовывать методы, которые они 
#       не используют. Лучше создавать несколько специализированных 
#       интерфейсов вместо одного общего.
# Преимущества: Повышает гибкость и модульность кода, 
#       снижает избыточные зависимости


from abc import ABC, abstractmethod

class Printer(ABC):
    @abstractmethod
    def print_document(self, document):
        pass

    @abstractmethod
    def fax_document(self, document):
        pass

    @abstractmethod
    def scan_document(self, document):
        pass

class OldPrinter(Printer):
    def print_document(self, document):
        # Логика печати документа
        pass

    def fax_document(self, document):
        raise NotImplementedError("Fax не поддерживается")

    def scan_document(self, document):
        raise NotImplementedError("Сканирование не поддерживается")

class MultiFunctionPrinter(Printer):
    def print_document(self, document):
        # Логика печати документа
        pass

    def fax_document(self, document):
        # Логика отправки факса
        pass

    def scan_document(self, document):
        # Логика сканирования документа
        pass
    
    
    
 
# -----------------------------------
from abc import ABC, abstractmethod

class Printer(ABC):
    @abstractmethod
    def print_document(self, document):
        pass

class Faxer(ABC):
    @abstractmethod
    def fax_document(self, document):
        pass

class Scanner(ABC):
    @abstractmethod
    def scan_document(self, document):
        pass

class OldPrinter(Printer):
    def print_document(self, document):
        # Логика печати документа
        pass

class MultiFunctionPrinter(Printer, Faxer, Scanner):
    def print_document(self, document):
        # Логика печати документа
        pass

    def fax_document(self, document):
        # Логика отправки факса
        pass

    def scan_document(self, document):
        # Логика сканирования документа
        pass
    
'''
Преимущества: Интерфейсы разделены на специализированные классы 
Printer, Faxer и Scanner. Класс OldPrinter реализует только печать, 
а класс MultiFunctionPrinter — все три функции. 
Это уменьшает зависимость от ненужных методов и делает систему более гибкой.

'''        

# 5. Принцип инверсии зависимостей (Dependency Inversion Principle - DIP)
# Суть: Зависимость должна строиться на абстракциях, а не 
#       на конкретных реализациях. Высокоуровневые модули 
#       не должны зависеть от низкоуровневых напрямую.
# Преимущества: Упрощает тестирование, делает код более 
#       гибким и слабо связанным




class LightBulb:
    def turn_on(self):
        print("Лампочка включена")

    def turn_off(self):
        print("Лампочка выключена")

class Switch:
    def __init__(self, lamp):
        self.bulb = lamp

    def operate(self):
        self.bulb.turn_on() # Жесткая зависимость от LightBulb    
        
        
'''
Проблема: Класс Switch напрямую зависит от класса LightBulb. 
Если захочется использовать другой тип устройства (например, вентилятор), 
придется изменять класс Switch. 
Зависимость от конкретной реализации делает систему менее гибкой.
'''


# -----------------------------------        
#        
from abc import ABC, abstractmethod

class LightSource(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

class LightBulb(LightSource):
    def turn_on(self):
        print("Лампочка включена")

    def turn_off(self):
        print("Лампочка выключена")

class LEDStrip(LightSource):
    def turn_on(self):
        print("Светодиодная лента включена")

    def turn_off(self):
        print("Светодиодная лента выключена")

class Switch:
    def __init__(self, light_source: LightSource):
        self.light_source = light_source

    def operate(self):
        self.light_source.turn_on()
 
'''
Преимущества: Класс Switch зависит от абстракции LightSource, 
что позволяет легко менять тип устройства без изменения самого переключателя. 
Это делает систему более гибкой и тестируемой.
 
'''