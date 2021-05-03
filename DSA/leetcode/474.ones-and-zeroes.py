#
# @lc app=leetcode id=474 lang=python3
#
# [474] Ones and Zeroes
#

# @lc code=start
class Solution:
    
    def __init__(self):
        self.dp = None
    
 
    
    
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        
        self.dp = [[[0 for i in range(n+1)] for j in range(m+1)] for k in range(len(strs)+1)] 
        
        
        for i in range(1,len(strs)+1):
            o,z = self.f(strs[i-1])
            for j in range(m+1):
                for k in range(n+1):
                    if j == k == 0:
                        continue
                    
                    
                    
                    if z <= j and o <= k:
                        self.dp[i][j][k] = max(1+self.dp[i-1][j-z][k-o],self.dp[i-1][j][k])
                    else:
                        self.dp[i][j][k] = self.dp[i-1][j][k]
                        
                    
                
        
        return self.dp[-1][-1][-1]
        
        
        
# @lc code=end

