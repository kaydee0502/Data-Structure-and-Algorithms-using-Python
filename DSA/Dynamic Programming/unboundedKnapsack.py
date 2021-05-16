#User function Template for python3

class Solution:
    def knapSack(self, N, W, val, wt):
        
        dp = [[0 for i in range(W+1)] for j in range(N+1)]
        
        for i in range(1,N+1):
            for j in range(1,W+1):
                if j>=wt[i-1]:
                    dp[i][j] = max(val[i-1]+dp[i][j-wt[i-1]],dp[i-1][j])
                else:
                    dp[i][j] = dp[i-1][j]
                    
                    
        #print(dp)
        return dp[-1][-1]        # code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, W = [int(x) for x in input().split()]
        val = input().split()
        for itr in range(N):
            val[itr] = int(val[itr])
        wt = input().split()
        for it in range(N):
            wt[it] = int(wt[it])
        
        ob = Solution()
        print(ob.knapSack(N, W, val, wt))
# } Driver Code Ends