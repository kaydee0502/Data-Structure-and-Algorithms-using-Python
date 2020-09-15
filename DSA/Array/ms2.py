# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 14:54:32 2020

@author: KayDee
"""

arr1 = [1,2,3,4]
arr2 = [-8,0,3,6,7,8]

def MergeSortedArray(arr1,arr2):
    
    val = arr1 + arr2
    arr1Item = arr1[0]
    arr2Item = arr2[0]
    i = 0
    j = 0
    SortedArray = []
    for k in range(len(val)):
        #print(arr1Item,arr2Item,i,j)
        if arr1Item <= arr2Item and i < len(arr1):
            SortedArray.append(arr1Item)
            i+=1
            if i < len(arr1):
                arr1Item = arr1[i]
        else:
            SortedArray.append(arr2Item)
            j+=1
            if j < len(arr2):
                arr2Item = arr2[j]
            
            
        
        
    return SortedArray
    
print(MergeSortedArray(arr1,arr2))