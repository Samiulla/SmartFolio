#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 12:34:18 2021

@author: samiullashaikh
"""
import requests
from pyquery import PyQuery
import csv
import time
from random import random

def get_all_urls(r):
    html = r.text
    pq = PyQuery(html)
    tags = pq('a.bl_12')
    for tag in tags:
        yield tag.attrib['href']

money_quote_url = 'https://www.moneycontrol.com/india/stockpricequote/'

r = requests.get(money_quote_url)

stockurls = get_all_urls(r)

with open('pb_16_Feb.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    
    for stockurl in stockurls:
        if stockurl is None or stockurl == '':
            continue
        
        time.sleep(random())
        try:
            r = requests.get(stockurl)
        except:
            continue
        pq = PyQuery(r.text)
        pbtags = pq('td.nsepb')
        name = pq('div.inid_name')[0].getchildren()[0].text
        if pbtags is not None and len(pbtags) > 0:
            print([name, pbtags[0].text])
            writer.writerow([name, pbtags[0].text])
        else:
            print([name, '--'])
            writer.writerow([name, '--'])


