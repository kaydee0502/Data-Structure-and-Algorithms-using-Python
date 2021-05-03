class Solution:
    
    def __init__(self):
        self.dp = None
    
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
        
        if self.dp[s][m][n] != -1:
            return self.dp[s][m][n]
        
        if z <= m and o <= n:
            
            self.dp[s][m][n] = max(1+self.r(s-1,m-z,n-o,strs),self.r(s-1,m,n,strs))
        else:
            self.dp[s][m][n] = self.r(s-1,m,n,strs)
            
        return self.dp[s][m][n]
        
    
    
    
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        
        self.dp = [[[-1 for i in range(n+1)] for j in range(m+1)] for k in range(len(strs)+1)]        
        self.r(len(strs),m,n,strs)
        
        return self.dp[-1][-1][-1]
        
        