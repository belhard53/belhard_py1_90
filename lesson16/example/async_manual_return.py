import time

def sleep(seconds):
    """Имитация ожидания через yield"""
    start = time.time()
    while time.time() - start < seconds:
        yield  # Приостанавливаем выполнение

def task1():
    count = 0
    while count < 5:
        print(f"Task 1: {count}")
        count += 1
        yield from sleep(1)
    return "Task 1 завершена!"

def task2():
    count = 0
    while count < 3:
        print(f"---Task 2: {count}")
        count += 1
        yield from sleep(3)
    return "Task 2 завершена!"

def event_loop(*tasks):    
    results = []
    tasks = list(tasks)
    
    while any(task for task in tasks if task is not None):
        for i, task in enumerate(tasks):
            if task:
                try:
                    next(task)
                except StopIteration as e:
                    results.append(e.value)  # Получаем return
                    tasks[i] = None
    
    print("Результаты:", results)


event_loop(task1(), task2())