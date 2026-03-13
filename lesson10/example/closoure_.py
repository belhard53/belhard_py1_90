# def f1():
#     print(123)
    
# a = f1   
# def f2():
#     return f1    

# b = f2()
# a()
# b()
# print(a is b)

# ----------------------------------------

# def f1(x1, x2):
#     x = 1
#     def wrapper(a):        
#         b = a**2 + x1 + x2 + x
#         return b
#     return wrapper

# a1 = f1(1, 2)
# a2 = f1(4, 5)

# b1 = map(a1, [1, 2, 3])
# b2 = map(a2, [1, 2, 3])
# b3 = map(f1(9, 10), [1, 2, 3])

# print(*b1)
# print(*b2)

# print(a2.__closure__[0].cell_contents)
# print(a2.__closure__[1].cell_contents)
# print(a2.__closure__[2].cell_contents)


def print1(a):
    def wrapper(b):
        print(f"{a}{' - ' if a else ''}{b}")
    return wrapper

pr_err = print1("Error")
pr_info = print1("Внимание")
pr = print1("")

pr_err("Пароль неверный") # перед сообщением будет слово Error
pr_info("В пароле должно быть более 7 символов")
pr("Ok")



        
        

    