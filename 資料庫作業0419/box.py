import matplotlib.pyplot as plt
import random
import pandas as pd
# 準備資料
data = pd.read_csv('hw0419.csv')
plt.boxplot(data)
plt.title('score')
plt.xlabel('ID')
plt.ylabel('score')
plt.show()