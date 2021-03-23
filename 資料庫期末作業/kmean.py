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
stock = pd.read_sql('SELECT * FROM final_view  order by Special_five', con = connect) #使用connect指定的Mysql獲取資料
#print(stock)

trans = [stock["add_code"].unique()]
trans = [i for item in trans for i in item]

id= trans[::1]#counts
total = [0]*len(id)

for i in range(len(stock["Special_five"])):
    for j in range(len(id)):
        if stock["add_code"][i]==id[j] and stock["level"][i] == "特優":
            total[j] += 3
        if stock["add_code"][i]==id[j] and stock["level"][i] == "優":
            total[j] += 2
        if stock["add_code"][i]==id[j] and stock["level"][i] == "良":
            total[j] += 1

X = list(zip(id,total))
X = np.array(X)
plt.style.use('ggplot')
plt.figure(figsize=(8,6))
plt.scatter(X[:,0],X[:,1],s=50, marker='o',alpha=0.5,label='各區權重(特優:3 優:2 良:1)')


from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=3)
kmeans.fit(X)
y_kmeans = kmeans.predict(X)

plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, s=50, cmap='viridis')

centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5);

plt.title('各區總權重之比較')
plt.xlabel('dist')
plt.ylabel('權重')

plt.legend(loc='upper right')
plt.show()

