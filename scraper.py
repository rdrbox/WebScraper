import requests
import string, re

from bs4 import BeautifulSoup

url = 'https://www.nature.com/nature/articles?sort=PubDate&year=2020&page=3'
ok_status = 200

r = requests.get(url)

if r.status_code == ok_status:
    soup = BeautifulSoup(r.content, 'html.parser')
    for item in soup.findAll('li', {'class': 'app-article-list-row__item'}):
        article_type = item.find('span', {'data-test': 'article.type'}).text
        if article_type.strip() == 'News':
            url = item.find('a', {'data-track-action': 'view article'})['href']
            req = requests.get(f'https://www.nature.com{url}')
            if req.status_code == ok_status:
                soup_news = BeautifulSoup(req.content, 'html.parser')
                main_content = soup_news.find('div', {'class': 'c-article-body main-content'}).text
                title = soup_news.find('h1').text.strip()

                for i in title:
                    if i in string.punctuation:
                        title = title.replace(i, '')

                new_title = re.sub(r'\s', '_', title)

            with open(f"{new_title}.txt", "wb") as f:
                f.write(main_content.encode('utf-8'))


else:
    print('The URL returned', r.status_code)
