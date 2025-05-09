# coding=utf-8
###################################################
# 004_Виджет Label (lesson4)
# python 3.x
# WebForMySelf - Андрей Кудлай, 2019
###################################################
# Writing sgiman, 2025

from tkinter import *

# О К Н О
root = Tk()
root.geometry('600x300+700+300')
root.resizable(False, False)  # изменяемый размер окна (запретить W & H)
root.iconbitmap('python.ico')   # иконка
root.title('TK LABEL') # заголовок

# T E S T  L A B E L
l = Label(root, text="Текcт в строке 1\nСтрока 2\nСтрока 3\nСтрока 4\nСтрока 5",
          bg="blue", fg="#fff", font=("Comic Sans MS", 10, "bold"), justify=LEFT, width=74, height=5, anchor=SW) # anchor - ориентация

# К А Р Т И Н К А
img = PhotoImage(file='python-logo.png')  # создать объект-картинку
l_logo = Label(root, image=img)           # разместить как "label"
l_logo.pack()                             # локализовать

# MAIN CYCLE
root.mainloop()
