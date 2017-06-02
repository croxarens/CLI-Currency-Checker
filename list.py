#!/bin/env python3
# -*- coding: utf-8 -*

import urllib.request
from bs4 import BeautifulSoup
import pickle
import os.path

user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
headers = {'User-Agent': user_agent}
url = 'http://www.xe.com/currency/'
data = ''

def list_currencies():
    cache_file = '/tmp/currencies.pickle'
    
    '''
    Check if the cache file exist.
    If so, load and return the values.
    '''
    if os.path.isfile(cache_file):
        with open(cache_file, 'rb') as f:
            currencies = pickle.load(f)

        return currencies

    # This part run only if the cache file has not been found
    req = urllib.request.Request(url, headers = headers)

    with urllib.request.urlopen(url) as response:
        html = response.read()

    soup = BeautifulSoup(html, 'html.parser')
    temp = {}

    for i in soup.find_all('li', class_='currencyListItem'):
        row = i.span.get_text()
        cur = row.split(' - ')
        temp[cur[0]] = cur[1]

    currencies = {}

    for key,value in sorted(temp.items()):
        currencies[key] = value

    del temp

    '''
    Save the result in a caching file
    '''
    with open(cache_file, 'wb') as f:
        pickle.dump(currencies, f)

    return currencies


# When the script is called alone
if __name__ == '__main__' :
    currencies = list_currencies()

    for k in currencies:
        print(k, ' - ', currencies[k])
