# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 16:42:15 2020

@author: KayDee
"""


def sprid(r,arr,c):
    #print(r,arr,arr[c])
    for i in range(len(arr)):
        if arr[i] == arr[c]:
            r[i] = True
    return r
    pass
T = int(input())
while T:
    n = int(input())
    arr = list(map(int,input().split()))
    st = [x+1 for x in range(n)]
    pos = []
    res = []
    for t in range(100):
        temp = []
        for i in st:
            temp.append(i+arr[i-1]*t)
            #print(i+arr[i-1]*t,end= " ")
        pos.append(temp)
        #print()
      
    for j in range(n):
        covid = j
        spread = [False for x in range(n)]
        spread[j] = True
        
        for k in pos:
            spread = sprid(spread,k,covid)
            #print(k,spread)
        res.append(sum(spread))
        
    print(min(res),max(res))
            
        
        
    #print(pos)
    T-=1