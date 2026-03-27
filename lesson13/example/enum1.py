'''
Enum — перечисление, набор именованных констант для представления 
        фиксированного набора значений 

Читаемость: BugStatus.in_progress вместо 1 или "in_progress"
Безопасность: IDE автодополнение + проверка типов
Единообразие: все константы в одном месте
Автодокументация: код сам объясняет себя


Когда использовать: 3+ связанных констант одного типа (статусы, роли, режимы, коды ошибок).
'''


import enum

# HTTP статусы
class HTTPStatus(enum.Enum):  
    OK = 200
    NOT_FOUND = 404
    SERVER_ERROR = 500

# Статусы багов
class BugStatus(enum.Enum):  
    NEW = "new"              
    INCOMPLETE = "incomplete"
    INVALID = "invalid"
    WONT_FIX = "wont_fix"
    IN_PROGRESS = "in_progress"
    FIX_COMMITTED = "fix_committed"
    FIX_RELEASED = "fix_released"

print(BugStatus.WONT_FIX, type(BugStatus.WONT_FIX))
print(f"Имя: {BugStatus.WONT_FIX.name}")        
print(f"Значение: {BugStatus.WONT_FIX.value}")   
# print(f"Числовой код: {BugStatus.WONT_FIX}")     

# Итерация
for status in BugStatus:
    print(f"{status.name}: {status.value}")

# Сравнение
bug = BugStatus.IN_PROGRESS
if bug == BugStatus.WONT_FIX:
    print("Не чинить")
else:
    print("Работать!")
