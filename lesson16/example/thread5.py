import threading

# тайер

def repeating_task():
    print("Вызов повторяющейся функции")
    # Запускаем таймер заново — повторяем вызов каждые 3 секунды
    t = threading.Timer(3, repeating_task)
    t.start()
    t.cancel()
    
    

print("Запуск повторяющегося таймера")
repeating_task()

# Чтобы программа не завершилась сразу (опционально)
import time
time.sleep(10)  # программа будет жить 10 секунд
print("Завершение.")

