# coding=utf-8
###################################################
# 006_Программа Цвета радуги. Часть 1 (lesson6)
# python 3.x
# WebForMySelf - Андрей Кудлай, 2019
###################################################
# Writing sgiman, 2025

#**************************************************
# VERSION 1
#**************************************************
from tkinter import *

# ГЛАВНОЕ ОКНО
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


# Buttons
btn_red = Button(root, bg="#ff0000", command=lambda: get_color('Красный', '#ff0000')).pack(fill=X)
btn_orange = Button(root, bg="#ff7d00", command=lambda: get_color('Оранжевый', '#ff7d00')).pack(fill=X)
btn_yellow = Button(root, bg="#ffff00", command=lambda: get_color('Желтый', '#ffff00')).pack(fill=X)
btn_green = Button(root, bg="#00ff00", command=lambda: get_color('Зеленый', '#00ff00')).pack(fill='x')
btn_blue = Button(root, bg="#007dff", command=lambda: get_color('Голубой', '#007dff')).pack(fill='x')
btn_dark_blue = Button(root, bg="#0000ff", command=lambda: get_color('Синий', '#0000ff')).pack(fill='x')
btn_violet = Button(root, bg="#7d00ff", command=lambda: get_color('Фиолетовый', '#7d00ff')).pack(fill='x')

root.mainloop()
