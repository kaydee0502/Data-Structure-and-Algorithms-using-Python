# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 12:08:53 2020

@author: KayDee
"""

def recsort(a):
    if len(a) <= 1:
        return
    
    temp = a.pop()
    recsort(a)
    recins(a,temp)
    
    
def recins(a,e):
    if not a:
        a.append(e)
        return
    if a[-1] <= e:
        a.append(e)
        return
    tep = a.pop()
    recins(a,e)
    a.append(tep)
        
    
    








arr = list(map(int,input("Enter an array : ").split()))
recsort(arr)
print(arr)
