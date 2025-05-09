# coding=utf-8
###################################################
# 005_Виджет Entry (lesson5)
# python 3.x
# WebForMySelf - Андрей Кудлай, 2019
###################################################
# Writing sgiman, 2025

from tkinter import *
from tkinter import Tk


###################################################
# ОДНОСТРОЧНЫЙ ТЕКСТ (ENTRY) - поле ввода
###################################################
root: Tk = Tk()
root.geometry('600x400+700+300')


# Command INSERT
def add_str():
    e.insert(END, 'Hello!')  # вставить в конец


# Command DELETE
def del_str():
    e.delete(0, END)  # удалить до конца


# Command GET
def get_str():
    l_text['text'] = e.get()


# *********************
# CREATE FILED ENTRY
# *********************
l = Label(root, text="Поле ввода")  # метка
l.pack()  # локализация по умолчанию

# Создать поле ввода
e = Entry(root)
# e = Entry(root, show='*')   # для паролей

# INSERT (test)
# e.insert(0, 'Hello')              # вставить в начало
# e.insert(END, ' world')           # вставить в конец
e.pack()

# BUTTONS & ACTIONS
btn_add = Button(root, text="Add", command=add_str).pack()      # ADD
btn_del = Button(root, text="Delete", command=del_str).pack()   # DEL
btn_get = Button(root, text="Get", command=get_str).pack()      # GET

# Заполнение текстового поля (фон, цвет)
l_text = Label(root, bg='blue', fg='white') # COLOR
l_text.pack(fill=X) # залить цветом по горизонтали (X)

# MAIN CYCLE
root.mainloop()

'''
Напишите программу, состоящую из семи кнопок, цвета которых соответствуют цветам радуги. 
При нажатии на ту или иную кнопку в текстовое поле должен вставляться код цвета, а в метку – название цвета.
#ff0000: Красный
#ff7d00: Оранжевый
#ffff00: Желтый
#00ff00: Зеленый
#007dff: Голубой
#0000ff: Синий
#7d00ff: Фиолетовый
'''
