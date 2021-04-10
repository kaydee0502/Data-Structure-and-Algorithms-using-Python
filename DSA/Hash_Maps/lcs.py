'''

128. Longest Consecutive Sequence
Hard

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

 

Constraints:

    0 <= nums.length <= 104
    -109 <= nums[i] <= 109

 
Follow up: Could you implement the O(n) solution?


'''

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        h = {}
        
        for i in nums:
            h[i] = 1
            
        count = 0
        
        cm = 0
        
        for i in nums:
            if not i-1 in h:
                t = i
                
                while t in h:
                    count+=1
                    t+=1
                    
                cm = max(cm,count)
                count = 0
            
        return max(cm,count)
