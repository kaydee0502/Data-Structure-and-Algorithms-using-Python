#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq
class Solution:
    
    
        
        
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        
        class Wrapper():
            def __init__(self, node):
                self.node = node
            def __lt__(self, other):
                return self.node.val < other.node.val
        
        k = len(lists)
        heap = []
        heapq.heapify(heap)
        
        for i in lists:
            if i:
                heapq.heappush(heap,Wrapper(i))
                
        dummy = ListNode(0)
        temp = dummy
        
        while len(heap) > 0:
            cur = heapq.heappop(heap).node
            
            temp.next = cur
            temp = temp.next
            cur = cur.next
            if cur:
                heapq.heappush(heap,(Wrapper(cur)))
                
        return dummy.next
            
            
        
# @lc code=end

