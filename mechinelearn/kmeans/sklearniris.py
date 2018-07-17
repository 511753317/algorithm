#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/06/29 13:52
@author: 柴顺进
@file: sklearniris.py 
@software:machineline
@note: 
"""  
from matplotlib import pyplot as plt
from sklearn import datasets

iris=datasets.load_iris()
x_index=3
color=['blue','red','green']
for label,color in zip(range(len(iris.target_names)),color):
    plt.hist(iris.data[iris.target==label, x_index],
        label=iris.target_names[label],
        color=color)
    plt.xlabel(iris.feature_names[x_index])
    plt.legend(loc='upper right')
plt.show()
