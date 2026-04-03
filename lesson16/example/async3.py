import asyncio
import time






def f0():
    print(111)
    time.sleep(1)
    print(222)

async def f1():
    print("Функция запущена1")
    await asyncio.sleep(1)
    print("Функция завершилась1")
    
async def f2():
    print("Функция запущена2")
    await asyncio.sleep(3)
    # time.sleep(3)
    print("Функция завершилась2")    

async def main():
    # Создание задачи
    task1 = asyncio.create_task(f2())  
    task2 = asyncio.create_task(f1())  
    # Ждем завершения задачи
    # await asyncio.sleep(5)
    
    await task1
    await task2
    
    
    
    
t = time.time()
asyncio.run(main())
print(time.time() - t)



# ----------------------------------------
    

# async def task_1():
#     """Имитация выполнения задачи, которая занимает 2 секунды."""
#     print("Начало задачи 1")
#     await asyncio.sleep(1)  # Имитация задержки
#     print("Завершение задачи 1")

# async def task_2():
#     """Имитация выполнения задачи, которая занимает 3 секунды."""
#     print("Начало задачи 2")
#     await asyncio.sleep(2)  # Имитация задержки
#     print("Завершение задачи 2")

# async def task_3():
#     """Имитация выполнения задачи, которая занимает 1 секунду."""
#     print("Начало задачи 3")
#     # await asyncio.sleep(3)  # Имитация задержки
#     time.sleep(3)
#     print("Завершение задачи 3")

# async def main():
#     """Запуск задач асинхронно."""
#     tasks = [task_1(), task_2(), task_3()]
#     await asyncio.gather(*tasks)

# # Запуск асинхронного кода
# asyncio.run(main())