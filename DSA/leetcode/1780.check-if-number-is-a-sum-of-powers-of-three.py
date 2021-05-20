#
# @lc app=leetcode id=1780 lang=python3
#
# [1780] Check if Number is a Sum of Powers of Three
#

# @lc code=start
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n:
            if n%3 == 2:
                return False
            n //= 3
            
        return True
            
        
# @lc code=end

