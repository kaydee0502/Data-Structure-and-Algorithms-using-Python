# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 20:41:01 2020

@author: KayDee
"""

T = int(input())
while T:
    n=int(input())
    arr = list(map(int,input().split()))
    cmf = 0
    for i in range(len(arr)):
        if arr[i] < 0 and cmf != 0:
            cmf = max(0,cmf+arr[i])
        if arr[i] > 0:
            cmf += arr[i]
    print(cmf)
            
    
    T-=1