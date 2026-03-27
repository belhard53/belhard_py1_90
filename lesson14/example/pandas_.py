#Для чего pandas: Анализ табличных данных — загрузка, очистка, фильтрация, группировка, статистика.
import pandas as pd 
from pathlib import Path

csv_dir =  Path(__file__).parent/'auto'
csv_file_in = Path(csv_dir, 'auto.csv')
csv_file_out = Path(csv_dir, 'auto_output.csv')


df = pd.read_csv(csv_file_in, 
                 sep = ";", 
                 names=["brand", "model", "year_start", "year_end"],
                 na_values=['-'])



import pandas as pd



print("1. DataFrame:")
print(df)

# 2. Информация о данных

print("\n2. df.info():")
print(df.info())
print("\n3. df.shape:", df.shape)
print("\n4. df.columns:")
print(df.columns.tolist())

# 5. Первые/последние строки
print("\n5. df.head():")
print(df.head())
print("\n6. df.tail():")
print(df.tail())

# 7. Статистика
print("\n7. df.describe():")
print(df.describe())

# 8. Выбор столбцов
print("\n8. Столбец model:")
print(df['model'])
print("\n9. Несколько столбцов:")
print(df[['brand', 'model']])

# 10. Фильтрация
print("\n10. Acura модели:")
print(df[df['brand'] == 'Acura'])
print("\n11. Годы после 1997:")
print(df[df['year_start'] > 1997])

# 12. Сортировка
print("\n12. По году начала:")
print(df.sort_values('year_start'))

# 13. Группировка
print("\n13. Кол-во по брендам:")
print(df.groupby('brand').size())

# 14. Добавление столбца
df['years_span'] = df['year_end'] - df['year_start']
print("\n14. Продолжительность:")
print(df)

# 15. Запись в CSV
df.to_csv(csv_file_out, index=False)
print("\n15. Сохранено в output.csv")
