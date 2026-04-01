import pandas as pd
from pydantic import BaseModel, ValidationError
import os

xls_file = f"{os.path.dirname(__file__)}\\test_data1.xls"
# Описываем модель для строки Excel
class User(BaseModel):
    fname: str
    lname: str
    age: int

# Чтение Excel в DataFrame с помощью pandas
df = pd.read_excel(xls_file, header=0)

# Валидация и преобразование в Pydantic-модели
users = []
for rec in df.to_dict(orient='records'):
    try:
        user = User(**rec)
        users.append(user)
    except ValidationError as e:
        print(f'Ошибка валидации для строки: {rec}\n', e)
        
print(*users, sep='\n')