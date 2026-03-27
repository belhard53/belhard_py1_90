from enum import Enum

class Color(Enum):
    RED = ('red', (255, 0, 0), 'красный')
    GREEN = ('green', (0, 255, 0), 'зелёный')
    BLUE = ('blue', (0, 0, 255), 'синий')
    YELLOW = ('yellow', (255, 255, 0), 'жёлтый')
    PURPLE = ('purple', (128, 0, 128), 'пурпурный')

    # для каждого атрибута будет запускаться конструктор
    def __init__(self, en_name, rgb, ru_name):
        self.en = en_name      # английское название
        self.rgb = rgb         # кортеж RGB
        self.ru = ru_name      # русское название

# Пример использования
print(Color.RED)           # Color.RED
print(Color.RED.en)        # 'red'
print(Color.RED.rgb)       # (255, 0, 0)
print(Color.RED.ru)        # 'красный'

# Вывод нескольких значений
print(Color.GREEN.en, Color.GREEN.rgb, Color.GREEN.ru)  # green (0, 255, 0) зелёный

# Перебор всех цветов
print('-'*30)
for color in Color:
    print(f"{color.name}: {color.en}, RGB={color.rgb}, RU='{color.ru}'")
