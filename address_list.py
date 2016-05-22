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

for page_num in range(1, 6, 1):
    # 進入關鍵字「全文」的搜尋結果
    url_menu = "http://www.president.gov.tw/Default.aspx?tabid=131&&word1=全文&sd=2008/05/20&ed=2016/05/19&size=100&currentpage=" + str(page_num)
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

file = open("address_list.txt", 'w', encoding = 'UTF-8')
for item in address_list:
    file.write("%s\n" % item)
file.close()

# # 把文章爬下來輸出成檔案
# for link in address_list:
#
#     # 網頁連結
#     url = str(link)
#
#     try:
#         response = requests.get(url)
#     except ConnectionError:
#         print('幹')
#         time.sleep(1)
#         response = requests.get(url)
#
#     soup = BeautifulSoup(response.text)
#
#     # 標題與日期萃取
#     title = soup.select('.Bulletinstitle')[0].text
#     date_ori = soup.select('.answer')[0]
#
#     # 日期格式處理
#     date_input = date_ori.text
#     date_input = date_input.strip()
#     date_input = date_input.strip('中華民國')
#     date_input = date_input.strip('日')
#     date_input = date_input.split('年')
#     year = int(date_input[0]) + 1911
#     date_input = date_input[1].strip('年').split('月')
#     date_output = date(year, int(date_input[0]), int(date_input[1])).strftime('%Y-%m-%d')
#
#     # 內文萃取
#     content = soup.select('.newscontent')[0]
#     content_text = content.text
#     content_text = re.sub(r'[\t\r\n　、。，「」《》(),；（）]', '', content_text) #去除雜訊
#     content_text = content_text.strip('這裡有一段影音')
#
#     # 內文斷詞
#
#     jieba.set_dictionary('dict.txt.big')
#     seg_list = jieba.cut(content_text, cut_all=False)
#     words = ' '.join(seg_list)
#
#     # 輸出斷詞後檔案
#     file = open("after_cut/" + str(date_output) + "_" + str(title) + ".txt", 'w', encoding = 'UTF-8')
#     file.write(words)
#     file.close()
