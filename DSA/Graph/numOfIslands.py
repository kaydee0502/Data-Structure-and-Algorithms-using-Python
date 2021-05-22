


class Solution:
    
    
    def dfs(self,i,j,m,n,mat):
        
        if i < 0 or j < 0 or i>=m or j>=n:
            return
        
        
        
        if mat[i][j] == "0":
            return 
        
        mat[i][j]="0"
        
        di = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        
        for x,y in di:
            self.dfs(i+x,j+y,m,n,mat)
            
        
    
    
    #Function to find the number of islands.
    def numIslands(self, grid):
        cc = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                if grid[i][j] == "1":
                    
                    self.dfs(i,j,len(grid),len(grid[0]),grid)
                    cc+=1
        return cc
	    
		#Code here

#{ 
#  Driver Code Starts



if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = map(int, input().split())
		grid = []
		for _ in range(n):
			a = list(input().split())
			grid.append(a)
		obj = Solution()
		ans = obj.numIslands(grid)
		print(ans)

# } Driver Code Ends