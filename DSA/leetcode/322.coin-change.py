#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
class Solution:
    
    def ccutil(self,i,amt,coins):
        #print(i,amt)
        if amt == 0:
            return 0
        
        if i == 0:
            return float("inf")
        
        
        if coins[i-1] <= amt:
            return min(1 + self.ccutil(i-1,amt-coins[i-1],coins), 1 + self.ccutil(i,amt-coins[i-1],coins),self.ccutil(i-1,amt,coins))
        else:
            return self.ccutil(i-1,amt,coins)
    
    def coinChange(self, coins: List[int], amount: int) -> int:
       a = self.ccutil(len(coins),amount,coins)
       if a == float("inf"):
           return -1
       return a
       
        
# @lc code=end

