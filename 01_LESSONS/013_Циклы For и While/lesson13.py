##############################################
# 013_Циклы For и While
# python 3.x
# WebForMySelf - Андрей Кудлай, 2019
##############################################
# Writing sgiman, 2025

i = 1
while i <= 10:
    print(i, end=' ')
    # i = i + 1
    i += 1

################################################
print()
print('hello', 'world', sep='!', end=' | ')     # сепаратор-разделитель и конец строки
print('hello2', 'world2')

################################################
s = 'Hello world'
for l in s:
    if l == ' ':
        continue
    print(f'"{l}"', end=' ')

################################################
print()
for i in 'Hello world':
    if i == ' ':
        break
    print(i, end=' ')
else:
    print('\nNo spaces')

################################################
for i in 'Helloworld':
    if i == ' ':
        break
    print(i, end=' ')
else:
    print('\nNo spaces')

################################################
# Вывод 1900 - 2025
year = 1900
while year <= 2025:
    print(year, end=' ')
    year += 1
else:
    print('Done')
