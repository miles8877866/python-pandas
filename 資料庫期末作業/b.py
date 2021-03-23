import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import pymysql
import numpy as np
plt.rcParams['font.sans-serif'] = ['SimSun'] # 步驟一（替換SimSun字型）
plt.rcParams['axes.unicode_minus'] = False  # 步驟二（解決座標軸負數的負號顯示問題）
MYSQL_HOST = 'localhost'
MYSQL_DB = 'db_demo'
MYSQL_USER = 'root'
MYSQL_PASS = 'n226165528'

connect = pymysql.connect(host = MYSQL_HOST, db = MYSQL_DB, user = MYSQL_USER, password = MYSQL_PASS,
            charset = 'utf8', use_unicode = True)
cursor = connect.cursor()
stock = pd.read_sql('SELECT * FROM final_view order by Special_five', con = connect) #使用connect指定的Mysql獲取資料
#print(stock)

counts_of_item = stock["dist"].value_counts()

trans = [counts_of_item]
trans2 = [stock["dist"].unique()]

trans = [i for item in trans for i in item]
trans2 = [i for item in trans2 for i in item]

item = trans2[::1]#item
counts = trans[::1]#counts
total = [0]*len(item)
length = len(item)

for i in range(len(stock["Special_five"])):
    for j in range(length):
        if stock["dist"][i]==item[j]:
            if(stock["level"][i] == "特優"):
                total[j] += 3
            if(stock["level"][i] == "優"):
                total[j] += 2
            if(stock["level"][i] == "良"):
                total[j] += 1
for i in range(length):
    total[i]=(total[i]/counts[i])
width = 0.5
print(item)

dframe = pd.DataFrame({'item':item, 'total':total})
ax = dframe.plot.bar(x='item', y='total', label='等級(平均)',rot=40)
plt.xlabel("區")
plt.ylabel("等級(特優:3，優:2，良:1)")
ax.legend()
plt.show()