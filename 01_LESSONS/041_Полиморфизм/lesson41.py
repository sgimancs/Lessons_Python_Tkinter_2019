# coding=utf-8
##############################################
# 041_Полиморфизм
# python 3.x
# WebForMySelf - Андрей Кудлай, 2019
##############################################
# Writing sgiman, 2025

from classes import Person, Employee

nc = 80
print()

# BASE (родительский класс)
person = Person('Katy', 30)
person.age = 35
person.print_info()     # основное инфо
print(person)           # имя класса
print('-' * nc)

# POLYMORPHISM (перегруженный класс)
employee = Employee('Nick', 30, 'Google')
employee.print_info()   # основное инфо
employee.more_info()    # доп. инфо (полиморфизм)
print(employee)         # имя класса
print('-' * nc)
