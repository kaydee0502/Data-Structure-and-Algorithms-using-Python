#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 12:58:05 2021

@author: kaydee
"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[1 for i in range(n)] for j in range(m)]
        
        for i in range(1,m):
            for j in range(1,n):
                try:
                    grid[i][j] = grid[i-1][j] + grid[i][j-1]
                except:
                    print(i,j,m,n,grid)
        return grid[m-1][n-1]