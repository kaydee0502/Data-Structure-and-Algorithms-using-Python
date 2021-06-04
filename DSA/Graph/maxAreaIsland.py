

'''
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

'''

from collections import deque
class Solution:
    
    
    def bfs(self,grid,vis,i,j):
        
        q = deque([(i,j)])
        vis[i][j] = True
        
        cc = 1
        while q:
            #print(cc,q)
            x,y = q.popleft()
            
            
            
            
            
            dirs = [(1,0),(-1,0),(0,1),(0,-1)]
            
            for o,p in dirs:
                o += x
                p += y
                
                if o < 0 or p < 0 or o >= len(grid) or p >= len(grid[0]):
                    continue
                if vis[o][p] == True or grid[o][p] == 0:
                    continue
                    
                q.append((o,p))
                vis[o][p] =True
                cc+=1
                
                 
        return cc
                
            
    
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        vis = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
        
        cmax = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and vis[i][j] == False:
                    area = self.bfs(grid,vis,i,j)
                    cmax = max(cmax,area)
                    
                    
        return cmax