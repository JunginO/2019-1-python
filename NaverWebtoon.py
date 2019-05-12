import requests

from bs4 import BeautifulSoup

r = requests.get('https://comic.naver.com/webtoon/weekdayList.nhn?week=monC')

soup = BeautifulSoup(r.text,'html.parser')

names=soup.select('div.list_area.daily_img > ul > li')

for name in names:
    toonname = name.find('dt').text
    toonlink = name.find('a').get('href')
    print(toonname, toonlink)

