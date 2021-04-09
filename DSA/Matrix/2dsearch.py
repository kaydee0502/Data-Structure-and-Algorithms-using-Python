'''

Leet code:

74. Search a 2D Matrix
Medium

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

    Integers in each row are sorted from left to right.
    The first integer of each row is greater than the last integer of the previous row.

 

Example 1:

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false

 

Constraints:

    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 100
    -104 <= matrix[i][j], target <= 104


'''

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        
        for i,r in enumerate(matrix):
            if r[0] <= target <= r[-1]:
                break
                
        for j in matrix[i]:
            if j == target:
                return True
            
        return False
        
        
'''

GFG


Search in a matrix
Easy Accuracy: 45.22% Submissions: 7473 Points: 2

Given a matrix mat[][] of size N x M, where every row and column is sorted in increasing order, and a number X is given. The task is to find whether element X is present in the matrix or not.


Example 1:

Input:
N = 3, M = 3
mat[][] = 3 30 38 
         44 52 54 
         57 60 69
X = 62
Output:
0
Explanation:
62 is not present in the
matrix, so output is 0


Example 2:

Input:
N = 1, M = 6
mat[][] = 18 21 27 38 55 67
X = 55
Output:
1
Explanation:
55 is present in the
matrix at 5th cell.


Your Task:
You don't need to read input or print anything. You just have to complete the function matSearch() which takes a 2D matrix mat[][], its dimensions N and M and integer X as inputs and returns 1 if the element X is present in the matrix and 0 otherwise.


Expected Time Complexity: O(N+M).
Expected Auxiliary Space: O(1).


Constraints:
1 <= N, M <= 30
1 <= mat[][] <= 100
1<= X <= 100
'''

class Solution:
	def matSearch(self,mat, N, M, X):
	    
	    #print(mat)
	    for i,r in enumerate(mat):
	        if r[0] <= X <= r[-1]:
	            for j in r:
        	        if j == X:
        	            return 1
	        
	    
	            
	    return 0
		# Complete this function

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        
        arr = [int(x) for x in input().split()]
        x = int(input())
        mat = [[0 for j in range(m)] for i in range(n)]
        
        for i in range(n):
            for j in range(m):
                mat[i][j] = arr[i * m + j]
        ob = Solution()
        print(ob.matSearch(mat, n, m, x))
# } Driver Code Ends


#GFG 2 traverse from top right

class Solution:
	def matSearch(self,mat, N, M, X):
	    
	    #print(mat)
	    i=0
	    j=M-1
	    
	    while i < N and j > -1:
	        if mat[i][j] == X:
	            return 1
	            
	        elif mat[i][j] > X:
	            j-=1
	       
	        else:
	            i+=1
	            
	    return 0
	        
	        
	        
# Leetcode 2 binary search

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        if not matrix:
            return False
        
        hi = (len(matrix)*len(matrix[0]))-1
        m = len(matrix[0])
        lo = 0
        
        
        while hi >= lo:
            mid = (hi+lo)//2
            print(lo,mid,hi)
            if matrix[mid//m][mid%m] == target:
                return True
            
            elif matrix[mid//m][mid%m] < target:
                lo = mid+1
                
            else:
                hi = mid-1
             
        return False
