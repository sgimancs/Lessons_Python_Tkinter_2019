# coding=utf-8
#######################################################
# 023_Пакет TTKThemes (lesson23)
# python 3.x
# WebForMySelf - Андрей Кудлай, 2019
#######################################################
# Writing sgiman, 2025

#-----------------------------------------------------
# pip install ttkthemes
# pip install requests
#-----------------------------------------------------#
# https://ttkthemes.readthedocs.io/en/latest/
#
# Themes:
# arc, clearlooks, plastik, radiance (Ubuntu)...
#

# from tkinter import *
from tkinter import ttk             # ttk style
from ttkthemes import ThemedTk      # пакет ttkthemes (темы из ThemedTk)

root = ThemedTk(theme="radiance")   # тема "radiance" из ThemedTk
root.geometry("400x300+700+300")

# Элементы
ttk.Button(root, text="Button").pack(pady=10)
ttk.Entry(root).pack()


root.mainloop()     # главный цикл


##############################
# T E M P L A T E (tkinter)
##############################
# from tkinter import *
#
# root = Tk()
#
# root.mainloop()
