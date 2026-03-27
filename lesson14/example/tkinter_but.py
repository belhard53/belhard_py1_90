import tkinter as tk
import random

def move_button(event=None):
    # Перемещаем кнопку в случайное место внутри окна
    x = random.randint(0, 200)
    y = random.randint(0, 200)
    btn.place(x=x, y=y)

root = tk.Tk()
root.title("Поймай кнопку")
root.geometry("300x300")

btn = tk.Button(root, text="Поймай меня!")
btn.place(x=100, y=100)

# Теперь "убегаем", когда мышь заходит на кнопку
btn.bind('<Enter>', move_button)

# Примеры распространённых событий в Tkinter:
# '<Enter>' — курсор вошёл в область виджета.
# '<Leave>' — курсор ушёл из области виджета.
# '<Button-1>' — нажатие левой кнопки мыши.
# '<ButtonRelease-1>' — отпускание левой кнопки мыши.
# '<Key>' — нажатие любой клавиши.

root.mainloop()