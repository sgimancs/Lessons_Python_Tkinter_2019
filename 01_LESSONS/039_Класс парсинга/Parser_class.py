#############################################
# PARSER CLASSES
# for lesson34 (034_Парсинг)
#############################################
from bs4 import BeautifulSoup
import urllib.request

#############################################
# Parser (класс)
#############################################
class Parser:

    # СВОЙСТВА
    raw_html = ''   # "сырой" (необработанной) HTML
    html = ''
    results = []    # список словарей с результатом

    # -------------------------------
    # КОНСТРУКТОР
    # -------------------------------
    def __init__(self, url, path):
        self.url = url      # адрес URL
        self.path = path    # путь (ссылка)

    # -------------------------------
    # GET HTML
    # -------------------------------
    def get_html(self):
        req = urllib.request.urlopen(self.url)  # запрос URL
        self.raw_html = req.read()              # Read HTML
        self.html = BeautifulSoup(self.raw_html, 'html.parser') # получить "сырой" HTML

    # -------------------------------
    # PARSING
    # -------------------------------
    def parsing(self):
        news = self.html.find_all('li', class_='liga-news-item')    # найти только блоки с новостями

        # Найти необходимые элементы (цикл)
        for item in news:
            title = item.find('span', class_='d-block').get_text(strip=True)    # заголовок (без пробелов в начале и в конце - stripe=True)
            desc = item.find('span', class_='name-dop').get_text(strip=True)    # описание (без пробелов в начале и в конце - stripe=True)
            href = item.a.get('href')   # ссылка (href) c тегом 'a'

            # Добавить в список словарей-новостей
            self.results.append({
                'title': title,
                'desc': desc,
                'href': href,
            })

    # -------------------------------
    # SAVE (file)
    # -------------------------------
    def save(self):
        # f = open(self.path, 'w', encoding='utf-8') # классика c ручным "f.close()"
        with open(self.path, 'w', encoding='utf-8') as f:   # открытие файла с помощью "with ... as" (файл закрывается автоматически в случае ошибке)
            i = 1
            for item in self.results:   # записать результат в файл
                f.write(
                    f'Новость № {i}\n\nНазвание: {item["title"]}\nОписание: {item["desc"]}\nСсылка: {item["href"]}\n\n**********************\n')
                i += 1

    # -------------------------------
    # ВЫПОЛНИТЬ (все методы)
    # -------------------------------
    def run(self):
        self.get_html()
        self.parsing()
        self.save()
