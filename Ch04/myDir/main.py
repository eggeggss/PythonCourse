# -*- coding: utf-8 -*-

import os

file="myFile.txt"

if os.path.exists(file):
    os.remove(file)
    
    
else:
    print("檔案未建立")
    #建立目錄
    if not (os.path.exists("myDir")):
       os.mkdir("myDir")

#os.mkdir() 建立目錄
#os.rmdir() 刪除目錄
#os.remove() 刪除檔案
#os.path.exists() 判斷是否存在

print ("*******")
#取得目前檔案路徑
print (os.path.abspath(__file__))
#取得目前目錄路徑
print (os.path.dirname(os.path.abspath(__file__)))
print (os.path.abspath(__file__))

#執行dos指令
#os.system("ifconfig")
os.system("cp main.py myDir")
