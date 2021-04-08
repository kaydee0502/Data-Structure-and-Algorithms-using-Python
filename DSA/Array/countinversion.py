'''

Count Inversions
Medium Accuracy: 39.43% Submissions: 39000 Points: 4

Given an array of integers. Find the Inversion Count in the array. 

Inversion Count: For an array, inversion count indicates how far (or close) the array is from being sorted. If array is already sorted then the inversion count is 0. If an array is sorted in the reverse order then the inversion count is the maximum. 
Formally, two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j.
 

Example 1:

Input: N = 5, arr[] = {2, 4, 1, 3, 5}
Output: 3
Explanation: The sequence 2, 4, 1, 3, 5 
has three inversions (2, 1), (4, 1), (4, 3).

Example 2:

Input: N = 5
arr[] = {2, 3, 4, 5, 6}
Output: 0
Explanation: As the sequence is already 
sorted so there is no inversion count.

Example 3:

Input: N = 3, arr[] = {10, 10, 10}
Output: 0
Explanation: As all the elements of array 
are same, so there is no inversion count.

Your Task:
You don't need to read input or print anything. Your task is to complete the function inversionCount() which takes the array arr[] and the size of the array as inputs and returns the inversion count of the given array.

Expected Time Complexity: O(NLogN).
Expected Auxiliary Space: O(N).

Constraints:
1 ≤ N ≤ 5*105
1 ≤ arr[i] ≤ 1018
'''

class Solution:
    #User function Template for python3
    
    # arr[]: Input Array
    # N : Size of the Array arr[]
    #Function to count inversions in the array.
    
    def __init__(self):
        self.invs = 0
        
    def merge(self,l,r):
        rlen = len(r)
        llen = len(l)
        i = 0
        j = 0
        arr = []
        while i < llen and j < rlen:
            if l[i] <= r[j]:
                arr.append(l[i])
                i+=1
            else:
                arr.append(r[j])
                self.invs += (llen - i)
                j+=1
                
        while i < llen:
            
            arr.append(l[i])
            i+=1
            
        while j < rlen:
            
            arr.append(r[j])
            j+=1
                
        return arr
    
    def mergesort(self, a):
        
        if len(a) <= 1:
            return a
        
        
        m = len(a)//2
        
       
        a1 = self.mergesort(a[:m])
        a2 = self.mergesort(a[m:])
        #print(a1,a2)
        return self.merge(a1,a2)
        
        
        
    
    def inversionCount(self, a,n):
       
        self.mergesort(a)    
        return self.invs
        # Your Code Here
#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for tt in range(t):
        n = int(input())
        a = list(map(int, input().strip().split()))
        obj = Solution()
        print(obj.inversionCount(a,n))
# } Driver Code Ends
