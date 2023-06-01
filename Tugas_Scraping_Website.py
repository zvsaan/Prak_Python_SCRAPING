import requests
from bs4 import BeautifulSoup as bs
import csv

URL = 'https://proxyway.com/news/page/'

titles_list = []
title_page6 = []

for page in range(1, 7):
    req = requests.get(URL + str(page) + '/')
    soup = bs(req.text, 'html.parser')

    titles = soup.find_all('h3', attrs={'class', 'archive-list__title'})

    count = 1
    for title in titles:
        d = {}
        d['Page Number'] = f'Page {page}'
        d['Title Number'] = f'Title {count}'
        d['Title Name'] = title.text
        count += 1
        titles_list.append(d)

    if page == 6:
        count = 1
        for title in titles:
            e = {}
            e['Page Number'] = f'Page {page}'
            e['Title Number'] = f'Title {count}'
            e['Title Name'] = title.text
            count += 1
            title_page6.append(e)

titles_all = titles_list + title_page6

filename = 'Tugas_Scraping_Website.csv'
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f, ['Page Number', 'Title Number', 'Title Name'])
    w.writeheader()
    w.writerows(titles_all)

print(' ')
print('Data telah berhasil disimpan dalam file', filename)