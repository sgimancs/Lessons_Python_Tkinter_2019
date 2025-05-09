# coding=utf-8
#######################################################
# 019_Метод Bind (lesson19)
# python 3.x
# WebForMySelf - Андрей Кудлай, 2019
#######################################################
# Writing sgiman, 2025

#
# BIND - отслеживание событий
#

from tkinter import *

root = Tk()
# root.geometry("400x300+1000+300")

# def f_event(event, key):
#     print(event, key)
#
#
# e = Entry(root, justify=CENTER, font="Arial 15")
# e.pack(fill=X, expand=1, padx=10, ipady=10)
# e.bind("<Button-1>", lambda event, key="Left click": f_event(event, key))
# e.bind("<Button-2>", lambda event, key="Middle click": f_event(event, key))
# e.bind("<Button-3>", lambda event, key="Right click": f_event(event, key))
# e.bind("<FocusIn>", lambda event, key="Focus": f_event(event, key))

l = Label(root, bg="#fff")
l.pack(pady=10, fill=X)
root.resizable(False, False)  # изменяемый размер окна (запретить W & H)

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
    def __init__(self, master, color):
        self.color = color
        self.b = Label(master, bg=color, width=4, height=2)
        self.b.pack(side=LEFT, padx=1)
        self.b.bind("<Button-1>", lambda event, key="lk": self.get_color(event, key))   # для "левой" кнопки мыши
        self.b.bind("<Button-3>", lambda event, key="rk": self.get_color(event, key))   # для "правой" кнопки мыши

    # Получить цвет
    def get_color(self, event, key):
        if key == 'lk':
            l['bg'] = self.color
        else:
            l['bg'] = '#fff'

#
for k, v in colors.items():
    MyLabels(root, k)

root.mainloop()     # main cycle
