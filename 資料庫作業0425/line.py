import matplotlib.pyplot as plt

import pandas as pd

import time

data=pd.read_csv('db1.csv')#匯入csv檔案
x = [1,2,3,4,5,6,7,8,9,10,11,12]
y = [0,0,0,0,0,0,0,0,0,0,0,0]

for i in range(len(data['ID'])):
    if(data['MONTH'][i]==1):
        y[0]+=data['NT'][i]
    elif(data['MONTH'][i]==2):
        y[1]+=data['NT'][i]
    elif(data['MONTH'][i]==3):
        y[2]+=data['NT'][i]
    elif(data['MONTH'][i]==4):
        y[3]+=data['NT'][i]
    elif(data['MONTH'][i]==5):
        y[4]+=data['NT'][i]
    elif(data['MONTH'][i]==6):
        y[5]+=data['NT'][i]
    elif(data['MONTH'][i]==7):
        y[6]+=data['NT'][i]
    elif(data['MONTH'][i]==8):
        y[7]+=data['NT'][i]
    elif(data['MONTH'][i]==9):
        y[8]+=data['NT'][i]
    elif(data['MONTH'][i]==10):
        y[9]+=data['NT'][i]
    elif(data['MONTH'][i]==11):
        y[10]+=data['NT'][i]
    elif(data['MONTH'][i]==12):
        y[11]+=data['NT'][i]


plt.style.use("ggplot") 
plt.plot(x,y)

plt.legend(labels=["NT(10M)"], loc = 'best')
plt.xlabel('Month', fontweight="bold")

plt.ylabel('NT', fontweight="bold")

plt.savefig("line1.png",   # 儲存圖檔
            bbox_inches='tight',               # 去除座標軸占用的空間
            pad_inches=0.0)                    # 去除所有白邊
plt.close()      # 關閉圖表




