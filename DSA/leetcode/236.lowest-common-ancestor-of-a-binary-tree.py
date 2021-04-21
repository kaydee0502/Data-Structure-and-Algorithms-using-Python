#
# @lc app=leetcode id=236 lang=python3
#
# [236] Lowest Common Ancestor of a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    

        
    def find(self,root,a,b):
        
        if not root or root == a or root == b:
            return root
        
        l = self.find(root.left,a,b)
        r = self.find(root.right,a,b)
        
        if l and r:
            return root
        return l or r
      
     
        
        
        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.find(root,p,q)
# @lc code=end

