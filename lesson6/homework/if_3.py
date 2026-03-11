'''
Запросить 3 числа. Вывести наибольшее  из них. Решить используя if.
'''



a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = float(input("Введите третье число: "))

if a >= b:
    max_number = a if a >= c else c
else:
    max_number = b if b >= c else c

print(f"Наибольшее число: {max_number}")


# ---еще вариант ------------------------


largest = a  

if b > largest:
    largest = b

if c > largest:
    largest = c

print("Наибольшее число:", largest)