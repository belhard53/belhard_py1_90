"""
Даны 4 переменные - a1, a2, a3, a4.
1 - вывести True если все они дробные числа
2 - вывести True если одна из них строка
3 - вывести True если  одна пара переменных является целочисленным типом. 
    Пары могут образовать только следующие переменные - a1-a3, a2-a4, a3-a4"
"""

a1 = 1.5
a2 = 2.7
a3 = "hello"
a4 = 4

# 1 - True если все дробные числа (float)
all_floats = all([isinstance(a1, float), 
                  isinstance(a2, float), 
                  isinstance(a3, float), 
                  isinstance(a4, float)])

# 2 - True если хотя бы одна строка (str)
any_string = any([isinstance(a1, str), 
                  isinstance(a2, str), 
                  isinstance(a3, str), 
                  isinstance(a4, str)])

# 3 - True если одна из трёх пар полностью целые числа (int)
pair1_int = isinstance(a1, int) and isinstance(a3, int)
pair2_int = isinstance(a2, int) and isinstance(a4, int)
pair3_int = isinstance(a3, int) and isinstance(a4, int)

one_pair_int = any([pair1_int, pair2_int, pair3_int])

print(all_floats)   # 1
print(any_string)   # 2
print(one_pair_int) # 3



# ---- пары еще вариант --------------------------------------------

a1, a2, a3, a4 = 1, 2, 3, 4

pairs = [(a1, a3), (a2, a4), (a3, a4)]
print(any(isinstance(pair[0], int) and isinstance(pair[1], int) for pair in pairs ))



# -- через комприхеншен -----------------

a1, a2, a3, a4 = 1, 2, 3, 4
a = [a1, a2, a3, a4]

# print (all(isinstance(i, float) for i in a))
print (all([isinstance(i, float) for i in a]))
print (any(isinstance(i, str) for i in a))

b = [(a1, a3), (a2, a3), (a3, a4)]
print (any((isinstance(i, int) for i in x) for x in b))
