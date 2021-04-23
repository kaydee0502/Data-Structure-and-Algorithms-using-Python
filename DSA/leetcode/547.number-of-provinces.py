#
# @lc app=leetcode id=547 lang=python3
#
# [547] Number of Provinces
#

# @lc code=start
class Solution:
    
    def bfs(self,s,mat):
        q = [s]
        
        
        while q:
            c = q.pop(0)
            mat[c][c] = 0
            for i in range(len(mat)):
                if mat[c][i] == 1:
                    mat[c][i] = 0
                    q.append(i)
                    
            
                
            
            
            
    
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        cc = 0
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    self.bfs(i,isConnected)
                    cc+=1
                    
        return cc
                    
                
        
# @lc code=end

