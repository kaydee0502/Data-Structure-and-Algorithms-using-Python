#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
class Solution:
    
    def dfs(self,grid,i,j,m,n):
        
        if i < 0 or j < 0 or i >= m or j >= n:
            return
    
        if grid[i][j] == "0":
            return
        
        
        grid[i][j] = "0"
        
        self.dfs(grid,i+1,j,m,n)
        self.dfs(grid,i-1,j,m,n)
        self.dfs(grid,i,j+1,m,n)
        self.dfs(grid,i,j-1,m,n)
        
        
        
    
    def numIslands(self, grid: List[List[str]]) -> int:
       
        islands= 0
        m = len(grid)
        n = len(grid[0])
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c]=="1":
                    
                    self.dfs(grid,r,c,m,n)   
                    islands+=1
                    
                    
        return islands
# @lc code=end

