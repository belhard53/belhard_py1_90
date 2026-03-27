from tkinter import *
from tkinter import ttk

win = Tk()
win.geometry('300x200')
win.title('Hello')

n = 0
def b_cl():
    global n
    n += 1
    btn['text'] = f'Clicks - {n}'
    
# Label
# Button
# Text
# Listbox


btn = ttk.Button(text='Click me', command=b_cl)

btn.pack(pady=50)

win.mainloop()
