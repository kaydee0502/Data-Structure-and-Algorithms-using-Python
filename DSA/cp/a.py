import math
t = int(input())
 
while t:
    n,m,k = map(int,input().split())
    dp = [[0 for i in range(m)] for j in range(n)]
    
    for i in range(m):
        dp[0][i] = i
        
    for i in range(n):
    
        dp[i][0] = i
    
    for i in range(1,n):
        for j in range (1,m):
            dp[i][j] = dp[i-1][j] + (j+1)
            
    if dp[-1][-1] == k:
        print("YES")
        
    else:
        print("NO")
    
    
    t-=1