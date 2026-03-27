from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
import pandas as pd



def mBox(text):     
    mb = QMessageBox(parent=mf)    
    mb.setText(text)
    mb.exec_()
    mf.show()
    


def lb2_fill():
    mf.listWidget_2.clear()
    mf.listWidget_3.clear()
    m = df[df['name'] == avto_selected]['model'].unique()
    mf.listWidget_2.addItems(m)


def lb3_fill():
    mf.listWidget_3.clear()
    y = df.loc[(df['name'] == avto_selected) & (df['model'] == model_selected)][['year1', 'year2']].values
    y = [str(i) for i in y[0]]
    mf.listWidget_3.addItems(y)


def lw1_select(i1, i2):
    global avto_selected
    global model_selected
    global year_selected
    # selection = event.widget.curselection()
    if i1:
        avto_selected = i1.text()
        model_selected = ""
        year_selected = ""
        # mf.listWidget_3.clear()
        lb2_fill()
        label_fill()


def lw2_select(i1, i2):
    global model_selected
    global year_selected
    if i1:
        year_selected = ""
        model_selected = i1.text()
        lb3_fill()
        label_fill()


def lw3_select(i1, i2):
    global year_selected
    if i1:
        year_selected = i1.text()
        label_fill()


def label_fill():
    mf.label1.setText(f"{avto_selected} {model_selected} {year_selected}")


def ok():
    mBox(f"ok - {avto_selected} {model_selected} {year_selected}")


#Создание окна
app = QtWidgets.QApplication([])
mf = uic.loadUi("avto.ui") # форма созданная в программе Qt Designer
mf.setWindowTitle("Avto_base")

avto_selected = ""
model_selected = ""
year_selected = ""

# читаем файл
df = pd.read_csv('auto.csv', sep=";", names=["name", "model", "year1", "year2"])
auto_list = df.name.unique()

# добавляем в список на окне машины
mf.listWidget_1.addItems(auto_list)


# подписка на события клика про элементу списка на окне
mf.listWidget_1.currentItemChanged.connect(lw1_select)
mf.listWidget_2.currentItemChanged.connect(lw2_select)
mf.listWidget_3.currentItemChanged.connect(lw3_select)
# подписка на событие клика по ОК
mf.buttonBox.accepted.connect(ok)

mf.label1.setText("")

mf.show()
app.exec()
