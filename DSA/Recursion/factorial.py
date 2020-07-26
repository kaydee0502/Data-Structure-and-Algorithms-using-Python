# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 20:50:47 2020

@author: KayDee
"""

def iterfact(n):
    ans = 1
    while n:
        ans *= n
        n-=1
    return ans

def recfact(n):
    if n == 0:
        return 1
    
    return n * recfact(n-1)
  

print(iterfact(5))
print(recfact(5))