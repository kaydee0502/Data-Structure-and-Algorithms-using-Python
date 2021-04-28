#
# @lc app=leetcode id=1392 lang=python3
#
# [1392] Longest Happy Prefix
#

# @lc code=start
class Solution:
    
    def kmp_table(self,pat):
        if not pat:
            return []
            
        if len(pat) == 1:
            return [0]
        
        table = [0] * len(pat)
        
        j = 0
        i = 1
        
        
        while i < len(pat):
            
            if pat[i] == pat[j]:
                table[i] = j + 1
                i+=1
                j+=1
                
            else:
            
                while not(j == 0 or pat[i] == pat[j]):
                    print(i,j)
                    j = table[j-1]
                
            
                if j != 0 or pat[i] == pat[j]:
                    table[i] = j+1
                else:
                    i+=1
                    
            
                    
        return table
                    
    def longestPrefix(self, s: str) -> str:
        a = self.kmp_table(s)
        
        return s[:a[-1]]
        
# @lc code=end

