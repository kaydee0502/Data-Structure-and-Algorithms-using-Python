'''


Fractional Knapsack
Medium Accuracy: 45.14% Submissions: 15392 Points: 4

Given weights and values of N items, we need to put these items in a knapsack of capacity W to get the maximum total value in the knapsack.
Note: Unlike 0/1 knapsack, you are allowed to break the item. 

 

Example 1:

Input:
N = 3, W = 50
values[] = {60,100,120}
weight[] = {10,20,30}
Output:
240.00
Explanation:Total maximum value of item
we can have is 240.00 from the given
capacity of sack. 

Example 2:

Input:
N = 2, W = 50
values[] = {60,100}
weight[] = {10,20}
Output:
160.00
Explanation:
Total maximum value of item
we can have is 160.00 from the given
capacity of sack.

 

Your Task :
Complete the function fractionalKnapsack() that receives maximum capacity , array of structure/class and size n and returns a double value representing the maximum value in knapsack.
Note: The details of structure/class is defined in the comments above the given function.


Expected Time Complexity : O(NlogN)
Expected Auxilliary Space: O(1)


Constraints:
1 <= N <= 10^5
1 <= W <= 10^5


'''


#User function Template for python3

class Solution:    
    #Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, W,Items,n):
        
        Items.sort(key = lambda x : x.weight/x.value)
        
        pro = 0.0
        
        for i in Items:
            #print(pro,i.weight)
            if W == 0:
                break
            
            if i.weight <= W:
                W-=i.weight
                pro+=i.value
                
            else:
                pro += i.value * (W/i.weight)
                W = 0
                
        return pro
                
                
        
            
        
        
        # code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

class Item:
    def __init__(self,val,w):
        self.value = val
        self.weight = w
        
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,W = map(int,input().strip().split())
        info = list(map(int,input().strip().split()))
        Items = [Item(0,0) for i in range(n)]
        for i in range(n):
            Items[i].value = info[2*i]
            Items[i].weight = info[2*i+1]
            
        ob=Solution()
        print("%.2f" %ob.fractionalknapsack(W,Items,n))

# } Driver Code Ends
