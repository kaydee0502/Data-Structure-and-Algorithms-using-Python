# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 16:23:17 2020

@author: KayDee
"""

def fibbiter(n):
    a = 0
    b = 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    for i in range(n-1):
        c = a + b
        a = b
        b = c
    return c
        
       
def fibbrec(n):
    if n < 2:
        return n
    return fibbrec(n-1) + fibbrec(n-2)
        
        
a = fibbiter(10)
b = fibbrec(7)
print(a,b)
        
    