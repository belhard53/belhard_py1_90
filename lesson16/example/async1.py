import asyncio
from time import sleep


# await func()    — ждёт завершения
# task = create_task(func())  — запускает ФОНОВО



async def async_func(n):
    print('Запуск ...', n)
    await asyncio.sleep(n)
    # sleep(1) # нельзя
    print('... Готово!', n)


async def main():
    # await async_func(1) # ожидает завершения функции
    # await async_func(1)
    
    # -----------
    task1 = asyncio.create_task(async_func(3)) # запускает функцию фоново
    task2 = asyncio.create_task(async_func(2))
    task3 = asyncio.create_task(async_func(1))
    await task1
    await task2
    await task3
    
    
    



asyncio.run(main())
