#
# @lc app=leetcode id=997 lang=python3
#
# [997] Find the Town Judge
#

# @lc code=start
class Solution:
    
    
    
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        
        nei = [0] * (N+1)
        
        for i in trust:
            nei[i[0]] -=1
            nei[i[1]] +=1
            
        for i in range(1,N+1):
            if nei[i] == N-1:
                return i
            
        return -1
        
        
        
# @lc code=end

