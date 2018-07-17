#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/07/17 16:53
@author: 柴顺进
@file: Elbowmethod.py 
@software:diagramalgorithm
@note: kmeans找到最佳K值的方式；肘部法则
"""  
import numpy as np
from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist
import matplotlib.pyplot as plt
cluster1 = np.random.uniform(0.5, 1.5, (2, 10))
cluster2 = np.random.uniform(3.5, 4.5, (2, 10))

X = np.hstack((cluster1, cluster2)).T

'''
参数的意义：
n_clusters:簇的个数，即你想聚成几类
init: 初始簇中心的获取方法
n_init: 获取初始簇中心的更迭次数
max_iter: 最大迭代次数（因为kmeans算法的实现需要迭代）
tol: 容忍度，即kmeans运行准则收敛的条件
precompute_distances：是否需要提前计算距离
verbose: 冗长模式（不太懂是啥意思，反正一般不去改默认值）
random_state: 随机生成簇中心的状态条件。
copy_x: 对是否修改数据的一个标记，如果True，即复制了就不会修改数据。
n_jobs: 并行设置
algorithm: kmeans的实现算法，有：'auto', 'full', 'elkan', 其中 'full'表示用EM方式实现
'''
K = range(1, 10)
# print(X)
meandistortions = []
for k in K:
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(X)
    meandistortions.append(sum(np.min(cdist(X,kmeans.cluster_centers_, 'euclidean'), axis=1)) / X.shape[0])
    '''
    # cdist(X, kmeans.cluster_centers_, 'euclidean')  求出X到cluster_centers_之间的距离
    #np.min(cdist(X,kmeans.cluster_centers_, 'euclidean'), axis=1)   按行的方向，对每一行求出一个最小值
    #sum(np.min(cdist(X,kmeans.cluster_centers_, 'euclidean'), axis=1)) 求出每次得到最小值列表的和
    # 求出每次最小值列表和的平均值
    '''
print(meandistortions)
plt.plot(K, meandistortions, 'bx-')
plt.xlabel('k')
# plt.ylabel('平均畸变程度',fontproperties=font)
plt.ylabel('Ave Distor')
# plt.title('用肘部法则来确定最佳的K值',fontproperties=font);
plt.title('Elbow method value K');
plt.show()