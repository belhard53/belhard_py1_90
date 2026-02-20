# # list() - списки
# # tuple() - кортежи - защищенный список
# # dict() - словари
# # set() - множества
# # frozenset() - защищенные множества

# b = []

# a = (12, 14, 78)
# color = (0-255, 100, 50)
# red = (255, 0, 0)

# a = (1, 2)
# b = 1, 2
# c = (1,)
# print(a, b, c, type(c))

# a = a + (3, 4)
# print(a)

# a = [1, 2, 3, 4]
# b = tuple(a)
# print(b)


# # --- словари ----------------------------------    

# # key (ключи) - только неизменяемые типы данных
# # value (значения) - любые типы данных

# [1, 2, 3]

# a = {1:11, 2:22, 3:33}
# b = {"name":"Вася", "age":44, 111:"Hello"}
# print(a[1])
# print(b["age"])
# b["age"] = 33
# print(b[111])

# d = {}
# d = dict()

# a = {"a":11, "b":22, "c":"Hello"}
# b = dict(a=11, b=22, c='Hello')
# c = dict(**a)
# print(a, b, c)

# sp = [("key1", "value1"), ("key2", "value2")]
# c = dict(sp)
# print(c)

# d1 = dict.fromkeys(["key1", "key2"], "value")
# d2 = dict.fromkeys(["key1", "key2"])
# print(d1, d2)

# # ----------------------------------------

# user = {"name":"Вася", "age":33, "active":True, 
#             "phones":["11111", "22222"], 
#             "phones2":{
#                 "mts":"111111", 
#                 "vel":"222222"
#             }
# }

# print(user['name'])
# print(user['phones2']['vel'])

# users = {}
# users['user1'] = user
# users['user2'] = user
# users['user3'] = user
# users[1] = user
# users[2] = user

# __import__('pprint').pprint(users)

# print(users[2])

# users = [
#     {"name":"Vasya1", "login":"vvasiiiia"},    
#     {"name":"Vasya2", "login":"vvasiiiia",  "age":23},    
#     {"name":"Vasya3", "login":"vvasiiiia",  "age":23},    
#     {"name":"Vasya4", "login":"vvasiiiia",  "age":23},    
#     {"name":"Vasya5", "login":"vvasiiiia",  "age":23},    
#     {"name":"Vasya6", "login":"vvasiiiia",  "age":23},    
#     {"name":"Vasya7", "login":"vvasiiiia",  "age":23},    
#     {"name":"Vasya8", "login":"vvasiiiia",  "age":23}
# ]

# print(users[1]['name'])

# --- методы ------------------------------------------
# d = {"name":"Вася", "age":44, 111:"Hello"}

# print(d.get('name'))
# print(d.get('login', "нет"))
# # d['login']

# print(d.values())
# print(list(d.values()))

# print(d.keys())
# print(list(d.keys()))

# print(d.items())
# print(list(d.items()))


# # удаление элементов
# # a = d.pop('age')
# # print(d, a)

# # d.popitem() # удаляет последний
# # print(d)

# # del d['age']

# # setdefault(key[, default]): Возвращает значение по ключу, если ключ существует, иначе добавляет ключ со значением

# d1 = {1:11, 2:22}
# d.update(d1)
# print(d)
# d2 = d | d1
# print(d2)

# --- множество -----------------------------------------------------

s = set()
s = {1, 2, 3, 4, 4}
s.add(5)
print(s)

a = [1, 2, 3, 4, 2, 4, 9]
b = set(a)
print(b)

d = {1:11, 2:22}
s = set(d)
print(s)

s1 = set("Hello pyython")
s2 = set("Hello pyython")
print(s1, s2)

b = frozenset(a)
print(b, type(b))

# -----------------------------------------

# ---------------------------------------


a = {8, 3, 1, 5 }
b = {6, 7, 8, 3}
# b = {8, 1, 3}


print("-"*30)
# Включает ли set другой set
print(a.issubset(b)) # все элементы a принадлежат b.
print( a <= b )

print(a.issuperset(b)) # все элементы b принадлежат a.
print( a >= b )


#объединение и пересечение

print(a | b) # об] объединить
print(a.union(b)) # объединить

print(a.intersection(b)) # пересечение - только общие
print(a & b)

print(a.difference(b)) # разность - есть только в первом
print(a - b)

print(a.symmetric_difference(b)) # есть в обоих но не общие
print(a ^ b)




