#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        f = head
        for i in range(n):
            f = f.next
            
        dummy = ListNode(0)
        dummy.next = head
        ret = dummy
        s = head
        
        while f:
            f =  f.next
            dummy = s
            s = s.next 
            
        dummy.next = dummy.next.next
        
        return ret.next
        
# @lc code=end

