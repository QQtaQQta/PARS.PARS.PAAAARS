import requests
from bs4 import BeautifulSoup

lst = []
pages = 2

def get_news_info(page_number):
    mainURL = f'https://www.nstu.ru/news/?page={page_number}'
    response = requests.get(mainURL)
    soup = BeautifulSoup(response.text, 'lxml')
    news = soup.find_all('div', class_='bottomLine')

    for post in news:
        url = post.select('a')[1]
        title = url.text
        link = url['href']
        newsID = int(link[link.find('=')+1:-1])

        lst.append({'title': title, 'id': newsID, 'link': link})

for page in range(1, pages + 1):
    get_news_info(page)

with open("qwerty.txt", "w") as file:
    for news_item in lst:
        file.write(f"заголовок: {news_item['title']}\n")
        file.write(f"ID: {news_item['id']}\n")
        file.write(f"ссылка: {news_item['link']}\n\n\n\n")