# -*- coding: utf-8 -*-

import requests
from requests.exceptions import ConnectionError
from bs4 import BeautifulSoup
from datetime import datetime, date
import jieba
import re
import time

# 網址list
address_list = []

for page_num in range(1, 2, 1):
    # 進入關鍵字「」的搜尋結果
    url_menu = "http://www.president.gov.tw/Default.aspx?tabid=131&&word1=%E5%9C%98%E6%8B%9C&word2=And&word3=%E6%96%B0%E6%98%A5&sd=2008/05/20&ed=2016/05/19&" + str(page_num)
    response_menu = requests.get(url_menu)
    soup_menu = BeautifulSoup(response_menu.text)
    # 單數篇搜尋結果
    search_table1 = soup_menu.findAll('tr', attrs={'class': 'wisemenu-twotrcolor'})
    for tag in search_table1:
        raw_link = tag.find('a', href=True)['href'].split('&')
        address_list.append("http://www.president.gov.tw" + raw_link[0] + "&" + raw_link[1])
    # 雙數篇搜尋結果
    search_table2 = soup_menu.findAll('tr', attrs={'class': 'wisemenu-trcolor'})
    for tag in search_table2:
        raw_link = tag.find('a', href=True)['href'].split('&')
        address_list.append("http://www.president.gov.tw" + raw_link[0] + "&" + raw_link[1])

file = open("新春團拜_address_list.txt", 'w', encoding='UTF-8')
for item in address_list:
    file.write("%s\n" % item)
file.close()

print(len(address_list))
