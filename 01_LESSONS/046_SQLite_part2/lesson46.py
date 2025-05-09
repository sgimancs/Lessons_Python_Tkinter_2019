# coding=utf-8
##############################################
# 046_Модуль SQLite. Часть 2
# python 3.x
# WebForMySelf - Андрей Кудлай, 2019
##############################################
# Writing sgiman, 2025

# https://docs.python.org/3/library/sqlite3.html#module-sqlite3
# https://sqlitestudio.pl/index.rvt?act=download

import sqlite3

#################################
# WRITE SQL
#################################

db = sqlite3.connect('test2_db.sqlite')
cursor = db.cursor()

# cursor.execute('''
# CREATE TABLE IF NOT EXISTS users (
#     id INTEGER PRIMARY KEY,
#     name TEXT NOT NULL,
#     email TEXT NOT NULL UNIQUE
# )
# ''')

# VARIANT 1 (STRING)
cursor.execute("INSERT INTO users (name, email, age, phone, comment) VALUES ('Иванов Иван', 'ivanov@gmail.com', 20, '0660419161', 'Test Person 1')")
cursor.execute("INSERT INTO users (name, email, age, phone, comment) VALUES ('Петров Пётр', 'petrov@gmail.com', 30, '0501234567', 'Test Person 2')")
cursor.execute("INSERT INTO users (name, email, age, phone, comment) VALUES ('Сидоров Сидор', 'sidorov@gmail.com', 40,'0671234567','Test Person 3')")
cursor.execute("INSERT INTO users (name, email, age, phone, comment) VALUES ('Пупкин Вася', 'pupkin@gmail.com', 25, '0991234567', 'Test Person 4')")

# VARIANT 2 (SCRIPT)
cursor.executescript('''
INSERT INTO users (name, email, age, phone, comment) VALUES ('John Doe', 'doe@gmail.com', 28, '0631234567', 'Test New 1');
INSERT INTO users (name, email, age, phone, comment) VALUES ('Nick Sand', 'sand@gmail.com', 32, '0441234567', 'Test New 2');
''')

# VARIANT 3 (ITERATION)
users = [
    ('User 1', 'user1@gmail.com', 21, '0507654321', 'Test User 1'),
    ('User 2', 'user2@gmail.com', 33, '0660504020', 'Test User 2'),
    ('User 3', 'user3@gmail.com', 42, '0931324589', 'Test User 3')
]
cursor.executemany("INSERT INTO users (name, email, age, phone, comment) VALUES (?, ?, ?, ?, ?)", users)

db.commit()

db.close()
