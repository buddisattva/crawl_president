import jieba
import re

f = open('pure_jieba.txt', 'r')
pure_content = f.read()
pure_content = re.sub(r'[\u0020\u00A0\f\t\r\n　]', '', pure_content)  # 去除雜訊

# 內文斷詞
jieba.set_dictionary('dict.txt.big')
jieba.add_word('世界和平日')
seg_list = jieba.cut(pure_content, cut_all=False)
words = ' '.join(seg_list)
words = re.sub(r'[、。，？！；「」《》(),（）:：]', '', words)
words = ' '.join(words.split())

print(words)

# 輸出斷詞後檔案
file = open("新春團拜/" + "總統府100年新春團拜暨茶會.txt", 'w', encoding = 'UTF-8')
file.write(words)
file.close()
