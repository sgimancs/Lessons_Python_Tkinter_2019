# coding=utf-8
#######################################################
# 022_Расширение TTK (lesson22)
# python 3.x
# WebForMySelf - Андрей Кудлай, 2019
#######################################################
# Writing sgiman, 2025

#
# ttk - расширение с новым набором виджетов
#

from tkinter import *
from tkinter import ttk     # расширение стилей и виджетов

root = Tk()
root.geometry("400x300+700+300")

#-----------------------------------------
# TTK Styles
#-----------------------------------------
s = ttk.Style()                             # задать стиль
#print(s.theme_names(), s.theme_use())       # список возможных тем и тема по умолчанию
s.theme_use('clam')                          # задать тему

# Конфигурация стиля
s.configure('.', foreground="red")     # "точка" - для всех
# s.configure('TButton', padding=6)          # только для всех (T)Element
s.configure('red.TButton', padding=6)   # только для одного (T)Element (red)

# Кнопки на окне root (собственный стиль)
Button(root, text="Button 1", padx=40, pady=5).pack(pady=10)                # standard
ttk.Button(root, text="Button 2", width=20, style="red.TButton").pack()     # ttk style для конкретной кнопки
ttk.Button(root, text="Button 3", width=20).pack(pady=10)                   # ttk style для всех кнопок

Entry(root).pack(pady=10)       # поле ввода (standard)
ttk.Entry(root).pack()          # поле ввода (ttk)


#-----------------------------------------
# Combobox (Select)
#-----------------------------------------
def choose(event):
    print(select.current(), select.get())   # индекс и значение


select = ttk.Combobox(root, values=["January", "February", "March", "April", "May"])
select.place(relx=0.5, rely=0.75, anchor=CENTER)
select.current(0)                               # выбор по умолчанию ("January")
select.bind("<<ComboboxSelected>>", choose)     # отслеживать селектор выбора

root.mainloop()                                 # главный цикл
