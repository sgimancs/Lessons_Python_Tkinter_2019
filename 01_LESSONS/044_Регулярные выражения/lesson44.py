# coding=utf-8
##############################################
# 044_Регулярные выражения
# python 3.x
# WebForMySelf - Андрей Кудлай, 2019
##############################################
# Writing sgiman, 2025

# https://ru.wikipedia.org/wiki/%D0%A0%D0%B5%D0%B3%D1%83%D0%BB%D1%8F%D1%80%D0%BD%D1%8B%D0%B5_%D0%B2%D1%8B%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F

# https://docs.python.org/3/library/re.html

# Регулярные выражения используются для поиска в строке некого шаблона

import re  # модуль для работы с регулярными выражениями

nc = 80
print()

s = 'Это просто строка текста. А это ещё одна строка текста.'  # исходная строка
pattern = 'строка'  # шаблон для поиска

# -----------------------------------------
#  STANDARD
# -----------------------------------------
print(s.find(pattern))  # index
print(pattern in s)  # bool
print('-' * nc)

##########################################
# MODULE RE
##########################################
# (1) re.search (метод)
pattern = 'строка'
if re.search(pattern, s):
    print('re.search:', 'Matched')
else:
    print('re.search:', 'No match')

match = re.search(pattern, s)   # поиск
print('START:', match.start())  # получить начало (index)
print('END:', match.end())      # получить конец (index)
print('-' * nc)

#####################################################
# (2) re.match (метод) - поиск с начала строки
# c учётом регистра
pattern = 'Это'
print('re.match:', re.match(pattern, s))
print('-' * nc)

#####################################################
# (3) re.findall - универсальный
pattern = 'строка'
print(re.findall(pattern, s))
print('-' * nc)

#####################################################
# (4) re.split
print('re.split:', re.split(r'\.', s))
print('-' * nc)

#####################################################
# SAMPLES (re.findall)
#####################################################
s = """Это просто строка текста.
А это ещё одна строка текста.
А это строка с цифрами: 1, 2, 3, 4, 5, 6, 7, 8, 9, ٣, 0, 10
А это строка с разными символами: '!', '@', '-', '&', '?', '_'
a\\b\tc
test string"""

pattern = r'\w+'            # 'w+' -  для поиска слов без спец. символов
# pattern = r'[а-яё]+'      # диапазон символов кириллицы
# pattern = r'[0-9]+'       # цифры
# pattern = r'[а-я0-9]+'    # кириллица и цифры
# pattern = r'\d+'          # только цифры
# pattern = r'[\da-]+'      #
# pattern = r'a\\b\tc'      #
# pattern = r'\w+$'         #

print(re.findall(pattern, s, flags=re.IGNORECASE))  # c игнорированием регистра
print('-' * nc)

#####################################################################
# VERIFICATION EMAIL
#####################################################################
# mail@mail.com
# kudlay@bank
# mail@google.com.ua


def validate_email(email):
    return bool(re.match(r'^.+@(\w+\.){0,2}[a-z]{2,6}$', email, re.IGNORECASE))   # Поиск:'^' - c начала, '$'- с конца


print(validate_email('mail@mail.com'))
print(validate_email('ivanov@bank'))
print(validate_email('mail@google.com.ua'))
print(validate_email('mail@google.com.infotest'))
