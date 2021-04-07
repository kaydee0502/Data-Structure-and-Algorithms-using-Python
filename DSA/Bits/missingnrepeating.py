#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 12:49:57 2021

@author: kaydee
"""

arr = [4,3,6,2,1,1]

n = 6

exor = 0

for i in range(n+1):
    exor ^= i
    
gxor = 0

for i in arr:
    gxor ^= i
    
xxory = gxor^exor

shifts = 0
temp = xxory
while temp != 1:
    temp = temp >> 1
    shifts +=1
    
ebin1 =0
ebin2 =0
gbin1 =0
gbin2 =0

for i in range(n+1):
    if i >> shifts == 1:
        ebin1^=i
    else:
        ebin2^=i
        
for i in arr:
    if i >> shifts == 1:
        gbin1 ^=i
        
    else:
        gbin2 ^=i
        

print(ebin1^gbin1,ebin2^gbin2)
