import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import time

df1=pd.read_csv('db1.csv')#匯入csv檔案
df2=pd.read_csv('db2.csv')


left = pd.DataFrame({
    'key':df1["ID"],
    'item':df1["ITEM"],
    'nt':df1["NT"]})

right = pd.DataFrame({
    'key':df2['ID'],
    'gender':df2['Gender']
    })

res = pd.merge(left,right, on='key')

sex = [0,1]
total = [0,1]

for i in range(len(res['key'])):
    if res['gender'][i]==1:
        total[1] += res['nt'][i]
    else:
        total[0] += res['nt'][i]    

data = pd.DataFrame({'gender':sex, 'total':total})

width = 0.5
fig, ax = plt.subplots()#做子圖
rects1 = ax.bar(sex[0], total[0], width, label='gender:0')
rects2 = ax.bar(sex[1], total[1], width, label='gender:1')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('total(NT)')
ax.set_title('the total payment of gender')
ax.legend()


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() , height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects1)
autolabel(rects2)

# Add some text for labels, title and custom x-axis tick labels, etc.

plt.savefig("bar_merge.png",   # 儲存圖檔
            bbox_inches='tight',               # 去除座標軸占用的空間
            pad_inches=0.0)                    # 去除所有白邊
plt.close()      # 關閉圖表
