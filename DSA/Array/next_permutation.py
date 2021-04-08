'''

31. Next Permutation
Medium

Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).

The replacement must be in place and use only constant extra memory.

 

Example 1:

Input: nums = [1,2,3]
Output: [1,3,2]

Example 2:

Input: nums = [3,2,1]
Output: [1,2,3]

Example 3:

Input: nums = [1,1,5]
Output: [1,5,1]

Example 4:

Input: nums = [1]
Output: [1]

 

Constraints:

    1 <= nums.length <= 100
    0 <= nums[i] <= 100


'''

class Solution:
    
    def rev(self,nums,start):
        stop = len(nums)-1
        while stop>start:
            nums[start],nums[stop] = nums[stop],nums[start]
            start+=1
            stop-=1
            
    
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        breakpoint = None
        for i in range(n-1,0,-1):
            if nums[i-1] < nums[i]:
                breakpoint = i-1
                break
            
        if breakpoint == None:
            nums.sort()
            return
            
        for j in range(n-1,breakpoint,-1):
            if nums[j] > nums[breakpoint]:
                nums[j],nums[breakpoint] = nums[breakpoint], nums[j]
                break
                
        self.rev(nums,i)
