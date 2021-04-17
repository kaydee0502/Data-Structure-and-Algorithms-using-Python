'''

328. Odd Even Linked List
Medium

2997

338

Add to List

Share
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]
Example 2:


Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]
 

Constraints:

The number of nodes in the linked list is in the range [0, 10^4].
-10^6 <= Node.val <= 10^6

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        
        if not head:
            return
        
        tail = None
        
        temp = head
    
        last = None
        while temp and temp.next and temp.next.next:
            
        
            temp = temp.next.next
            
        if temp.next:
            last = temp.next
            
        tail = temp
        stop = tail
        
        
       
        temp = head
        print(stop.val)
        
        while temp != stop:
            
            p = temp.next
            
            temp.next = temp.next.next
            p.next = None
            
            tail.next = p
            tail = tail.next
            
            temp = temp.next
            
        if last:
            tail.next = last
        return head
        
        
        
        
