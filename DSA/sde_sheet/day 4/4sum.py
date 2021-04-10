'''

18. 4Sum
Medium

Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

    0 <= a, b, c, d < n
    a, b, c, and d are distinct.
    nums[a] + nums[b] + nums[c] + nums[d] == target

You may return the answer in any order.

 

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]

 

Constraints:

    1 <= nums.length <= 200
    -109 <= nums[i] <= 10^9
    -109 <= target <= 10^9



'''

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        quads = []
        for i in range(len(nums)-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            
            for j in range(i+1,len(nums)-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                    
                ftar = target - nums[i] - nums[j]
                k = j+1
                l = len(nums)-1
                
                while k < l:
                    if nums[k] + nums[l] > ftar:
                        l-=1
                        
                    elif nums[k] + nums[l] < ftar:
                        k+=1
                        
                    else:
                        #print(nums,ftar,i,j,k,l)
                        quads.append([nums[i],nums[j],nums[k],nums[l]])
                        
                        while k < l and nums[k] == nums[k+1]:
                            k+=1
                            
                        k+=1
                        
                        while k < l and nums[l] == nums[l-1]:
                            l-=1
                            
                        l-=1
        
        return quads
        
                         
                
                
                
