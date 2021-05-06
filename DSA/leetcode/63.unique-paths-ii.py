#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0
        #print(*obstacleGrid,sep="\n")
        
        
        f = False
        for i in range(m):
            if obstacleGrid[i][0] == 1:
                
                f = True
                
            if f:
                obstacleGrid[i][0] = 0
            else:
                obstacleGrid[i][0] = 1        
            
        f = False
        for i in range(1,n):
            if obstacleGrid[0][i] == 1:
                f = True
            
            if f:
                obstacleGrid[0][i] = 0
            else:
                obstacleGrid[0][i] = 1
            
        #print("-------------")
        for i in range(1,m):
            for j in range (1,n):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                else:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
                    
        #print(*obstacleGrid,sep="\n")
        return obstacleGrid[-1][-1]
            
        
# @lc code=end

