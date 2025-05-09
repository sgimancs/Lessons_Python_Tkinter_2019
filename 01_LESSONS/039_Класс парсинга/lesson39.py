# coding=utf-8
##############################################
# 039_Класс парcинга
# python 3.x
# WebForMySelf - Андрей Кудлай, 2019
##############################################
# Writing sgiman, 2025

from Parser_class import Parser

nc = 80
print()

# -------------------------
#  PARSING HTML (web page)
# -------------------------
parser = Parser('https://www.ua-football.com/sport', 'news.txt')    # создать объект "parser"
parser.run()
print('-' * nc)

# TESTING
# print(parser.raw_html)    # сырой
# print('-' * nc)

# print(parser.html)        # обработанный
# print('-' * nc)

print(parser.results)       # результат (список словарей-новостей)
print('-' * nc)

