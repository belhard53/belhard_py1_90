import multiprocessing
import time
from math import sqrt, pi

def f1(n):
    a = n**1000000 
    return a

if __name__ == '__main__':
    n = 10_000    
    start = time.time()
    
    # Последовательно 
    f1(n)    
    f1(n)    
    f1(n)    
    print(f"Последовательно: время: {time.time()-start:.2f}s")
    
    # multiprocessing 
    start = time.time()
    with multiprocessing.Pool(3) as pool:  # 3 ядра
        results = pool.map(f1, [n, n, n])
    print(f"Multiprocessing: время: {time.time()-start:.2f}s")


