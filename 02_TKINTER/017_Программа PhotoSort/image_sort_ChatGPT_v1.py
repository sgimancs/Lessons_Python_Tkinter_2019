########################################################################
# image_sort_ChatGPT
#
# PROMPT:
# Создать на python и tkinter программу сортировки фото и картинок
# из указанного каталога по дате последней модификации.
#-----------------------------------------------------------------------
# Функции программы:
#   Выбор папки с изображениями.
#   Поиск всех изображений (форматы .jpg, .jpeg, .png, .gif, .bmp, .tiff).
#   Сортировка по дате последней модификации (от новых к старым).
#   Отображение списка с датой и путем к файлу
#
########################################################################
import os
import tkinter as tk
from tkinter import filedialog, messagebox
from datetime import datetime

IMAGE_EXTENSIONS = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff')

def get_sorted_images_by_mod_time(folder_path):
    files = []
    for fname in os.listdir(folder_path):
        if fname.lower().endswith(IMAGE_EXTENSIONS):
            full_path = os.path.join(folder_path, fname)
            mod_time = os.path.getmtime(full_path)
            files.append((mod_time, full_path))
    # Сортировка по убыванию (новые выше)
    return sorted(files, key=lambda x: x[0], reverse=True)

def browse_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        sorted_images = get_sorted_images_by_mod_time(folder_selected)
        listbox.delete(0, tk.END)
        if not sorted_images:
            messagebox.showinfo("Результат", "Изображения не найдены в выбранной папке.")
            return
        for mod_time, path in sorted_images:
            date_str = datetime.fromtimestamp(mod_time).strftime('%Y-%m-%d %H:%M:%S')
            listbox.insert(tk.END, f"{date_str} - {path}")

# Создание окна
root = tk.Tk()
root.title("Сортировка изображений по дате модификации")
root.geometry("800x600")

# Кнопка выбора папки
btn_browse = tk.Button(root, text="Выбрать папку", command=browse_folder)
btn_browse.pack(pady=10)

# Список для вывода изображений
listbox = tk.Listbox(root, width=120, height=30)
listbox.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Запуск приложения
root.mainloop()
