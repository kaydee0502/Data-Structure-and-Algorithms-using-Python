#
# @lc app=leetcode id=1103 lang=python3
#
# [1103] Distribute Candies to People
#

# @lc code=start
class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        
        ini = [0] * num_people
        
       
        i = 0
        row = 0
        while candies:
            #print(ini)
            if i >= num_people:
        
                i = i%num_people
                row += 1
            
            give = row*num_people + (i+1)
            
            if give > candies:
                ini[i] += candies
                return ini
            else:
                ini[i]+=give
                candies -= give
            i+=1
        return ini
            
            
            
            
# @lc code=end

