##############################################
# 015_Завершение программы Блокнот (lesson15)
# python 3.x
# WebForMySelf - Андрей Кудлай, 2019
##############################################
# Writing sgiman, 2025

from tkinter import *

# Импортировать классы дополнительно
from tkinter import messagebox
from tkinter import filedialog

#---------------------------------------------
# Window
#---------------------------------------------
root = Tk()
root.geometry('800x500+700+300')   # размер: (WxH) + (позиция окна: +X+Y)
root.iconbitmap('nt.ico')           # иконка
root.title('БЛОКНОТ TK')            # заголовок

main_menu = Menu(root)
root.config(menu=main_menu)

# Словарь тем
theme_colors = {
    "dark": {
        "text_bg": "#343D46", "text_fg": "#fff", "cursor": "#EDA756", "select_bg": "#4E5A65"
    },
    "light": {
        "text_bg": "#fff", "text_fg": "#000", "cursor": "#8000FF", "select_bg": "#777"
    }
}


#============================================
# A C T I O N S
#============================================
def about_program():
    messagebox.showinfo(title='About notepad', message='Программа Notepad Version 0.0.1')


def notepad_quit():
    answer = messagebox.askokcancel(title="Выход", message='Закрыть программу?')
    if answer:
        root.destroy()


def open_file():
    file_path = filedialog.askopenfilename(title="Выбор файла",
                                           filetypes=(("Текстовые документы (*.txt)", "*.txt"), ("Все файлы", "*.*")))
    if file_path:
        t.delete('1.0', END)
        f = open(file_path, 'r', encoding='utf-8')
        text = f.read()
        #t.insert('1.0', open(file_path, encoding='utf-8').read())
        t.insert('1.0', text)
        f.close()


def save_file():
    file_path = filedialog.asksaveasfilename(filetypes=(("Текстовые документы (*.txt)", "*.txt"), ("Все файлы", "*.*")))
    f = open(file_path, 'w', encoding='utf-8')
    text = t.get('1.0', END)
    f.write(text)
    f.close()


def change_theme(theme):
    t['bg'] = theme_colors[theme]['text_bg']
    t['fg'] = theme_colors[theme]['text_fg']
    t['insertbackground'] = theme_colors[theme]['cursor']
    t['selectbackground'] = theme_colors[theme]['select_bg']


#---------------------------------------------
# File Menu
#---------------------------------------------
file_menu = Menu(main_menu, tearoff=0)
file_menu.add_command(label="Открыть", command=open_file)
file_menu.add_command(label="Сохранить", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Выход", command=notepad_quit)
main_menu.add_cascade(label="Файл", menu=file_menu)

#---------------------------------------------
# Theme Menu
#---------------------------------------------
theme_menu = Menu(main_menu, tearoff=0)
theme_menu_sub = Menu(theme_menu, tearoff=0)
theme_menu_sub.add_command(label="Light Theme", command=lambda: change_theme('light'))
theme_menu_sub.add_command(label="Dark Theme", command=lambda: change_theme('dark'))
theme_menu.add_cascade(label="Оформление", menu=theme_menu_sub)
theme_menu.add_command(label="О программе", command=about_program)
main_menu.add_cascade(label="Разное", menu=theme_menu)

#---------------------------------------------
# TEXT AREA
#---------------------------------------------
f_text = Frame(root)
f_text.pack(fill=BOTH, expand=1)

# text - объект "t"
t = Text(f_text, bg=theme_colors['dark']['text_bg'], fg=theme_colors['dark']['text_fg'], padx=10, pady=10, wrap=WORD,
         insertbackground=theme_colors['dark']['cursor'], selectbackground=theme_colors['dark']['select_bg'],
         width=30, spacing3=10, font=("Courier New", 11))
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
