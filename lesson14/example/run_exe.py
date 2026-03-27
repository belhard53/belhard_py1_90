import subprocess

# запуск программы с параметрами
# ping -n 1 google.com
result = subprocess.run(
    ["ping", "-n", "1", "google.com"],
    capture_output=True,    # Захватывает вывод!
    text=True,             # Строки вместо байтов
    encoding='cp866'       # Windows кодировка
)

print("STDOUT:", result.stdout)
print("STDERR:", result.stderr)
print("Код возврата:", result.returncode)

if result.returncode == 0:
    print("ОК", result.stdout)
else:
    print("ОШИБКА", result.stderr, f"(код: {result.returncode})")
    
    
# --------------------------
print('--------------------')

try:
    result = subprocess.run(["ping", "-n", "1", "google1.com"], 
                            capture_output=True, 
                            text=True, check=True, 
                            encoding='cp866')
    print("Вывод:", result.stdout)
except subprocess.CalledProcessError as e:
    print('*****************')
    print(f"Ошибка {e.returncode}: {e.stderr}")    
    
    
# --------------------------
print('--------------------')

from pathlib import Path

app = Path(__file__).parent / 'to_exe' / 'tkinter_but.exe'
subprocess.run([app])