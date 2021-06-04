'''

1296. Divide Array in Sets of K Consecutive Numbers
Medium

757

72

Add to List

Share
Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into sets of k consecutive numbers
Return True if it is possible. Otherwise, return False.

 

Example 1:

Input: nums = [1,2,3,3,4,4,5,6], k = 4
Output: true
Explanation: Array can be divided into [1,2,3,4] and [3,4,5,6].
Example 2:

Input: nums = [3,2,1,2,3,4,3,4,5,9,10,11], k = 3
Output: true
Explanation: Array can be divided into [1,2,3] , [2,3,4] , [3,4,5] and [9,10,11].
Example 3:

Input: nums = [3,3,2,2,1,1], k = 3
Output: true
Example 4:

Input: nums = [1,2,3,4], k = 3
Output: false
Explanation: Each array should be divided in subarrays of size 3.



'''


class Solution:
    
    def getC(self,nums,h,k):
        #print(h)
        for i in nums:
            if i in h and not i-1 in h:
                c = k
                j = i
                
                for j in range(i,i+k):
                    if not j in h:
                        break
                else:
                    for j in range(i,i+k):
                        h[j]-=1
                        if h[j] == 0:
                            del h[j]
                            
                    return True
                    
                
              
                        
                    

        
    
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        h = {}
        
        for i in nums:
            if not i in h:
                h[i] = 0
            h[i] += 1
            
            
        
        while h:
            
            
            if not self.getC(nums,h,k):
                return False
            
        return True
            
        
        