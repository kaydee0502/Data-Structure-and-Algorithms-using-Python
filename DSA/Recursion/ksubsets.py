# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 07:57:14 2020

@author: KayDee
"""

def ksubs(st,k,subs,subset):
    #print(st)
    
    if len(subs) == k:
        subset.append("".join(subs))
        return
    if len(st) == 0:
        return subs
    
        #return subs
        
    #print(st[-1])
    
        
    ksubs(st[1:],k,subs+[st[0]],subset)
    ksubs(st[1:],k,subs,subset)
    

subs = []
l = ksubs("kaydee",3,[],subs)
print(subs)