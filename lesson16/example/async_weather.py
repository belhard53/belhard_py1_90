import asyncio
import time
from aiohttp import ClientSession
import requests

n_step:int = 0

async def aget_weather(city:str, n_city):
    '''
    асинхронная функция получения погоды
    '''
    global n_step
    async with ClientSession() as session:
        url = f'http://api.openweathermap.org/data/2.5/weather'
        params = {'q': city, 'APPID': '2a4ff86f9aaa70041ec8e82db64abf56'}

        async with session.get(url=url, params=params) as response:
            weather_json = await response.json()            
            n_step += 1 
            # принт не асинхронный,  но  выполняется моментально и не блокирует ЭвентЛууп
            print(f'{n_step} - {n_city} {city}: {weather_json["weather"][0]["main"]}')
    

def get_weather(city, n_city):    
    '''
    синхронная функция получения погоды
    '''
    global n_step
    
    url = f'http://api.openweathermap.org/data/2.5/weather'
    params = {'q': city, 'APPID': '2a4ff86f9aaa70041ec8e82db64abf56'}
    res = requests.get(url, params).json()
    
    n_step += 1      
    print(f'{n_step} - {n_city} {city}: {res["weather"][0]["main"]}')

# import pprint
# pprint.pprint()    


async def async_main(cities_):
    tasks = []
    for i, city in enumerate(cities_):
        tasks.append(asyncio.create_task(aget_weather(city, i)))

    for task in tasks:
        await task
        
    # или так
    # tasks = [aget_weather(city, i) for i, city in enumerate(cities_)]
    # await asyncio.gather(*tasks)
        

def thread_main(cities):    
    from threading import Thread, Lock
    lock = Lock()
    with lock:
        lt = [Thread(target=get_weather, args=(c, i)) for i, c in enumerate(cities)]
        for t in lt:
            t.start()
        for t in lt:
            t.join()
    
        
        
    
    
def sync_main(cities_):    
    for i, city in enumerate(cities_):
        get_weather(city, i)

    


cities = ['Moscow', 'St. Petersburg', 'Rostov-on-Don', 'Kaliningrad', 'Vladivostok',
          'Minsk', 'Beijing', 'Delhi', 'Istanbul', 'Tokyo', 'London', 'New York']


t = time.time()


# ---------------------------

# sync_main(cities*4) # синхронный вариант

# asyncio.run(async_main(cities*4)) # асинхронный вариант

thread_main(cities*4) # вариант на потоках


print(time.time() - t)

