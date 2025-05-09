##############################################
# 031_Модуль Datetime
# python 3.x
# WebForMySelf - Андрей Кудлай, 2019
##############################################
# Writing sgiman, 2025

from datetime import date, datetime, timedelta  # импортировать только классы
import locale   # локальная кодировка

import random   # импортировать модуль 'random'
import os

nc = 80
print()

####################################################################
# date.today (базовый)
####################################################################
today = date.today()
print('TODAY:', today)              # текущая дата (en-format)
print('-' * nc)

print('TODAY-DAY:', today.day)            # день (свойство)
print('TODAY-MONTH:', today.month)        # месяц (свойство)
print('TODAY-YEAR:', today.year)          # год (свойство)
print('TODAY-WEEKDAY:', today.weekday())  # дни недели (0-6) - метод
print('-' * nc)

####################################################################
# datetime (альтернативный)
####################################################################
now = datetime.today()          # дата (вариант 1) - метод today()
now2 = datetime.now()           # дата (вариант 2) - метод now()
print(now, now2, sep='\n')
print('-' * nc)

print('NOW:', now)                      # 2025-04-24 05:16:06.809452
print('NOW-DAY:', now.day)              # день (свойство)
print('NOW-MONTH:', now.month)          # месяц (свойство)
print('NOW-YEAR:', now.year)            # год (свойство)
print('NOW-WEEKDAY:', now.weekday())    # дни недели (0-6) - метод
print('NOW-HOUR:', now.hour)            # часы (свойство)
print('NOW-MINUTE:', now.minute)        # минуты (свойство)
print('NOW-SECOND:', now.second)        # секунды (свойство)
print('-' * nc)

days = ['пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс']
print('NOW-WEEKDAY:', days[now.weekday()])  # день недели (ru-текст)
print('-' * nc)

locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')  # Cyrillic UTF-8
# locale.setlocale(locale.LC_ALL, 'ru_RU')

now = datetime.now()
print('DATETIME-NOW (RU):', now)
print('-' * nc)

####################################################################
# strftime (форматированный!!!)
####################################################################
print('NOW-STRFTIME (%a)', now.strftime('%a'))
print('NOW-STRFTIME (%A)', now.strftime('%A'))

print(f'Дата (%A, %d %b %Y): {now.strftime("%A, %d %b %Y")}')   # Date (ru-format)
print(f'Время (%H:%M:%S): {now.strftime("%H:%M:%S")}')          # Time (ru-format)
print('-' * nc)

print('Дата и время (%c):', now.strftime('%c'))
print('Только дата (%x):', now.strftime('%x'))
print('Только время (%X):', now.strftime('%X'))
print('-' * nc)

####################################################################
# timedelta
####################################################################
now = datetime.today()
print('Дата и время (%c):', now.strftime('%c'))
d1 = now + timedelta(days=1, hours=2, minutes=10)           # добавить и изменить дату
print('Дата и время (corrects) (%c):', d1.strftime('%c'))  # отформатировать и вывести
print('-' * nc)


######################################################################
# ChatGPT
# Написать функцию на python для получения дерева заданного каталога.
#  - Обходит все файлы и папки внутри заданного каталога.
#  - Рекурсивно обрабатывает вложенные папки.
#  - Формирует строку, представляющую дерево каталогов.
######################################################################
# import os

def get_directory_tree(path, prefix=''):
    tree_str = ''
    entries = sorted(os.listdir(path))                                  # LISTDIR
    for index, entry in enumerate(entries):                             # ЦИКЛ ENUMERATE
        full_path = os.path.join(path, entry)                           # PATH
        connector = '├── ' if index < len(entries) - 1 else '└── '      # ПСВЕДОГАФИКА + NAME
        tree_str += f"{prefix}{connector}{entry}\n"                     # форматированная строка
        if os.path.isdir(full_path):                                    # вывод
            extension = '│   ' if index < len(entries) - 1 else '    '  # ПСВЕДОГАФИКА + EXT
            tree_str += get_directory_tree(full_path, prefix + extension)
    return tree_str


# Пример использования:
if __name__ == "__main__":
    # directory = "."  # или укажите путь к нужному каталогу
    directory = "../"  # или укажите путь к нужному каталогу
    print(get_directory_tree(directory))

####################################################################
# ДОМАШНЕЕ ЗАДАНИЕ (lesson24, lesson25)
# Игра "Угадай число"
####################################################################
# import random

x = random.randint(1, 10)
user_num = 0
cnt = 0

while True:
    user_num = int(input('Я загадал число от 1 до 10 - угадай его: '))
    cnt += 1
    if user_num == x:
        print(f'Ты угадал число за {cnt} попыток')
        print("""
                ------------
                |           |
                |  0     0  |
                |     <     |
                |  .     .  |
                |   `...`   |
                ------------
                """)
        if input('Сыграем еще? "y|n":') == 'y':
            x = random.randint(1, 10)
            cnt = 0
        else:
            print('Спасибо за игру')
            break
    elif user_num > x:
        print('Мое число меньше')
    else:
        print('Мое число больше')

print('-' * nc)

##############################################################
# ChatGPT
##############################################################
def draw_smiley():
    smiley = [
        "╔═══════════╗",
        "║  ◕     ◕  ║",
        "║     ▄     ║",
        "║   ╚═══╝   ║",
        "╚═══════════╝"
    ]
    for line in smiley:
        print(line)


draw_smiley()

