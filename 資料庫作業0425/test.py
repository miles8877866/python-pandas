from matplotlib import pyplot as plt
import numpy as np
#定义两个矩阵
A1=np.array([0,0])
B1=np.array(([2,0],[0,2]))
#以 A1为均值，B1为协方差矩阵，生成正态分布的随机数
C1=np.random.multivariate_normal(A1,B1,10)
C2=np.random.multivariate_normal(A1+0.2,B1+0.2,10)
#画布的大小为长8cm高6cm
plt.figure(figsize=(8,6))
#画图吧，s表示点点的大小，c就是color嘛，marker就是点点的形状哦o,x,*><^,都可以啦
#alpha,点点的亮度，label，标签啦
plt.scatter(C1[:,0],C1[:,1],s=30,c='red',marker='o',alpha=0.5,label='C1')
plt.scatter(C2[:,0],C2[:,1],s=30,c='blue',marker='x',alpha=0.5,label='C2')
#下面三行代码很简单啦
plt.title('basic scatter plot ')
plt.xlabel('variables x')
plt.ylabel('variables y')

plt.legend(loc='upper right')#这个必须有，没有你试试看

plt.show()#这个可以没有