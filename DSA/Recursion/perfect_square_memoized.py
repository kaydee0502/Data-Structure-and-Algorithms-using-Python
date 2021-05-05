class Solution:
    
    def __init__(self):
        self.dp = None
    
    def cc(self,sqs,i,n):
        if n == 0:
            return 0
        
        if i == 0:
            return float("inf")
        
        if self.dp[i][n] != -1:
            return self.dp[i][n]
        
        if sqs[i-1] <= n:
            self.dp[i][n] = min(1+self.cc(sqs,i,n-sqs[i-1]),1+self.cc(sqs,i-1,n-sqs[i-1]),self.cc(sqs,i-1,n))
        else:
            self.dp[i][n] = self.cc(sqs,i-1,n)
    
        return self.dp[i][n]
    
    def numSquares(self, n: int) -> int:
        
        
        sqs = []
        
        i = 1
        while i**2 <= n:
            sqs.append(i**2)
            i+=1
            
            
        self.dp = [[-1 for i in range(n+1)] for k in range(len(sqs)+1)]
        #print(sqs)
        return self.cc(sqs,len(sqs),n)