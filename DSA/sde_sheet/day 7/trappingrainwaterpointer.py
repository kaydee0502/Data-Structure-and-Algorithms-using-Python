'''

42. Trapping Rain Water
Hard

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
    0 <= n <= 3 * 104
    0 <= height[i] <= 105



'''

class Solution:
    def trap(self, height: List[int]) -> int:
        
        
        l = 0
        r = len(height)-1
        
        lmax = 0
        rmax = 0
        
        water = 0
        
        while l<r:
            
            #print(l,r,water)
            if height[l] <= height[r]:
                
                
                lmax = max(lmax,height[l])
                water += (lmax - height[l]) 
                l+=1
                
            else:
                
                
                
                rmax = max(rmax,height[r])
                water += (rmax - height[r])
                r-=1
                
        return water
                
       
