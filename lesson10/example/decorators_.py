
# def f1():
#     print(111)
   
# def f2():
#     print(222)    
    
# def ff2(f):
#     print('start')
#     f()
#     print('end')
    
# ff2(f2)    
# # -------------------------------

# def d1(f):
#     def wrapper(*args, **kwargs):
#         print('start')
#         res = f(*args, **kwargs)
#         print('end')
#         return res
#     return wrapper

# @d1
# def f1():
#     print(1111)
#     return 123

# @d1
# def f2(a, b, c):
#     print(2222)
#     print(a, b, c)
#     return  a+b+c


# print(f2(1, 2, c=22))
# print(f1())


# f2_orig = f2.__closure__[0].cell_contents
# f2_orig(1, 2, 3)

# ---------------------------------


# ------------------------------
# декораторы с настройкой параметров

import os
BASE_DIR = os.path.dirname(__file__)

def logging(filename=f'{BASE_DIR}\\log3.txt'):
    # print(filename)
    def _loging(func):
        def wrapper(*args, **kwargs):
            with open (filename, "a", encoding='utf8') as f:
                from time import time, ctime, strftime
                # f.write(f"{ctime()} - запущена {func.__name__}\n")
                f.write(f"{strftime('%M:%S')} - запущена {func.__name__}\n")                
            func(*args, **kwargs)
                                        
        return wrapper
    return _loging


@logging(filename=os.path.join(BASE_DIR, "log1.txt"))
# @logging(filename=f'{BASE_DIR}\\log1.txt') # или так
def f1():
    print(123)
   
@logging(filename="log2.txt")
def f2():
    a = 1+1
    
@logging()
def f3():
    a = 1+1

    
f1()    



