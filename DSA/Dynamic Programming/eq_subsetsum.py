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
        target = sum(nums)//2
        if sum(nums)%2 == 1:
            return False
        
        dp = [[False for i in range(target+1)] for j in range(len(nums) + 1)]
        
        for i in range(len(nums)+1):
            dp[i][0] = True
            
        for i in range(1,len(nums)+1):
            for j in range(1,target+1):
                if nums[i-1] <= j:
                    dp[i][j] = dp[i-1][j-nums[i-1]] or dp[i-1][j]
                    
                else:
                    dp[i][j] = dp[i-1][j]
        
        #print(*dp,sep= "\n")
        return dp[-1][-1]
        
# @lc code=end

