#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode,l = float("-inf"),r= float("inf")) -> bool:
        if not root:
            return True
        
        #print(root.val,cmin,cmax)
        if not l < root.val < r:
            return False
            
        a = self.isValidBST(root.left, l=l, r = root.val)
        b = self.isValidBST(root.right, l = root.val, r=r )
        
        
        return a and b
                
        
        

        
        
        
        
# @lc code=end

