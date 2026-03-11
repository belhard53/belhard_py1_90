
# def f1():
#     global a        
#     # a = 2  
#     a += 12
#     b = 1
#     print(111, a, b)
#     # print(111, locals())
#     c.append(44)
#     def f2():
#         global a
#         nonlocal b
        
#         a += 10
#         b +=10
#         c = 3
        
        
#     f2()
#     print(222, b)
    
    


# a = 1
# c = [1, 2]
# f1()

# print(333, a, c)
# # print(globals())
# --------------------------------------------------------


# def f1(text:str):
#     if not text:
#         return
#     print(text)
#     f1(text[:-1])
    
    
# f1("Hello Python")    
    
    
    
# n = 0
# def f1():
#     global n
#     n += 1
#     print(n)    
#     if n<500:
#         f1()
    
# f1()    
# -------------------------------------

# def print_n(*args, n=1):
#     # print(*args, sep='-')
#     for a in args:
#         print(a*n)

# print_n(1, 2, 3, 4, 5, n=5)

# def f1(a, **kwargs):
#     print(kwargs)

# f1(a=1, b=2, c=3, user='vasya')


# def f1(a, b=1, *args, **kwargs):
#     print(args)
#     print(kwargs)

# f1(1, 2, 3, 4,  b=2, c=3, user='vasya')


def f1(a, /, c, d):
# def f1(a, *, c, d):
    print(a, c, d)
    
f1(1, c=2, d=3)



# Порядок параметров, который Python ожидает — строго определён для однозначной 
# интерпретации вызова функции:
    # позиционные-only 
    # позиционные или именованные (по умолчанию)
    # *args
    # именованные-only параметры (после *args)
    # **kwargs
    
    # def example(a, b, /, c, d=4, *args, e, f=6, **kwargs):
    #     print(f"a={a}, b={b}, c={c}, d={d}")
    #     print(f"args={args}")
    #     print(f"e={e}, f={f}")
    #     print(f"kwargs={kwargs}")    
    
        # В определении функций символ / используется для обозначения, 
        # что все параметры, объявленные слева от него, являются только 
        # позиционными — их можно передавать в функцию лишь по позиции, а не по имени.
        
# -----------------

# # a, b, c = 1, 2, 3, 4
# a, b, *c = [1, 2, 2, 3, 4, 5, 6]
# a, *b, c = [1, 2, 2, 3, 4, 5, 6]
# a, *b, c = 1, 2, 2, 3, 4, 5, 6
# print(a, b, c)

# --------------------------

# lambda  - анонимная функция

def f1():
    print(123)
    
a = f1

b = [f1, a, lambda:print(123)]

b[0]() # все работает одинаково
b[1]() # все работает одинаково
b[2]() # все работает одинаково


# a = lambda:1

# b1 = lambda x:x**2

# def b2(x):
#     return x**2

# print(b1(2))
# print(b2(2))

# map(b2, [1, 2, 3])
# map(lambda x:x**2, [1, 2, 3])

# print((lambda x1, x2:x1**2+x2)(2, 3))

# # a = map(lambda x: int(x), ["1", "2", "3"])
# # a = map(lambda x: int(x)==2, ["1", "2", "3"])
# a = map(lambda x: [i for i in range(int(x))], ["1", "2", "3"])
# print(*a)


# -------------------------------------
# sorted()

# l = ["qwe", 'dsdsda', 'b', 'dsdd']
# l.sort(key=len)
# l.sort(key=lambda x: x[-1])
# sorted(l, key=lambda x: x[-1])
# print(l)

# a = [[11, 2], [2, 4], [1, 5], [8, 3]]
# b = sorted(a, key=lambda x: x[1])

# # # сортировка словарей
# d = {1:11, 9:22, 3:33, 4:77, 7:44}
# print(d.items())
# d2 = dict(sorted(d.items(), key=lambda item:item[0])) # сортировка по ключу
# d3 = dict(sorted(d.items(), key=lambda item:item[1])) # сортировка по значению
# print(d2)
# print(d3)



users = [
    {'name':'vasia!',
        'age':25, 
        'surname':'vasiapupkin!', 
        'phone':'3752323232'},
    {'name':'DIma11111111111', 
        'age':33,
        'surname':'DimaKr!ivenyz', 
        'phone':'3752323232'},
    {'name':'Petia', 
        'age':21,
        'surname':'DimaKrivenyz', 
        'phone':'3752323232'}
]

# b = sorted(users, key=lambda user: user['age'], reverse=True)
# b = sorted(users, key=lambda user: len(user['name']), reverse=True)

# print(b)



# # ----------------------------------
# # filter

def f1(user):
    return "!" in user['surname']

users2 = filter(f1, users)

users2 = filter(lambda user: "!" in user['surname'], users)
users4 = filter(lambda user: user['age'] > 30, users)

print(list(users2))
print(list(users4))