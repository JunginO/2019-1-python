import requests

from bs4 import BeautifulSoup

r = requests.get('https://www.naver.com/')

soup = BeautifulSoup(r.text,'html.parser')

s= soup.find_all('span',{'class':'ah_k'})
num=0
for x in s:
    num=num+1
    print("%d위:" %num, x.text)
