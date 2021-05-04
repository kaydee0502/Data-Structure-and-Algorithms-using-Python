'''

Coin Change
Category	Difficulty	Likes	Dislikes
algorithms	Medium (37.78%)	6785	194
Tags
Companies
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

 

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0
Example 4:

Input: coins = [1], amount = 1
Output: 1
Example 5:

Input: coins = [1], amount = 2
Output: 2
 

Constraints:

1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104


'''

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
       