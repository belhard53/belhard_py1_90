
a = True
b = False

# 1 + 2 = 3 # математическое выражение
# 1 < 2 = True # логическое выражение - ответ всегда только True или False
# 2 < 3 and 5 == 5 = True # сложное (составное) логическое выражение

if  2 < 3 and 5 == 5:
    print(1)
else:
    print(2)
    print(3)

print(a==1 and b == 2) # одновременно 2 варианта
print(a==1 or b == 2) # хотя бы один вариант

# ------------------
a, b, c = 1, 2, 3

if a==1:
    if b == 2:
        print(1)
        print(11)
        print(111)
    else:
        print(333)        
    print(444)
else:
    print(2)    



b=10
if a==1:
    if c==3:
        if b == 2:
            print(11111111)
        else:
            print("er1")
    else:
        print("er2")
else:
    print("er3")
    
    
# --- elif ----------------------    
# для a == 1,2,3,4 - своя команда иначе ошибка

# a = 1

# так неправильно
if a == 1:
    print(1)
if a == 2:
    print(2)
if a == 3:
    print(3)
else:
    print("err")    
    
    
# правильно но громоздко
a = 7
if a == 1:
    print(1)
else:
    if a == 2:
        print(2)
    else:
        if a == 3:
            print(3)
        else:
            if a == 4:
                print(3)
            else:
                print("err")    
                
                
a = 2
if a == 1:
    print(1)
elif a == 2:
    print(2)
elif a == 3:
    print(3)
elif a == 4:
    print(3)
else:
    print("err")     

# print('end')     

# if выше можно заменить словарем
a = 1
d = {1:"Hello",2:2,3:3,4:4}
print(d[a])  


# --- and or ---------------------------------------------

# a, b, c = 1, 2, 3
# print(a==1 and b == 2) # одновременно 2 варианта
# print(a==1 or b == 2) # хотя бы один вариант

# if a == 1 and b == 1 and c == 2:
#     pass

# if a == 1 and (b == 1 or c == 2):
#     pass

# if a == 1 and b == 1 and c == 2:
#     print(1)
# else:
#     print(2)


# ok = True and True --> True
# ok = True and False --> False

# ok = True or True --> True
# ok = True or False --> True

# ok = True or False or False --> True
# ok = True or False and True --> True
# ok = False and True or False --> False
# ok = False or False or False --> False


# приоритет операторов 
# 1. not
# 2. and
# 3. or

# ok = False and False or True    # - True
# ok = False and (False or True)    # - False - скобки решают


# ok = True or False and False    # - True (сначала and по приоритету)
# ok = (True or False) and False    # - False - скобки решают



# -----------------------
# ok = 2 == 3
# ok = 2 > 3
# ok = 2 < 3
# ok = 2 <= 3
# ok = 2 >= 3
# ok = 2 != 3 
# ok = not 2 == 2                

# ---------------------------


# ok = True
# ok = a==1
# a=1
# b = ""


# # if ok==True: bad practice
# if ok:
#     print(1)
# else:
#     print(2)
    
# if a > 0: # bad practice
#     pass    
# if a:
#     pass    

# if len(b) != 0: # bad practice
#     pass
# if b:
#     pass

# c = []
# if len(c) == 0: # bad practice
# if not c:
    # pass
    
# -------------------
# # тернарный if

# a = a + 10 if b == 2 else 3  # if для a+10  
# a = a + (10 if b == 2 else 3) # if для 10  
# print(a)
# print(f"hello {1 if b == 1 else 2}")    
# print(f"hello"  if b == 2 else "python")      

# -------------------------
# is_admin = False
# is_moderator = True
# age = 20

# if is_admin or is_moderator and age > 18: # неправильно
# if is_admin or (is_moderator and age) > 18: # неправильно
# if (is_admin or is_moderator) and age > 18:    # так правильно 
#     print("Доступ разрешен!")
# else:
#     print("Доступ запрещен.")


# -- проверка себя ------------------------
# x = True
# y = False
# z = False

# if not x or y:
#     print(1)
# elif not x or not y and z:
#     print(2)
# elif not x or y or not y and x:
#     print(3)
# else:
#     print(4)



# ------------------
# # проверка перед сравнение чтобы не было ошибки
# user = ['name1', 'pass1','log1']
# user = []
# if user and user[1] == 'pass1':
#     print(1)

# -------------------- проверка типов
# if type(a) == int:
#     print(1)

# if isinstance(a, int) 
# # if isinstance(a, (int, bool) # или
# if isinstance(a, int | bool): # или  python 3.10+
#     pass

# ----------------- any all
# print(all([1, 2, 0, True])) # все True
# print(any([1, 2, 0, True])) # хотя бы 1 True



# # ------------------ диапазоны 
# a = 33

# вне диапазона
# if a < 20 or a > 40:
#     pass

# внутри диапазона
# if a > 20 and a < 40:
# if  20 < a < 40: #аналогично
#     pass
# if  20 <= a <= 40:
#     pass


# ------------------------ match
# a = 9
# match a:
#     case 1 | 5 | 6:
#         print(11)
#     case 2 | 9:
#         print(22)
#     case 3:
#         print(33)
#     case _: # else
#         print("default")