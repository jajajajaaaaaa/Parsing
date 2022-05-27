import requests
from bs4 import BeautifulSoup
import csv
from time import sleep
from random import randint

f = open('anime.csv', 'w', encoding='UTF-8_sig', newline='\n')
file = csv.writer(f)
file.writerow(['title', 'text', 'Image URL'])

for ind in range(1, 7):
    url = 'https://myanimelist.net/topanime.php' + str(ind)
    r = requests.get(url)
    print(r.status_code)
    soup = BeautifulSoup(r.text, 'html.parser')
    section = soup.find('h3', class_="hoverinfo_trigger fl-l fs14 fw-b anime_ranking_h3")
    rating = section.find_all('span', class_ ='text on score-label score-9')
    for each in rating:
        category = each.aside.a.text
        title = each.header.h5.a.text
        text = each.p.text
        image_url = each.img.attrs.get('src')

        file.writerow([title, text, image_url])
    sleep(randint(15, 20))

f.close()