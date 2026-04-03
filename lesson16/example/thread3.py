# зачем нужна блокировка
# Lock нужен при конкуренции за РЕСУРС!
# Сценарии, где ОБЯЗАТЕЛЕН Lock
    # 1. Общий счётчик    
    # 2. Запись в файл
    # 3. Общий список/словарь
    # 4. База данных



import threading
from time import sleep

counter = 0
lock = threading.Lock()

def increase(by, n):
    global counter
    # Захватываем блокировку перед изменением общего ресурса
    lock.acquire() # Ждёт, пока lock свободен, Захватывает (locked = True), Другие корутины ЖДУТ!
    try:
        local_counter = counter
        local_counter += by
        sleep(1)  # имитируем какую-то работу для эффекта гонки без блокировки
        
        counter = local_counter
        print(f'counter {n} = {counter}')
    except:
        print('errrrr-----')
    finally:
        # Обязательно освобождаем блокировку, даже если исключение
        lock.release()
        pass

if __name__ == "__main__":
    t1 = threading.Thread(target=increase, args=(10, 1))
    t2 = threading.Thread(target=increase, args=(20, 2))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print(f'Итоговое значение counter: {counter}')


# современный способ
# with lock:
#     pass
# Автоматически: acquire() + release()