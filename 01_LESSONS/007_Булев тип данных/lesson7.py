##############################################
# 007_Булев тип данных
# python 3.x
# WebForMySelf - Андрей Кудлай, 2019
##############################################
# Writing sgiman, 2025

# CTRL + / - закоментировать несколько строк
# test = None     # неопределённая переменная
# test = 123
# print(test)

# x = 1
# y = 5
# x = 1; y = 5  # не рекомендуется
# x, y = (1, 5)   # кортеж
# print(x, y)

# bool
# my_true = True
# my_false = False
#
# print(type(my_true))
# print(type(my_false))

# приведение типов
# str(), int(), float(), bool()

x = 5.6
print(x, type(x))
x = int(x)
print(x, type(x))
x = str(x)
print(x, type(x))

x = bool(x)
print(x, type(x))

x = 0   # >0,<0 - True | 0, '', None - False
x = bool(x)
print(x, type(x))
