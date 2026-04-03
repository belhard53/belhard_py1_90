from turtle import *
import random as rnd
from threading import Thread, Lock

setup(800, 600)

exit_fl = False
# t1 = Turtle('turtle')
# t2 = Turtle('turtle')
lock = Lock()
def f1(t):
    t.left(rnd.randint(1,90))
    for i in range(100):
        t.speed(1)
        # t.left(rnd.randint(1,360))
        # t.speed(rnd.randint(1, 4))
        # t.fd(rnd.randint(40, 80))
        t.fd(200)
        t.lt(90)
        if exit_fl: break

for i in range(2):
    Thread(target=f1, args=(Turtle('turtle'),)).start()



mainloop()
exit_fl = True