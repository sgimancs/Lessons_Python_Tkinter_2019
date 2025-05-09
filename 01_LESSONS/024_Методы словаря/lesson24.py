##############################################
# 024_Методы словаря
# python 3.x
# WebForMySelf - Андрей Кудлай, 2019
##############################################
# Writing sgiman, 2025

import random

# dict.clear() - очищает словарь

# dict.copy() - возвращает копию словаря

# dict.get(key[, default]) - возвращает значение ключа, но если его нет,
# не бросает исключение, а возвращает default (по умолчанию None)

# dict.items() - возвращает пары (ключ, значение)
# dict.keys() - возвращает ключи в словаре

# dict.pop(key[, default]) - удаляет ключ и возвращает значение.
# Если ключа нет, возвращает default (по умолчанию бросает исключение)

# dict.popitem() - удаляет и возвращает пару (ключ, значение).
# Если словарь пуст, бросает исключение KeyError. Помните, что словари не упорядочены

# dict.setdefault(key[, default]) - возвращает значение ключа, но если его нет,
# не бросает исключение, а создает ключ со значением default (по умолчанию None)

# dict.update([other]) - обновляет словарь, добавляя пары (ключ, значение) из other.
# Существующие ключи перезаписываются. Возвращает None (не новый словарь!)

# dict.values() - возвращает значения в словаре

nc = 80
print()

product1 = {'title': 'Sony', 'price': 100}
print('ITEMS:', product1.items())
print('KEYS:', product1.keys())
print('-' * nc)

# МЕТОД POP()
print('POP:', product1.pop('title', 'NO'))  # Удалить ключ и вернуть значение - pop(). Если нет ключа,то 'NO"
print(product1)
print('-' * nc)

# МЕТОД SETDEFAULT()
product2 = {'title': 'Sony', 'price': 100}
print('BEFORE:', product2)
print('SETDEFAULT:', product2.setdefault('title2', 'test'))  # добавить по умолчанию, если нет ключа
print('AFTER:', product2)
print('-' * nc)

# МЕТОД UPDATE()
product3 = {'title': 'Sony', 'price': 100}
print('ORIG:', product3)
product3.update({'test': 'value'})  # добавить в словарь элемент (ключ:значение)
product3.update({'price': 200})     # заменить значение (price)
print('UPDATE:', product3)
print('-' * nc)

# МЕТОД VALUES()
print('VALUES:', product2.values())
print('-' * nc)
print()

"""
Создайте игру "Угадай число". 
В коде программы в переменную запишите любое число от 1 до 100 
(в следующих уроках мы узнаем, как генерировать случайное число), 
которое и должен угадать игрок. Далее программа должна спросить у игрока угадать число. 
Если пользователь не угадал число - программа сообщает, 
что загаданное число больше/меньше и предлагает попробовать еще раз, 
при этом программа ведет счета кол-ва попыток игрока. 
Если игрок угадал число, тогда программа благодарит за игру и сообщает кол-во попыток, 
за которое было угадано число.
"""

######################################################
# ChatGPT (1 sec)
######################################################
# import random

print('*' * nc)
print('ChatGPT')
print('*' * nc)

# Загадываем число от 1 до 10
secret_number = random.randint(1, 10)
attempts = 0  # Счётчик попыток

print("Добро пожаловать в игру 'Угадай число'!")
print("Я загадал число от 1 до 10. Попробуй угадать его.")

while True:
    guess = input("Введите ваше предположение: ")

    # Проверяем, что введено число
    if not guess.isdigit():
        print("Пожалуйста, введите число от 1 до 10.")
        continue

    guess = int(guess)
    attempts += 1

    if guess < secret_number:
        print("Загаданное число больше.")
    elif guess > secret_number:
        print("Загаданное число меньше.")
    else:
        print(f"Поздравляю! Вы угадали число за {attempts} попыток.")
        print("Спасибо за игру!")
        break
