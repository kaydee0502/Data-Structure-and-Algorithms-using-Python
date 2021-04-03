'''

Max rectangle
Medium Accuracy: 47.59% Submissions: 23830 Points: 4

Given a binary matrix. Find the maximum area of a rectangle formed only of 1s in the given matrix.

Example 1:

Input:
n = 4, m = 4
M[][] = {{0 1 1 0},
         {1 1 1 1},
         {1 1 1 1},
         {1 1 0 0}}
Output: 8
Explanation: For the above test case the
matrix will look like
0 1 1 0
1 1 1 1
1 1 1 1
1 1 0 0
the max size rectangle is 
1 1 1 1
1 1 1 1
and area is 4 *2 = 8.

Your Task: 
Your task is to complete the function maxArea which returns the maximum size rectangle area in a binary-sub-matrix with all 1’s. The function takes 3 arguments the first argument is the Matrix M[ ] [ ] and the next two are two integers n and m which denotes the size of the matrix M. 

Expected Time Complexity : O(n*m)
Expected Auixiliary Space : O(m)

Constraints:
1<=n,m<=1000
0<=M[][]<=1
'''

class Solution:
    
    def nsl(self,arr,n):
        stack = []
        smallLeft = []
        for i in range(n):
            while stack:
                if stack[-1][0] < arr[i]:
                    smallLeft.append(stack[-1][1])
                    break
                stack.pop()
            else:
                smallLeft.append(-1)
                
            stack.append([arr[i],i])
        
        return smallLeft
        
    def nsr(self,arr,n):
        stack = []
        smallRight = []
        
        for i in range(n-1,-1,-1):
            while stack:
                if stack[-1][0] < arr[i]:
                    smallRight.append(stack[-1][1])
                    break
                stack.pop()
            else:
                smallRight.append(n)
            stack.append([arr[i],i])
        return smallRight[::-1]
        
    def maxArea(self,M, n, m):
        # code here
        #print(self.nsl([6,2,5,4,5,1,6],7))
        #print(self.nsr([6,2,5,4,5,1,6],7))
        curr = [0]*m
        area = float("-inf")
        for i in range(n):
            for j in range(m):
                if M[i][j]!=0:
                    curr[j] += 1
                else:
                    curr[j] = 0
                    
            sL = self.nsl(curr,m)
            sR = self.nsr(curr,m)
            tarea = float("-inf")
            for k in range(m):
                if sL[k] == -1 and sR[k] == m:
                    temp = m*curr[k]
                else:
                    temp = (sR[k] - sL[k] - 1)*curr[k]
                
                if temp > tarea:
                    tarea = temp
                    
            if tarea > area:
                area = tarea
                
        return area
                    
            
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3



# Driver Code 
if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        R, C = input().split()
        a=list(map(int,input().split()))
        j=0
        A=[]
        R=int(R)
        C=int(C)
        for i in range(0,R):
            A.append(a[j:j+C])
            j=j+C
        # print(A)
        print(Solution().maxArea(A, R, C)) 
