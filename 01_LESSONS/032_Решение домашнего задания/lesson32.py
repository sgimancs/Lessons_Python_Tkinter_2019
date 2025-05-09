##############################################
# 032_Решение домашнего задания
# python 3.x
# WebForMySelf - Андрей Кудлай, 2019
##############################################
# Writing sgiman, 2025

##############################################
# ДЗ - ДЕРЕВО КАТАЛОГА
##############################################
import os

nc = 80
print()
print('-' * nc)

##############################################################
"""
    1-й элемент: Адрес очередного каталога в виде строки.
    2-й элемент: Список имён подкаталогов первого уровня вложенности для данного каталога.
    3-й элемент: Список имён файлов данного каталога.
"""
tree = os.walk('folder')    # генератор дерева (кортежи)
for f in tree:              # вывод кортежей дерева
    print(f)

print('-' * nc)


##############################################################
def read_dir(folder):
    for root, dirs, files in os.walk(folder):   # распаковка кортежа в переменные (root, dirs, files)
        level = root.count(os.sep)              # корректный слэш ("\" - win, "/" - unix)
        # print(root, files, level)             # test level
        indent = ' ' * 4 * level                # отступы (level)
        print(f'{indent}[{os.path.basename(root)}]')    # только базовые имена папок
        sub_indent = ' ' * 4 * (level + 1)  # отступы для вложенных папок
        # print(root, files, level, indent, sub_indent) # test
        for file in files:  # итоговое дерево
            print(f'{sub_indent}{file}')    # вывод дерева каталога


read_dir('folder')
print('-' * nc)


######################################################################
# ChatGPT
# Написать функцию на python для получения дерева заданного каталога.
#  - Обходит все файлы и папки внутри заданного каталога.
#  - Рекурсивно обрабатывает вложенные папки.
#  - Формирует строку, представляющую дерево каталогов.
######################################################################
# import os

"""
def get_directory_tree(path, prefix=''):
    tree_str = ''
    entries = sorted(os.listdir(path))  # LISTDIR
    for index, entry in enumerate(entries): # ЦИКЛ ENUMERATE
        full_path = os.path.join(path, entry)   # PATH
        connector = '├── ' if index < len(entries) - 1 else '└── '  # ПСВЕДОГАФИКА + NAME
        tree_str += f"{prefix}{connector}{entry}\n" # форматированная строка
        if os.path.isdir(full_path):    # вывод
            extension = '│   ' if index < len(entries) - 1 else '    '  # ПСВЕДОГАФИКА + EXT
            tree_str += get_directory_tree(full_path, prefix + extension)
    return tree_str

# Пример использования:
if __name__ == "__main__":
    # directory = "."  # или укажите путь к нужному каталогу
    directory = "../"  # или укажите путь к нужному каталогу
    print(get_directory_tree(directory))

"""