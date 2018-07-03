#! user/bin/env python
# -*- encoding:utf-8 -*-

"""
@time: 2018/07/02 23:10
@author: chaishunjin
@file:stackfack.py
@software:Algorithm
@note:
"""
from dis import dis


def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x - 1)


# dis(fact)
fact(3)
