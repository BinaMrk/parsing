from bs4 import BeautifulSoup
import requests
import lxml


def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/108.0.0.0 Safari/537.36',
    }

    req = requests.get(url, headers=headers)
    return req


print(get_html('https://av.by/'))


def parse(html):
    soup = BeautifulSoup(get_html(html).text, 'html.parser')
    catalog_list = soup.find_all('li', 'catalog__item')
    for item in catalog_list:
        print(f'{item.a.attrs.get("href")}')
    return soup

parse('https://av.by/')

def parse(html):
    soup = BeautifulSoup(get_html(html).text, 'html.parser')
    price_byn = soup.find_all('div', 'listing-item__price')
    price_list = []
    for price in price_byn:
        price_encode_ = price.text.encode('ascii', errors='ignore')
        price_decode_ = price_encode_.decode('UTF-8')
        price_list.append(int(price_decode_[:price_decode_.index('.')]))
    print(f'The average price of a Mercedes: {sum(price_list) // len(price_list)}')
    print(f'Mercedes minimum price: {min(price_list)}')
    print(f'Mercedes maximum price: {max(price_list)}')


parse('https://cars.av.by/mercedes-benz')