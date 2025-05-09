##############################################
# 010_Методы строк
# python 3.x
# WebForMySelf - Андрей Кудлай, 2019
##############################################
# Writing sgiman, 2025

# Строка - неизменяемый массив
#
# https://docs.python.org/3/library/stdtypes.html#string-methods
# https://pythonworld.ru/tipy-dannyx-v-python/stroki-funkcii-i-metody-strok.html

"""
len(str) - Длина строки

str.capitalize() - Переводит первый символ строки в верхний регистр, а все остальные в нижний

str.center(width, [fill]) - Возвращает отцентрованную строку,
по краям которой стоит символ fill (пробел по умолчанию)

str.count(str, [start],[end]) - Возвращает количество непересекающихся вхождений подстроки
в диапазоне [начало, конец] (0 и длина строки по умолчанию)

str.find(str, [start],[end]) - Поиск подстроки в строке. Возвращает номер первого вхождения или -1

str.index(str, [start],[end]) - Поиск подстроки в строке. Возвращает номер первого вхождения или вызывает ValueError

str.replace(шаблон, замена) - Замена шаблона

str.split([символ])- Разбиение строки по разделителю

str.isdigit() - Состоит ли строка из цифр
str.isalpha() - Состоит ли строка из букв
str.isalnum() - Состоит ли строка из цифр или букв
str.islower() - Состоит ли строка из символов в нижнем регистре
str.isupper() - Состоит ли строка из символов в верхнем регистре
"""

s = 'hello'
print(len(s))

s2 = s.capitalize()
print(s, s2)
print(s.center(20, '!'))
print("*" * 20)

print(s.count('l', 0, 4))
print(s.find('a'))
print(s.index('o'))
print(s.replace('l', 't'))

s = 'Hello world'
print(s.split())  # список ['Hello', 'world']
s = 'Hello, world'
print(s.split(','))  # список ['Hello', 'world'] - для разделителя ","

print("*" * 20)

s = '123'
print(s.isdigit())
s = 'Hello'
print(s.isalpha())
