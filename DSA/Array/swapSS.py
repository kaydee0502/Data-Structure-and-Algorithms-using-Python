# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 21:10:52 2020

@author: KayDee
"""

arr= [4,3,1,2]

r = len(arr)
i = 0
swaps = 0
while i < r:
   
    if arr[i] == i+1:
        i+=1
        continue
    else:
        
        arr[arr[i]-1],arr[i]=arr[i],arr[arr[i]-1]
        swaps += 1
        print(arr)
        #break
        