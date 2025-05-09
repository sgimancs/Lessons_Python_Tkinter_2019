# coding=utf-8
##############################################
# 038_Инкапсуляция
# python 3.x
# WebForMySelf - Андрей Кудлай, 2019
##############################################
# Writing sgiman, 2025

# Инкапсуляция - "сокрытие в капсуле" - область видимости
# C++: private (класс), public (все), protected (наследники)
# Полной инкапсуляции в Python нет...

from classes import Person

nc = 80
print()

person1 = Person('John')
person1.print_info()
person2 = Person('Katy')
# print(person2.__age)          # error
print('PROTECT:', person2._Person__age)  # ???? доступ к защищённому свойству (возможен, но не рекомендуется)
print('-' * nc)

# C помощью стандартных методов (способ 1)
print('AGE PERSON2 GET_AGE():', person2.get_age())  # метод для возврата защищенного параметра
person2.set_age(25)  # метод для установки защищенного параметра
print('-' * nc)

# С помощью декораторов (способ 2)
print('PERSON2.AGE', person2.age)
person2.age = 35
person2.print_info()
print('-' * nc)
