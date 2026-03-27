# import time

# t1 = time.time()
# t2 = time.localtime()
# t3 = time.gmtime(500_000)
# print(t1)
# print(t2)
# print(t2.tm_mday, t2.tm_hour)
# print(t3)
# print(time.ctime(t1))

# print(time.strftime(r"%Y/%m/%d %H:%M:%S", t2))
# # time.sleep(2)
# print(time.strftime(r"%Y/%m/%d %H:%M:%S"))

# t4 = time.strptime('11 11 11 2024', r'%H %M %S %Y')
# print(t4)

# time.sleep(5)

# while 1:
#     op1
#     if Sleep(2)

# ---------------------------------

# datetime
# 	date — хранит дату
# 	time — хранит время
# 	datetime — хранит дату и время


from datetime import datetime as dt
from datetime import time as t
from datetime import date as d




timestamp = 1528797322
date_time = dt.fromtimestamp(timestamp)

current_date_time = dt.now()
print(current_date_time)
current_date = d.today()
# curent_time = t.isoformat
print(current_date_time.day, current_date_time.hour)
print(current_date_time, "/", 
      current_date, '/', 
      current_date_time.time())
print(f"Текущее время {current_date_time:%d.%m.%Y %H-%M}")
# # #Текущее время 24.02.2017 15:51

date1 = d(2023,1,15)
d_txt = date1.strftime("%d")
print(d_txt)
print(f"{date1.day}.{date1.month}.{date1.year}")

print(current_date_time.strftime(r"%d-%m/%Y %H-%M:%S"))
print(f"{current_date_time.day}.{current_date_time.month}.{current_date_time.year}")


date_object = dt.strptime("22/11/2022", r"%d/%m/%Y")
print(date_object, date_object.month)


# timedelta - хранит какое-то время которое можно прибавить или отнять
from datetime import timedelta
time_add = timedelta(days=365)
current_date_time += time_add
print(current_date_time)

# разница в датах
d1 = dt.strptime("01.02.2017", "%d.%m.%Y")
d2 = dt.strptime("01.03.2017 2", "%d.%m.%Y %H")
d3 = dt.now()
delta = d2 - d1
delta2 = d3 - d1
print( delta2, "/", delta2.days, "/",  
            delta2.seconds, "/", delta2.total_seconds())

print(d1 < d2)


'''
%a	Abbreviated weekday name.	Sun, Mon, ...
%A	Full weekday name.	Sunday, Monday, ...
%w	Weekday as a decimal number.	0, 1, ..., 6
%d	Day of the month as a zero-padded decimal.	01, 02, ..., 31
%-d	Day of the month as a decimal number.	1, 2, ..., 30
%b	Abbreviated month name.	Jan, Feb, ..., Dec
%B	Full month name.	January, February, ...
%m	Month as a zero-padded decimal number.	01, 02, ..., 12
%-m	Month as a decimal number.	1, 2, ..., 12
%y	Year without century as a zero-padded decimal number.	00, 01, ..., 99
%-y	Year without century as a decimal number.	0, 1, ..., 99
%Y	Year with century as a decimal number.	2013, 2019 etc.
%H	Hour (24-hour clock) as a zero-padded decimal number.	00, 01, ..., 23
%-H	Hour (24-hour clock) as a decimal number.	0, 1, ..., 23
%I	Hour (12-hour clock) as a zero-padded decimal number.	01, 02, ..., 12
%-I	Hour (12-hour clock) as a decimal number.	1, 2, ... 12
%p	Locale’s AM or PM.	AM, PM
%M	Minute as a zero-padded decimal number.	00, 01, ..., 59
%-M	Minute as a decimal number.	0, 1, ..., 59
%S	Second as a zero-padded decimal number.	00, 01, ..., 59
%-S	Second as a decimal number.	0, 1, ..., 59
%f	Microsecond as a decimal number, zero-padded on the left.	000000 - 999999
%z	UTC offset in the form +HHMM or -HHMM.	 
%Z	Time zone name.	 
%j	Day of the year as a zero-padded decimal number.	001, 002, ..., 366
%-j	Day of the year as a decimal number.	1, 2, ..., 366
%U	Week number of the year (Sunday as the first day of the week). All days in a new year preceding the first Sunday are considered to be in week 0.	00, 01, ..., 53
%W	Week number of the year (Monday as the first day of the week). All days in a new year preceding the first Monday are considered to be in week 0.	00, 01, ..., 53
%c	Locale’s appropriate date and time representation.	Mon Sep 30 07:06:05 2013
%x	Locale’s appropriate date representation.	09/30/13
%X	Locale’s appropriate time representation.	07:06:05
%%	A literal '%' character.	%
'''