#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        
        if not root:
            return
        
        q = [root]
        
        bfs = []
        l = [root.val]
        i = 0
        
        while q:
            if len(q) == len(l):
                if i%2 != 0:
                    l.reverse()
                    
                bfs.append(l)
                l = []
                i+=1

                    
            
            if q[0].left:
                q.append(q[0].left)
                l.append(q[0].left.val)
                
            if q[0].right:
                q.append(q[0].right)
                l.append(q[0].right.val)
                
            q.pop(0)
        return bfs
        
        
# @lc code=end

