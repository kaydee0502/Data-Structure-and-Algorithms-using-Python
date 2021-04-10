'''

Largest subarray with 0 sum
Easy Accuracy: 46.94% Submissions: 49096 Points: 2

Given an array having both positive and negative integers. The task is to compute the length of the largest subarray with sum 0.

Example 1:

Input:
N = 8
A[] = {15,-2,2,-8,1,7,10,23}
Output: 5
Explanation: The largest subarray with
sum 0 will be -2 2 -8 1 7.

Your Task:
You just have to complete the function maxLen() which takes two arguments an array A and n, where n is the size of the array A and returns the length of the largest subarray with 0 sum.

Expected Time Complexity: O(N*Log(N)).
Expected Auxiliary Space: O(N).

Constraints:
1 <= N <= 104
-1000 <= A[i] <= 1000, for each valid i
'''

def maxLen(n, arr):
    
    S = 0
    h = {0:-1}
    MAX = 0
    
    for i in range(n):
        S+=arr[i]
        #print(S,i)
        if S in h:
            MAX = max(MAX,(i-h[S]))
            
        else:
            h[S] = i
    #Code here
    #print(h)
    return MAX

#{ 
#  Driver Code Starts
if __name__=='__main__':
    t= int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(maxLen(n ,arr))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends
