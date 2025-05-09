# coding=utf-8
#######################################################
# 009_Позиционирование виджетов. Метод Pack (lesson9)
# python 3.x
# WebForMySelf - Андрей Кудлай, 2019
#######################################################
# Writing sgiman, 2025

#-------------------------------------------------------
# pip -V      (version)
# pip freeze  (install)
# pip list    (install)
#-------------------------------------------------------

from tkinter import *

#-------------------------
# Window
#-------------------------
root = Tk()
root.geometry('600x400+700+300')

#-------------------------
# Frame()
#-------------------------
# f_top = Frame(root)
# f_bottom = Frame(root)
# f_top.pack()
# f_bottom.pack()

#-------------------------
# LabelFrame()
#-------------------------
f_top = LabelFrame(root, text="Top Frame", padx=10, pady=10)        # frame TOP
f_bottom = LabelFrame(root, text="Bottom Frame", padx=10, pady=10)  # frame BUTTOM
f_top.pack(pady=10) # localisation TOP
f_bottom.pack()     # localisation BUTTOM

#-------------------------
# Labels with frame
#-------------------------
l1 = Label(f_top, text="1", font="15", fg="#fff", bg="#3498db", width=8, height=4).pack(side=LEFT)
l2 = Label(f_top, text="2", font="15", fg="#fff", bg="#2ecc71", width=8, height=4).pack(side=LEFT)
l3 = Label(f_bottom, text="3", font="15", fg="#fff", bg="#f1c40f", width=8, height=4).pack(side=LEFT)
l4 = Label(f_bottom, text="4", font="15", fg="#fff", bg="#34495e", width=8, height=4).pack(side=LEFT)

# Single label
l1 = Label(root, text="XYZ", font="15", fg="#fff", bg="#3498db", width=8, height=4).pack(expand=1, anchor=NE)

root.mainloop()
