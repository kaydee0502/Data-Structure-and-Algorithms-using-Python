#
# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset Sum
#

# @lc code=start
class Solution:
   
    def __init__(self):
        self.cache = {}
    
    def part(self,t,i,csum,nums):
        
        if i < 0 and csum == t:
            return True
        
        if i < 0:
            return False
        
        if (i,csum) in self.cache:
            return self.cache[(i,csum)]
        
        
        p = self.part(t,i-1,csum+nums[i],nums)
        n = self.part(t,i-1,csum-nums[i],nums)
        
        self.cache[(i,csum)] = p+n
        return p+n
    
    def canPartition(self, nums: List[int]) -> bool:
        target = 0
        
        return self.part(target,len(nums)-1,0,nums)
        
# @lc code=end

