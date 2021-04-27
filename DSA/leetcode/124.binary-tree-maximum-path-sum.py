#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
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
        self.msum = float("-inf")
        
    def rec(self,root):
        if not root:
            return 0
        
        lmax = max(self.rec(root.left),0)
        rmax = max(self.rec(root.right),0)
        
        cmax = root.val + lmax + rmax
        
        self.msum = max(self.msum,cmax)
        
        return root.val + max(lmax,rmax)
    
    
        
    def maxPathSum(self, root: TreeNode) -> int:
        self.rec(root)
        return self.msum
# @lc code=end

