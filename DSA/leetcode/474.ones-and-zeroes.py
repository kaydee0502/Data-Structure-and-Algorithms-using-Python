#
# @lc app=leetcode id=474 lang=python3
#
# [474] Ones and Zeroes
#

# @lc code=start
class Solution:
    
    def f(self,st):
        o = 0
        z = 0
        for i in st:
            if i =="0":
                z+=1
            else:
                o+=1
                
        return o,z
    
    def r(self,s,m,n,strs):
        if s == 0 or (m == 0 and n == 0):
            return 0
        
        o,z = self.f(strs[s-1])
        #print(o,z,strs[s-1])
        
        if z <= m and o <= n:
            
            return max(1+self.r(s-1,m-z,n-o,strs),self.r(s-1,m,n,strs))
        else:
            return self.r(s-1,m,n,strs)
        
    
    
    
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        return self.r(len(strs),m,n,strs)
        
        
        
# @lc code=end

