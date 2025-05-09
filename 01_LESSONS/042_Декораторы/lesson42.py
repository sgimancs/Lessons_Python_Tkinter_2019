# coding=utf-8
##############################################
# 042_Декораторы
# python 3.x
# WebForMySelf - Андрей Кудлай, 2019
##############################################
# Writing sgiman, 2025

# фУНКЦИЯ ТАКЖЕ ЯВЯЛЕТСЯ ОБЪЕКТОМ (как и данные)

nc = 80
print()

# ---------------------------------------------
# Функция вызывает другую функцию
# ---------------------------------------------
def hello():
    return 'Hello, I am func "hello"'


def super_func(func):
    print('Hello, I am func "super_func"')
    print(func())  # выполнить переданную функцию func()


super_func(hello)  # вызов функции hello()
print('-' * nc)


# ---------------------------------------------
# Выполнить ссылку на функцию
# ---------------------------------------------
def hello():
    return 'Hello, I am func "hello"'


test = hello  # ссылка на функцию
print(test())  # выполнить функцию test() по ссылке на функцию hello()
print('-' * nc)


# ---------------------------------------------------
#  Д Е К О Р А Т О Р Ы (обёртки функций)
# передача функции в виде аргументов другой функции
# ---------------------------------------------------
# Идея декораторов
def my_decorator(func):
    def func_wrapper():     # Функция-Обёртка
        print('my_decorator:', 'Code before')
        func()
        print('my_decorator:', 'Code after')
    return func_wrapper


@my_decorator
def func_test():
    print('func_test:', 'Hello, I am func "func_test"')


# ----------------------
# Без @my_decorator
# ----------------------
# test = my_decorator(func_test)  # ссылка на функцию-декоратор
# test()

# С @my_decorator - синтаксический "сахар"
func_test()

print('-' * nc)

# ----------------------
#  DECORATOR SAMPLE
# ----------------------
def make_title(fn):                     # fn - ссылка на функцию
    def wrapped():                      # функция-обёртка
        title = fn()                    # выполнить fn() --> hi()
        title = title.capitalize()      # заглавные (заменить строку)
        title = title.replace(',', '')  # удалить запятые (заменить строку)
        return title

    return wrapped


@make_title     # декоратор
def hi():
    return 'hello, world'


print('hi(): ', hi())
print('-' * nc)
