# coding=utf-8
##############################################
# 040_Наследование
# python 3.x
# WebForMySelf - Андрей Кудлай, 2019
##############################################
# Writing sgiman, 2025

from classes import Person, Employee    # импорт классов "Person, Employee" из модуля "classes"

nc = 80
print()

person = Person('Katy', 30)
person.age = 35
person.print_info()
print('-' * nc)

employee = Employee('Nick', 30)
employee.print_info()   # метод из родительского класса "Person" (базовый)
employee.more_info()    # метод из дочернего класса "Person" (расширен)
print('-' * nc)
