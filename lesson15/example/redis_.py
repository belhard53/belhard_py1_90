# pip install redis
import redis 

r = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)


r.set('foo', 'hello world')
print('foo:', r.get('foo'))  # -> 'hello world'

# Установка с истечением срока (5 сек) TTL
r.set('foo1', 'hello again', ex=5)

# # Инкремент/декремент числа
# r.set('counter', 10)
# r.incr('counter')
# print('counter +1:', r.get('counter'))  # 11
# r.decr('counter')
# print('counter -1:', r.get('counter'))  # 10



# ### Списки (queue/stack) — RPUSH/LPUSH/LPOP/RPOP ===

# # Очередь сообщений
# print('------------------------')
# r.delete('messages')
# r.rpush('messages', 'Hello, world!')
# r.rpush('messages', 'Hello, user!')
# print('messages list:', r.lrange('messages', 0, -1))  # ['Hello, world!', 'Hello, user!']
# first = r.lpop('messages')
# print('first pop:', first)  # 'Hello, world!'
# print('messages list:', r.lrange('messages', 0, -1))


### === Кэширование: получение/сохранение с истечением срока ===
# print('------------------------')
# def cache_get_or_set(key, create_func, ex=30): #ex в секундах
#     val = r.get(key)
#     if val is not None:
#         return val
#     val = create_func()
#     r.set(key, val, ex=ex)
#     return val

# # Пример кэширования
# result = cache_get_or_set('heavy:calc', lambda: 'result123')
# print('Cached:', result)

# ### ===  Проверка наличия ключа и удаление ===
# print('Exists foo:', r.exists('foo'))
# r.delete('foo')
# print('Exists foo after delete:', r.exists('foo'))
