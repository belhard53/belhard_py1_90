import threading
import time

def worker():    
        time.sleep(2)
        print('ok')


t = time.time()
        

t1 = threading.Thread(target=worker)
t2 = threading.Thread(target=worker)
t3 = threading.Thread(target=worker)
t4 = threading.Thread(target=worker)
t5 = threading.Thread(target=worker)

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()

t1.join()
t2.join()
t3.join()
t4.join()
t5.join()

print(time.time() - t)





