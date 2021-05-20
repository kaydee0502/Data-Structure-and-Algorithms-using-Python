#
# @lc app=leetcode id=1662 lang=python3
#
# [1662] Check If Two String Arrays are Equivalent
#

# @lc code=start
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        i = 0
        isub = 0
        j = 0
        jsub = 0
        
        while 1:
            #print(i,isub,j,jsub)
            if word1[i][isub] != word2[j][jsub]:
                return False
            if isub < len(word1[i])-1:
                isub +=1
            else:
                isub = 0
                i += 1 
            if jsub < len(word2[j])-1:
                jsub+=1
            else:
                jsub=0
                j+=1
            
            if i >= len(word1) and j >= len(word2):
                return True
            if i >= len(word1) or j >= len(word2):
                return False
            
                
# @lc code=end

