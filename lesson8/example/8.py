# a = 1
# b = 2

# def print_n(n:int, text:str="python", flag:bool=False, 
#                     end=" ", p_param:dict={"sep":" ", "end":"\n"}):
#     '''
#     печатает n раз
#     '''
#     if flag:
#         print(11111)
#     for i in range(n):
#         # print(text, end=end)
#         print(text, text, text, **p_param)


        
# print_n(5, flag=True, end="///", p_param={"sep":"---", "end":"///"})
# print_n(5)
        
        

def f1(a):
    b = a*2
    return b
    # return b, a

b = f1(10)
print(b)

# --- проверка и ошибки --------------------------

def s1(a: int, b: int) -> int:    
    if isinstance(a, int) and isinstance(b, int):
        # ss = a*b
        # return ss
        # или так
        return a*b
    
    
a = s1(1, 2)
if not a is None:
    print(a)
else:
    print('errrrrr')


def s1(a: int, b: int) -> int:    
    if isinstance(a, int) and isinstance(b, int):
        # ss = a*b
        # return ss
        # или так
        return a*b
    
    raise TypeError("Неправильный тип")
    

try:
    s = s1(4, "5")
except Exception as e:
    print(f"---err---\n{e}")
else:
    print(s)
    




def s1(a: int, b: int) -> tuple[int, str]:
    err = ''
    s1 = 0
    if isinstance(a, int) and isinstance(b, int):
        s1 = a*b        
    else:
        err = 'err type'
    return s1, err
    
# res = s1(1, 'ds')
res, err = s1(1, 'ds')
if err:
    print(f'Ошибка {err}')


# -----------------------------------
print(s1(4, 5))  # позиционные
s = s1(a=4, b=5)  # именованные
print(s)


# -----------------------
def max_n(a, b):
    return a if a > b else b

a1, a2, a3 = 5, 4, 2
print(max_n(max_n(a1, a2), a3))

