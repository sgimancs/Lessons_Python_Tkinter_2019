##############################################
# 012_Оператор IF
# python 3.x
# WebForMySelf - Андрей Кудлай, 2019
##############################################
# Writing sgiman, 2025

# True, False (только c заглавной литеры)
# 0, None - это False
# Операторы сравнения:
# ==, != (<>), >, <, >=, <=
# print(3 == 3)

"""
if выражение 1:
    блок кода 1
elif выражение 2:
    блок кода 2
else:
    блок кода 3
"""

x = 0
if x:
    print('Переменная x вернула ИСТИНУ')
else:
    print('Переменная x вернула ЛОЖЬ')

if 1:
    print('Выражение истинно')
else:
    print('Выражение ложно')

###############################################################
light = 'blue'
if light == 'red':
    print('Stop')
elif light == 'yellow':
    print('Wait')
elif light == 'green':
    print('Go')
else:
    print('What?')

###############################################################
age = int(input('Сколько Вам лет? '))   # Ввод с консоли
if age >= 18:
    print('Добро пожаловать')
else:
    print(f'Вам {age} лет, не хватает {18 - age}')

###############################################################
time = 12
if time < 12 or time > 13:
    print('Open1')
else:
    print('Close1')

###############################################################
# or, and, not

time = 12
if time < 12 or time > 13:
    print('open2')
else:
    print('close2')

time = 8
day = 'st'
if time >= 8 and day != 'su':
    print('Open3')
else:
    print('Close3')

x = 0
if not x:
    print('OK')
else:
    print('NO')

###############################################################
# Аналог тернарного оператора
x = 1

res = 'OK' if x else 'NO'
print(res)
print('OK' if x else 'NO')
