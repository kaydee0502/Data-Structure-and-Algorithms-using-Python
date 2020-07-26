# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 17:24:48 2020

@author: KayDee
"""

a = [2, 65, 32, 2, 1, 7, 8]

def selectionsort(n):
    for i in range(len(n)):
        m = i
        for j in range(i+1,len(n)):
            if n[j] < n[m]:
                m = j
        n[i],n[m] = n[m],n[i]
        
    return n

res = selectionsort(a)
print(res)
