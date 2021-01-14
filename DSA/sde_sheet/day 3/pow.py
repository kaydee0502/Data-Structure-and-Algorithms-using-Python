#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 13:45:42 2021

@author: kaydee
"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1/x
            n = n*-1
            
        if n == 0:
            return 1
        
        if n % 2 ==0:
            res = self.myPow(x*x,n//2)
        else:
            res = x * self.myPow(x*x,n//2)
        
        return res