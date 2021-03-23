import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


df = pd.read_csv("hw0419.csv")

x = np.arange(len(df["ID"]))  # the label locations
x+=1#從ID1開始
width = 0.5  # the width of the bars

fig, ax = plt.subplots()#做子圖
rects1 = ax.bar(x - width/ 2, df["A_class"], width, label='A_Class')
rects2 = ax.bar(x + width/2, df["B_class"], width, label='B_Class')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Scores')
ax.set_title('Score of A&B')
ax.set_xticks(x)
ax.set_xticklabels(df["ID"])
ax.legend()


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects1)
autolabel(rects2)

fig.tight_layout()

plt.show()
