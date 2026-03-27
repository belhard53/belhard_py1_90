from tkinter import *

# создаём главное окно
window = Tk()
window.title('Пример рисования в Tkinter')
window.geometry('400x400')

# создаём холст (Canvas)
canvas = Canvas(window, width=400, height=400, bg='white')
canvas.pack()

# рисуем две пересекающиеся линии — желтые диагонали
canvas.create_line(0, 0, 400, 400, width=3, fill='yellow')
canvas.create_line(0, 400, 400, 0, width=3, fill='yellow')

# рисуем прямоугольник с белой заливкой и синей обводкой
canvas.create_rectangle(50, 100, 200, 250, outline='blue', fill='white', width=3)

# рисуем овал (эллипс), внутри прямоугольника 300х150
canvas.create_oval(150, 200, 300, 350, outline='pink', fill='pink', width=2)

# рисуем многоугольник (треугольник)
canvas.create_polygon(250, 50, 300, 150, 200, 150, outline='grey', fill='grey', width=2)

# выводим текст
canvas.create_text(200, 370, text="Рисунок на Canvas", font="Verdana 14", fill='red')

window.mainloop()
