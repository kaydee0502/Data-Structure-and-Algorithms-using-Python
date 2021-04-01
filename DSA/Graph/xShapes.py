#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 10:20:15 2021

@author: kaydee
"""

'''

Given  a grid of n*m consisting of O's and X's. The task is to find the number of 'X' total shapes.
Note: 'X' shape consists of one or more adjacent X's (diagonals not included).
 

Example 1:

Input: grid = {{X,O,X},{O,X,O},{X,X,X}}
Output: 3
Explanation: 
The grid is-
X O X
O X O
X X X
So, X with same colour are adjacent to each 
other vertically for horizontally (diagonals 
not included). So, there are 3 different groups 
in the given grid.

Example 2:

Input: grid = {{X,X},{X,X}}
Output: 1
Expanation: 
The grid is- 
X X
X X
So, X with same colour are adjacent to each
other vertically for horizontally (diagonals
not included). So, there is only 1 group
in the given grid.

 

Your Task:
You don't need to read or print anything. Your task is to complete the function xShape() which takes grid as input parameter and returns the count of total X shapes.
 

Expected Time Compelxity: O(n*m)
Expected Space Compelxity: O(n*m)
 

Constraints:
1 ≤ n, m ≤ 100

'''


class Solution:
    
    
    def dfs(self, cords, grid, vis, n,m):
        
        r = cords[0]
        c = cords[1]
        
        vis[r][c] = True
        
        # check UP
        if r > 0 and grid[r-1][c] == "X" and vis[r-1][c] == False:
            self.dfs([r-1,c],grid,vis,n,m)
        
        #check LEFT
        if c > 0 and grid[r][c-1] == "X" and vis[r][c-1] == False:
            self.dfs([r,c-1],grid,vis,n,m)
            
        #check DOWN
        if r < n-1 and grid[r+1][c] == "X" and vis[r+1][c] == False:
            self.dfs([r+1,c],grid,vis,n,m)
        
        #check RIGHT
        if c < m-1 and grid[r][c+1] == "X" and vis[r][c+1] == False:
            self.dfs([r,c+1],grid,vis,n,m)
        
        
    def xShape(self, grid):
   		#Code here
   		n = len(grid)
   		m = len(grid[0])
   		vis = [[False for x in range(m)] for y in range(n)]
   		cc = 0
   		for r in range(n):
   		    for c in range(m):
   		        if vis[r][c] == False and grid[r][c] == 'X': 
   		            self.dfs([r,c], grid, vis, n,m)
   		            cc += 1
   		            
   		return cc
#{ 
#  Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = map(int, input().split())
		grid = [['#' for i in range(m)] for j in range(n)]
		for i in range(n):
			s = input().strip()
			for j in range(m):
				grid[i][j] = s[j]
		obj = Solution()
		ans = obj.xShape(grid)
		print(ans)
# } Driver Code Ends