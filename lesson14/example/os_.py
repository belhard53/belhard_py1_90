import os

# 1. Получение текущей рабочей директории
cwd = os.getcwd()
print(f"1. Текущая рабочая директория: {cwd}")

# 2. Изменение рабочей директории
os.chdir('..')  # поднимаемся на уровень выше
print(f"2. После изменения: {os.getcwd()}")

# 3. Создание одной директории
try:
    os.mkdir('new_folder')
    print("3. Папка 'new_folder' создана")
except FileExistsError:
    print("3. Папка 'new_folder' уже существует")

# 4. Создание вложенных папок (дерева)
os.makedirs('new_folder/subfolder', exist_ok=True)
print("4. Создание дерева каталогов 'new_folder/subfolder'")

# 5. Удаление пустой директории
try:
    os.rmdir('new_folder/subfolder')
    print("5. Удалена папка 'new_folder/subfolder'")
except FileNotFoundError:
    print("5. Папка 'new_folder/subfolder' не найдена")

# 6. Переименование файла или директории
if os.path.exists('new_folder'):
    try:
        os.rename('new_folder', 'renamed_folder')
        print("6. Папка переименована в 'renamed_folder'")
    except:
        print("6. уже есть")

# 7. Проверка существования файла или папки
exists = os.path.exists('renamed_folder')
print(f"7. Существование 'renamed_folder': {exists}")

# 8. Получение списка файлов и папок в директории
print("8. Содержимое текущей папки:")
for item in os.listdir('.'):
    print(f"  {item}")

# 9. Получение абсолютного пути файла или папки
abs_path = os.path.abspath('../..\\renamed_folder')
print(f"9. Абсолютный путь 'renamed_folder': {abs_path}")

# 10. Работа с переменными окружения
user = os.getenv('USERNAME') or os.getenv('USER')
print(f"10. Имя пользователя из переменной окружения: {user}")

# Опционально: установка переменной окружения (не влияет на системные переменные вне скрипта)
os.putenv('MY_VAR', '123')
print(f"    MY_VAR = {os.getenv('MY_VAR')}")

# изменяет переменную только для текущего процесса Python и его дочерних процессов.

# СОЗДАТЬ ПУТЬ из обрывков
os.path.join(cwd, 'folder1', 'folder2')
path1 = os.path.join(cwd, 'folder1', 'folder2', 'some_file.txt')