'''
Замена print() для продакшена — уровни, файлы, ротация, формат.

Уровни (по важности)
DEBUG (10)	Отладка, детали алгоритма	DEBUG: ищем пользователя ID=123
INFO (20)	Нормальная работа	INFO: пользователь авторизован
WARNING (30)	Не критично, но подозрительно	WARNING: файл не найден
ERROR (40)	Ошибка, но приложение живо	ERROR: база недоступна
CRITICAL (50)	Фатально, приложение падает	CRITICAL: потеряно соединение с БД

Суть: DEBUG в разработке, INFO в тестах, WARNING+ в продакшене. 
Меняешь level — меняется весь объём логов!

'''

import logging    

# level = фильтр по уровню, все что ниже игнор

# в консоль
# logging.basicConfig(level=logging.INFO) 
# logging.basicConfig(level=logging.DEBUG) 

# logging.info("Log1")
# logging.debug("Log2")



# # в файл

# logging.basicConfig(level=logging.INFO, filename='app.log')
# logging.basicConfig(level=logging.DEBUG, filename='my_log.log',
#                 format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


# logging.debug('111')
# logging.info('222')
# logging.warning('333')
# logging.error('444')
# logging.critical('555')


# --------------------------------

# logger = logging.getLogger(__name__)  # Логгер по имени модуля
# logger.setLevel(logging.DEBUG)

# # Форматтер
# formatter = logging.Formatter(
#     '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
# )

# # Файл + консоль
# file_handler = logging.FileHandler('app.log')
# file_handler.setFormatter(formatter)

# console_handler = logging.StreamHandler()
# console_handler.setFormatter(formatter)

# logger.addHandler(file_handler)
# logger.addHandler(console_handler)

# logger.info("Готово!")

# -----------------------------------

# для модулей
# logger = logging.getLogger(__name__)
# # Правило: logger = logging.getLogger(__name__) в начале каждого модуля.
# class MyClass:
#     def method(self):
#         logger.info("Метод вызван")
#         try:
#             1 / 0
#         except:
#             logger.exception("Ошибка деления!")
#             # logger.exception() — логирование с полным стек-трейсом
#             logger.error("Ошибка", exc_info=True)  # То же самое
#             # logger.warning("Предупреждение", exc_info=True)
            
# a = MyClass()
# a.method()            