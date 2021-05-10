#User function Template for python3

class Solution:
    
    def isPalin(self,S):
        return S == S[::-1]
        
        
    def recus(self,S,s,e,res,strs):
        print(s,e)
        if s > e:
            print("lol")
            strs.append(res)
            return
        
        i = s
        while i <= e:
            if self.isPalin(S[s:i+1]):
                print(S[s:i+1])
             
                self.recus(S,i+1,e,res+[S[s:i+1]],strs)
            i+=1
                
        
        
        
        
        
        
    
    def getGray(self, S):
        s = 0
        e = len(S)-1
        strs = []
        
        self.recus(S,s,e,[],strs)
        return sorted(strs)
        # code here 

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        S=input()
        
        ob = Solution()
        allPart = ob.getGray(S)
        
        for i in range(len(allPart)): 
            for j in range(len(allPart[i])): 
                print(allPart[i][j], end = " ") 
            print() 
# } Driver Code Ends