from time import sleep

def f1(n):
    for i in range(10):
        print(n)
        sleep(0.1)
        yield
        
def f2(*ff):
    while 1:
        for f in ff:
            next(f)
        

        
f2(f1(1), f1(2))