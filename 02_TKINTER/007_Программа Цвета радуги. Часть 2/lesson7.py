# coding=utf-8
###################################################
# 007_Программа Цвета радуги. Часть 2 (lesson7)
# python 3.x
# WebForMySelf - Андрей Кудлай, 2019
###################################################
# Writing sgiman, 2025

#**************************************************
# VERSION 2 (optimization)
#**************************************************
from tkinter import *

root = Tk()

'''
Напишите программу, состоящую из семи кнопок, цвета которых соответствуют цветам радуги. 
При нажатии на ту или иную кнопку в текстовое поле должен вставляться код цвета, 
а в метку – название цвета.
#ff0000: Красный
#ff7d00: Оранжевый
#ffff00: Желтый
#00ff00: Зеленый
#007dff: Голубой
#0000ff: Синий
#7d00ff: Фиолетовый
'''

#----------------------------------------
# get_color()
#----------------------------------------
def get_color(text_color, hex_color):
    l['text'] = text_color           # название цвета в label
    e.delete(0, END)            # удалить до конца
    e.insert(0, hex_color)     # вставить в начало

# Label & Entry
l = Label(root)                                 # object "label" на окне "root"
e = Entry(root, width=30, justify='center')     # objet "field entry" на окне "root"
l.pack()                                        # localisation label
e.pack()                                        # localisation entry field

# Colors
colors = {
    "#ff0000": "Красный",       # 1
    "#ff7d00": "Оранжевый",     # 2
    "#ffff00": "Желтый",        # 3
    "#00ff00": "Зеленый",       # 4
    "#007dff": "Голубой",       # 5
    "#0000ff": "Синий",         # 6
    "#7d00ff": "Фиолетовый",    # 7
}

# Buttons (cycle)
for k, v in colors.items():
    Button(root, bg=k, command=lambda text=v, hex=k: get_color(text, hex)).pack(fill=X)

root.mainloop()     # главный цикл
