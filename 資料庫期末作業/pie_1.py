import pandas as pd
import matplotlib.pyplot as plt
import pymysql
plt.rcParams['font.sans-serif'] = ['SimSun'] # 步驟一（替換sans-serif字型）
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

h=0 #high level
m=0 #mid
l=0 #low

for i in range(len(stock['level'])):
    if(stock['level'][i]=='特優'):
        h+=1
    if(stock['level'][i]=='優'):
        m+=1
    if(stock['level'][i]=='良'):
        l+=1


plt.figure(figsize=(6,9)) #圖框架大小
category = ['特優', '優', '良'] # 製作圓餅圖的類別標籤
separeted = (0, 0.1, 0)                  # 依據類別數量，分別設定要突出的區塊

size = [h, m, l]     # 製作圓餅圖的數值來源
plt.pie(size,                           # 數值
        labels = category,                # 標籤
        autopct = "%1.1f%%",            # 將數值百分比並留到小數點一位
        explode = separeted,            # 設定分隔的區塊位置
        pctdistance = 0.6,              # 數字距圓心的距離
        textprops = {"fontsize" : 12},  # 文字大小
        shadow=True)                    # 設定陰影

plt.axis('equal')                                          # 使圓餅圖比例相等
plt.title("評價比例", {"fontsize" : 18})  # 設定標題及其文字大小
plt.legend(loc = "best")    
plt.show()
plt.savefig("evaluation of pie.png",   # 儲存圖檔
            bbox_inches='tight',               # 去除座標軸占用的空間
            pad_inches=0.0)                    # 去除所有白邊
