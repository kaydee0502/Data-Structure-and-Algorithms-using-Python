#User function Template for python3

class Solution:
    
    def __init__(self):
        self.prof = 0
    
    def ksUtil(self,W,wt,vl,n,i,p):
        
        self.prof = max(p,self.prof)
        
        if i >= n:
            return
        
    
        if wt[i] <= W:
            
            self.ksUtil(W-wt[i],wt,vl,n,i+1,p+vl[i])
        self.ksUtil(W,wt,vl,n,i+1,p)
        
        
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
       self.ksUtil(W,wt,val,n,0,0)
       return self.prof
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