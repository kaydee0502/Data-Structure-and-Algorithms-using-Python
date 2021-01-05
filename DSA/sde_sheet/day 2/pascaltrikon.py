#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 13:27:53 2021

@author: kaydee
"""


def generate(numRows: int):
    n = numRows
    if n == 0:
        return []
    if n == 1:
        return [[1]]
    
    if n == 2:
        return [[1],[1,1]]
    
    pascal = [[1],[1,1]]
    
    for r in range(2,n):
        row = [1]
        for t in range(1,len(pascal[r-1])):
            row.append(pascal[r-1][t]+pascal[r-1][t-1])
        row.append(1)
        pascal.append(row)
        
    return pascal

print(*generate(10),sep="\n")