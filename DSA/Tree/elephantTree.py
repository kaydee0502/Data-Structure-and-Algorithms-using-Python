'''
Elephant Tree
Given a binary tree root, return the same tree except every node's value is replaced by its original value plus all of the sums of its left and right subtrees.

Constraints

n ≤ 100,000 where n is the number of nodes in root


'''

# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:


    def solve(self, root):
        if not root:
            return None

        a = self.solve(root.left)
        b = self.solve(root.right)

        t = root.val
        if a:
            t+=a.val
        if b:
            t+=b.val
            
        root.val = t

      
        return root

        