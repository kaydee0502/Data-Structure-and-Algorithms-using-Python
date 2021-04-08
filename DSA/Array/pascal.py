'''
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

 

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:

Input: numRows = 1
Output: [[1]]

 

Constraints:

    1 <= numRows <= 30
'''

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        
        if numRows == 2:
            return [[1],[1,1]]
        
        # triangle
        ptri = []
        for i in range(numRows):
            row = [1]
            #initial nominator
            n = i
            #initial denominator
            d = 1
            # cumulative nominator
            nc = n
            # cumulative denominator
            dc = d
            for j in range(i):
                #print(">>",i,j)
                #print(n,d)
                row.append(nc//dc)
                
                n-=1
                nc = nc *n
                
                d+=1
                dc = dc*d
                
            ptri.append(row)

            
        return ptri

