import requests

url = input('Input the URL:')
ok_status = 200

r = requests.get(url)

# if re.search('imdb.com/title', url):
#     r = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})
#     if r.status_code == ok_status:
#         soup = BeautifulSoup(r.content, 'html.parser')
#         title = soup.find('h1').text
#         description = soup.find('span', {'data-testid': 'plot-l'}).text
#
#         print({"title": title, "description": description})
# else:
#     print('Invalid movie page!')

if r.status_code == ok_status:
    with open('source.html', 'wb') as f:
        f.write(r.content)
    print('Content saved.')
else:
    print('The URL returned', r.status_code)
