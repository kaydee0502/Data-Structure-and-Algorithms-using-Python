'''

Diagonal Tree Traversal

Given a binary tree root, return the sum of each of the diagonals in the tree starting from the top to bottom right.

Constraints

    n ≤ 100,000 where n is the number of nodes in root

Example 1
Input
Visualize

root = [1, [4, null, null], [2, [5, [7, null, null], [6, null, null]], [3, null, null]]]

Output

[6, 15, 7]

Explanation

The diagonals are:

1 -> 2 -> 3
4 -> 5 -> 6
7

Example 2
Input
Visualize

root = [1, [2, null, null], [3, null, null]]

Output

[4, 2]



'''

# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def __init__(self):
        self.h = {}

    def ino(self,root,col):
        if not root:
            return

        if not col in self.h:
            self.h[col] ={root.val}
        else:
            self.h[col].add(root.val)

        self.ino(root.left,col+1)
        self.ino(root.right,col)

    def solve(self, root):
        self.ino(root,0)
        res = []

        for i in self.h:
            res.append(sum(list(self.h[i])))

        return res
        