#
# @lc app=leetcode id=997 lang=python3
#
# [997] Find the Town Judge
#

# @lc code=start
class Solution:
    
    
    
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        
        ine = [0] * (N+1)
        out = [0] * (N+1)
        
        for i in trust:
            ine[i[1]] += 1
            out[i[0]] += 1
            
        for i in range(1,N+1):
            if ine[i] == N-1 and out[i] == 0:
                return i
            
        return -1
        
        
        
# @lc code=end

