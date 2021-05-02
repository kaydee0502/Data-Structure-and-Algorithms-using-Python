'''

Vertical Lines in Binary Tree
Given a binary tree root, return the number of unique vertical lines that can be drawn such that every node has a line intersecting it. Each left child is angled at 45 degrees to its left, while the right child is angled at 45 degrees to the right.

For example, root and root.left.right are on the same vertical line.

Constraints

1 ≤ n ≤ 100,000 where n is the number of nodes in root
Example 1
Input
Visualize
root =
1

2

4

3

5

Output
5
Explanation
There's a unique vertical line over every node.

Example 2
Input
Visualize
root =
1

2

3

4

Output
4

'''

# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def __init__(self):
        self.h = set()


    def ino(self,root,l):
        if not root:
            return

        self.ino(root.left,l-1)
        self.h.add(l)


        self.ino(root.right,l+1)

    def solve(self, root):
        self.ino(root,0)
        return len(self.h)

     

        