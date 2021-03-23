import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("C:\\Users\\as722\\Desktop\\資料庫\\資料庫作業0419\\hw0419.csv")
PassA = 0
FailA = 0
PassB = 0
FailB = 0

for i in range(len(data['A_class'])):
    if(data['A_class'][i]>59):
        PassA+=1
    else:
        FailA+=1

plt.figure(figsize=(6,9)) #圖框架大小
category = ['Pass', 'Fail'] # 製作圓餅圖的類別標籤
separeted = (0, 0.1)                  # 依據類別數量，分別設定要突出的區塊
size = [PassA, FailA]               # 製作圓餅圖的數值來源

plt.subplot(1,2,1)
plt.pie(size,                           # 數值
        labels = category,                # 標籤
        autopct = "%1.2f%%",            # 將數值百分比並留到小數點一位
         explode = separeted,            # 設定分隔的區塊位置
        pctdistance = 0.6,              # 數字距圓心的距離
        textprops = {"fontsize" : 12},  # 文字大小
        shadow=True)                    # 設定陰影

plt.axis('equal')                                          # 使圓餅圖比例相等
plt.title("Pie chart of A", {"fontsize" : 18})  # 設定標題及其文字大小
plt.legend(loc = "best")    

#B-----------------------------------------------------------------------------------------B

for i in range(len(data['B_class'])):
    if(data['B_class'][i]>59):
        PassB+=1
    else:
        FailB+=1

categoryB = ['Pass', 'Fail'] # 製作圓餅圖的類別標籤
# separeted = (0, 0, 0.3, 0, 0.3)                  # 依據類別數量，分別設定要突出的區塊
sizeB = [PassB, FailB]               # 製作圓餅圖的數值來源

plt.subplot(1,2,2)
plt.pie(sizeB,                           # 數值
        labels = category,                # 標籤
        autopct = "%1.2f%%",            # 將數值百分比並留到小數點一位
        explode = separeted,            # 設定分隔的區塊位置
        pctdistance = 0.6,              # 數字距圓心的距離
        textprops = {"fontsize" : 12},  # 文字大小
        shadow=True)                    # 設定陰影

 
plt.axis('equal')                                          # 使圓餅圖比例相等
plt.title("Pie chart of B", {"fontsize" : 18})  # 設定標題及其文字大小
plt.legend(loc = "best")                                   # 設定圖例及其位置為最佳

plt.show()
# plt.savefig("score use pie.png",   # 儲存圖檔
#             bbox_inches='tight',               # 去除座標軸占用的空間
#             pad_inches=0.0)                    # 去除所有白邊
# plt.close()      # 關閉圖表