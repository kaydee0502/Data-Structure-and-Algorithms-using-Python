'''


Peak element 
Easy Accuracy: 48.41% Submissions: 72226 Points: 2
A peak element in an array is the one that is not smaller than its neighbours.
Given an array arr[] of size N, find the index of any one of its peak elements.
Note: The generated output will always be 1 if the index that you return is correct. Otherwise output will be 0. 


Example 1:

Input:
N = 3
arr[] = {1,2,3}
Output: 2
Explanation: index 2 is 3.
It is the peak element as it is 
greater than its neighbour 2.
Example 2:

Input:
N = 2
arr[] = {3,4}
Output: 1
Explanation: 4 (at index 1) is the 
peak element as it is greater than 
its only neighbour element 3.
 

Your Task:
You don't have to read input or print anything. Complete the function peakElement() which takes the array arr[] and its size N as input parameters and return the index of any one of its peak elements.

 

Expected Time Complexity: O(log N)
Expected Auxiliary Space: O(1)



'''

# your task is to complete this function
# function should return index to the any valid peak element
class Solution:   
    def peakElement(self,arr, n):
        
        if n == 1:
            return 0
            
        if n == 2:
            if arr[0] > arr[1]:
                return 0
                
            return 1
            
        
        if arr[0] > arr[1]:
            return 0
            
        if arr[-1] > arr[-2]:
            return n-1
            
            
        l = 0
        
        r = n-1
        
        
        while l <= r:
            
            m = (l+r) // 2
            #print(l,m,r)
            
            if arr[m] >= arr[m-1] and arr[m] >= arr[m+1]:
               
                return m
                
            if arr[m] < arr[m-1]:
                r = m-1
                
                
            elif arr[m] < arr[m+1]:
                l = m+1
                
            #print(l,m,r)
               
        #print(m) 
        return m
                
                
        # Code here


#{ 
#  Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        index = Solution().peakElement(arr.copy(), n)
        flag = False
        if index<0 or index>=n:
            flag = False
        else:
            if index == 0 and n==1:
                flag = True
            elif index==0 and arr[index]>=arr[index+1]:
                flag = True
            elif index==n-1 and arr[index]>=arr[index-1]:
                flag = True
            elif arr[index-1] <= arr[index] and arr[index] >= arr[index+1]:
                flag = True
            else:
                flag = False

        if flag:
            print(1)
        else:
            print(0)
# Contributed by: Harshit Sidhwa

# } Driver Code Ends