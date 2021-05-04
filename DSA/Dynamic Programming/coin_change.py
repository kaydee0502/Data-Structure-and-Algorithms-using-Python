'''
322. Coin Change
Medium

6785

194

Add to List

Share
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
1 <= coins[i] <= 2^31 - 1
0 <= amount <= 10^4

'''


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
       