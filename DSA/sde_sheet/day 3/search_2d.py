#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 13:16:41 2021

@author: kaydee
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in range(len(matrix)):
            if matrix[row][0] <= target and target <= matrix[row][-1]:
                print("5")
                l = 0
                r = len(matrix[row])-1
                
                
                while l<=r:
                    
                    m=(l+r)//2
                    print(l,m,r)
                    if matrix[row][m] == target:
                        return 1
                    
                    
                    if matrix[row][m] < target:
                        l = m+1
                    
                    if matrix[row][m] > target:
                        r = m-1
                        
                    print(l,m,r)
                    
                    
                return 0