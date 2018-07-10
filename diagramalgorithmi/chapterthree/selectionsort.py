#! user/bin/env python
# -*- encoding:utf-8 -*-
"""
@time: 2018/07/02 22:19
@author: chaishunjin
@file:selectionsort.py
@software:Algorithm
@note:
"""


def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]  # 存储最小的值
            smallest_index = i  # 存储最小的值
    return smallest_index


# 选择排序
def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr


print(selectionSort([5, 3, 6, 2, 10]))
