# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 21:49:05 2020

@author: KayDee
"""

T = int(input())
while T:
    n,k = list(map(int,input().split()))
    arr = input()
    
    b = {"0":0,"1":0}
    for i in arr:
        b[i]+=1
        
    folds = n//k
    
    if b["0"]%folds!=0 or b["1"]%folds!=0:
        print("IMPOSSIBLE")
    else:
        
        b["0"] //= folds
        b["1"] //= folds
        
        s = "0"*b["0"] + "1"*b["1"]
        #print(s)
        res = ""
        
        for j in range(folds):
            if j%2==0:
                res+=s
            else:
                res+=s[::-1]
        print(res)
            
        
        
    T-=1