# coding=utf-8
#########################################################
# 010_Позиционирование виджетов. Метод Grid (lesson10_2)
# python 3.x
# WebForMySelf - Андрей Кудлай, 2019
#########################################################
# Writing sgiman, 2025

from tkinter import *

root = Tk()
root.geometry('600x400+1000+300')

f = Frame(root)
f.pack(pady=10)

#-----------------------------------
# GRID BUTTONS (var 2)
#-----------------------------------
btn_list = [
    '7', '8', '9',
    '4', '5', '6',
    '1', '2', '3',
    '0',
]

row = 0
column = 0

for i in btn_list:
    if i == '0':
        Button(f, text=i, padx=10, pady=5).grid(row=row, columnspan=3)
    else:
        Button(f, text=i, padx=10, pady=5).grid(row=row, column=column)
    column += 1
    if column == 3:
        column = 0
        row += 1

root.mainloop()
