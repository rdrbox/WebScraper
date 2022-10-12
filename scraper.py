import re

import requests
import re

from bs4 import BeautifulSoup

url = input('Input the URL:')
ok_status = 200

if re.search('imdb.com/title', url):
    r = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})
    if r.status_code == ok_status:
        soup = BeautifulSoup(r.content, 'html.parser')
        title = soup.find('h1').text
        description = soup.find('span', {'data-testid': 'plot-l'}).text

        print({"title": title, "description": description})
else:
    print('Invalid movie page!')
