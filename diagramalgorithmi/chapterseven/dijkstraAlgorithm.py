#! user/bin/env python
# -*- encoding:utf-8 -*-

"""
@time: 2018/07/03 23:01
@author: chaishunjin
@file:dijkstraAlgorithm.py
@software:algorithm
@note:
"""
graph = {}  # 一个散列表,将所有邻居都存储在散列表中
graph["start"] = {}  # 使用另一个散列表，表示这些边的权重
graph["start"]["a"] = 6
graph["start"]["b"] = 2
graph["a"] = {}  # 添加其他节点及其邻居
graph["a"]["fin"] = 1
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5  # 终点没有任何邻居

# 用一个散列表来存储每个节点的开销
infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

# 一个存储父节点的散列表
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None
processed = []  # 用于记录处理过的节点，因为对于同一个节点，不能处理多次


def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:  # 遍历所有的节点
        cost = costs[node]
        # 如果当前节点的开销更低且未处理过，就将其视为开销最低的节点
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


# 在未处理的节点中找出开销最小的节点
node = find_lowest_cost_node(costs)
while node is not None:  # 这个while循环在所有节点都被处理过后结束
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():  # 遍历当前节点的所有邻居
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            # 如果经当前节点前往该邻居更近，就更新该邻居的开销
            costs[n] = new_cost
            # 将该邻居的父节点设置为当前节点
            parents[n] = node
    processed.append(node)  # # 将当前节点标记为处理过
    node = find_lowest_cost_node(costs)  # 找出接下来要处理的节点，并循环
