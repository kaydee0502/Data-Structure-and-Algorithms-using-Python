#
# @lc app=leetcode id=494 lang=python3
#
# [494] Target Sum
#

# @lc code=start
import math
class Solution:
    
    def __init__(self):
        self.cache={}
    
    def tsum(self,csum,ind,target,nums):
        if ind < 0 and csum == target:
            return 1
        if ind < 0:
            return 0
        
        if (csum,ind) in self.cache:
            return self.cache[(csum,ind)]
        
        p = self.tsum(csum + nums[ind], ind-1,target,nums)
        n = self.tsum(csum - nums[ind],ind -1 ,target, nums)  
        
        self.cache[(csum,ind)] = p + n 
        return p + n 
    
    
    
    
    
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        return self.tsum(0,len(nums)-1,target,nums)
# @lc code=end

