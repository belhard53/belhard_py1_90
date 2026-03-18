
# так можно добавить путь к поиску - в данном случае родительская папка
# import sys
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) 


# from ..import_2 import f # папка выше
from import_2 import f2
from .import_4 import f5

def f3():    
    print(333333)
    f2()

def f4():
    print(4444444)
    

