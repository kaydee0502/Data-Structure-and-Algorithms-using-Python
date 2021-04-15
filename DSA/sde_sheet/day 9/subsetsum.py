'''



Subset Sums
Basic Accuracy: 61.62% Submissions: 1422 Points: 1

Given a list(Arr) of N integers, print sums of all subsets in it. Output should be printed in increasing order of sums.

Example 1:

Input:
N = 2
Arr = [2, 3]
Output:
0 2 3 5
Explanation:
When no elements is taken then Sum = 0.
When only 2 is taken then Sum = 2.
When only 3 is taken then Sum = 3.
When element 2 and 3 are taken then 
Sum = 2+3 = 5.

Example 2:

Input:
N = 3
Arr = [5, 2, 1]
Output:
0 1 2 3 5 6 7 8

Your Task:  
You don't need to read input or print anything. Your task is to complete the function subsetSum() which takes a list/vector and an integer N as an input parameter and return the list/vector of all the subset sums in increasing order.

Expected Time Complexity: O(2^N)
Expected Auxiliary Space: O(2^N)

Constraints:
1 <= N <= 15
0 <= Arr[i] <= 10000


'''

#User function Template for python3
class Solution:
    def __init__(self):
        self.sums = []
    
    def f(self,arr,N,s):
        if N == -1:
            self.sums.append(s)
            return s
        
        a_p = self.f(arr,N-1,s)
        a = self.f(arr,N-1, s+arr[N])
        #print(a,a_p)
        
        
        
        
	def subsetSums(self, arr, N):
	    self.f(arr,N-1,0)
	    #print(self.sums)
	    return sorted(self.sums)
		

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        N = int(input())
        arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.subsetSums(arr, N)
        for x in ans:
            print(x,end=" ")
        print("")

# } Driver Code Ends
