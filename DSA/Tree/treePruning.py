'''
Tree Pruning
Given a binary tree root, prune the tree so that subtrees containing all 0s are removed.

Constraints

n ≤ 100,000 where n is the number of nodes in root
Example 1
Input
Visualize
root = [0, [1, null, null], [0, [1, [0, null, null], [0, null, null]], [0, null, null]]]
Output
Visualize
[0, [1, null, null], [0, [1, null, null], null]]
Explanation
We do not remove the tree at the root or its right child because they still have a 1 as a descendant.

'''
# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve2(self, root):
        if not root:
            return

        

        l = self.solve2(root.left)
        r = self.solve2(root.right)

        if l:
            root.left = None

        if r:
            root.right = None

        if not root.left and not root.right and root.val == 0:
            #print("lol")
            return True

    def solve(self, root, par=None):
        self.solve2(root)

        return root
