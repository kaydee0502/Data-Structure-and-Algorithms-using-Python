# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 21:15:32 2020

@author: KayDee
"""

from collections import Counter
val = 0
lis = 'lmfaaao bruhh'
count = {}
for i in lis:
    count[i] = None
    
for i in count.keys():
    for j in lis:
        if i == j:
            val+=1
            count[i] = val
    val = 0
    
    

            