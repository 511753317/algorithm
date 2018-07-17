#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/07/17 19:59
@author: 柴顺进
@file: kmeansgraph.py 
@software:diagramalgorithm
@note: 
"""  
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import pairwise_distances_argmin
from sklearn.datasets import load_sample_image
from sklearn.utils import shuffle
from time import time
n_colors = 64
# 加载本地数据库里面的图片
china = load_sample_image("china.jpg")
# 转换为浮点数而不是默认的8位整数编码。
# 每一行有255个颜色分类
# 在[0-1]范围内
china = np.array(china, dtype=np.float64) / 255

# 45/5000加载图像并转换为2D numpy数组。
w, h, d = original_shape = tuple(china.shape)
assert d== 3
image_array = np.reshape(china, (w * h, d))
print("Fitting model on a small sub-sample of the data")
t0 = time()
image_array_sample = shuffle(image_array, random_state=0)[:1000]
kmeans = KMeans(n_clusters=n_colors, random_state=0).fit(image_array_sample)
print("done in %0.3fs." % (time() - t0))
# 获取所有的标签
print("Predicting color indices on the full image (k-means)")
t0 = time()
labels = kmeans.predict(image_array)
print("done in %0.3fs." % (time() - t0))

def recreate_image(codebook, labels, w, h):
#重新创建代码簿和标签中的（压缩）图像
    d = codebook.shape[1]
    image = np.zeros((w, h, d))
    label_idx = 0
    for i in range(w):
        for j in range(h):
            image[i][j] = codebook[labels[label_idx]]
            label_idx += 1
    return image

# 显示所有结果以及原始图像
plt.figure(1)
plt.clf()
ax = plt.axes([0, 0, 1, 1])
plt.axis('off')
plt.title('Original image (96,615 colors)')
plt.imshow(china)
plt.figure(2)
plt.clf()
ax = plt.axes([0, 0, 1, 1])
plt.axis('off')
plt.title('Quantized image (64 colors, K-Means)')
plt.imshow(recreate_image(kmeans.cluster_centers_, labels, w, h))
plt.show()