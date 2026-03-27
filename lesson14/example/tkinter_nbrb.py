import tkinter as tk
import requests
from datetime import date

def get_exchange_rates(date):
    # date = '2024-05-31'
    try:
        url = f"https://www.nbrb.by/api/exrates/rates?ondate={date}&periodicity=0"
        print(url)
        response = requests.get(url)
              
        data = response.json()
        return data
    except requests.RequestException as e:
        print(f"Error fetching exchange rates: {e}")
        return None

def display_exchange_rates():
    date = date_entry.get()  # Получаем введенную дату из текстового поля
    
    rates = get_exchange_rates(date.replace('/','-'))    
    if rates:
        for rate in rates:
            if rate["Cur_Abbreviation"] == "USD":
                value = rate["Cur_OfficialRate"]
                label = f"USD: {value:.2f} BYN"
                usd.config(text=label)
            elif rate["Cur_Abbreviation"] == "EUR":
                value = rate["Cur_OfficialRate"]
                label = f"EURO: {value:.2f} BYN"
                euro.config(text=label)
            if rate["Cur_Abbreviation"] == "RUB":
                value = rate["Cur_OfficialRate"]/100
                label = f"RUB: {value:.2f} BYN"
                rur.config(text=label)

# Создаем главное окно
root = tk.Tk()
root.title("Курсы валют")
root.geometry('250x300')

# Создаем виджеты
date_label = tk.Label(root, text="Введите дату (ГГГГ/ММ/ДД):", 
                      font=("Arial", 10), justify='center')
date_entry = tk.Entry(root, font=("Arial", 12), justify='center')

usd = tk.Label(root, text="", font=("Arial", 12))
euro = tk.Label(root, text="", font=("Arial", 12))
rur = tk.Label(root, text="", font=("Arial", 12))

update_button = tk.Button(root, text="Обновить", command=display_exchange_rates)

# Размещаем виджеты на форме
date_label.pack()
date_entry.pack(pady=3)
usd.pack(pady=15)
euro.pack(pady=15)
rur.pack(pady=15)
update_button.pack(pady=30)

# Запрашиваем и отображаем курсы валют
date_entry.insert(0, date.today().strftime("%Y-%m-%d"))
display_exchange_rates()

# Запускаем главный цикл событий
root.mainloop()
