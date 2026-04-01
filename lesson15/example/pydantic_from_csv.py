# pip install pydantic-csv

from pydantic import BaseModel
from pydantic_csv import BasemodelCSVReader
import os

csv_file = f"{os.path.dirname(__file__)}\\test_data1.csv"

# Определяем модель для строки CSV
class User(BaseModel):
    fname: str
    lname: str
    age: int

with open(csv_file) as f:
    reader = BasemodelCSVReader(f, User)
    for row in reader:
        print(row)  # row — это объект User, уже прошедший типовую валидацию