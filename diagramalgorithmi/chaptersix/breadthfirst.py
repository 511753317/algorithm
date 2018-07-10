#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/07/03 20:42
@author: 柴顺进
@file: breadthfirst.py 
@software:diagramalgorithm
@note: # 广度优先算法
"""
from collections import deque  # 使用函数deque来创建一个双端队列。

# 1。通过散列和列表来实现有向图结构
graph = {}
graph["you"] = ["alice", "bob", "claire"]  # 相当于 you-->alice,bob,claire这三个路径
graph["bob"] = ["anuj", "peggy"]  # 相当于 bob-->anuj,peggy这三个路径的有向图
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

search_queue = deque()  # 创建一个队列
search_queue += graph["you"]  # 将你的邻居都加入到这个搜索队列中


# 判断一个人是不是芒果销售商
def person_is_seller(name):
    return name[-1] == 'm'


# 实现有向图查找算法
def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []  # 这个列表用于记录检查过的人
    while search_queue:  # 只要队列不为空
        person = search_queue.popleft()  # 就取出其中的第一个人
        if not person in searched:  # 仅当这个人没检查过 才进行检查
            if person_is_seller(person):  # 检查这个人是否是芒果销售商
                print(person + " is a mango seller!")
                return True
            else:
                search_queue += graph[person]  # 不是芒果销售商。将这个人的朋友都加入搜索队列
                searched.append(person)  # 将这个人标记为检查过
    return False  # 如果到达了这里，就说明队列中没人是芒果销售商


search("you")
