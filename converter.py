#!/bin/env python3
# -*- coding: utf-8 -*

import urllib.request, list, settings
from bs4 import BeautifulSoup


def convert(from_, to, amount = 1) :
    url = 'http://www.xe.com/currencyconverter/convert/?Amount=' + str(amount) + '&From=' + from_ + '&To=' + to
    req = urllib.request.Request(url, headers = settings.headers)

    with urllib.request.urlopen(req) as response:
        html = response.read()

    soup = BeautifulSoup(html, 'html.parser')
    return soup.find('span', class_='uccResultAmount').get_text()
