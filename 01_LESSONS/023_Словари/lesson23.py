##################################################
# 023_Словари
# python 3.x
# WebForMySelf - Андрей Кудлай, 2019
##################################################
# Writing sgiman, 2025

# Словари - ассоциативные таблицы или хеш-массивы
nc = 80

d = {}  # пустой словарь

print(type(d), '\n', '-' * nc)

# стандартный словарь
product1 = {
    'title': 'Sony',
    'price': 100
}

product2 = dict(title='iPhone', price=110)  # конструктор словаря (возможны методы)

##################################################

# Список с вложенными списками
users = [
    ['bob@gmail.com', 'Bob'],
    ['katy@gmail.com', 'Katy'],
    ['john@gmail.com', 'John']
]

# Преобразовать список к словарю (ключ:значение)
d_users = dict(users)
print('СПИСОК:', users)
print('СЛОВАРЬ:', d_users)
print('-' * nc)

# Кортеж с вложенными кортежами
users_t = (
    ('bob@gmail.com', 'Bob'),
    ('katy@gmail.com', 'Katy'),
    ('john@gmail.com', 'John')
)

# Преобразовать кортеж в словарь
t_users = dict(users_t)

print('КОРТЕЖ:', users_t)
print('СЛОВАРЬ:', t_users)
print('-' * nc)

##################################################
print(d)  # пустой словарь
print(product1)
print(product2)

# Создание словаря из списка (метод - dict.fromkeys)
# product3 = dict.fromkeys(['price1', 'price2', 'price3'])  # price = None
product3 = dict.fromkeys(['price1', 'price2', 'price3'], 50)  # price = 50
print('-' * nc)
print(product3)
print('-' * nc)

# ГЕНЕРАТОР СЛОВАРЯ
nums = {i: i + 1 for i in range(1, 10)}  # ключ:значение (i:i+1) в диапазоне 1...9
print(nums)
print('-' * nc)

########################################
# ПОЛУЧЕНИЕ ДАННЫХ ИЗ СЛОВАРЯ
########################################
prod1 = {'title': 'Sony', 'price': 100}  # variant 1 - {'key': value,}
prod2 = dict(title='iPhone', price=110)  # variant 2 - dict(key=value,) c именованными аргументами

print('TITLE PROD1:', prod1['title'])
print('PRICE PROD1:', prod1['price'])
print('TITLE PROD2:', prod2['title'])
print('PRICE PROD2:', prod2['price'])
print('-' * nc)

print(prod1.get('title', 'NO'))  # if no key
print('-' * nc)

# print(nums['1'])          # error
print('NUMS[1]:', nums[1])  # OK
print('-' * nc)

print('TITLE:', prod1['title'])  # значения по ключу - если нет - "error"
print('TITLE:', prod1.get('title2'))  # метод get() - если нет "None"
print('TITLE:', prod1.get('title2', 'NO'))  # метод get() - если нет "NO"
print('-' * nc)

# ПЕРЕБРАТЬ СЛОВАРЬ
# variant1 - ключ: значение (с форматированием строки вывода)
for key in prod1:
    print(f'{key}: {prod1[key]}')
print('-' * nc)

# variant2 - метод items()
for key, value in prod1.items():
    print(key, value, sep=': ')
print('-' * nc)

# СПИСОК СЛОВАРЕЙ
products = [
    {'title': 'Sony', 'price': 100},
    {'title': 'iPhone', 'price': 110},
    {'title': 'Samsung', 'price': 90}
]

print(products)
print('-' * nc)

for product in products:
    print(product['title'], product['price'], sep=': ')  # вывод списка словарей

print('-' * nc)
