#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return
        try:
            root = TreeNode(preorder[0])
        except:
            print(inorder,preorder)
            return
        spl = inorder.index(preorder[0])
        preorder = preorder[1:]
        
        lin = inorder[:spl]
        rin = inorder[spl+1:]
        lpre= preorder[:spl]
        rpre= preorder[spl:]
        
        
        root.left = self.buildTree(lpre,lin)
        root.right = self.buildTree(rpre,rin)
        
        return root
        
        
# @lc code=end

