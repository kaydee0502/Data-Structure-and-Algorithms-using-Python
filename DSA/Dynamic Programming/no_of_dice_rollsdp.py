class Solution:
    def __init__(self):
        self.c = 0
    
    
    def r(self,d,f,t):
        
        if d == 0 and t == 0:
            return  1
        
        if d == 0:
            return 0
        
        for j in range(1,f+1):
            if t >= j:
                
                a = self.r(d-1,f,t-j)
                if a:
                    #print(d,t,j)
                    self.c += a
                    
                    
        return 0
        
        
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        MOD = 10**9+7
        dp = [[0 for i in range(target+1)] for j in range(d+1)]
        
        dp[0][0] = 1
        
        
        

        for i in range(1,d+1):
            for j in range(i,target+1):
                for k in range(1,f+1):
                    if k <= j:
                        
                        dp[i][j] += dp[i-1][j-k]
                        
    
                
                       

                        

        #print(dp)
                    
        
        
        
       
        return dp[-1][-1]%MOD