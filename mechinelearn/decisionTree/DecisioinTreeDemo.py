#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/07/10 17:23
@author: 柴顺进
@file: DecisioinTreeDemo.py 
@software:diagramalgorithm
@note: 决策树算法简单实现：ID3算法的信息增益来实现的
@reference：来源于https://blog.csdn.net/huahuazhu/article/details/73167610
"""  
from math import log
import operator
from mechinelearn.decisionTree import treePlotter  # 本文件同一目录下的文件


def createDataSet():
    """
    创建数据集使用
    :return:返回数据集和对应的标签页
    """
    dataSet = [[1, 1, 'yes'],
               [1, 1, 'yes'],
               [1, 0, 'no'],
               [0, 1, 'no'],
               [0, 1, 'no']]
    labels = ['no surfacing', 'flippers']
    return dataSet, labels


def calcShannonEnt(dataSet):
    """
    计算信息熵：第三步执行，给第二步找最佳属性调用
    :param dataSet: 数据集
    :return:返回信息熵
    """
    numEntries = len(dataSet)  # 样本数
    labelCounts = {}   # 创建一个数据字典：key是最后一列的数值（即标签，也就是目标分类的类别），value是属于该类别的样本个数
    for featVec in dataSet:  # 遍历整个数据集，每次取一行
        currentLabel = featVec[-1]  # 取该行最后一列的值
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    shannonEnt = 0.0  # 初始化信息熵
    for key in labelCounts:
        # 计算对应的label中每一种情况对应的比例
        prob = float(labelCounts[key])/numEntries
        shannonEnt -= prob * log(prob, 2)  # log base 2  计算信息熵
    return shannonEnt


# #### 按给定的特征划分数据 #########
def splitDataSet(dataSet, axis, value):  # axis是dataSet数据集下要进行特征划分的列号例如outlook是0列，value是该列下某个特征值，0列中的sunny
    retDataSet = []
    for featVec in dataSet:  # 遍历数据集，并抽取按axis的当前value特征进划分的数据集(不包括axis列的值)
        if featVec[axis] == value: #
            reducedFeatVec = featVec[:axis]    # chop out axis used for splitting
            reducedFeatVec.extend(featVec[axis+1:])
            retDataSet.append(reducedFeatVec)
            # print axis,value,reducedFeatVec
    # print retDataSet
    return retDataSet


# #### 选取当前数据集下，用于划分数据集的最优特征
def chooseBestFeatureToSplit(dataSet):
    """
    选取数据集的最优划分特征；第二步执行
    :param dataSet:
    :return:
    """
    numFeatures = len(dataSet[0]) - 1      # 获取当前数据集的特征个数，最后一列是分类标签
    baseEntropy = calcShannonEnt(dataSet)  # 计算当前数据集的信息熵
    bestInfoGain = 0.0; bestFeature = -1   # 初始化最优信息增益和最优的特征
    for i in range(numFeatures):        # 遍历每个特征iterate over all the features
        featList = [example[i] for example in dataSet]  # 获取数据集中当前特征下的所有值
        uniqueVals = set(featList)       # 获取当前特征值，例如outlook下有sunny、overcast、rainy
        newEntropy = 0.0
        for value in uniqueVals:    # 计算每种划分方式的信息熵
            subDataSet = splitDataSet(dataSet, i, value)
            prob = len(subDataSet)/float(len(dataSet))
            newEntropy += prob * calcShannonEnt(subDataSet)
        infoGain = baseEntropy - newEntropy     # 计算信息增益
        if (infoGain > bestInfoGain):       # 比较每个特征的信息增益，只要最好的信息增益
            bestInfoGain = infoGain         # if better than current best, set to best
            bestFeature = i
    return bestFeature                      # returns an integer


def majorityCnt(classList):
    """
    该函数使用分类名称的列表，然后创建键值为classList中唯一值的数据字典。字典
    对象的存储了classList中每个类标签出现的频率。最后利用operator操作键值排序字典，
    :param classList: 
    :return: 出现次数最多的分类名称
    """
    classCount = {}
    for vote in classList:
        if vote not in classCount.keys(): classCount[vote] = 0
        classCount[vote] += 1
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]

# #### 生成决策树主方法
def createTree(dataSet,labels):
    """
    决策树主方法；第一个执行
    :param dataSet:
    :param labels:
    :return:返回树结构
    """
    classList = [example[-1] for example in dataSet]  # 返回当前数据集下标签列所有值
    if classList.count(classList[0]) == len(classList):  # classList.count()统计第0个元素出现的次数
        # 当类别完全相同时则停止继续划分，直接返回该类的标签
        return classList[0]
    if len(dataSet[0]) == 1:  # 遍历完所有的特征时，仍然不能将数据集划分成仅包含唯一类别的分组 dataSet
        return majorityCnt(classList)  # 由于无法简单的返回唯一的类标签，这里就返回出现次数最多的类别作为返回值

    # 获取最好的分类特征索引
    bestFeat = chooseBestFeatureToSplit(dataSet)
    bestFeatLabel = labels[bestFeat]  # 获取该特征的名字

    # 这里直接使用字典变量来存储树信息，这对于绘制树形图很重要。
    myTree = {bestFeatLabel:{}}  # 当前数据集选取最好的特征存储在bestFeat中
    del(labels[bestFeat]) # 删除已经在选取的特征
    featValues = [example[bestFeat] for example in dataSet]
    uniqueVals = set(featValues)
    for value in uniqueVals:
        subLabels = labels[:]       # copy all of labels, so trees don't mess up existing labels
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeat, value),subLabels)
    return myTree


def classify(inputTree,featLabels,testVec):
    firstStr = inputTree.keys()[0]
    secondDict = inputTree[firstStr]
    featIndex = featLabels.index(firstStr)
    key = testVec[featIndex]
    valueOfFeat = secondDict[key]
    if isinstance(valueOfFeat, dict):
        classLabel = classify(valueOfFeat, featLabels, testVec)
    else: classLabel = valueOfFeat
    return classLabel

def storeTree(inputTree,filename):
    import pickle
    fw = open(filename,'w')
    pickle.dump(inputTree,fw)
    fw.close()

def grabTree(filename):
    import pickle
    fr = open(filename)
    return pickle.load(fr)


# 调用测试：------------------------------------------------
# dataSet, labels = createDataSet()





# ---------------------------------------------------------

if __name__ == '__main__':
    fr = open('tennies.txt')
    lenses = [inst.strip().split(' ') for inst in fr.readlines()]
    lensesLabels = ['outlook', 'temperature','huminidy','windy']
    lensesTree =createTree(lenses, lensesLabels)
    print(lensesTree)
    # treePlotter.createPlot(lensesTree)