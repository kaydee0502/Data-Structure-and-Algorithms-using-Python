#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq
class Solution:
    
    def inio(self,root,k,heap):
        if not root:
            return
        #print(heap)
        if len(heap) < k:
            heapq.heappush(heap,-1*root.val)
        else:
            heapq.heappushpop(heap,-1*root.val)
            
        self.inio(root.left,k,heap)
        self.inio(root.right,k,heap)
        
        
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        heap = []
        heapq.heapify(heap)
        
        self.inio(root,k,heap)
        return -1*heap[0]
        
# @lc code=end

