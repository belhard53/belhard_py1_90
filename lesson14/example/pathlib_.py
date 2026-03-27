from pathlib import Path

# 1. Создание пути и объединение
# p = Path('/home/user')
# p = Path.cwd()
p = Path(__file__).parent # без parent на конце будет файл

docs = p / 'documents' / 'file.txt'
# docs = Path(p, 'documents', 'file.txt')

print(f"1. Объединённый путь: {docs}")


# 2. Текущая и домашняя директория
print(f"2. Текущая директория: {Path.cwd()}")
print(f"   Домашняя директория: {Path.home()}")

# 3. Проверка существования файла или папки
path_check = Path('example.txt')
print(3, path_check)
print(f"3. Существует 'example.txt'? {path_check.exists()}")

# 4. Создание вложенных папок
new_dir = Path('my_folder/subfolder')
new_dir.mkdir(parents=True, exist_ok=True)
print(f"4. Создан каталог: {new_dir.resolve()}")

# 5. Получение имени, расширения и родителя
p2 = Path('/home/user/documents/file.txt')
print(f"5. Имя файла: {p2.name}")
print(f"   Расширение: {p2.suffix}")
print(f"   Родительская папка: {p2.parent}")

# 6. Итерация содержимого текущей папки
print("6. Содержимое текущей папки:")
for item in Path('.').iterdir():
    print(f"   {item.name} — {'папка' if item.is_dir() else 'файл'}")

# 7. Поиск файлов с маской (текущая папка)
print("7. *.py файлы в текущей папке:")
for py_file in Path('.').glob('*.py'):
    print(f"   {py_file.name}")

# 8. Запись и чтение текста в файл
file_path = Path('example.txt')
file_path.write_text("Привет, pathlib!")
content = file_path.read_text()
print(f"8. Прочитано из файла: {content}")

# 9. Переименование файла
new_file = Path('new_example.txt')
if file_path.exists():
    file_path.rename(new_file)
    print(f"9. Файл переименован в {new_file}")

# 10. Абсолютный путь и разрешение ссылок
print(f"10. Абсолютный путь: {new_file.resolve()}")
