# coding=utf-8
##############################################
# 035_Ошибки и исключения
# python 3.x
# WebForMySelf - Андрей Кудлай, 2019
##############################################
# Writing sgiman, 2025

# -------------------------------------------
# Рейтинг языков программирования 2024-2025:
# Python — 1 место
# JavaScript — 2 место
# Java — 3 место
# Typescript — 4 место
# C# — 5 место
# PHP — 6 место
# C++ — 7 место
# C — 8 место

# from typing_extensions import no_type_check

nc = 80
print()

# EXCEPTIONS with ERROR:
# print('Hello')
# print(100 / 0)
# print(1 + '2')
# print(int('test'))

try:
     num = 100 / 0
except ZeroDivisionError:       # исключение при делении на ноль - продолжить с num=0
     num = 0
     print("EXCEPTION1:", num)
except TypeError:               # исключение для типа продолжить с num=1
     num = 1
     print("EXCEPTION1:", num)

try:
    num = 100 / 2
except Exception:                   # любое исключение
    num = 0
else:                               # если нет ошибок
    print("EXCEPTION2:", 'Else')
finally:                            # выполняется всегда
    print("EXCEPTION2:", 'Finally')

print('-' * nc)

print(num)
print('Hi')
print('-' * nc)

##########################################################
# --- Try 1 ---
while True:
    try:
        num = int(input('Enter your number: '))
        print(f'100 / {num} = {100 / num}')
        break
    except ZeroDivisionError:                           # исключение при делении на ноль
        print('The number must be greater than zero')
    except ValueError:                                  # исключение при ошибочном значении
        print('Must be a number')

# --- Try 2 ---
while True:
    try:
        num = int(input('Enter your number: '))
        print(f'100 / {num} = {100 / num}')
        break
    except Exception:                                   # любые исключения
        print('The number must be greater than zero')
