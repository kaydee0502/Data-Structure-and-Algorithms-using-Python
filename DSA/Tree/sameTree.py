'''

100. Same Tree
Easy

3154

85

Add to List

Share
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

 

Example 1:


Input: p = [1,2,3], q = [1,2,3]
Output: true
Example 2:


Input: p = [1,2], q = [1,null,2]
Output: false
Example 3:


Input: p = [1,2,1], q = [1,1,2]
Output: false
 

Constraints:

The number of nodes in both trees is in the range [0, 100].
-10^4 <= Node.val <= 10^4

'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    
    
    def look(self,r1,r2):
        if not r1 and not r2:
            return True
        
        if not r1 or not r2:
            return False
        
        if r1.val != r2.val:
            return False
        
        
        a =  self.look(r1.left,r2.left)
        b = self.look(r1.right,r2.right)
        
        return a and b
        
        
    
            
        
        
        
        
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        return self.look(p,q)
        
