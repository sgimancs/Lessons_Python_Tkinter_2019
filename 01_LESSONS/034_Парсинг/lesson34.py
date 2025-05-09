# coding=utf-8
##############################################
# 034_Парсинг
# python 3.x
# WebForMySelf - Андрей Кудлай, 2019
##############################################
# Writing sgiman, 2025

# Console: help(modules) - python
# https://docs.python.org/3/py-modindex.html
# -------------------------------------------
# PIP:
# beautifulsoup4
# https://pypi.org/project/beautifulsoup4/
# -------------------------------------------
# CONSOLE:
# pip -V    (version)
# pip freeze (install)
# pip install beautifulsoup4
# (beautifulsoup4==4.13.4, soupsieve==2.7)
# -------------------------------------------
# 1 pip install beautifulsoup4
# 2 pip install requests
# 3 pip install fake-useragent
# 4 pip install lxml
# -------------------------------------------
# website:
# https://www.ua-football.com/sport
#

from bs4 import BeautifulSoup
import urllib.request

nc = 80
print()

# READ HTML
req = urllib.request.urlopen('https://www.ua-football.com/sport')
# print(req)  # test 1
html = req.read()   # "сырой" (необработанной) HTML
# print(html)  # test 2

# PARSING
soup = BeautifulSoup(html, 'html.parser')
news = soup.find_all('li', class_='liga-news-item') # получить список вех новостей (по выбранным тегам)
# print(news)   # test 3
results = []

# Найти необходимые элементы
for item in news:
    title = item.find('span', class_='d-block').get_text(strip=True)    # заголовок (без пробелов в начале и в конце)
    print(title)    # test 4

    desc = item.find('span', class_='name-dop').get_text(strip=True)    # описание (без пробелов в начале и в конце)
    print(desc)     # test 5

    href = item.a.get('href')   # ссылка (href) c тегом 'a'
    print(href)     # test 6

    print('-' * 128)

    # Добавить в список словарей
    results.append({
        'title': title,
        'desc': desc,
        'href': href,
    })

# Открыть (создать) и записать файл (классика)
f = open('news.txt', 'w', encoding='utf-8')

i = 1
for item in results:
    f.write(
        f'Новость № {i}\n\nНазвание: {item["title"]}\nОписание: {item["desc"]}\nСсылка: {item["href"]}\n\n**********************\n')
    i += 1

f.close()
