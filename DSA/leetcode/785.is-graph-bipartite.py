#
# @lc app=leetcode id=785 lang=python3
#
# [785] Is Graph Bipartite?
#

# @lc code=start
from collections import defaultdict
class Solution:
    def __init__(self):
        self.g = defaultdict(list)
        
    
    def addEdge(self,u,v):
        self.g[u] = v
        
    def biUtil(self,u,color):
        
        q = [u]
        color[u] = 0
        
        while q:
            
            u = q.pop(0)
            
            for v in self.g[u]:
                if color[v] == -1:
                    q.append(v)
                    color[v] = 1 - color[u]
                    
                elif color[u] == color[v]:
                    return False
                
        return True
            
        
    
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = 0
        
        for i in range(len(graph)):
            if graph[i]:
                n = max(n,max(graph[i]))
                self.addEdge(i,graph[i])
            
        color = [-1] * (n+1)
        
        for i in range(n):
            if color[i] == -1:
                if not self.biUtil(i,color):
                    return False
        
        return True
                                  
        
# @lc code=end

