'''
51. N-Queens
Hard

2884

107

Add to List

Share
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

 

Example 1:


Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
Example 2:

Input: n = 1
Output: [["Q"]]
 

Constraints:

1 <= n <= 9

'''

class Solution:
    
    
    def __init__(self):
        self.cache = {}
    
    def checkRow(self,row):
        if list(filter(lambda x : x == "Q",row)) != []:
            return False
        return True
    
    def checkCol(self,chess,i):
        n = len(chess)
        
        for c in chess:
            if c[i] == "Q":
                return False
            
        return True
    
    
    def checkDiag(self,x,y,chess):
        if chess[x][y] == "Q":
            return False
            
        i,j = x,y   
        while min(i,j) != -1:
            if chess[i][j] == "Q":
                return False
            i-=1
            j-=1
            
        i,j = x,y
        while max(i,j) != len(chess):
            if chess[i][j] == "Q":
                return False
            i+=1
            j+=1
            
        i,j = x,y
        
        while i != -1 and j != len(chess):
            if chess[i][j] == "Q":
                return False
            
            i-=1
            j+=1
            
            
        i,j = x,y
        
        while j != -1 and i != len(chess):
            if chess[i][j] == "Q":
                return False
            
            i+=1
            j-=1
            
            
        return True
    
    
    
            
            
        
        
    def nQ(self,chess,n,q,res,j):
        if q <= 0:
            t = []
            for i in chess:
                t.append("".join(i))
            res.append(t)
            #print(res)
          
            return
        
        for i in range(n):
                if chess[i][j] == "." and self.checkRow(chess[i]) and self.checkCol(chess,j) and self.checkDiag(i,j,chess):
                    chess[i][j] = "Q"
                    
                    
                    self.nQ(chess,n,q-1,res,j+1)
                    
                    chess[i][j] = "."
                    
                    
                    
            
            
        
    
    
    
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        chess = [["." for i in range(n)] for j in range(n)]
        
        res = []
        
        self.nQ(chess,n,n,res,0)
        
        return sorted(res)
       
        
        
        
        
        