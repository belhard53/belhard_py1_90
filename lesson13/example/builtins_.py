# import builtins as b

# print(dir(b))




# print = 123
# print(1212)
# builtins.print('Hello')
# a = 1
# c = 2
# breakpoint()

# print(hash(12345))
# print(hash('12345'))
# print(hash('12345'))
# print(hash('12345'))

# ------------------------------

# import builtins

# # Сохраняем оригинал
# original_print = print

# # Новая версия
# def new_print(*args, **kwargs):
#     pass  # Молчит
#     # original_print('Это новый принт')
#     # original_print(*args)


# builtins.print = new_print

# print("Это НЕ выведется!")  # Ничего!

# # Восстанавливаем
# original_print("Всё работает!")

# ------------------------


# def bar():
#     '''    doc bar    '''
#     a = 123
#     print('This bar function')
    
# bar.a = 123    
# print(1, bar.__annotations__)
# print(2, bar.__name__)
# print(3, bar.__code__)
# print(4, bar.__builtins__)
# print(5, bar.__dict__)
# print(6, bar.__sizeof__())
# print(7, bar.__class__)
# print(8, bar.__doc__)