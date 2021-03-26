class Solution:
    def celebrity(self, M, n):
        # code here 
        stack = []
        # Iterate over the entire matrix
        for i,r in enumerate(M):
            for j,c in enumerate(r):
                # Check if cell value is 1, this means this cell at i position knows jth
                # person which makes jth person a possible celebrity
                if c == 1:
                    stack.append(j)
                    
        # if no one knows anybody, that simply means no one is celebrity
        if not stack:
            return -1
        
        # Check each candidates, if they really do not know anyboby then they are celebrity, return that index
        
        while stack:
            temp = stack.pop()
            for k in M[temp]:
                if k == 1:
                    break
            else:
                return temp
                
        # if every candidates fails the check, return -1
        return -1
