'''

Minimum sum partition 
Hard Accuracy: 50.0% Submissions: 12736 Points: 8
Given an integer array arr of size N, the task is to divide it into two sets S1 and S2 such that the absolute difference between their sums is minimum and find the minimum difference

Example 1:

Input: N = 4, arr[] = {1, 6, 11, 5} 
Output: 1
Explanation: 
Subset1 = {1, 5, 6}, sum of Subset1 = 12 
Subset2 = {11}, sum of Subset2 = 11   
Example 2:
Input: N = 2, arr[] = {1, 4}
Output: 3
Explanation: 
Subset1 = {1}, sum of Subset1 = 1
Subset2 = {4}, sum of Subset2 = 4

Your Task:  
You don't need to read input or print anything. Complete the function minDifference() which takes N and array arr as input parameters and returns the integer value

Expected Time Complexity: O(N*|sum of array elements|)
Expected Auxiliary Space: O(N*|sum of array elements|)

Constraints:
1 ≤ N*|sum of array elements| ≤ 10^6

'''

#User function Template for python3

class Solution:
	def minDiffernce(self, arr, n):
	    renge = sum(arr)
	    
	    dp = [[False for i in range(renge+1)] for j in range(n+1)]
	    
	        
	    for i in range(n+1):
	        for j in range(renge+1):
	            
	            if i == 0:
	                dp[i][j] = False
	                
	            if j == 0:
	                dp[i][j] = True
	                
	            elif arr[i-1] <= j:
	                dp[i][j] = dp[i-1][j-arr[i-1]] or dp[i-1][j]
	            else:
	                dp[i][j] = dp[i-1][j]
	                
	                
	    diff = float("inf")
	    
	    for i in range(renge):
	        if i*2 > renge:
	            break
	        #print(i)
	        if dp[-1][i] and renge - i*2 < diff:
	       
	            diff = renge - (i*2)
	            
	    return diff
	            
	            
	            
	            
	            
	   

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minDiffernce(arr, N)
		print(ans)

# } Driver Code Ends