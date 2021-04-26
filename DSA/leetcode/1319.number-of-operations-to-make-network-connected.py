#
# @lc app=leetcode id=1319 lang=python3
#
# [1319] Number of Operations to Make Network Connected
#

# @lc code=start
class Solution:
    
    def __init__(self):
        self.g = defaultdict(list)
    
    def addEdge(self,u,v):
        self.g[u].append(v)
        self.g[v].append(u)
        
    
    def dfs(self,s,vis):
        
        vis[s] = True
        
        for i in self.g[s]:
            if vis[i] == False:
                self.dfs(i,vis)
        
        
        
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        CC = 0
        
        for i in connections:
            self.addEdge(i[0],i[1])        
        
        vis = [False] * n
        
        for i in range(n):
            if vis[i] == False:
                self.dfs(i,vis)
                CC+=1
                
        edges = len(connections)
        
        if edges >= n-1:
            return CC-1
        
        return -1
        
# @lc code=end

