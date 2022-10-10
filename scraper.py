import requests, json

res = requests.get(input('Input the URL:'))

quote = res.json()

if quote.get('content') is None:
    print('Invalid quote resource!')
else:
    print(quote.get('content'))
