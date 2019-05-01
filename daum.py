import requests

from bs4 import BeautifulSoup

r = requests.get('https://www.daum.net/')

soup = BeautifulSoup(r.text,'html.parser')

s= soup.find_all('a',{'class':'link_issue'})
num=0
for x in s:
    num=num+1
    if num%2 == 0:
        k=num/2
        print("%d위:" %k, x.text)

