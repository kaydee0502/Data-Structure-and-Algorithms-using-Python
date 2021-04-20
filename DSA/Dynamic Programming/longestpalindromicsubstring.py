'''

5. Longest Palindromic Substring
Medium

10441

678

Add to List

Share
Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
Example 3:

Input: s = "a"
Output: "a"
Example 4:

Input: s = "ac"
Output: "a"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters (lower-case and/or upper-case),

'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        
        dp = [[-1 for i in range(len(s))] for j in range(len(s))]
        
        for i in range(len(dp)):
            dp[i][i] = 1
        
        
        maxl = [0,0]
        
        for i in range(1,len(dp)):
            if s[i] == s[i-1]:
                dp[i-1][i] = 1
                maxl = [i-1,i]
        
        
        #print(*dp,sep="\n")
        
        
        
        for i in range(len(s)-1,-1,-1):
            for j in range(i+2,len(s)):
                
                
                if s[i] == s[j] and dp[i+1][j-1]==1:
                    #print(i,j)
                    #print(*dp,sep="\n")
                    if j-i > maxl[1] - maxl[0]:
                        maxl = [i,j]
                    dp[i][j] = 1
                    
                else:
                    dp[i][j] = 0
                    
        #print(maxl)
        return s[maxl[0]:maxl[1]+1]
                    
                
                    
                    