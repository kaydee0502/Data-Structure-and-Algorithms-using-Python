#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def reverse(self,node,head):
        if not head:
            return node
        
        temp = head.next
        head.next = node
        
        return self.reverse(head,temp)
    
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        f = head
        s = head
        prev = None
        n = 0
        while f.next and f.next.next:
            n+=1
            f = f.next.next
            prev = s
            s = s.next
            
        
        if not f:
            s= prev
        
        
            
        print(s.val)
        s.next = self.reverse(None,s.next)
        
        r = s.next
        l = head
        for i in range(n):
            temp = s.next
            s.next = s.next.next
            temp.next = l.next
            l.next = temp
            l = l.next.next
            
        return head
            
        
        
        
        
        
        
       
            
            
    
        
        
# @lc code=end

