import requests

from bs4 import BeautifulSoup

r = requests.get('https://www.daum.net/')

soup = BeautifulSoup(r.text,'html.parser')

se = []
se=soup.select('ol.list_hotissue.issue_row > li ')

num=0
for s in se:
        num=num+1
        k = s.select('div[class=rank_cont]')[0]
        print(num, '위', k.select_one('span[class=txt_issue]').text)
