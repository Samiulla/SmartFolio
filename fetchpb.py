#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 20:25:15 2021

@author: samiullashaikh
"""


from nsetools import Nse
nse = Nse()
all_stock_codes = nse.get_stock_codes()

for symbol in all_stock_codes.keys():
    q = nse.get_quote(symbol)
    print(symbol, all_stock_codes[symbol], q['totalTradedVolume'], q['low52'], q['high52'], [], sep=',') 