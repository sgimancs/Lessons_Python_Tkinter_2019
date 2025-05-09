##############################################
# 030_Модули в Python
# python 3.x
# WebForMySelf - Андрей Кудлай, 2019
##############################################
# Writing sgiman, 2025

# https://docs.python.org/3/library/
# https://docs.python.org/3/library/index.html

import os  # standard lib
import random  # импортировать весь модуль
# from random import *  # импортировать все методы
# import random as r    # псевдоним
from random import randint, shuffle  # импортировать только методы

import libs

# from libs import get_count, get_len

nc = 80
print(__name__)
print()

print(os.getcwd())  # current directory
print('-' * nc)

print('random.randint:', random.randint(1, 100))  # random module (all)
print('randint:', randint(1, 100))  # methods randint & shuffle (from random module)
print('-' * nc)

#########################################################################
l = [1, 2, 3, 4, 5]
shuffle(l)  # случайно перемешать массив (список)
print('shuffle:', l)
print('-' * nc)

#########################################################################
print(__name__)
print('-' * nc)

#########################################################################
print(libs.get_count('hello', 'l'))
print(libs.get_len('hello'))
# print(get_count('hello', 'l'))
# print(get_len('hello'))
print('-' * nc)

#########################################################################
f = libs.get_count  # ссылка на функцию (для сокращения)
print(f('hello', 'l'))
print('-' * nc)


#########################################################################
def get_sum(a, b):
    return a + b


gs = get_sum  # ссылка на функцию (для сокращения)
print(gs(1, 2))
print('-' * nc)
