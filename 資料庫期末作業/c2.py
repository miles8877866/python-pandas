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

counts_of_item = stock["level"].value_counts()

trans = [counts_of_item]
trans2 = [stock["dist"].unique()]

trans = [i for item in trans for i in item]
trans2 = [i for item in trans2 for i in item]

item = trans2[::1]#item
counts = trans[::1]#counts
totalH = [0]*len(item)
totalM = [0]*len(item)
totalL = [0]*len(item)
length = len(item)
for i in range(len(stock["Special_five"])):
    for j in range(length):
        if stock["dist"][i]==item[j] and stock["level"][i]=="優":
            totalH[j] += 1
width = 0.5
dframe = pd.DataFrame({'item':item, 'totalH':totalH})
ax = dframe.plot.bar(x='item', y='totalH', label='數量(間)',rot=40)
plt.xlabel("區")
plt.ylabel("數量(間)")
ax.legend()
plt.show()