# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 20:34:36 2020

@author: KayDee
"""

def gcd(a,b):
    if a==0:
        return b
    return gcd(b%a,a)
    
def lcm(m,n):
    return m*n//gcd(m,n)    
    
    
print(lcm(15,20))