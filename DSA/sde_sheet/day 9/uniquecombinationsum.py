'''


40. Combination Sum II
Medium

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

 

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]

 

Constraints:

    1 <= candidates.length <= 100
    1 <= candidates[i] <= 50
    1 <= target <= 30




'''

class Solution:
    
    
    def rec(self,a,currsum,t,p,r):
        
        if currsum == t:
            p.append(r)
        
        
        for i in range(len(a)):
            if i > 0 and a[i] == a[i-1]:
                continue
            
            # terminate if sum is already exceeded
            if currsum > t:
                break
                
            self.rec(a[i+1:],currsum+a[i],t,p,r+[a[i]])
        
        
    
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        p = []
        
        
        candidates.sort()
        
        self.rec(candidates,0,target,p,[])
        
        return p

