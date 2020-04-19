import matplotlib.pyplot as plt

import pandas as pd


motor = pd.read_csv("hw0419.csv")
ym = [None] * len(motor["ID"])
#use for to change data type
for i in range(len(motor["ID"])):
    ym[i]= str(motor["ID"][i])

motor["ID"] = ym #replace


plt.style.use("ggplot")
#畫第一條線，plt.plot(x, y, c)參數分別為x軸資料、y軸資料及線顏色 = 紅色
plt.plot(motor["ID"], motor["A_class"],c = "r")  
#畫第二條線，plt.plot(x, y, c)參數分別為x軸資料、y軸資料、線顏色 = 綠色及線型式 = -.
plt.plot(motor["ID"], motor["B_class"], "g-.")

# 設定圖例，參數為標籤、位置
plt.legend(labels=["A_class", "B_class"], loc = 'best')
plt.xlabel("ID", fontweight = "bold")                # 設定x軸標題及粗體
plt.ylabel("Score", fontweight = "bold")    # 設定y軸標題及粗體
plt.title("Score of A&B class", fontsize = 15, fontweight = "bold", y = 1.1)   # 設定標題、文字大小、粗體及位置
plt.xticks(rotation=45)   # 將x軸數字旋轉45度，避免文字重疊

# plt.savefig("score.png",   # 儲存圖檔
#             bbox_inches='tight',               # 去除座標軸占用的空間
#             pad_inches=0.0)                    # 去除所有白邊
# plt.close()      # 關閉圖表

plt.show()