import requests
from bs4 import BeautifulSoup
r = requests.get('https://comic.naver.com/webtoon/list.nhn?titleId=183559&weekday=mon')
html = r.text
info=[]

soup = BeautifulSoup(html, 'html.parser')
title=soup("td",{"class":"title"})
stars=soup("div",{"class":"rating_type"})
k=0
g=0
for titles in title:
    k+=1
for g in range(k):
    info.append([title[g].a.text,stars[g].strong.text])
    print("title:"+info[g][0]+" stars:"+info[g][1])