#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
class Solution:
    def __init__(self):
        self.dp = None
    
    def ccutil(self,i,amt,coins):
        
        #print(i,amt)
        if amt == 0:
            return 0
        
        if i == 0:
            return float("inf")
        
        if self.dp[i][amt] != -1:
            return self.dp[i][amt]
        
        if coins[i-1] <= amt:
            self.dp[i][amt] =  min(1 + self.ccutil(i-1,amt-coins[i-1],coins), 1 + self.ccutil(i,amt-coins[i-1],coins),self.ccutil(i-1,amt,coins))
        else:
            self.dp[i][amt] = self.ccutil(i-1,amt,coins)

        return self.dp[i][amt]
     
    def coinChange(self, coins: List[int], amount: int) -> int:
        
       self.dp = [[-1 for i in range(amount+1)] for j in range(len(coins)+1)]
       a = self.ccutil(len(coins),amount,coins)
       if a == float("inf"):
           return -1
       return a
       
        
# @lc code=end

