# coding=utf-8
#######################################################
# 018_Программа Часы (lesson18)
# python 3.x
# WebForMySelf - Андрей Кудлай, 2019
#######################################################
# Writing sgiman, 2025

# сборка приложения в виде одного файла
#  pyinstaller -w notepad_tk.py

from tkinter import *
import time

root = Tk()

# https://ru.wikiversity.org/wiki/%D0%9A%D1%83%D1%80%D1%81_%D0%BF%D0%BE_%D0%B1%D0%B8%D0%B1%D0%BB%D0%B8%D0%BE%D1%82%D0%B5%D0%BA%D0%B5_Tkinter_%D1%8F%D0%B7%D1%8B%D0%BA%D0%B0_Python


def tick():
    watch.after(200, tick)                  # рекурсия (ф-я "tick") через каждые 200 миллисекунд
    watch['text'] = time.strftime("%H:%M:%S")   # вывод времени


watch = Label(root, font="Arial 70")
watch.pack()
tick()

root.mainloop()
