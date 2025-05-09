##########################################################
# 012_Виджеты Text и Scrollbar (lesson12)
# python 3.x
# WebForMySelf - Андрей Кудлай, 2019
###########################################################
# Writing sgiman, 2025

from tkinter import *

#---------------------------------
# Window
#---------------------------------
root = Tk()
root.geometry('400x300+700+300')

#=================================
# ACTIONS
#=================================
# Insert ("Hello")
def add_str():
    t.insert('2.4', 'Hello!')

# Insert (Text)
def add_text():
    text = "Почему он используется? Давно выяснено, что при оценке дизайна и композиции читаемый текст мешает сосредоточиться. \nLorem Ipsum используют потому, что тот обеспечивает более или менее стандартное заполнение шаблона, а также реальное распределение букв и пробелов в абзацах, которое не получается при простой дубликации.\nЗдесь ваш текст.. Здесь ваш текст.. Здесь ваш текст..\nМногие программы электронной вёрстки и редакторы HTML используют Lorem Ipsum в качестве текста по умолчанию, так что поиск по ключевым словам lorem ipsum сразу показывает, как много веб-страниц всё ещё дожидаются своего настоящего рождения. За прошедшие годы текст Lorem Ipsum получил много версий. \nНекоторые версии появились по ошибке, некоторые - намеренно (например, юмористические варианты)."
    t.insert('2.4', text)       # '2.4' - строка.позиция

# Delete
def del_str():
    # t.delete('2.4', '2.10')
    t.delete('1.0', END)        # удалить с 1-й строки и до конца

# Get
def get_str():
    print(t.get('1.0', END))    # вывести с 1-й строки и до конца

#---------------------------------
# Menu
#---------------------------------
f_menu = Frame(root, bg="#1F252A", height=40)
f_text = Frame(root)
f_menu.pack(fill=X)
f_text.pack(fill=BOTH, expand=1)

#---------------------------------
# Label Menu
#---------------------------------
l_menu = Label(f_menu, text="Menu", bg="#2B3239", fg="#C6DEC1", font=("Arial", "10"))
l_menu.place(x=10, y=10)

#---------------------------------
# Buttons
#---------------------------------
btn_add = Button(root, text="Hello", command=add_str).place(x=50, y=10)
btn_add_text = Button(root, text="Text", command=add_text).place(x=95, y=10)
btn_del = Button(root, text="Delete", command=del_str).place(x=140, y=10)
btn_get = Button(root, text="Get", command=get_str).place(x=190, y=10)

#---------------------------------
# Text Area
#---------------------------------
# bg - цвет фона
# fg - цвет текста
# padx, pady - отступы
# wrap - перенос текста (по словам или литерам)
# insertbackground - цвет курсора
# selectbackground - цвет выделенного текста
# width - значение для Scrollbar
# spacing3 - отступы в между строками

t = Text(f_text, bg="#343D46", fg="#C6DEC1",
         padx=10, pady=10, wrap=WORD,
         insertbackground="#EDA756", selectbackground="#4E5A65",
         width=30, spacing3=10)
t.pack(fill=BOTH, expand=1, side=LEFT)

#---------------------------------
# Scrollbar
#---------------------------------
scroll = Scrollbar(f_text, command=t.yview)     # скроллинг по вертикали (y)
scroll.pack(fill=Y, side=LEFT)                  # локализовать по оси Y слева
t.config(yscrollcommand=scroll.set)             # действие (функция)
print(t['width'], t['height'])                  # test

#=================================
# Main Cycle
#=================================
root.mainloop()

#---------------------------------------------------
# Lorem Ipsum
# https://ru.lipsum.com/
#---------------------------------------------------
