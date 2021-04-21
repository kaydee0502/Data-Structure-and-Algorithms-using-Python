#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def __init__(self):
        self.trav = []
    
    def inorder(self,root):
        if not root:
            return 
    
        self.inorder(root.left)
        self.trav.append(root.val)
        self.inorder(root.right)
        
    
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        self.inorder(root) 
        return self.trav
        
       
        
        
# @lc code=end

