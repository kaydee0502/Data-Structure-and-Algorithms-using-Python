# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 21:34:14 2020

@author: KayDee
"""

dump = int(input())
arr = list(map(int,input().split()))
arr.sort()
print(arr[-1]*arr[-2])