##################################################
# КЛАССЫ (ПОЛИМОРФИЗМ)
# lesson38 (038_Инкапсуляция)
# lesson40 (040_Наследование)
##################################################
# Наследование позволяет создавать новый класс на основе существующего класса.
# Наследник наследует от родительского класса все публичные свойства и методы.
# Родительскй класс  - base class, parent class, super class.
# Дочерний класс (наследник) - подкласс, subclass.
# ------------------------------------------------
# Полиморфизм - изменение функционала
# от унаследованного базового класса
#
# Все классы наследуются от одного супер-класса "object"
#

class Person:
    # __parameter - защищенный (инкапсулирующий) - не доступен
    # _parameter - уровень соглашений для кодеров (считается защищённым параметром) - доступен

    # --------------------------------
    # КОНСТРУКТОР для "Person"
    # --------------------------------
    def __init__(self, name, age):
        self.name = name
        self.__age = age

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

    # Переопределить метод "__str__" для супер-класса "object"
    def __str__(self):
        # return f'Name: {self.name}'               # вернуть имя
        return 'Class ' + self.__class__.__name__   # вернуть имя класса


# --------------------------------
# Employee (наследник от Person)
# расширение базового класса
# П О Л И М О Р Ф И З М
# (перегружаемые методы)
# --------------------------------
class Employee(Person):

    # Переопределённый КОНСТРУКТОР для родителя "Person"
    def __init__(self, name, age, company):
        # super(Employee, self).__init__(name, age)    # OLDS (устарело)
        super().__init__(name, age)     # инициализация от родителя
        self.company = company          # доп. инициализация

    def more_info(self):
        print(f'{self.name} works in {self.company}')

    # Переопределённый (перегруженный) МЕТОД
    def print_info(self):
        super().print_info()            # метод от родителя
        print(f'Work: {self.company}')  # дополнительный функционал
