#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/07/10 16:13
@author: 柴顺进
@file: DecisionTree.py 
@software:diagramalgorithm
@note: 决策树使用sklearn代码实现
"""  
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import tree
import pydotplus
from IPython.display import display, Image

adult_data = pd.read_csv('./DecisionTree.csv')
feature_columns = [u'workclass', u'education', u'marital-status', u'occupation', u'relationship', u'race', u'gender', u'native-country']
label_column = ['income']

# 区分特征和目标列
features = adult_data[feature_columns]
label = adult_data[label_column]
# 对数据进行处理
features = pd.get_dummies(features)
# 初始化一个决策树分类器
clf = tree.DecisionTreeClassifier(criterion='entropy', max_depth=4)
# 用决策树分类器拟合数据
clf = clf.fit(features.values, label.values)

clf.predict(features.values)

# 可视化一下这颗决策树
dot_data = tree.export_graphviz(clf,
                                out_file=None,
                                feature_names=features.columns,
                                class_names = ['<=50k', '>50k'],
                                filled = True,
                                rounded =True
                               )

graph = pydotplus.graph_from_dot_data(dot_data)
display(Image(graph.create_png()))
plt.imshow(graph.create_png())
plt.show()