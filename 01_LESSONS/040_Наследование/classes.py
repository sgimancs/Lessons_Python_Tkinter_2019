##################################################
# КЛАССЫ (НАСЛЕДОВАНИЕ)
# from lesson38 (038_Инкапсуляция)
##################################################
# Наследование позволяет создавать новый класс на основе существующего класса.
# Наследник наследует от родительского класса все публичные свойства и методы.
# Родительскй класс  - base class, parent class, super class.
# Дочерний класс (наследник) - подкласс, subclass.
#

class Person:
    # __parameter - защищенный (инкапсулирующий) - не доступен
    # _parameter - уровень соглашений для кодеров (считается защищённым параметром) - доступен

    # --------------------------------
    # КОНСТРУКТОР для "Person"
    # --------------------------------
    def __init__(self, name, age):
        self.name = name    # открытое св-во - доступно всем
        self.__age = age    # закрытое св-во - доступно только в базовом родителе

    # --------------------------------
    # print_info()
    # --------------------------------
    def print_info(self):
        print(f'Name: {self.name}, Age: {self.__age}')

    # --------------------------------
    # КЛАСCИЧЕCКИЙ МЕТОД для GET-SET
    # --------------------------------
    # def get_age(self):
    #     return self.__age
    #
    # def set_age(self, value):
    #     if value in range(1, 101):
    #         self.__age = value
    #     else:
    #         print('Wrong age')

    # --------------------------------
    # GET-SET с помощью декораторов
    # --------------------------------
    # GET
    @property
    def age(self):
        return self.__age

    # SET
    @age.setter
    def age(self, value):
        if value in range(1, 101):
            self.__age = value
        else:
            print('Wrong age')

# --------------------------------
# Employee (наследник от Person)
# расширение базового класса
# без конструктора
# --------------------------------
class Employee(Person):

    company = 'Google'

    def more_info(self):
        print(f'{self.name} works in {self.company}')
