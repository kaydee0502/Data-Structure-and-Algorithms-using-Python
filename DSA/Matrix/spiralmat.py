'''

54. Spiral Matrix
Medium

3711

660

Add to List

Share
Given an m x n matrix, return all elements of the matrix in spiral order.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100

'''

class Solution:
    
    
    def __init__(self):
        self.a = []
        
        
    def popu(self,s,l,r,u,d,m):
        
        print(self.a,s,l,r,u,d)
        #right
        nex = s
        
        if l > r or u > d:
            return
        
        i = l
        while i <= r:
            self.a.append(m[s][i])
            
            if i==r:
                break
            i+=1
            travright=True
            
     
        s+=1
        #down
        while s <= d:
            self.a.append(m[s][i])
            
            if s==d:
                break
            s+=1
            travdown = True
            
        i-=1    
        
    
        
        #left
        while i >= l:
            self.a.append(m[s][i])
            if i == l:
                break
                
            i-=1
            
        s-=1
        #up
        
        while s > u:
            self.a.append(m[s][i])
            if s == u+1:
                break
                
            s-=1
            
        
        self.popu(nex+1,l+1,r-1,u+1,d-1,m)
        
        
        
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        s = 0
        l,r,u,d = 0,len(matrix[0])-1,0,len(matrix)-1
        
        
        
        if len(matrix) == 1:
            return matrix[0]
        if len(matrix[0]) == 1:
            for i in matrix:
                self.a.append(i[0])
            return self.a
        
        
        
        self.popu(s,l,r,u,d,matrix)
        return self.a[:len(matrix)*len(matrix[0])]
        
        
# method 2 (better)

class Solution:
    def __init__(self):
        self.s = []


    def dfs(self,m,n,i,j,mat,vis):

        si,sj = i,j
        #print(*vis,sep="\n")
        #print("ok",i,j,m,n)
        if i<0 or j<0 or i>=n or j>=m:
            return

        if vis[i][j] == 1:
            return

      
        
        while j < m and vis[i][j] == 0:
            vis[i][j] = 1
            self.s.append(mat[i][j])
            j+=1

        j-=1
        i+=1
        
        #print(i,j)
        
      

        while i < n and vis[i][j] == 0:
            vis[i][j] = 1
            self.s.append(mat[i][j])
            i+=1

        i-=1
        j-=1

        
        #print(i,j)
        
    
        while j >= 0 and vis[i][j] == 0:
            vis[i][j] = 1
            self.s.append(mat[i][j])
            j-=1

        j+=1
        i-=1
        
        #print(i,j)
       

        while i >= 0 and vis[i][j] == 0:

            vis[i][j] = 1
            self.s.append(mat[i][j])
            i-=1
        i+=1
        j+=1
       
        #print(i,j)

        

        self.dfs(m,n,si+1,sj+1,mat,vis)

        
        


        





    def solve(self, matrix):
        if not matrix:
            return []
        if not matrix[0]:
            return []
        n = len(matrix)
        m = len(matrix[0])
        vis = [[0 for i in range(m)] for j in range(n)]

        i = 0
        j = 0
        self.dfs(m,n,i,j,matrix,vis)
        return self.s


        
