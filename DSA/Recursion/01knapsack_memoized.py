#User function Template for python3

class Solution:
    
    def __init__(self):
        self.dp = None
   
    
    def ksUtil(self,W,wt,vl,n):
        
       
        
        if n <= 0 or W <= 0:
            return 0
            
        if self.dp[n][W] != -1:
            return self.dp[n][W]
        
    
        if wt[n-1] <= W:
            
            self.dp[n][W] = max(vl[n-1]+self.ksUtil(W-wt[n-1],wt,vl,n-1), self.ksUtil(W,wt,vl,n-1))
        
        else:
            self.dp[n][W] = self.ksUtil(W,wt,vl,n-1)
        return self.dp[n][W]
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
        self.dp = [[-1 for i in range(W+1)] for j in range(n+1)]
        
        
        self.ksUtil(W,wt,val,n)
        
        #print(self.dp)
        return self.dp[-1][-1]
       
        # code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        W = int(input())
        val = list(map(int,input().strip().split()))
        wt = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.knapSack(W,wt,val,n))
# } Driver Code Ends