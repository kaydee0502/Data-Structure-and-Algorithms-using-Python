#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 21:46:33 2021

@author: kaydee
"""

'''


Maximum Rectangular Area in a Histogram
Medium Accuracy: 47.42% Submissions: 13855 Points: 4

Find the largest rectangular area possible in a given histogram where the largest rectangle can be made of a number of contiguous bars. For simplicity, assume that all bars have the same width and the width is 1 unit.

Example 1:

Input:
N = 7
arr[] = {6,2,5,4,5,1,6}
Output: 12
Explanation: 


Example 2:

Input:
N = 8
arr[] = {7 2 8 9 1 3 6 5}
Output: 16
Explanation: Maximum size of the histogram 
will be 8  and there will be 2 consecutive 
histogram. And hence the area of the 
histogram will be 8x2 = 16.

Your Task:
The task is to complete the function getMaxArea() which takes the array arr[] and its size N as inputs and finds the largest rectangular area possible and returns the answer.

Expected Time Complxity : O(N)
Expected Auxilliary Space : O(N)

Constraints:
1 <= N <= 106
1 <= arr[i] <= 1012

'''


#User function Template for python3
'''
Function Arguments :
		@param  : histogram( given list containing info about histogram)
		@return : integer
'''

class Solution:
    def getMaxArea(self,histogram):
        
        smallerToLeft = []
        smallerToRight = None
        maxAr = float("-inf")
        stack = []
        
        # nearest smaller to left
        for i in range(len(histogram)):
            while stack:
                if stack[-1][0] < histogram[i]:
                    smallerToLeft.append(stack[-1][1])
                    break
                stack.pop()
            else:
                smallerToLeft.append(-1)
            stack.append([histogram[i],i])
            
        stack = []
        
        # nearest smaller to right + area calculations
        for i in range(len(histogram)-1,-1,-1):
            while stack:
                if stack[-1][0] < histogram[i]:
                    smallerToRight = stack[-1][1]
                    break
                stack.pop()
            else:
                smallerToRight = len(histogram)
           
            h = histogram[i]
            
            stack.append([histogram[i],i])
            currentArea = (h+ h*((smallerToRight-1) - (smallerToLeft[i]+1)))
            if currentArea > maxAr:
                maxAr = currentArea
            
            
        
        return maxAr
            
                
                

#{ 
#  Driver Code Starts
#Initial Template for Python 3

# by Jinay Shah 

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        a = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.getMaxArea(a))
# } Driver Code Ends