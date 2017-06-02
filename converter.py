#!/bin/env python3
# -*- coding: utf-8 -*

import urllib.request, list
from bs4 import BeautifulSoup


user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
headers = {'User-Agent': user_agent}

def convert(from_, to, amount = 1) :
    url = 'http://www.xe.com/currencyconverter/convert/?Amount=' + str(amount) + '&From=' + from_ + '&To=' + to
    req = urllib.request.Request(url, headers = headers)

    with urllib.request.urlopen(url) as response:
        html = response.read()

    soup = BeautifulSoup(html, 'html.parser')
    return soup.find('span', class_='uccResultAmount').get_text()


if __name__ == '__main__':
    value = convert('USD', 'EUR', 500.54)
    print('1 USD =', value, 'EUR')
