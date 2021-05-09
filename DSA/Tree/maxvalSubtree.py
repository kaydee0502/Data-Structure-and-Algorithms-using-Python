'''

Subtree with Maximum Value
Given a binary tree root, return the maximum sum of a subtree. A subtree is defined to be some node in root including all of its descendants. A subtree sum is the sum of all the node values in the subtree. A subtree can be null in which case its sum is 0.

Constraints

1 ≤ n ≤ 100,000 where n is the number of nodes in root

'''

# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def __init__(self):
        self.csum = float("-inf")

    def inor(self,root):
        if not root:
            return 0

        a1 = self.inor(root.left)
        a2 = self.inor(root.right)

        subtreeSum = root.val+a1+a2

        self.csum = max(self.csum,subtreeSum)

        return subtreeSum


    def solve(self, root):
        self.inor(root)
        if self.csum < 0:
            return 0

        return self.csum

        