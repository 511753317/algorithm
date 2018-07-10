#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/07/04 12:35
@author: 柴顺进
@file: Greedyalgorithm.py 
@software:diagramalgorithm
@note: 贪婪算法实现
"""  
states_needed = set(["mt", "wa", "or", "id", "nv", "ut","ca", "az"]) # 你传入一个数组，它被转换为集合

# 可供选择的广播台清单，使用散列表来表示
stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])
# 存储最终选择的广播台
final_stations = set()

best_station = None
states_covered = set()
while states_needed:
    for station, states_for_station in stations.items():
        covered = states_needed & states_for_station
        if len(covered) > len(states_covered):  # 计算交集
            best_station = station
            states_covered = covered

final_stations.add(best_station)
states_needed -= states_covered

print(final_stations)
