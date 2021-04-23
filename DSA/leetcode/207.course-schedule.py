#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start
from collections import defaultdict
class Solution:
    
    def __init__(self):
        self.g = defaultdict(list)
        
        
    def addEdge(self,u,v):
        self.g[u].append(v)
        
    def isCycle(self,s,vis,rec):
        vis[s] = True
        rec[s] = True
        #print(rec,vis)
        
        for i in self.g[s]:
            if rec[i] == True:
                return True
            
            if vis[i] == False:
                if self.isCycle(i,vis,rec):
                    return True
                
            
        rec[s] = False
        return False
        
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        for i in prerequisites:
            self.addEdge(i[1],i[0])
            
        vis = [False] *(numCourses+1)
        
        for i in range(numCourses):
            #print(self.g)
            if vis[i] == False:
                rec = [False]*numCourses
                if self.isCycle(i,vis,rec):
                    return False
                
        return True
            
            
# @lc code=end

