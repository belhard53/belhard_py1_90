import math



# ----------------------
import decimal
a = 0.1 + 0.1 + 0.1
print(a, round(a, 2))
b = decimal.Decimal("0.1")
c = b + b + b
print(c)


# ------------------------
import array
# array — компактные массивы чисел (экономия памяти vs списки).

# Создание
arr = array.array('i', [1, 2, 3, 4, 5])  # 'i' = signed int
print(arr)  # array('i', [1, 2, 3, 4, 5])

# Операции как со списком
arr.append(10)
arr[0] = 100
print(arr)  # array('i', [100, 2, 3, 4, 5, 10])

# В список
print(arr.tolist())  # [100, 2, 3, 4, 5, 10]


# ------------------------------------

import statistics

data = [10, 12, 15, 13, 11, 14, 12]

print(f"Среднее: {statistics.mean(data):.2f}")        # 12.43
print(f"Медиана: {statistics.median(data)}")         # 12.0
print(f"Мода: {statistics.mode(data)}")              # 12
print(f"Стд.откл: {statistics.stdev(data):.2f}")     # 1.72
print(f"Дисперсия: {statistics.variance(data):.2f}") # 2.95

# -----------------------------------------
import pickle # сохраняет загружает объекты

l = [1, 2, 3, [5, 6, 7]]

with open('data.bin', 'wb') as f:
    pickle.dump(l, f)
    
with open('data.bin', 'rb') as f:    
    l2 = pickle.load(f)
print(l2)



