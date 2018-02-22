from bs4 import BeautifulSoup
from urllib import request, error

with request.urlopen('http://akipress.org/') as resp:
    data = resp.read()
    soup = BeautifulSoup(data,'html.parser')
    items = soup.find_all('a', attrs={'class': 'newslink'})
    for item in items:
        if 'svodka' in item.get('href'):
            news = request.urlopen(item.get("href"))
            news_data = news.read()
            item_soup = BeautifulSoup(news_data,'html.parser')
            news_item = item_soup.find(id='news_text')
            # print('result:', news_item)
            news_p = news_item.find_all('p')
            print(news_p.get_text())
