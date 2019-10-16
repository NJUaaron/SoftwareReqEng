import matplotlib.pyplot as plt
from gensim.models import word2vec
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans

def readFile(filePath):
    vecList = []
    with open(filePath, 'r') as f:
        for line in f:
            row = []
            serialNo = True
            for d in line.split(','):
                if not serialNo:
                    row.append(float(d))
                else:
                    serialNo = False
            vecList.append(row)
    return vecList

filePath = r"G:\学习\大四上\软件需求工程\作业\实验一\data\vec.csv"

X = readFile(filePath)
estimator = KMeans(n_clusters=3)#构造聚类器
estimator.fit(X)#聚类
label_pred = estimator.labels_ #获取聚类标签

x0 = X[label_pred == 0]
x1 = X[label_pred == 1]
x2 = X[label_pred == 2]
plt.scatter(x0[:, 0], x0[:, 1], c = "red", marker='o', label='label0')
plt.scatter(x1[:, 0], x1[:, 1], c = "green", marker='*', label='label1')
plt.scatter(x2[:, 0], x2[:, 1], c = "blue", marker='+', label='label2')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc=2)
plt.show()
