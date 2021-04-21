#
# @lc app=leetcode id=647 lang=python3
#
# [647] Palindromic Substrings
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        
        dp = [[-1 for i in range(len(s))] for j in range(len(s))]
        
        subs = 0
        for i in range(len(s)):
            dp[i][i] = 1
            subs += 1
            
        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                subs+=1
                dp[i-1][i] = 1
                
        
        for i in range(len(s)-1,-1,-1):
            for j in range(i+2,len(s)):
                if s[i] == s[j] and dp[i+1][j-1] == 1:
                    dp[i][j] = 1
                    subs+=1
                    
        return subs
                
            
        
               
               
# @lc code=end

