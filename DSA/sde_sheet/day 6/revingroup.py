'''

25. Reverse Nodes in k-Group
Hard

Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

Follow up:

    Could you solve the problem in O(1) extra memory space?
    You may not alter the values in the list's nodes, only nodes itself may be changed.

 

Example 1:

Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]

Example 2:

Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]

Example 3:

Input: head = [1,2,3,4,5], k = 1
Output: [1,2,3,4,5]

Example 4:

Input: head = [1], k = 1
Output: [1]

 

Constraints:

    The number of nodes in the list is in the range sz.
    1 <= sz <= 5000
    0 <= Node.val <= 1000
    1 <= k <= sz



'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def rev(self,prev,t1,t2):
      
        a = None
        b = t1
        c = t1.next
        
        while b:
            b.next = a
            
            a = b
            b = c
            if not b or b == t2:
                break
                
            c = c.next
            
        prev.next = a
        t1.next = t2
        
    
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        
        if not head:
            return
        
        
        dummy = ListNode(0)
        dummy.next = head
        
        t1=head
        t2=head
        prev = dummy
        
        
        i = 0
        while t2:
            
            for j in range(k):
                
                if not t2:
                    return dummy.next
            
                t2 = t2.next
                
        
            self.rev(prev,t1,t2)
            
            prev = t1
            t1 = t2
            i+=1
            
            
            
        return dummy.next
    
            
            
        
