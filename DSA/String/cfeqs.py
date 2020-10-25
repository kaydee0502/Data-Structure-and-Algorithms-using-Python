# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 20:10:48 2020

@author: KayDee
"""

T = int(input())
while T:
    num = int(input())
    chars = ""
    chash = {}
    for i in range(num):
        chars += input()
        
    for j in chars:
        if not j in chash:
            chash[j] = 0
        chash[j]+=1
        
    for x,y in chash.items():
        if y % num != 0:
            print("NO")
            break
    else:
        print("YES")
        
    
    T-=1