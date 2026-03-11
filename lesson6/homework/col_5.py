"""
Запросить фразу 
    - вывести на экран количество уникальных символов
    - вывести на экран количество уникальных слов
    -* вывести символ который встречался чаще всего

"""




from collections import Counter 
a = "asas df sdmf sdif;lksdmklmlkamsdlk maslkdmamsdasdaaaaaaaa"
b = Counter(a)
c = b.most_common(1)
print(f"{c[0][0]} - {c[0][1]}")