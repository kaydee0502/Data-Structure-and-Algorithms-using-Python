# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 19:37:26 2020

@author: KayDee
"""
from collections import Counter as C
T = int(input())
while T:
    n = int(input())
    arr = list(map(int,input().split()))
    h1 = C(arr)
    h2 = C(h1.values())
    m = max(h2.values())
    res = []
    for i,j in h2.items():
        if j == m:
            res.append(i)
            
    print(min(res))
            
        
        
    #print(h2)
    T-=1