#
# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#

# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        dp = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        dp[0][0] = grid[0][0]
        #print(dp)
        for i in range(1,len(grid[0])):
            dp[0][i] = dp[0][i-1]+grid[0][i]
            
        #print(dp)    
        for j in range(1,len(grid)):
            dp[j][0] = dp[j-1][0] + grid[j][0]
        
        #print(dp)
        for i in range(1,len(grid)):
            for j in range(1,len(grid[i])):
                dp[i][j] = grid[i][j] + min(dp[i-1][j],dp[i][j-1])
                
                
        return dp[-1][-1] 
        
        
# @lc code=end

