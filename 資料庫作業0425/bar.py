import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import time

df=pd.read_csv('db1.csv')#匯入csv檔案
counts_of_item = df["ITEM"].value_counts()

trans = [counts_of_item]
trans2 = [df["ITEM"].unique()]

trans = [i for item in trans for i in item]
trans2 = [i for item in trans2 for i in item]

item = trans2[::1]#item
counts = trans[::1]#counts
total = [0]*len(item)
length = len(item)

for i in range(len(df["ID"])):
    for j in range(length):
        if df["ITEM"][i]==item[j]:
            total[j] += df["NT"][i]
width = 0.5
print(item)

dframe = pd.DataFrame({'item':item, 'total':total})
ax = dframe.plot.bar(x='item', y='total', label='Total(NT)',rot=40)
plt.xlabel("item")
plt.ylabel("Total")
ax.legend()

# Add some text for labels, title and custom x-axis tick labels, etc.

plt.savefig("bar.png",   # 儲存圖檔
            bbox_inches='tight',               # 去除座標軸占用的空間
            pad_inches=0.0)                    # 去除所有白邊
plt.close()      # 關閉圖表
