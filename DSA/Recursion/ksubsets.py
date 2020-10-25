# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 07:57:14 2020

@author: KayDee
"""
subset = []
def ksubs(st,k,subs):
    #print(st)
    global subset
    if len(subs) == k:
        subset.append(subs)
    if len(st) == 0:
        return subs
    
        #return subs
        
    #print(st[-1])
    ksubs(st[:-1],k,subs+st[-1])
    ksubs(st[:-1],k,subs)
    


l = ksubs("kaydee",3,"")
print(list(set(subset)))