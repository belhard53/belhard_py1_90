# while (пока)- когда не знаем сколько повторов
# for - когда знаем сколько раз повторить, или что то перебрать

# a = 0
# while a<=10:    
#     a+=1    
#     if a==6:
#         continue    
#     if a == 6:
#         break    
#     print(a)    
# else:
#     print('else')
    
# print('end')

# ---------------------------

# a = int(input("age "))
# while a<18:
#     print("no")
#     a = int(input("age "))
    
# print('end')    

# a = 0
# while a<18:    
#     a = int(input("age "))
    
# ----------------------

# pas = input("pas: ")

# while pas != '1234':
#     print('err')
#     pas = input("pas: ")
#     if pas == 'stop':
#         break
# else:
#     print('else')

# print('ok')

# --------------------


# menu = '''
# 1 - ПОГОДА
# 2 - АНЕКДОТ
# 3 - КУРСЫ ВАЛЮТ
# 0 - ВЫХОД
# '''

# res = input(menu)

# while res != '0':
#     if res == '1':
#         print(1)
#     elif res == '2':
#         print(2)
#     elif res == '3':
#         print(3)
#     else:
#         print('err')
#     res = input(menu)
#     # break
    
    # -----------------------------
    
# a = 0 
# a = 1 
# b = "Hello"
# # while 1:
# # while a: good
# # while a!=0: bad
# while b:
#     print(b)
#     b = b[:-1]    

# ---------------------------------------------------------

# a = range(5)
# a = list(range(5))
# a = list(range(50, 101))
# a = list(range(50, 101, 5))
# print(a)

# for i in range(3):
#     print('ok', i)
#     # print(i**2)
#     # print(i**3)
    
# for _ in range(3):
#     print('ok')
        
# for i in range(5):
#     print(i)
#     i = 4

    
# for i in range(5):
#     print(i)
#     if i == 3:
#         break
# else:
#     print('else')    


# for i in "12345":
# # for i in "_____":
#     print(i)
    
# for user in ['user', 'suer1', 'user2']:
#     print(user)
#     for char in user:
#         print(char)
    
    
    
# bad_symbol = "!@#$%^&*()"
# login = 'Vasya123@!'
# for s in login:
#     if s in bad_symbol:
#         print("errr", s)
#     # print(s)
# # ---------------------

# users = ["user1", "user2", "user3", "user4"]

# for user in users:
#     print(user)

# i = 1
# for user in users:
#     print(i, user)    
#     i += 1    

# print()    
# for i in range(len(users)):
#     print(i+1, users[i]) 
    
# # print(list(enumerate(users, 1)))
# for i, user in enumerate(users):
#     print(i, user)

# --------------------------------------


# a = [
#   [1, 2, 3],
#   [3, 4, 5],
#   [7, 8, 8],
# ]

# for i in a:
#     for j in i:
#         print(i, j)             
# --------------------------------------

users = [
    {"name":"Vasya1", "login":"vvasiiiia",  "age":23},    
    {"name":"Vasya2", "login":"vvasiiiia",  "age":23},    
    {"name":"Vasya3", "login":"vva@siiiia!",  "age":23},    
    {"name":"Vasya4", "login":"vvasiiiia",  "age":23},    
    {"name":"Vasya5", "login":"vvasiiiia!",  "age":23},    
    {"name":"Vasya6", "login":"vv#asiiiia",  "age":23},    
    {"name":"Vasya7", "login":"vvasiiiia",  "age":23},    
    {"name":"Vasya8", "login":"vvasiiiia!",  "age":23}
]

# for user in users:
#     print(user)
#     print(user['name'])
      


user = {"name":"Vasya", "login":"vasya123",  "age":23}
for i in user:
    print(i)
    
for i in user.values():
    print(i)
    
for key, val in user.items():
    print(key, val)
    
for key in user:
    print(key, user[key])    
    
# ------------------------
a = [1, 2, 3]
b = [4, 5, 6]
c = [8, 9, 0]

for i1, i2, i3 in zip(a, b, c): # перебор двух или более списков
    print(i1, i2, i3)        