# coding=utf-8
##############################################
# 045_Модуль SQLite. Часть 1
# python 3.x
# WebForMySelf - Андрей Кудлай, 2019
##############################################
# Writing sgiman, 2025

# https://docs.python.org/3/library/sqlite3.html#module-sqlite3
# https://sqlitestudio.pl/index.rvt?act=download

import sqlite3

#################################
# CREATE DB (TABLE)
#################################
db = sqlite3.connect('test1_db.sqlite')
cursor = db.cursor()

# cursor.execute('''
# CREATE TABLE users (
#     id INTEGER PRIMARY KEY,
#     name TEXT NOT NULL,
#     email TEXT NOT NULL UNIQUE,
#     age INTEGER NOT NULL,
#     phone TEXT NOT NULL,
#     comment TEXT NOT NULL
# )
# ''')

cursor.execute('''
CREATE TABLE users (
    id INTEGER PRIMARY KEY UNIQUE, 
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    phone TEXT NOT NULL,
    comment TEXT NOT NULL     
)
''')


db.close()
