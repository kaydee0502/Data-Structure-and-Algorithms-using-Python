'''
279. Perfect Squares
Medium

4326

235

Add to List

Share
Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

 

Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
 

Constraints:

1 <= n <= 10^4
'''

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
            
            
        self.dp = [float("inf")] * (n+1)
        self.dp[0] = 0
        print(self.dp)
        
     
            
        for i in range(1,n+1):
            for j in sqs:
                if j <= i:
                    self.dp[i] = min(1+self.dp[i-j],self.dp[i]) 
                    
        #print(*self.dp)
        
        return self.dp[-1]
        
    
        
# @lc code=end

