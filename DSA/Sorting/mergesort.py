# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 13:31:33 2020

@author: KayDee
"""

a = [2, 65, 32,44,678,876,666,666,666,4444, 2, 1, 7, 8,1,15,12,0,0-1]

def mergeSort(arr):
    if len(arr) == 1:
        return arr
    left = arr[:len(arr)//2]
    right = arr[len(arr)//2:]
    print(left,right)
    
    return merge(mergeSort(left),mergeSort(right))
    
    
    
    
  
def merge(arr1,arr2):
    f_arr = []
    while (len(arr1) != 0) and (len(arr2) !=0):
        print(f_arr)
        if arr1[0] < arr2[0]:
            f_arr.append(arr1[0])
            arr1.pop(0)
        else:
            f_arr.append(arr2[0])
            arr2.pop(0)
    
    return f_arr +arr1 +arr2
    
res = mergeSort(a)
#print(merge([2,3,4,7],[1,3,5,7,9]))

print(res)

    