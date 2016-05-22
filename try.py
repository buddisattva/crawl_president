# -*- coding: utf-8 -*-

import requests
from requests.exceptions import ConnectionError
from bs4 import BeautifulSoup
from datetime import datetime, date
import jieba
import re

# 讀取網頁
response = requests.get("http://www.president.gov.tw/Default.aspx?tabid=131&itemid=36476")
soup = BeautifulSoup(response.text)

# 標題與日期萃取
title = soup.select('.Bulletinstitle')[0].text
date_ori = soup.select('.answer')[0]

# 日期格式處理
date_input = date_ori.text
date_input = date_input.strip()
date_input = date_input.strip('中華民國')
date_input = date_input.strip('日')
date_input = date_input.split('年')
year = int(date_input[0]) + 1911
date_input = date_input[1].strip('年').split('月')
date_output = date(year, int(date_input[0]), int(date_input[1])).strftime('%Y-%m-%d')

# 內文萃取
content = soup.select('.newscontent')[0]
content_text = content.text
content_text = re.sub(r'[\t\r\n　、。，？！；「」《》(),（）]', '', content_text)  # 去除雜訊
content_text = content_text.strip('這裡有一段影音')
# 去除講稿前面的文字
split_content = re.split(r'全文[\u2E80-\u9FFF]+：', content_text)
del split_content[0]
# 真正的講稿內容
pure_content = ''.join(split_content)

# 內文斷詞

jieba.set_dictionary('dict.txt.big')
seg_list = jieba.cut(pure_content, cut_all=False)
cut_words = ''.join(seg_list)
print(cut_words)

# 輸出斷詞後檔案
file = open(str(date_output) + "_" + str(title) + ".txt", 'w', encoding='UTF-8')
file.write(cut_words)
file.close()
