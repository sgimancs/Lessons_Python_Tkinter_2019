########################################################################
# image_sort_ChatGPT_v2
#
# PROMPT:
# Создать на python и tkinter программу сортировки фото и картинок
# из указанного каталога по дате последней модификации.
#
# Добавить:
#   - Возможность копирования/перемещения файлов.
#   - Визуальный предпросмотр миниатюр изображений.
#   - Фильтрация по дате, размеру и типу.
#
#-----------------------------------------------------------------------
# Функции программы:
#   Выбор папки с изображениями.
#   Поиск всех изображений (форматы .jpg, .jpeg, .png, .gif, .bmp, .tiff).
#   Сортировка по дате последней модификации (от новых к старым).
#   Отображение списка с датой и путем к файлу
#
# Добавлено:
#   Предпросмотр миниатюр изображений (с помощью PIL/Pillow).
#   Кнопки "Копировать" и "Переместить" выбранные файлы.
#
# Фильтры:
#   По типу файла (.jpg, .png, и т.д.).
#   По размеру файла (в KB).
#   По диапазону даты модификации.
#
#   pip install pillow
########################################################################

import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from datetime import datetime
from PIL import Image, ImageTk

IMAGE_EXTENSIONS = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff')

class ImageSorterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Сортировка изображений по дате модификации")
        self.root.geometry("1000x700")

        self.images_data = []
        self.selected_folder = ""

        self.setup_ui()

    def setup_ui(self):
        # Верхняя панель
        top_frame = tk.Frame(self.root)
        top_frame.pack(fill=tk.X, pady=5)

        tk.Button(top_frame, text="Выбрать папку", command=self.browse_folder).pack(side=tk.LEFT, padx=5)
        tk.Button(top_frame, text="Копировать", command=self.copy_selected).pack(side=tk.LEFT, padx=5)
        tk.Button(top_frame, text="Переместить", command=self.move_selected).pack(side=tk.LEFT, padx=5)

        # Фильтры
        filter_frame = tk.Frame(self.root)
        filter_frame.pack(fill=tk.X, padx=10)

        tk.Label(filter_frame, text="Тип:").pack(side=tk.LEFT)
        self.type_var = tk.StringVar()
        self.type_filter = ttk.Combobox(filter_frame, textvariable=self.type_var)
        self.type_filter['values'] = ('Все',) + IMAGE_EXTENSIONS
        self.type_filter.current(0)
        self.type_filter.pack(side=tk.LEFT, padx=5)

        tk.Label(filter_frame, text="Мин. размер (KB):").pack(side=tk.LEFT)
        self.min_size_var = tk.StringVar()
        tk.Entry(filter_frame, textvariable=self.min_size_var, width=6).pack(side=tk.LEFT, padx=5)

        tk.Label(filter_frame, text="Дата от (YYYY-MM-DD):").pack(side=tk.LEFT)
        self.date_from_var = tk.StringVar()
        tk.Entry(filter_frame, textvariable=self.date_from_var, width=10).pack(side=tk.LEFT, padx=5)

        tk.Label(filter_frame, text="Дата до:").pack(side=tk.LEFT)
        self.date_to_var = tk.StringVar()
        tk.Entry(filter_frame, textvariable=self.date_to_var, width=10).pack(side=tk.LEFT, padx=5)

        tk.Button(filter_frame, text="Применить фильтры", command=self.apply_filters).pack(side=tk.LEFT, padx=10)

        # Основная область
        main_frame = tk.PanedWindow(self.root, sashrelief=tk.RAISED, sashwidth=4)
        main_frame.pack(fill=tk.BOTH, expand=1)

        # Список файлов
        left_frame = tk.Frame(main_frame)
        self.listbox = tk.Listbox(left_frame, selectmode=tk.SINGLE, width=80)
        self.listbox.pack(fill=tk.BOTH, expand=True)
        self.listbox.bind("<<ListboxSelect>>", self.show_thumbnail)

        # Область предпросмотра
        right_frame = tk.Frame(main_frame)
        self.preview_label = tk.Label(right_frame)
        self.preview_label.pack(padx=10, pady=10)

        main_frame.add(left_frame)
        main_frame.add(right_frame)

    def browse_folder(self):
        self.selected_folder = filedialog.askdirectory()
        if self.selected_folder:
            self.load_images()

    def load_images(self):
        self.images_data.clear()
        self.listbox.delete(0, tk.END)
        for fname in os.listdir(self.selected_folder):
            if fname.lower().endswith(IMAGE_EXTENSIONS):
                path = os.path.join(self.selected_folder, fname)
                mod_time = os.path.getmtime(path)
                size_kb = os.path.getsize(path) // 1024
                self.images_data.append({
                    'path': path,
                    'mod_time': mod_time,
                    'size_kb': size_kb,
                    'ext': os.path.splitext(fname)[1].lower()
                })
        self.images_data.sort(key=lambda x: x['mod_time'], reverse=True)
        self.update_listbox()

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for img in self.images_data:
            date_str = datetime.fromtimestamp(img['mod_time']).strftime('%Y-%m-%d %H:%M:%S')
            self.listbox.insert(tk.END, f"{date_str} - {os.path.basename(img['path'])}")

    def apply_filters(self):
        filtered = []
        type_filter = self.type_var.get()
        min_size = int(self.min_size_var.get()) if self.min_size_var.get().isdigit() else 0
        date_from = self.parse_date(self.date_from_var.get())
        date_to = self.parse_date(self.date_to_var.get(), end=True)

        for img in self.images_data:
            if type_filter != 'Все' and img['ext'] != type_filter:
                continue
            if img['size_kb'] < min_size:
                continue
            if date_from and img['mod_time'] < date_from.timestamp():
                continue
            if date_to and img['mod_time'] > date_to.timestamp():
                continue
            filtered.append(img)

        self.images_data = filtered
        self.update_listbox()
        self.preview_label.config(image='')

    def parse_date(self, date_str, end=False):
        try:
            if date_str:
                dt = datetime.strptime(date_str, "%Y-%m-%d")
                return dt.replace(hour=23, minute=59, second=59) if end else dt
        except:
            return None
        return None

    def show_thumbnail(self, event):
        selection = self.listbox.curselection()
        if not selection:
            return
        index = selection[0]
        img_path = self.images_data[index]['path']
        try:
            image = Image.open(img_path)
            image.thumbnail((300, 300))
            self.tk_image = ImageTk.PhotoImage(image)
            self.preview_label.config(image=self.tk_image)
        except Exception as e:
            self.preview_label.config(text="Ошибка при загрузке изображения")

    def copy_selected(self):
        self._move_or_copy_selected(move=False)

    def move_selected(self):
        self._move_or_copy_selected(move=True)

    def _move_or_copy_selected(self, move):
        index = self.listbox.curselection()
        if not index:
            messagebox.showwarning("Внимание", "Выберите файл из списка")
            return

        target_folder = filedialog.askdirectory(title="Выберите папку назначения")
        if not target_folder:
            return

        src_path = self.images_data[index[0]]['path']
        fname = os.path.basename(src_path)
        dst_path = os.path.join(target_folder, fname)

        try:
            if move:
                shutil.move(src_path, dst_path)
            else:
                shutil.copy2(src_path, dst_path)
            messagebox.showinfo("Успех", f"Файл {'перемещён' if move else 'скопирован'}: {dst_path}")
            self.load_images()
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось выполнить операцию: {e}")

# Запуск приложения
if __name__ == "__main__":
    root = tk.Tk()
    app = ImageSorterApp(root)
    root.mainloop()
