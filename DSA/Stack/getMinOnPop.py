def _push(a,n):
    '''
    :param a: given array
    :param n: given size of array
    :return: stack
    '''
    stack = []
    if not a:
        return stack
    current_min = a[0]
    for i in a:
        if i < current_min:
            current_min = i

        stack.append([i,current_min])
    return stack


    # code here
    
def _getMinAtPop(stack):
    '''
    :param stack: our stack
    :return: none, print the elements in order of pop one by one, new line is not required
    '''
    while stack:
        temp = stack.pop()
        print(temp[1],end = " ")
    print()
    # code here

stack = _push([1,6,46,-1,2,0,5],7)
_getMinAtPop(stack)




# GFG


'''

Get minimum element from stack 
Medium Accuracy: 24.49% Submissions: 100k+ Points: 4
You are given N elements and your task is to Implement a Stack in which you can get minimum element in O(1) time.

Example 1:

Input:
push(2)
push(3)
pop()
getMin()
push(1)
getMin()
Output: 3 2 1
Explanation: In the first test case for
query 
push(2)  the stack will be {2}
push(3)  the stack will be {2 3}
pop()    poped element will be 3 the
         stack will be {2}
getMin() min element will be 2 
push(1)  the stack will be {2 1}
getMin() min element will be 1
Your Task:
You are required to complete the three methods push() which take one argument an integer 'x' to be pushed into the stack, pop() which returns a integer poped out from the stack and getMin() which returns the min element from the stack. (-1 will be returned if for pop() and getMin() the stack is empty.)

Expected Time Complexity : O(1) for all the 3 methods.
Expected Auixilliary Space : O(1) for all the 3 methods.

Constraints:
1 <= Number of queries <= 100
1 <= values of the stack <= 100

'''

#User function Template for python3

class stack:
    def __init__(self):
        self.s=[]
        self.minEle=float("inf")

    def push(self,x):
        
        if x < self.minEle:
            self.minEle = x
            
        self.s.append([x,self.minEle])
        
        #CODE HERE

    def pop(self):
        #print(self.s)
        if self.s:
            s = self.s.pop()
            if self.s:
            
                self.minEle = self.s[-1][1]
            else:
                self.minEle = float("inf")
            return s[0]
        return -1
        #CODE HERE
        

    def getMin(self):
        if self.s:
        
            return self.s[-1][1]
        return -1
        #CODE HERE

#{ 
#  Driver Code Starts
#contributed by RavinderSinghPB
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        q = int(input())

        arr = [int(x) for x in input().split()]

        stk=stack()  

        qi = 0
        qn=1
        while qn <= q:
            qt = arr[qi]

            if qt == 1:
                stk.push(arr[qi+1])
                qi+=2
            elif qt==2:
                print(stk.pop(),end=' ')
                qi+=1
            else:
                print(stk.getMin(),end=' ')
                qi+=1
            qn+=1
        print()

# } Driver Code Ends