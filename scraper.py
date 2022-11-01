import requests
import string
import re, os
import shutil

from bs4 import BeautifulSoup


def clear():
    with os.scandir('.') as it:
        for entry in it:
            if not entry.name.startswith(('.', '_')) and entry.is_dir():
                if re.match('Page', entry.name):
                    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), entry.name)
                    shutil.rmtree(path)


def soup_obj(url_, ok_status=200):
    r_ = requests.get(url_)
    if r_.status_code == ok_status:
        return BeautifulSoup(r_.content, 'html.parser')
    return r_.status_code


def get_page_list_posts(soup_):
    return soup_.findAll('li', {'class': 'app-article-list-row__item'})


def get_link_list_posts_type(list_post_, type_post):
    l_link = []
    for item in list_post_:
        article_type = item.find('span', {'data-test': 'article.type'}).text.strip()
        if article_type == type_post:
            url_ = item.find('a', {'data-track-action': 'view article'})['href']
            l_link.append(f'https://www.nature.com{url_}')

    return l_link


def get_title_content_post(soup_):
    content = soup_.find('div', {'class': 'c-article-body main-content'}).text
    title = soup_.find('h1').text.strip()
    return title, content


def new_file_name(title):
    for el in title:
        if el in string.punctuation:
            title = title.replace(i, '')

    return re.sub(r'\s', '_', title)


if __name__ == '__main__':
    clear()
    page = input()
    post_type = input()

    for i in range(1, int(page) + 1):
        os.mkdir(f'Page_{i}')
        url = f'https://www.nature.com/nature/articles?sort=PubDate&year=2020&page={i}'
        soup = soup_obj(url)
        list_post = get_page_list_posts(soup)
        list_link = get_link_list_posts_type(list_post, post_type)
        if len(list_link) == 0:
            continue

        for link in list_link:
            soup_link = soup_obj(link)
            title_link, content_link = get_title_content_post(soup_link)
            file_name = new_file_name(title_link)
            with open(f"./Page_{i}/{file_name}.txt", "wb") as f:
                f.write(content_link.encode('utf-8'))
