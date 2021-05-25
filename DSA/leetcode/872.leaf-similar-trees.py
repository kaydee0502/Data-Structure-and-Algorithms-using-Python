#
# @lc app=leetcode id=872 lang=python3
#
# [872] Leaf-Similar Trees
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def getLeafs(self,root,leafs):
        if not root:
            return
        
        self.getLeafs(root.left,leafs)
        
        if not root.left and not root.right:
            leafs.append(root.val)
            
        self.getLeafs(root.right,leafs)
        
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        
        a = []
        b = []
        self.getLeafs(root1,a)
        self.getLeafs(root2,b)
        
        return a == b
        
# @lc code=end

