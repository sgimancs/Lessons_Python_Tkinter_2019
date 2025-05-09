# coding=utf-8
###################################################
# 001_Виджет Button. Часть 1 (lesson2)
# python 3.x
# WebForMySelf - Андрей Кудлай, 2019
###################################################
# Writing sgiman, 2025

from tkinter import *       # все классы
# from tkinter import ttk   # стили

#-------------------------------
# Window
#-------------------------------
root = Tk()
root.geometry('600x400+800+300')
root.iconbitmap('python.ico')           # иконка
root['bg'] = 'blue'
root.title('Первая Кнопка')

def clicked():
    print('Clicked')


#-------------------------------
# Properties Button
#-------------------------------
# btn = Button(root, text="Кнопка", command=clicked, font="Arial 20 italic")
# btn = Button(root, text="Кнопка", fg='blue', command=clicked, font=("Comic Sans MS", 20), padx=5, pady=5)
# btn = Button(root, text="Кнопка", fg='blue', command=clicked, font=("Arial", 20), padx=5, pady=5)
# btn = Button(root, text="Кнопка 1\n22", justify=LEFT)

#-------------------------------
# Create Button
#-------------------------------
btn = Button(root, text="Кнопка", fg='blue', command=clicked, padx=5, pady=5)   # конструктор
btn.configure(width=10)         # конфиг
btn['font'] = ("Arial", 15)     # словарь

#-------------------------------
# Location
#-------------------------------
btn.place(relx=0.5, rely=0.5, anchor='c')
# btn.pack()    # default location

root.mainloop()
