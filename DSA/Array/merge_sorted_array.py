# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 20:59:09 2020

@author: KayDee
"""

arr1 = [1,13,55,210,1000,3000]
arr2 = [20,20,300,500,550,700,8000]
f_arr = []


while (len(arr1) != 0) and (len(arr2) !=0):
    if arr1[-1] > arr2[-1]:
        p = arr1.pop()
        f_arr.append(p)
    else:
        p = arr2.pop()
        f_arr.append(p)
        
a = arr1 if len(arr1)>len(arr2) else arr2

f_arr = a+f_arr[::-1]

print(f_arr)
    
    
        
        
        
        