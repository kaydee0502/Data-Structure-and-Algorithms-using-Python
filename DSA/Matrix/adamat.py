# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 15:06:13 2020

@author: KayDee
"""

T = int(input())

def comp(a,b):
    if a < b:
        return 1
    else:
        return -1



while T:
    n = int(input())
    matrix = []
    crow = []
    ccol = []
    cs = 0
    
    for i in range(n):
        a = list(map(int,input().split()))
        matrix.append(a)
        ccol.append(a[0])
    crow = matrix[0]  
    cc = comp(crow[1],ccol[1])
    #print(crow)
    #print(ccol)
    for r in range(1,n):
        tc = comp(crow[r],ccol[r])
        if tc!=cc:
            cs+=1
        cc = tc
        #print(crow[r],ccol[r])
        
    if crow[-1] > ccol[-1]:
        cs+=1
    print(cs)
    T-=1