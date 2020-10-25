# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 05:40:41 2020

@author: KayDee
"""
from math import ceil

for _ in range(int(input())):
    n,l = map(int,input().split())
    que = list(map(int,input().split()))
    tur = []
    
    for i in que:
        tur.append(ceil(i/l))
        
    inds = [x for x in range(1,n+1)]
    
    quef = list(zip(tur,inds))
    quef.sort()
    ext = []
    for k in range(n):
        ext.append(quef[k][1])
    print("Case #{}:".format(_+1),*ext)
  