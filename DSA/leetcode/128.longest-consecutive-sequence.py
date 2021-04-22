#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        H = {}
        
        for i in nums:
            if not i in H:
                H[i] = 0
            H[i]+=1
            
        
        seq = 0
        curr = 0
        
        for i in nums:
            if not i-1 in H:
                
                while i in H:
                    curr+=1
                    i+=1
            seq = max(seq,curr)
            curr = 0
            
        return max(seq,curr)
                    
        
         
# @lc code=end

