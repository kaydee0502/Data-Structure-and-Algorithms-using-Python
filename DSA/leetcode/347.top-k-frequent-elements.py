#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
from heapq import *
class Solution:
    def __init__(self):
        self.heap = []
    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heapify(self.heap)
        
        h = {}
        
        for i in nums:
            
            if not i in h:
                h[i] = 0
            h[i]+=1
            
         
                
           
            heappush(self.heap,(-h[i],i))
          
                
        res = []
        s = set()
        #print(self.heap)
        
        while len(res) < k:
            c,v = heappop(self.heap)
            if v in s:
                continue
            else:
                s.add(v)
                res.append(v)
        
        
        return res
        
        
        
# @lc code=end

