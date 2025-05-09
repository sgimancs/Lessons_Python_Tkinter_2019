##############################################
# 011_Форматирование строк
# python 3.x
# WebForMySelf - Андрей Кудлай, 2019
##############################################
# Writing sgiman, 2025

# CTRL+ALT+L - переформатирование кода

name = 'John'
age = 30

#---------------------------------------------------------
# УСТАРЕВШИЕ ВАРИАНТЫ (С/С++)
#---------------------------------------------------------
print('My name is ' + name + '. I\'m ' + str(age))  # с разрывом строки (классика)
print('My name is %(name)s. I\'m %(age)d' % {'name': name, 'age': age})  # старый вариант
print('My name is %s. I\'m %d' % (name, age))  # позиционные маркеры
print('Title: %s, Price: %.2f' % ('Sony', 40))

#---------------------------------------------------------
# format() - метод
#---------------------------------------------------------
print('My name is {}. I\'m {}'.format(name, age))  # позиционные аргументы
print('My name is {0}. I\'m {1}'.format(name, age))  # позиционные аргументы
print('My name is {name}. I\'m {age}'.format(name=name, age=age))  # именные аргументы
print('My name is {x}. I\'m {y}'.format(x=name, y=age))  # именные аргументы

title = 'Sony'
price = 40.55
print('Title: {}, Price: {}'.format(title, price))

###########################################################
# f-strings (новый метод форматирования, начиная c 3.6)
###########################################################
print(f'My name is {name}. I\'m {age}')
print(f'My name is {name}. I\'m {age + 5}')

print('5 + 2 = {}'.format(5 + 2))
print(f'5 + 2 = {5 + 2}')

print(f'Title: {title}, Price: {price}')
