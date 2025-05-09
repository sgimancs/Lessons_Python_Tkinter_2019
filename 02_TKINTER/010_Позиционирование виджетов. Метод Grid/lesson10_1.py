# coding=utf-8
#########################################################
# 010_Позиционирование виджетов. Метод Grid (lesson10_1)
# python 3.x
# WebForMySelf - Андрей Кудлай, 2019
#########################################################
# Writing sgiman, 2025

from tkinter import *

root = Tk()
root.geometry('600x400+700+300')

f = Frame(root)
f.pack(pady=10)

#-----------------------------------
# GRID BUTTONS (var 1)
#-----------------------------------
btn7 = Button(f, text='7', padx=10, pady=5).grid(row=0, column=0)
btn8 = Button(f, text='8', padx=10, pady=5).grid(row=0, column=1)
btn9 = Button(f, text='9', padx=10, pady=5).grid(row=0, column=2)
btn4 = Button(f, text='4', padx=10, pady=5).grid(row=1, column=0)
btn5 = Button(f, text='5', padx=10, pady=5).grid(row=1, column=1)
btn6 = Button(f, text='6', padx=10, pady=5).grid(row=1, column=2)
btn1 = Button(f, text='1', padx=10, pady=5).grid(row=2, column=0)
btn2 = Button(f, text='2', padx=10, pady=5).grid(row=2, column=1)
btn3 = Button(f, text='3', padx=10, pady=5).grid(row=2, column=2)
btn0 = Button(f, text='0', padx=10, pady=5).grid(row=3, column=0, columnspan=3)


root.mainloop()
