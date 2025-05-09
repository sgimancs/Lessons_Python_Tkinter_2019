# coding=utf-8
#######################################################
# 019_Метод Bind (lesson19_2)
# python 3.x
# WebForMySelf - Андрей Кудлай, 2019
#######################################################
# Writing sgiman, 2025

#
# BIND - отслеживание событий
#

from tkinter import *

root = Tk()
root.geometry("250x100+700+300")
root.resizable(False, False)    # изменяемый размер окна (запретить W & H)
root.iconbitmap('python.ico')               # иконка
root.title('BIND COLOR')                    # заголовок

l = Label(root, bg="#fff")
l.pack(pady=15, fill=X)

# Словарь цветов
colors = {
    "#ff0000": "Красный",
    "#ff7d00": "Оранжевый",
    "#ffff00": "Желтый",
    "#00ff00": "Зеленый",
    "#007dff": "Голубой",
    "#0000ff": "Синий",
    "#7d00ff": "Фиолетовый",
}

###############################################################
# MyLabels() - CLASS
###############################################################
class MyLabels:
    #----------------------------------
    # C O N S T R U T O R
    #----------------------------------
    def __init__(self, master_key, color):
        self.color = color
        self.b = Label(master_key, bg=color, width=4, height=2)
        self.b.pack(side=LEFT, padx=1)
        self.b.bind("<Button-1>", lambda event, key="left_key": self.get_color(event, key))   # для "левой" кнопки мыши ("lk")
        self.b.bind("<Button-3>", lambda event, key="right_key": self.get_color(event, key))   # для "правой" кнопки мыши ("rk")

    # Получить цвет
    def get_color(self, event, key):
        if key == 'left_key':           # если нажата левая кнопка - цвет
            l['bg'] = self.color
        else:                           # иначе - белый цвет
            l['bg'] = '#fff'

#==================================
# Заполнить цветами метки
#==================================
for k, v in colors.items():
    MyLabels(root, k)   # создать экземпляры меток в цикле

root.mainloop()         # main cycle
