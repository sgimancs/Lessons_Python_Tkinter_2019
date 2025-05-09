######################################################################################
# ChatGPT (ООП)
#-------------------------------------------------------------------------------------
# Напиcать программу на python и tkinter c использованием классов ООП,
# состоящую из семи кнопок, цвета которых соответствуют цветам радуги.
# При нажатии на ту или иную кнопку в текстовое поле должен вставляться код цвета,
# а в метку – название цвета.
#
# Цвета радуги должны быть следующие:
# #ff0000: Красный
# #ff7d00: Оранжевый
# #ffff00: Желтый
# #00ff00: Зеленый
# #007dff: Голубой
# #0000ff: Синий
# #7d00ff: Фиолетовый
######################################################################################

import tkinter as tk


###########################################
#  RainbowApp (CLASS)
###########################################
class RainbowApp:
    #--------------------------------------
    # КОНСТРУКТОР
    #--------------------------------------
    def __init__(self, root):
        self.root = root
        self.root.title("Цвета радуги")

        # Словарь цветов радуги: код цвета и название
        self.colors = {
            "#ff0000": "Красный",
            "#ff7d00": "Оранжевый",
            "#ffff00": "Желтый",
            "#00ff00": "Зеленый",
            "#007dff": "Голубой",
            "#0000ff": "Синий",
            "#7d00ff": "Фиолетовый"
        }

        self.create_widgets()

    #--------------------------------------
    # create_widgets()
    #--------------------------------------
    def create_widgets(self):
        # Метка для названия цвета
        self.color_label = tk.Label(self.root, text="Выберите цвет", font=("Arial", 14))
        self.color_label.pack(pady=10)

        # Текстовое поле для HEX-кода
        self.color_entry = tk.Entry(self.root, font=("Arial", 14), justify="center")
        self.color_entry.pack(pady=10)

        # Рамка для кнопок (фрейм с отступами)
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        # Создание кнопок по цветам
        for color_code, color_name in self.colors.items(): # сканировать по ключу (color_code) и значению (color_name)
            btn = tk.Button(
                button_frame,   # frame
                bg=color_code,  # bg color
                width=10,       # width
                height=2,       # height
                command=lambda c=color_code: self.on_color_button_click(c)  # action
            )
            btn.pack(side=tk.LEFT, padx=5)


    #--------------------------------------
    # on_color_button_click()
    #--------------------------------------
    def on_color_button_click(self, color_code):
        color_name = self.colors[color_code]    # название цвета
        self.color_label.config(text=color_name)    # установить цвет
        self.color_entry.delete(0, tk.END)  # удалить (поле ввода)
        self.color_entry.insert(0, color_code)  # вставить (поле ввода)


###############################
# START
###############################
if __name__ == "__main__":
    root = tk.Tk()          # окно
    app = RainbowApp(root)  # RAINBOW OBJECT
    root.mainloop()         # главный цикл

#-------------------------------------------------------------------------------------------------------
# Особенности:
#  - Используется класс RainbowApp для всей логики интерфейса.
#  - Цвета радуги хранятся в словаре как атрибут класса.
#  - Методы create_widgets и on_color_button_click разделяют создание интерфейса и обработку событий.
#-------------------------------------------------------------------------------------------------------
