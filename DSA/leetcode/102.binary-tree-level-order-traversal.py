#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        
        if not root:
            return []
        q = [root]
        bfs = []
        levels = [root.val]
        
        while q:
            if len(q) == len(levels):
                bfs.append(levels)
                levels = []
                
            if q[0].left:
                q.append(q[0].left)
                levels.append(q[0].left.val)
                
            if q[0].right:
                q.append(q[0].right)
                levels.append(q[0].right.val)
                
            q.pop(0)
            
            
        return bfs
            
        
        
        
# @lc code=end

