#
# @lc app=leetcode id=417 lang=python3
#
# [417] Pacific Atlantic Water Flow
#

# @lc code=start
class Solution:
    
    def cago(self,ocean,i,j,m,n,vis,parent,visited):
        
        
        
        
        if i < 0 or j < 0:
            vis[0] = True
            return
            
        if i >= m or j >= n:
            vis[1] = True
            return
        #print(i,j)
        
        if ocean[i][j] > parent:
            return
        
        if visited[i][j] == True:
            return
        visited[i][j] = True
        
        
        
        
        #print(i,j,"down")
        
        self.cago(ocean,i+1,j,m,n,vis,ocean[i][j],visited)
        #print(i,j,"up")
        self.cago(ocean,i-1,j,m,n,vis,ocean[i][j],visited)
        #print(i,j,"right")
        self.cago(ocean,i,j+1,m,n,vis,ocean[i][j],visited)
        #print(i,j,"left")
        self.cago(ocean,i,j-1,m,n,vis,ocean[i][j],visited)
            
        
        
        
    
    
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        res = []
        m = len(heights)
        n = len(heights[0])
        
        for r in range(len(heights)):
            for c in range(len(heights[r])):
                check = [False,False]
                visi = [[False for i in range(n)] for j in range(m)]
                self.cago(heights,r,c,m,n,check,float("inf"),visi)
                #print(r,c,check)
                if sum(check) == 2:
                    res.append([r,c])
                    
        
        return res
                
# @lc code=end

