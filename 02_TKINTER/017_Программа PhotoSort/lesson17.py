# coding=utf-8
#######################################################
# 017_Программа PhotoSort (lesson17)
# python 3.x
# WebForMySelf - Андрей Кудлай, 2019
#######################################################
# Writing sgiman, 2025

from tkinter import *
from tkinter import filedialog      # браузер для файлов
from tkinter import messagebox      # выпадающие окна
from tkinter import ttk             # стиль OS
import os                           # OS path
from datetime import datetime       # дата-время

#--------------------------------------------------------------
# choose_dir() - выбор папки с изображениями
#--------------------------------------------------------------
def choose_dir():
    dir_path = filedialog.askdirectory()  # имя файла
    e_path.delete(0, END)            # очистить
    e_path.insert(0, dir_path)      # вставить


#--------------------------------------------------------------
#  f_start() - сортировка по дате модификации файла
#--------------------------------------------------------------
def f_start():
    cur_path = e_path.get()     # получить текущий путь
    if cur_path:                                            # если имеется текущий путь
        for folder, subfolders, files in os.walk(cur_path): # сканирование текущего директория
            for file in files:                              # только для файлов
                path = os.path.join(folder, file)           # полный путь к файлу - поддиректории игнорируются
                mtime = os.path.getmtime(path)              # дата модификации файла (timestamp)
                #print(mtime)    # test
                date = datetime.fromtimestamp(mtime)        # преобразовать дату (standard)
                #print(mtime)    # test
                date = date.strftime("%Y-%m-%d")            # YYYY-MM-DD (format)
                #print(mtime)   # test
                date_folder = os.path.join(cur_path, date)  # новый путь с датой
                #print(date_folder) # test
                if not os.path.exists(date_folder):         # если этот путь не существует
                    os.mkdir(date_folder)                   # создать папку ("mkdir")
                os.rename(path, os.path.join(date_folder, file))    # переместить в эту папку ("rename") - откуда куда
        messagebox.showinfo('Success', 'Сортировка выполнена успешно')
        e_path.delete(0, END)   # очистить поле ввода
    else:
        messagebox.showwarning('Warning', 'Выберите папку с фотографиями')


#=======================================
# О К Н О
#=======================================
root = Tk()
root.title('PhotoSort')
root.geometry("500x150+700+300")

# Шрифт
s = ttk.Style()
s.configure('my.TButton', font=("Helvetica", 15))

# Фрейм
frame = Frame(root, bg="#56ADFF", bd=5)
frame.pack(pady=10, padx=10, fill=X)

# Поле ввода
e_path = ttk.Entry(frame)
e_path.pack(side=LEFT, ipady=2, expand=True, fill=X)

# Кнопки
btn_dialog = ttk.Button(frame, text="Выбрать папку", command=choose_dir)
btn_dialog.pack(side=LEFT, padx=5)

btn_start = ttk.Button(root, text="Start", style="my.TButton", command=f_start)
btn_start.pack(fill=X, padx=10)

# Main cycle
root.mainloop()
