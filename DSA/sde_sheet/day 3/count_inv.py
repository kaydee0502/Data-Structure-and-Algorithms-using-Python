#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 16:13:24 2021

@author: kaydee
"""


inv = 0
def merge(l,r):
    global inv
    i = 0
    j = 0
    #print(l,r)
    
    
    n = []
    
    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            n.append(l[i])
            i+=1
        else:
            inv+=len(l) - i
            n.append(r[j])
            j+=1
        
        
    while i < len(l):
        n.append(l[i])
        i+=1
        
    while j < len(r):
        n.append(r[j])
        j+=1
    #print(inv)
    return n
        


def mergesort(a,left,right):
    if len(a) > 1:
        
        mid = (len(a))//2
        
        L = a[:mid]
        R = a[mid:]
        #print(L,R)
        L = mergesort(L,left,mid)
        R = mergesort(R,mid+1,right)
        #print(L,R)
        n = merge(L,R)
        
        
        return n
    else:
        return a
    

a = "468 335 1 170 225 479 359 463 465 206 146 282 328 462 492 496 443 328 437 392 105 403 154 293 383 422 217 219 396 448 227 272 39 370 413 168 300 36 395 204 312 323"
a = list(map(int,a.split()))
print(mergesort(a,0,len(a)-1))
print(inv)