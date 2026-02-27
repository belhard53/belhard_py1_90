'''
Запросить количество секунд. 
Вывести на экран время в формате ЧЧ:ММ:СС равное эти секундам.
Пример: 35457 -> 09:50:57
Сделать 2 варианта с форматной строкой и без.

'''


seconds = int(input("Введите количество секунд: "))
print(f"Время: {seconds // 3600:02}:{seconds % 3600 // 60:02}:{seconds % 60:02}")
print(
    "Время: ",
    str(seconds // 3600).zfill(2),
    ":",
    str(seconds % 3600 // 60).zfill(2),
    ":",
    str(seconds % 60).zfill(2),
    sep="",
)


# --------------------------2
num_seconds = int(input("Введите количество секунд: "))

hours = num_seconds // 3600
minutes = (num_seconds % 3600) // 60
seconds = num_seconds % 60

formatted_time1 = f"{hours:02}:{minutes:02}:{seconds:02}"

# без форматной строки
formatted_time2 = "{:02}:{:02}:{:02}".format(hours, minutes, seconds)

print(formatted_time1)
print(formatted_time2)