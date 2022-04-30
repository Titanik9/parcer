import requests
from bs4 import BeautifulSoup

url = 'https://auto.ru/cars/all/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
lol = soup.find_all('div', class_='ListingItemPrice__content')

for lol in lol:
    print(lol.text)