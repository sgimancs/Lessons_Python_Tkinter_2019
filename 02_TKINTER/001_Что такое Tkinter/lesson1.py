# coding=utf-8
###################################################
# 001_Что такое Tkinter (lesson1)
# python 3.x
# WebForMySelf - Андрей Кудлай, 2019
###################################################
# Writing sgiman, 2025

#-------------------------------------------------------
# pip -V      (version)
# pip freeze  (install)
# pip list    (install)
#-------------------------------------------------------

# https://www.tutorialspoint.com/python3/python_gui_programming.htm
#
# Tkinter (от англ. Tk interface) — кросс-платформенная событийно-ориентированная
# графическая библиотека на основе средств Tk (1991)
#
# Tk (Toolkit — «набор инструментов», «инструментарий») — кроссплатформенная библиотека
# базовых элементов графического интерфейса (1991)
#
# Tcl (Tool Command Language) — «командный язык инструментов» (1988)
#

from tkinter import *


root = Tk()     # root - main window

root.title('Мое первое GUI приложение') # заголовок
root.iconbitmap('python.ico')           # иконка
root.geometry('600x400+800+300')       # размер: WxH + позиция окна: +X+Y
# root.resizable(False, False)  # изменяемый размер окна (запретить W & H)

# Фон Окна
# root.config(bg='#000')    # variant 1
root['bg'] = 'blue'         # variant 2

root.mainloop()     # главный цикл (события окна для взаимодействия с пользователем)

##############################
# T E M P L A T E (tkinter)
##############################
# from tkinter import *
#
# root = Tk()
#
# root.mainloop()
