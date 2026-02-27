# List comprehension - условно "генераторы списков"
from pprint import pprint

# a = []
# for i in range(1, 11):
#     a.append(i**2)

# print(a)    

# a = [i**2 for i in range(1, 11)]
# print(a)

# # a = [input(f"{i} >>>") for i in range(3)]
# # print(a)

# a = [i**2 for i in range(1, 11) if i%2==0 ]
# print(a)

# a = [1, 2, 3, 4, 5]
# b = [str(i) for i in a]
# print(b)

# b = [i**(2 if i%2==0 else 3) for i in [1, 4, 30, 22, 2] if i < 5]
# b = [(i, i**(2 if i%2==0 else 3)) for i in [1, 4, 30, 22, 2] if i < 5]
# print(b)


# users = [
#     {"name": "Vasya1", "login": "vvasiiiia",  "age": 23},
#     {"name": "Vasya2", "login": "vvasiiiia",  "age": 23},
#     {"name": "Vasya3", "login": "vva@siiiia!",  "age": 23},
#     {"name": "Vasya4asas", "login": "vvasiiiia",  "age": 12},
#     {"name": "Vasya5", "login": "vvasiiiia!",  "age": 23},
#     {"name": "Vasya6", "login": "vv#asiiiia",  "age": 12},
#     {"name": "Vasya7", "login": "vvasiiiia",  "age": 23},
#     {"name": "Vasya8", "login": "vvasiiiia!",  "age": 23}
# ]

# users2 = [user for user in users if user['age']<20]
# users3 = [[user['name'], user['age']] for user in users]
# user1 = [user for user in users if user['name']=='Vasya8'][0]
# pprint(users2)
# pprint(user1)
# pprint(users3)

# user1 = [char.lower()+"-" for char in [user['name']
#                           for user in users if user['age'] == 12]]



# # Все пары чисел из двух списков
# a = [1, 2, 3]
# b = ['a', 'b']

# pairs = [(x, y) for x in a for y in b]
# print(pairs)


# numbers = [1, 2, 3]
# result = [(x, y) for x in numbers for y in range(x)]



# словари
# users4 = {user['name']:user['age'] for user in users}
# pprint(users4)

# a = (i for i in range(10))
# print(a)




# тесты
import timeit

numbers = list(range(1_000_000))


def for_loop():
    result = []
    for n in numbers:
        if n % 2 == 0:
            result.append(n)
    return result


def comprehension():
    return [n for n in numbers if n % 2 == 0]

print("for:", timeit.timeit(for_loop, number=30))
print("comp:", timeit.timeit(comprehension, number=30)) #чуть быстрее

