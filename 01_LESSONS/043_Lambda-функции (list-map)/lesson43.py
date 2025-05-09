# coding=utf-8
##############################################
# 043_Lambda-функции
# python 3.x
# WebForMySelf - Андрей Кудлай, 2019
##############################################
# Writing sgiman, 2025

import random

# Лямбда функции - анонимные функции, лямбда выражения
# Содержат только одно выражение
# Лямбда функции чаще используются в качестве аргумента
#
nc = 80
print()


def get_square(num):
    return num ** 2


print(get_square(5))
print('-' * nc)

get_square = lambda num: num ** 2  # не рекомендуется!!!
print(get_square(10))
print('-' * nc)

###############################################################

print((lambda num: num ** 2)(7))  # (lambda) + (аргумент)
print('-' * nc)

# ---------------------------
# Удвоение чисел в списке
# ---------------------------
l = [1, 2, 3]  # [2, 4, 6]


# With standard function
def get_double(l):
    return [i * 2 for i in l]


# With lambda function
def get_double(l):
    return list(map(lambda num: num * 2, l))    # "map iterator" - применить выражение (функцию) к каждому элементу последовательности (список/кортеж)


print(get_double(l))

print('-' * nc)

# Test map(func(),array) with lambda
print(list(map(lambda x: x/2, [1,2,3,4,5])))
print(list(map(lambda x: x/2, (1,2,3,4,5))))
print(list(map(lambda x: x/2, list(range(1,10)))))

print('-' * nc)

########################################################################

# Генерируем список из 10 случайных чисел от 1 до 100
random_numbers = [random.randint(1, 100) for _ in range(10)]
print(random_numbers)


