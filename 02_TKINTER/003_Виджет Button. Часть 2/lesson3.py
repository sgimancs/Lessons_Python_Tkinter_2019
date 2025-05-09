# coding=utf-8
###################################################
# 003_Виджет Button. Часть 2 (lesson3)
# python 3.x
# WebForMySelf - Андрей Кудлай, 2019
###################################################
# Writing sgiman, 2025

from tkinter import *
import time

# ------------------------------------------
# WINDOW
# ------------------------------------------
root = Tk()
root.title('Counter')
root.geometry('600x400+800+300')


# ------------------------------------------
# check_time()
# ------------------------------------------
def check_time():
    btn_time['text'] = time.strftime('%H:%M:%S')
    print(time.strftime('%H:%M:%S'))


clicks = 0


# ------------------------------------------
# counter()
# ------------------------------------------
def counter():
    global clicks
    clicks += 1
    root.title(f'Counter: {clicks}')


# ------------------------------------------
#   CREATE BUTTONS
# ------------------------------------------
btn_time = Button(root, text="Check time", command=check_time)
btn_time.pack()

btn_cnt = Button(root, text="Counter", command=counter)
btn_cnt.pack()

root.mainloop()
