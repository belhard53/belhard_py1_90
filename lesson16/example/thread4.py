import threading
import time

# Создаём объект-событие
event = threading.Event()

def waiter():
    print("Waiter: Жду сигнал...")
    event.wait()  # Ждём, пока событие не будет установлено
    print("Waiter: Сигнал получен! Продолжаю работу.")

def setter():
    print("Setter: Подготавливаюсь, потом сигнализирую через 3 секунды.")
    time.sleep(3)
    event.set()  # Посылаем сигнал — разблокируем все ожидающие потоки
    print("Setter: Сигнал отправлен.")

if __name__ == "__main__":
    t1 = threading.Thread(target=waiter)
    t2 = threading.Thread(target=setter)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Основной поток завершён.")
