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

with open('pb_10_Mar.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    row = ['Name', 'P/B', 'P/E', 'Sector P/E', 'P/S']
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
        sec_pe_tags = pq('td.nsesc_ttm')
        petags = pq('td.nsepe')
        name = pq('div.inid_name')[0].getchildren()[0].text
        row = [name]
        if pbtags is not None and len(pbtags) > 0:
            row.append(pbtags[0].text)
        
        else:
            row.append('--')
        
        if petags is not None and len(petags) > 0:
            row.append(petags[0].text)
        
        else:
            row.append('--')
        
        if sec_pe_tags is not None and len(sec_pe_tags) > 0:
            row.append(sec_pe_tags[0].text)
        
        else:
            row.append('--')
            
        if row[-1] != '--' and row[-2] != '--':
            row.append(float(row[-2].replace(',',''))/float(row[-1].replace(',','')))
        else:
            row.append('--')
        writer.writerow(row)


