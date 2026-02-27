

# a = ["1", "2", 'три', '4', '5']

# for i in a:
#     try:
#         print(int(i))
#     except:
#         print('errr')

a = "13"

try:
    a = int(a)
    b = 10 / a
    print(b)
    if a == 13:
        raise ValueError("13 err")
    
    # a = h
except ValueError as e:
    print('err1')
    print(e)
except ZeroDivisionError:
    print('err2')
except Exception as e:
    print('err3')
    print(e)
    print(e.with_traceback)
else:
    # выполняется когда в try не было ошибок
    print('no err')
finally:
    # выполняется всегда
    print('all')



# пример использования 
# while 1:
#     a = input("...: ")
#     try:
#         a = int(a)
#         break
#     except:
#         print('errr')

# print(a*10)




