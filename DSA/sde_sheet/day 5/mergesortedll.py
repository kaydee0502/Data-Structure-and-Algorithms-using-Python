'''

21. Merge Two Sorted Lists
Easy

Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

 

Example 1:

Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:

Input: l1 = [], l2 = []
Output: []

Example 3:

Input: l1 = [], l2 = [0]
Output: [0]

 

Constraints:

    The number of nodes in both lists is in the range [0, 50].
    -100 <= Node.val <= 100
    Both l1 and l2 are sorted in non-decreasing order.



'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        if not l1 and not l2:
            return
        
        if not l1:
            return l2
        
        if not l2:
            return l1
        
        
        if l1.val <= l2.val:
            s1 = l1
            s2 = l2
        else:
            print("swap")
            s1=l2
            s2 = l1
            
        
        toret = s1
        t = None
        #print(s1.val,s2.val)
        while s1 and s2:
            t = None
            while s1 and s1.val <= s2.val:
            
                t = s1
                s1 = s1.next
                
            
            t.next = s2
            s1,s2 = s2,s1

        
        #s1.next = s2
        return toret
