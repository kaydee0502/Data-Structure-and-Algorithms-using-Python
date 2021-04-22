#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    
    def rec(self,r,l,p,t):
        #print(r,l)
        if r <= 0 and l <= 0:
            p.append(t)
            return
            
        if r==l:
            self.rec(r,l-1,p,t+"(")
        else:
            if l >0:
                self.rec(r,l-1,p,t+"(")
            if r >0:
                self.rec(r-1,l,p,t+")")
            
    
    def generateParenthesis(self, n: int) -> List[str]:
        parens = []
        self.rec(n,n,parens,"")
        return parens
        
        
# @lc code=end

