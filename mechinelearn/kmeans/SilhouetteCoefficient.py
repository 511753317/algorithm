#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/07/17 16:59
@author: 柴顺进
@file: SilhouetteCoefficient.py 
@software:diagramalgorithm
@note: 轮廓系数衡量聚类的分离度
"""  
import numpy as np
from sklearn.cluster import KMeans
from sklearn import metrics
import matplotlib.pyplot as plt

# 分割出6个子图， 并在1号作图
plt.figure(figsize=(8, 10))
plt.subplot(3, 2, 1)
# 初始化原始数字点
x1 = np.array([1, 2, 3, 1, 5, 6, 5, 5, 6, 7, 8, 9, 7, 9])
x2 = np.array([1, 3, 2, 2, 8, 6, 7, 6, 7, 1, 2, 1, 1, 3])
X = np.array(list(zip(x1, x2))).reshape(len(x1), 2)
# 在1号子图做出原始数据点阵的分布
# xlim 坐标的刻度
plt.xlim([0, 10])
plt.ylim([0, 10])
plt.title('Sample')
plt.scatter(x1, x2)

# 点的颜色
colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'b']
# 点的标号
markers = ['o', 's', 'D', 'v', '^', 'p', '*', '+']
# 簇的个数
tests = [2, 3, 4, 5, 8]
subplot_counter = 1  # 训练模型
for t in tests:
    subplot_counter += 1
    plt.subplot(3, 2, subplot_counter)
    kmeans_model = KMeans(n_clusters=t).fit(X)
    for i, l in enumerate(kmeans_model.labels_):
        plt.plot(x1[i], x2[i], color=colors[l], marker=markers[l], ls='None')
        plt.xlim([0, 10])
        plt.ylim([0, 10])
        # silhouette_score计算所有样本的平均轮廓系数。
        # kmeans_model.labels_ 每个样本的预测标签。即预测的类的标签
        # metric='euclidean' 用的方法为欧式距离
        plt.title('K = %s, SCoefficient = %.03f' % (t, metrics.silhouette_score(X, kmeans_model.labels_, metric='euclidean')))
plt.show()