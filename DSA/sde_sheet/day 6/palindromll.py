'''

234. Palindrome Linked List
Easy

Given the head of a singly linked list, return true if it is a palindrome.

 

Example 1:

Input: head = [1,2,2,1]
Output: true

Example 2:

Input: head = [1,2]
Output: false

 

Constraints:

    The number of nodes in the list is in the range [1, 105].
    0 <= Node.val <= 9

 
Follow up: Could you do it in O(n) time and O(1) space?

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def Rev(self,p):
        a = None
        b = p
        c = p.next
        
        while b:
            b.next = a
            
            a = b
            b = c
            if not b:
                return a
            c = c.next
            
        return a
            
        
        
    def isPalindrome(self, head: ListNode) -> bool:
        
       
        if not head.next:
            return True
            
        
        f = head
        s = head
        
        while f.next and f.next.next:
            f = f.next.next
            s = s.next
            
        s.next = self.Rev(s.next)
        
        s = s.next
        
        k = head
        
        while s:
            if s.val != k.val:
                return False
                
            s = s.next
            k = k.next
            
        return True
    
        
