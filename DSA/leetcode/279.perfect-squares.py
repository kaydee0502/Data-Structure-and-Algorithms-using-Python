#
# @lc app=leetcode id=279 lang=python3
#
# [279] Perfect Squares
#

# @lc code=start
class Solution:
    
    def cc(self,sqs,i,n):
        if n == 0:
            return 0
        
        if i == 0:
            return float("inf")
        
        if sqs[i-1] <= n:
            return min(1+self.cc(sqs,i,n-sqs[i-1]),1+self.cc(sqs,i-1,n-sqs[i-1]),self.cc(sqs,i-1,n))
        else:
            return self.cc(sqs,i-1,n)
    
    def numSquares(self, n: int) -> int:
        sqs = []
        
        i = 1
        while i**2 <= n:
            sqs.append(i**2)
            i+=1
        #print(sqs)
        return self.cc(sqs,len(sqs),n)
        
    
        
# @lc code=end

