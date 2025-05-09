# coding=utf-8
#######################################################
# 010_Позиционирование виджетов. Метод Grid (lesson10)
# python 3.x
# WebForMySelf - Андрей Кудлай, 2019
#######################################################
# Writing sgiman, 2025

from tkinter import *

root = Tk()

#-----------------------------------
# LOGIN FORM
#-----------------------------------
l_user = Label(root, text="Login:").grid(row=0, column=0, padx=10, pady=10, sticky=W)
e_user = Entry(root).grid(row=0, column=1, columnspan=2, padx=10, sticky=W+E)

l_pass = Label(root, text="Password:").grid(row=1, column=0, padx=10, sticky=W)
e_pass = Entry(root, show='*').grid(row=1, column=1, columnspan=2, padx=10, sticky=W+E)

btn_login = Button(root, text="Вход", padx=5).grid(row=2, column=0, padx=10, pady=10, sticky=W)
btn_reg = Button(root, text="Регистрация", padx=5).grid(row=2, column=1)
btn_forgot = Button(root, text="Забыли пароль?", padx=5).grid(row=2, column=2, padx=10)


root.mainloop()
