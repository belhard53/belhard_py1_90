import threading
import time

def worker():
    while True:
        print("Работаю в фоне...")
        time.sleep(1)

t = threading.Thread(target=worker)
t.daemon = True  # делаем поток демоном (закончится вместе с программой)
t.start()

time.sleep(3)
print("Главный поток завершился, программа выйдет, не дожидаясь worker")
