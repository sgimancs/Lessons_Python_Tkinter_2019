# coding=utf-8
#######################################################
# 008_Программа Цвета радуги. Часть 3 (lesson8) - ООП
# python 3.x
# WebForMySelf - Андрей Кудлай, 2019
#######################################################
# Writing sgiman, 2025

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

colors = {
    "#ff0000": "Красный",
    "#ff7d00": "Оранжевый",
    "#ffff00": "Желтый",
    "#00ff00": "Зеленый",
    "#007dff": "Голубой",
    "#0000ff": "Синий",
    "#7d00ff": "Фиолетовый",
}


############################################
# MyButtons() - CLASS
############################################
class MyButtons:

    #-----------------------
    # КОНСТРУКТОР
    #-----------------------
    def __init__(self, master, text_color, hex_color):
        self.text_color = text_color
        self.hex_color = hex_color
        self.b = Button(root, bg=hex_color, command=self.get_color)
        self.b.pack(fill=X)

    #-----------------------
    # get_color()
    #-----------------------
    def get_color(self):
        l['text'] = self.text_color
        e.delete(0, END)
        e.insert(0, self.hex_color)


###########################################################

# Label & Entry
l = Label(root)
e = Entry(root, width=30, justify='center')
l.pack()
e.pack()

# Create Buttons
for k, v in colors.items():
    MyButtons(root, v, k)   # class init


root.mainloop() # main cycle

