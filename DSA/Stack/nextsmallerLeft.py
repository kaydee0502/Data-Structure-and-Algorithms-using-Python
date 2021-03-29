#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 20:32:41 2021

@author: kaydee
"""

def ngl(arr,n):
    stack = []
    
    
    ans = []
    for i in range(len(arr)):
        while stack:
            if stack[-1] < arr[i]:
                ans.append(stack[-1])
                
                break
            stack.pop()
        else:
            ans.append(-1)
            
        stack.append(arr[i])
            
    return ans



print(ngl([1,3,2,4],4))

            