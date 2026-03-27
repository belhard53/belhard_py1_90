from itertools import cycle

count = 0
for char in cycle('DOG'):
    if count >= 7:
        break
    print(char, end=' ')  # Выведет: D O G D O G D
    count += 1



# 1. Выборка первых N элементов из итератора — islice
from itertools import islice

data = (x*x for x in range(100))  # Генератор квадратов чисел
first_five = list(islice(data, 5))
print(first_five)  # [0, 1, 4, 9, 16]
# Используйте для взятия "среза" из потока данных без преобразования его в список.

# 2. Группировка подряд идущих одинаковых элементов — groupby
from itertools import groupby

items = "AAABBCCDAA"
groups = [(k, list(g)) for k, g in groupby(items)]
print(groups)
# [('A', ['A', 'A', 'A']), ('B', ['B', 'B']),
#  ('C', ['C', 'C']), ('D', ['D']), ('A', ['A', 'A'])]
# Удобно для сжатия последовательностей или подсчёта длины серий.



# 3. Создание пар подряд идущих элементов — pairwise (рецепт)
from itertools import tee

def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

lst = [1, 2, 3, 4]
for x, y in pairwise(lst):
    print(x, y)
# 1 2
# 2 3
# 3 4
# Часто встречается в анализе временных рядов и сравнении соседних значений.

# 4. Группировка по N элементов — grouper (рецепт)
from itertools import zip_longest

def grouper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)

data = 'ABCDEFG'
print(list(grouper(data, 3, 'x')))
# [('A', 'B', 'C'), ('D', 'E', 'F'), ('G', 'x', 'x')]
# Полезно для пакетной обработки данных или формирования "страниц" для вывода.

# 5. Сумма произведений (скалярное произведение) — dotproduct (рецепт)
from itertools import starmap
import operator

def dotproduct(vec1, vec2):
    return sum(starmap(operator.mul, zip(vec1, vec2)))

a = [1, 2, 3]
b = [4, 5, 6]
print(dotproduct(a, b))  # 32
# Этот паттерн упрощает вычисления с векторами и списками.

# 6. “Маска” фильтрации — compress
from itertools import compress

data = ['a', 'b', 'c', 'd']
selectors = [1, 0, 1, 0]
result = list(compress(data, selectors))
print(result)  # ['a', 'c']
# Применяется для отбора элементов по булевой маске или для работы с флагами.

# 7. Фильтрация по условию — filterfalse и dropwhile / takewhile
from itertools import filterfalse, dropwhile, takewhile

# filterfalse: оставляет элементы, для которых условие ложно
data = [1, 2, 3, 4, 5]
odd = list(filterfalse(lambda x: x % 2 == 0, data))
print(odd)  # [1, 3, 5]

# dropwhile/takewhile: "срезают" первую часть по предикату
print(list(dropwhile(lambda x: x < 4, data)))    # [4, 5]
print(list(takewhile(lambda x: x < 4, data)))    # [1, 2, 3]
# Это идеальные инструменты для отбрасывания заголовков, отбора или остановки по условию.

# 8. Все элементы уникальны? — all_equal (рецепт)
from itertools import groupby

def all_equal(iterable):
    g = groupby(iterable)
    return next(g, True) and not next(g, False)

print(all_equal(['A','A','A']))  # True
print(all_equal([1,2,1]))        # False
# Удобно для быстрой проверки однородности коллекции.

# 9. Силовые множества (все подмножества) — powerset (рецепт)
from itertools import chain, combinations

def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))

print(list(powerset([1, 2, 3])))
# [(), (1,), (2,), (3,), (1,2), (1,3), (2,3), (1,2,3)]