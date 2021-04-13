'''
15. 3Sum
Medium

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Example 2:

Input: nums = []
Output: []

Example 3:

Input: nums = [0]
Output: []

 

Constraints:

    0 <= nums.length <= 3000
    -105 <= nums[i] <= 105




'''


class Solution:
    def threeSum(self, nums):
        
        nums.sort()
        #print(nums)
        h = {}
        trips = []
        i = 0 
        while i < len(nums)-2:
            j = i+1
            k = len(nums)-1
            
            target = 0 - nums[i]
            
            while j < k:
                #print(i,j,k,target)
                if nums[j] + nums[k] < target:
                    j+=1
                elif nums[j] + nums[k] > target:
                    k-=1
                    
                else:
                    trips.append([nums[i],nums[j],nums[k]])
                    
                    while j<k and nums[j] == nums[j+1]:
                        j+=1
                    j+=1
                    while j<k and nums[k] == nums[k-1]:
                        k-=1
                    k-=1
            while i <len(nums)-2 and nums[i] == nums[i+1]:
                i+=1
        
            i+=1
            
      
        #print(t)
        return trips
