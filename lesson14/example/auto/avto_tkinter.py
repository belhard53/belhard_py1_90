from tkinter import *
import pandas as pd
import ctypes 


def mBox(text, title='', style=0):
    # месажбокс от виндовс - для разнообразия - так тоже можно
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)


avto_selected = ""
model_selected = ""
year_selected = ""


def win_setup():
    root.title("AVTO")
    root.geometry("440x300")
    lb1 = Listbox(root, name='lb_1')
    lb2 = Listbox(root, name='lb_2')
    lb3 = Listbox(root, name='lb_3')
    lb1.place(x=10, y=10)
    lb2.place(x=150, y=10)
    lb3.place(x=290, y=10)
    b1 = Button(root, width=10, height=1, text="OK", command=b_ok_click)
    b1.place(x=180, y=270)

    lb1.bind('<<ListboxSelect>>', lb_select)
    lb2.bind('<<ListboxSelect>>', lb_select)
    lb3.bind('<<ListboxSelect>>', lb_select)
    # b1.bind('<<ButtonClick>>', b_ok_click)

    l1 = Label(root, font="Arial 20")
    l1.place(x=10, y=200)

    return lb1, lb2, lb3, l1



def b_ok_click():
    mBox(f"{avto_selected} {model_selected} {year_selected}")

def lb2_fill():
    lb2.delete(0, END)
    m = a[a['name'] == avto_selected]['model'].unique()
    for i, n in enumerate(m):
        lb2.insert(i, n)

def lb3_fill():
    lb3.delete(0, END)
    y = a.loc[(a['name'] == avto_selected) & (a['model'] == model_selected)][['year1', 'year2']].values
    for i, n in enumerate(y[0]):
        lb3.insert(i, n)

def lb_select(event):
    global avto_selected
    global model_selected
    global year_selected
    selection = event.widget.curselection()
    if selection:
        index = selection[0]
        if str(event.widget) == '.lb_1':
            avto_selected = event.widget.get(index)
            model_selected = ""
            year_selected = ""
            lb3.delete(0, END)
            lb2_fill()
        elif str(event.widget) == '.lb_2':
            year_selected = ""
            model_selected = event.widget.get(index)
            lb3_fill()
        elif str(event.widget) == '.lb_3':
            year_selected = event.widget.get(index)
        l1.config(text= f"{avto_selected} {model_selected} {year_selected}")


root = Tk()
lb1, lb2, lb3, l1 = win_setup()


# Если у csv есть строчка с названием колонок names не надо
a = pd.read_csv('auto.csv', sep = ";", names=["name", "model", "year1", "year2"])
l = a.name.unique()

for i,n in enumerate(l):
    lb1.insert(i, n)



root.mainloop()


