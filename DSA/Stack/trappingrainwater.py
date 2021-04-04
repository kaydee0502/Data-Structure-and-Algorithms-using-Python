'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

Example 1:

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9

 

Constraints:

    n == height.length
    0 <= n <= 3 * 10^4
    0 <= height[i] <= 10^5

'''

class Solution:
    def trap(self, height: List[int]) -> int:
        lmax = []
        rmax = []
        
        cmax = [-1,-1]
        for i in range(len(height)):
            lmax.append(cmax[1])
            if height[i] > cmax[0]:
                cmax = [height[i],i]
                
        cmax = [-1,-1]
        
        for i in range(len(height)-1,-1,-1):
            rmax.append(cmax[1])
            if height[i] > cmax[0]:
                cmax = [height[i],i]
                
       
        rmax.reverse()
        water = 0
        for i in range(len(height)):
            if lmax[i] == -1 or rmax[i] == -1:
                water+=0
            elif height[i] < height[lmax[i]] and height[i] < height[rmax[i]]:
               
                wtt = min(height[lmax[i]],height[rmax[i]])
                water += wtt - height[i]
                
        return water
