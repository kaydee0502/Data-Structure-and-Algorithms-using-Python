# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 16:06:46 2020

@author: KayDee
"""

def sieve(n):
    s = [1]*(n+1)
    s[0] = 0
    s[1] = 0
    for i in range(2,n+1):
        if s[i] == 1:
            for j in range(i*i,n+1,i):
                
                #print(j,i)
                s[j] = 0
    anime = 0
    #print(s)
    for x in range(n+1):
        if s[x] == 1:
            anime+=x
    return anime
    
    
T = int(input())
while T:
    
    m = int(input())
    
    print(sieve(m))
    T-=1