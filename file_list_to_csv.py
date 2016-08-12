import os
from os import walk
import csv

os.chdir(os.path.dirname(__file__) + "/新春")

filelist = []
for (dirpath, dirnames, filenames) in walk(os.getcwd()):
    filelist.extend(filenames)
    break

# 把目錄下所有TXT檔案加到list裡面
txtfilelist = []
for filename in filelist:
    if os.path.splitext(filename)[1] == '.txt':
        txtfilelist.append(filename.split('.')[0])

print(txtfilelist)

# 準備好要紀錄資訊的csv檔
csvfile = open("新春系列文表格.csv", 'w', encoding='UTF-8')

for filename in txtfilelist:
    csvfile.write("%s" % filename.split('_')[0])
    csvfile.write(',')
    csvfile.write("%s" % filename.split('_')[1])
    csvfile.write('\n')

csvfile.close()
