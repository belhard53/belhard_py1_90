# GIL 
# processor bound

from threading import *
from time import sleep, time

ts = time()

def f1(v):
    # sleep(v)
    a = 10000**1000000
    # print(v)
    
def f2(v):
    a = 10000**1000000    
    # sleep(v)
    # print(v)

def main():
    t1 = Thread(target=f1, args=(1,))
    t2 = Thread(target=f2, args=(1,))
    t3 = Thread(target=f2, args=(1,))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()
    
def main2():
    f1(1)
    f2(1)
    f2(1)    

main()
print('end')
print(time()-ts)
