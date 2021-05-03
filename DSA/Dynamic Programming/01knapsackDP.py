#User function Template for python3

class Solution:
    
    def __init__(self):
        self.dp = None
   
   
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
        self.dp = [[0 for i in range(W+1)] for j in range(n+1)]
        
        
        for i in range(1,n+1):
            for j in range(1,W+1):
                
                if wt[i-1] <= j:
                    
                    self.dp[i][j] = max(val[i-1]+self.dp[i-1][j-wt[i-1]],self.dp[i-1][j])
                else:
                    self.dp[i][j] = self.dp[i-1][j]
                    
        
                    
    
        
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