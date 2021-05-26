#
# @lc app=leetcode id=462 lang=python3
#
# [462] Minimum Moves to Equal Array Elements II
#

# @lc code=start


class Solution:
    def getMed(self,seq):
        a = sorted(seq)
        
        if len(a) %2==0:
            return (a[(len(a)//2)-1]+a[len(a)//2])//2
        else:
            return a[len(a)//2]
        
    def minMoves2(self, nums: List[int]) -> int:
        mid = self.getMed(nums)
        
        cost = 0
        
        for i in nums:
            cost += abs(i-mid)
            
        return cost
        
# @lc code=end

