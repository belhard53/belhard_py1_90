from time import *
import threading as th

def f1(data, val):
    for i in range(val):
        print(strftime('%M-%S'), '---', th.current_thread().name + f' - {i}', data)
        sleep(1)



th_list = []

for i in range(1, 4):
    t1 = th.Thread(target=f1, args = (time(), i), name = "thr_" + str(i))
    th_list.append(t1)
    t1.start()
    

print('Потоков запущенно', th.active_count())

for i in th_list:
    i.join()

print('list---', th_list)

