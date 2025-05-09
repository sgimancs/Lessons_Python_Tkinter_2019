##########################################################
# 013_Виджеты Text и Scrollbar (lesson13)
# python 3.x
# WebForMySelf - Андрей Кудлай, 2019
###########################################################
# Writing sgiman, 2025

from tkinter import *

#---------------------------------------------
# Window
#---------------------------------------------
root = Tk()
root.geometry('600x400+700+300')

#=============================================
# M E N U
#=============================================
main_menu = Menu(root)          # экземпляр класса "Меnu" для окна "root"
root.config(menu=main_menu)

# main_menu.add_command(label="File")
# main_menu.add_command(label="About")


def about_program():
    print('ADOUT')


#---------------------------------------------
# File
#---------------------------------------------
file_menu = Menu(main_menu, tearoff=0)              # пункт меню (без отрыва) - "File"
main_menu.add_cascade(label="Файл", menu=file_menu) # каскадное меню "File" - прикрепить к "file_menu"

file_menu.add_command(label="Открыть")      # подменю "Open"
file_menu.add_command(label="Сохранить")    # подменю "Save"
file_menu.add_separator()                   # separator
file_menu.add_command(label="Выход")        # подменю "Exit"

#---------------------------------------------
# About
#---------------------------------------------
help_menu = Menu(main_menu, tearoff=0)                  # главный пункт меню (без отрыва) - "Help"
main_menu.add_cascade(label="Справка", menu=help_menu)  # главное каскадное меню "Help" - прикрепить к "help_menu"

# Вложенные меню
help_menu_sub = Menu(help_menu, tearoff=0)
help_menu_sub.add_command(label="Онлайн")
help_menu_sub.add_command(label="Оффлайн")

# Подменю
help_menu.add_cascade(label="Помощь", menu=help_menu_sub)
help_menu.add_command(label="О программе", command=about_program)

#---------------------------------------------
# TEXT AREA
#---------------------------------------------
# f_menu = Frame(root, bg="#1F252A", height=40)
# f_menu.pack(fill=X)
f_text = Frame(root)
f_text.pack(fill=BOTH, expand=1)

t = Text(f_text, bg="#343D46", fg="#C6DEC1", padx=10, pady=10, wrap=WORD,
         insertbackground="#EDA756", selectbackground="#4E5A65", width=30, spacing3=10)
t.pack(fill=BOTH, expand=1, side=LEFT)

#---------------------------------------------
# Scrollbar
#---------------------------------------------
scroll = Scrollbar(f_text, command=t.yview)
scroll.pack(fill=Y, side=LEFT)
t.config(yscrollcommand=scroll.set)


#=============================================
# MAIN CYCLE
#=============================================
root.mainloop()
