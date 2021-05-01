class Solution:
    
    
    def isRow(self,r,num):
        return not num in r
    
    def isCol(self,sud,j,num):
        for i in range(9):
            if sud[i][j] == num:
                return False
            
        return True
    
    def isBox(self,sud,x,y,num):
        r = (x//3)*3
        c = (y//3)*3
        #print(r,c,num,sud)

        for i in range(r,r+3):
            for j in range(c,c+3):
                #print(i,j,sud[i][j] ==num,sud[i][j],num)
                if sud[i][j] == num:
                    return False
                
        return True
                
        
        
    def checkB(self,sud):
        for i in sud:
            if "." in i:
                return False
        return True
    
    
    def solve(self,sud):

        if self.checkB(sud):
            return True
            
        
        for X in range(81):
            
            i = X//9
            j = X%9
            
            if sud[i][j] == ".":
               

                for k in range(1,10):
                     if self.isRow(sud[i],str(k)) and self.isCol(sud,j,str(k)) and self.isBox(sud,i,j,str(k)):
                        #print(sud)
                        sud[i][j] = str(k)
                      

                        if self.solve(sud):
                            return True



                        sud[i][j] = "."
                break
               
        return False
                    
                    
                    
                    
        
    
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.solve(board)