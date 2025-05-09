# coding=utf-8
##############################################
# 045_Модуль SQLite. Часть 3
# python 3.x
# WebForMySelf - Андрей Кудлай, 2019
##############################################
# Writing sgiman, 2025

# https://docs.python.org/3/library/sqlite3.html#module-sqlite3
# https://sqlitestudio.pl/index.rvt?act=download

import sqlite3

nc = 80
print()

#################################
# READ SQL
#################################

# -----------------------------------------------
#  СОЗДАНИЕ СЛОВАРЯ
# -----------------------------------------------
def dict_factory(cur, row):
    d = {}
    for idx, col in enumerate(cur.description):
        d[col[0]] = row[idx]
    return d

########################################################################
db = sqlite3.connect('test3_db.sqlite')
db.row_factory = dict_factory
cursor = db.cursor()

########################################################################
# SELECT SAMPLES
email = 'petrov@gmail.com'
cursor.execute(f"SELECT * FROM users WHERE email = '{email}'")  # не рекомендуется !!!
cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
res = cursor.fetchone()     # одна строка
print(res)
print('-' * nc)

email = 'petrov@gmail.com'
cursor.execute("SELECT * FROM users WHERE email = ? OR name = ?", (email, 'john Doe'))
res = cursor.fetchone()     # одна строка
print(res)
print('-' * nc)

email = 'petrov-x@gmail.com'
cursor.execute("SELECT * FROM users WHERE email = :email OR name = :name", {'email': email, 'name': 'John Doe'})
res = cursor.fetchone()     # одна строка
print(res)
print('-' * nc)

# SELECT ALL
cursor.execute("SELECT * FROM users")

res = cursor.fetchone()     # первая строка
print('fetchone:', res)
print('-' * nc)

res = cursor.fetchall()     # все строки (список кортежей)
print('fetchall:', res)
print('-' * nc)

# ALL USERS (name - email)
for user in res:
     print(user['name'], user['email'])

print('-' * nc)

########################################################################
# ADD USERS (total_changes) - WRITE
cursor.execute("INSERT INTO users (name, email, age, phone, comment) "
               "VALUES ('User 4', 'user4@gmail.com', 23, '0507654321', 'Test User4 (Add)')")

cursor.execute("INSERT INTO users (name, email, age, phone, comment) "
               "VALUES ('User 5', 'user5@gmail.com', 37, '0677654210','Test User5 (Add)')")

db.commit()

print(db.total_changes)
print('-' * nc)

db.close()
