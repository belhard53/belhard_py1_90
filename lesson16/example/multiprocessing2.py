# Process (ручное управление)

import multiprocessing
import time

def worker(name, duration):
    print(f"{name} начал")
    time.sleep(duration)
    print(f"{name} закончил")
    return f"{name}: {duration}s"

if __name__ == '__main__':
    processes = []
    
    # Создаём процессы
    for i in range(4):
        p = multiprocessing.Process(
            target=worker, 
            args=(f"Процесс-{i}", 10)
        )
        processes.append(p)
        p.start()
    
    # Ждём завершения
    for p in processes:
        p.join()
    
    print("Все процессы завершены!")