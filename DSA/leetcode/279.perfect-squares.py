#
# @lc app=leetcode id=279 lang=python3
#
# [279] Perfect Squares
#

# @lc code=start

    
class Solution:
    
    def __init__(self):
        self.dp = None
    
    
    
    def numSquares(self, n: int) -> int:
        
        
        sqs = []
        
        i = 1
        while i**2 <= n:
            sqs.append(i**2)
            i+=1
            
            
        self.dp = [[float("inf") for i in range(n+1)] for k in range(len(sqs)+1)]
        #print(sqs)
        
        for i in range(len(sqs)+1):
            self.dp[i][0] = 0
            
        for i in range(1,len(sqs)+1):
            for j in range(1,n+1):
                if sqs[i-1] <= j:
                    self.dp[i][j] = min(1+self.dp[i][j-sqs[i-1]],1+self.dp[i-1][j-sqs[i-1]],self.dp[i-1][j])
                else:
                    self.dp[i][j] = self.dp[i-1][j]             
        
        return self.dp[-1][-1]
        
    
        
# @lc code=end

