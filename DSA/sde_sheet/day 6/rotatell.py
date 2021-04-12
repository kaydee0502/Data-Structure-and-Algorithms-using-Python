'''

61. Rotate List
Medium

Given the head of a linked list, rotate the list to the right by k places.

 

Example 1:

Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Example 2:

Input: head = [0,1,2], k = 4
Output: [2,0,1]

 

Constraints:

    The number of nodes in the list is in the range [0, 500].
    -100 <= Node.val <= 100
    0 <= k <= 2 * 10^9



'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        
        if not head or k ==0:
            return head
        COUNT = 0
        
        t = head
        
        while t:
            COUNT +=1
            t = t.next
            
        k = k % COUNT
        if k == 0:
            return head
        
        k = COUNT - k-1
        
        t = head
        head2 = head
        for i in range(k):
            t = t.next
            
        head = t.next
        t.next = None
        t = head
        
        while t.next:
            t = t.next
            
        t.next= head2
        
        return head
            
        
        
