'''


Linked List in Zig-Zag fashion
Easy Accuracy: 52.86% Submissions: 9018 Points: 2

Given a Linked list, rearrange it such that converted list should be of the form a < b > c < d > e < f .. where a, b, c are consecutive data node of linked list and such that the order of linked list is sustained.
For example: In 11 15 20 5 10 we consider only 11 20 5 15 10 because it satisfies the above condition and the order of linked list. 5 20 11 15 10 is not considered as it does not follow the order of linked list.

To maintain the order, keep swapping the adjacent nodes of the linked list (whenever required) to get the desired output.  

Example 1:

Input:
LinkedList: 1->2->3->4 
Output: 1 3 2 4

Example 2:

Input:
LinkedList: 11->15->20->5->10
Output: 11 20 5 15 10
Explanation: In the given linked list,
after arranging them as 11 < 20 > 5
< 15 > 10 in the pattern as asked above.

Your Task:
The task is to complete the function zigZag() which should reorder the list as required and return the head of the linked list.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

Constraints:
1 <= size of linked list(a) <= 1000

'''


#User function Template for python3


'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
'''
class Solution:
    
    def swap(self,a,b,p,n):
        
        p.next = b
        a.next = n
        b.next = a
        
        #print(p.data,a.data,b.data,n.data)
        
        pass
    
    
    def zigzag(self, head_node):
        dummy = Node(0)
        dummy.next = head_node
        tmp = dummy.next
        i = 0
        prev = dummy
        
        
        while tmp.next:
            
            a = tmp
            b = tmp.next
            #print(a.data,b.data,i)
            if i % 2 == 0:
                if a.data > b.data:
                    #print("<")
                    self.swap(a,b,prev,b.next)
                    tmp = b
                    pass
                
            else:
                if a.data < b.data:
                    #print(">")
                    self.swap(a,b,prev,b.next)
                    tmp = b
                    pass
                
            prev = tmp
            i+=1
            tmp = tmp.next
            
        return dummy.next
        
        
        # Complete this function

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import io
import sys

# Node class
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

#Linked list class
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    # append at the end of the list
    def append(self,new_node):
        if self.head is None:
            self.head=new_node
            self.tail=new_node
            return
        self.tail.next=new_node
        self.tail = self.tail.next

# Print linked list
def print_list(head_node):
    curr_node = head_node;
    while curr_node is not None:
        print(curr_node.data, end = ' ')
        curr_node = curr_node.next
    print()

if __name__ == '__main__':
    for cases in range(int(input())):
        n = int(input())
        nodes = list(map(int,input().strip().split()))
        
        a = LinkedList()
        for x in nodes:
            a.append(Node(x))
        
        print_list(Solution().zigzag(a.head))

# } Driver Code Ends
