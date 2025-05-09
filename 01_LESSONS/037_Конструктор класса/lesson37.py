# coding=utf-8
##############################################
# 037_Конструктор класса
# python 3.x
# WebForMySelf - Андрей Кудлай, 2019
##############################################
# Writing sgiman, 2025

from classes import Person
# import classes

# Экземпляры класса Person
person1 = Person('John')                # from classes import Person
# person1 = classes.Person('John')      # import classes

person1.print_info()

person2 = Person('Katy')
person2.print_info()
