# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 11:47:58 2020

@author: KayDee
"""

def mergeSortedArray(m,n,s):
    
    
    try:
        item1 = m[0]
        item2 = n[0]
        
        if item1 > item2:
            s.append(item2)
            n.pop(0)
        else:
            s.append(item1)
            m.pop(0)
        
        mergeSortedArray(m,n,s)
    except:
        ret = (s + m + n)
    finally:
        return ret
        
#no loops, mergesorted using recursion@!!!!
    
    
result = mergeSortedArray([0,3,15,25,33,333],[3,6,19,34,332],[])
print(result)