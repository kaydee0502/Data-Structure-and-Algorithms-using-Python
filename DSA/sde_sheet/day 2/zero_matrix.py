#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 13:44:42 2021

@author: kaydee
"""

class Solution:
    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeros = []
        
        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                if matrix[r][c] == 0:
                    zeros.append(c)
                
                
            if any(list([True if i==0 else False for i in matrix[r]])):
                matrix[r] = [0]*len(matrix[r])
                
                
        for r in range(len(matrix)):
            for z in set(zeros):
                matrix[r][z] = 0
                