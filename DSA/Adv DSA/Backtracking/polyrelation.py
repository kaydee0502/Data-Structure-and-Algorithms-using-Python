# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 22:43:20 2020

@author: KayDee
"""

T = int(input())
while T:
    poly = int(input())
    for i in range(poly):
        dump = input()
    tot = poly
    while poly//2 > 2:
        tot+=poly//2
        poly //= 2
        
    print(tot)
        
    T-=1