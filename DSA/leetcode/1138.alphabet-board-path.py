#
# @lc app=leetcode id=1138 lang=python3
#
# [1138] Alphabet Board Path
#

# @lc code=start
class Solution:
    
    
    def findz(self,c,brd,i,j,res):
        if brd[i][j] == c:
            res+="!"
            return res,i,j
        
        if (ord(brd[i][j])-97)%5 != 0:
            return self.findz(c,brd,i,j-1,res+"L")
        else:
            return self.findz(c,brd,i+1,j,res+"D")
    
    def find(self,c,brd,i,j,res):
        if brd[i][j] == c:
            res+="!"
            return res,i,j
        
        
        
        if (ord(c)-97)//5 == (ord(brd[i][j])-97)//5 and ord(c) > ord(brd[i][j]):
            return self.find(c,brd,i,j+1,res+"R")
            
        elif (ord(c)-97)//5 == (ord(brd[i][j])-97)//5 and ord(c) < ord(brd[i][j]):
            return self.find(c,brd,i,j-1,res+"L")
               
        elif ord(c) < ord(brd[i][j]):
            return self.find(c,brd,i-1,j,res+"U")
            
        else:
            return self.find(c,brd,i+1,j,res+"D")
            
            
    
    
    def alphabetBoardPath(self, target: str) -> str:
        
        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
        
        s = [0,0]
        fin = ""
        for i in target:
            if i == "z":
                r,s[0],s[1] = self.findz(i,board,s[0],s[1],"")
            else:
                r,s[0],s[1] = self.find(i,board,s[0],s[1],"")
            fin += r
            
        return fin
            
            
        
# @lc code=end

