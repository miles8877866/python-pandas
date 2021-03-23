import matplotlib.pyplot as plt
import random
import pandas as pd
# 準備資料
data = pd.read_csv('hw0419.csv')
plt.subplot(1,2,1)
plt.boxplot(data['A_class'])
plt.title('scoreA')
plt.xlabel('A')
plt.ylabel('score')

for i in range(len(data['B_class'])):
    if data['B_class'][i] is None:
        data['B_class'].fillna(0)


plt.subplot(1,2,2)
plt.boxplot(data['B_class'])
plt.title('scoreB')
plt.xlabel('B')
plt.ylabel('score')
plt.show()