# coding=utf-8
#######################################################
# 021_Виджет TopLevel (lesson21)
# python 3.x
# WebForMySelf - Андрей Кудлай, 2019
#######################################################
# Writing sgiman, 2025

#=========================================================
# Окно верхнего уровня для создания многооконных программ
#=========================================================
from tkinter import *

root = Tk()
root.geometry("400x300+700+300")


def open_win():
    win = Toplevel()                # окно верхнего уровня
    win.geometry("200x100+800+450") # геометрия

    win.overrideredirect(1)         # игнорировать окно (без меню) - полезно для ЗАСТАВКИ
    win.grab_set()                  # фокус только на окно

    Label(win, text="Hello from Toplevel", bg="#000", fg="#fff").pack(expand=1, fill=BOTH)

    win.after(3000, lambda: win.destroy())  # время (пауза) до закрытия окна (3 сек.)

# Кнопка
Button(root, text="Open", command=open_win, padx=40, pady=5).place(relx=0.5, rely=0.5, anchor=CENTER)

# Главный цикл
root.mainloop()
