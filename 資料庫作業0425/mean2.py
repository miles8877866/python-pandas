import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df=pd.read_csv('db1.csv')#匯入csv檔案

trans = [df["ID"].unique()]
trans = [i for item in trans for i in item]

id= trans[::1]#counts
total = [0]*len(id)


for i in range(len(df["ID"])):
    for j in range(len(id)):
        if df["ID"][i]==id[j]:
            total[j] += df["NT"][i]

id = [0]*len(id)
X = list(zip(id, total))
X = np.array(X)
print(X)

plt.style.use('ggplot')
plt.figure(figsize=(8,6))
plt.scatter(X[:,0],X[:,1],s=50, marker='o',alpha=0.5,label='total of id')


from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=3)
kmeans.fit(X)
y_kmeans = kmeans.predict(X)

plt.scatter(X[:,0],X[:,1], c=y_kmeans, s=50, cmap='viridis')

centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5);
#下面三行代码很简单啦
plt.title('basic scatter plot ')
plt.ylabel('variables y')

plt.legend(loc='upper right')#这个必须有，没有你试试看

plt.show()#这个可以没有

