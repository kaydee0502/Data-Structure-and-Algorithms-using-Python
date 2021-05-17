'''

Rod Cutting 
Easy Accuracy: 77.49% Submissions: 1435 Points: 2
Given a rod of length N inches and an array of prices that contains prices of all pieces of size smaller than N. Determine the maximum value obtainable by cutting up the rod and selling the pieces.

 

Example 1:

Input:
N = 8
Price[] = {1, 5, 8, 9, 10, 17, 17, 20}
Output:
22
Explanation:
The maximum obtainable value is 22 by
cutting in two pieces of lengths 2 and 
6, i.e., 5+17=22.
Example 2:

Input:
N=8
Price []={3,   5,   8,   9,  10,  17,  17,  20}
Output: 24
Explanation: 
The maximum obtainable value is 
24 by cutting the rod into 8 pieces 
of length 1, i.e, 8*3=24. 

Your Task:  
You don't need to read input or print anything. Your task is to complete the function cutRod() which takes the array A[] and its size N as inputs and returns the maximum price obtainable.

 

Expected Time Complexity: O(N2)
Expected Auxiliary Space: O(N)

 

Constraints:
1 <= N <= 1000
1 <= Ai <= 10^5

'''

#User function Template for python3

def cutRod( price, n):
    
    dp =[[0 for i in range(n+1)] for j in range(len(price)+1)]
    
    for i in range(1,len(price)+1):
        for j in range(1,n+1):
            if j >= i:
                dp[i][j] = max(price[i-1]+dp[i][j-(i)],dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]
           
    #print(*dp,sep="\n")     
    return dp[-1][-1]
    
    



#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        print(cutRod(a, n))

        T -= 1


if __name__ == "__main__":
    main()





    
# } Driver Code Ends