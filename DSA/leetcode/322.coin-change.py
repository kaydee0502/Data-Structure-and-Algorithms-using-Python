#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
class Solution:
    def __init__(self):
        self.dp = None
    
    def coinChange(self, coins: List[int], amount: int) -> int:
        
       self.dp = [[float("inf") for i in range(amount+1)] for j in range(len(coins)+1)]
       
       for i in range(len(coins)+1):
           self.dp[i][0] = 0
           
       for i in range(1,len(coins)+1):
           for j in range(1,amount+1):
               if coins[i-1] <= j:
                   
                   self.dp[i][j] = min(1+self.dp[i-1][j-coins[i-1]],1+self.dp[i][j-coins[i-1]],self.dp[i-1][j])
               else:
                   self.dp[i][j] = self.dp[i-1][j]
                   
               
       #print(*self.dp,sep= "\n")
       a = self.dp[-1][-1]
       if a == float("inf"):
           return -1
       return a
       
        
# @lc code=end

