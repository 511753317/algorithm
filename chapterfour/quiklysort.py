#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/07/03 17:49
@author: 柴顺进
@file: quiklysort.py 
@software:diagramalgorithm
@note: 
"""


def quicksort(array):
    if len(array) < 2:
        return array
    else:  #
        pivot = array[0]  # 递归条件,这个是每次选取数组的第一个值进行分组
        less = [i for i in array[1:] if i <= pivot]  # 通过函数式编程划分出比第一个小的
        greater = [i for i in array[1:] if i > pivot]  # 通过函数式编程划分出比第一个大的
        return quicksort(less) + [pivot] + quicksort(greater)  # 递归调用分组


print(quicksort([10, 5, 2, 3]))
