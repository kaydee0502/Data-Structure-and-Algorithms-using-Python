'''

572. Subtree of Another Tree
Easy

3338

163

Add to List

Share
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4 
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.
 

Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def isSame(self,r1,r2):
        if not r1 and not r2:
            return True
        
        if not r1 or not r2:
            return False
        
        if r1.val!=r2.val:
            return False
        
        a = self.isSame(r1.left,r2.left)
        b = self.isSame(r1.right,r2.right)
        
        return a and b
        
    
    
    def ino(self,root,mroot):
        if not root:
            return
        
        a = self.ino(root.left,mroot)
        
        if self.isSame(root,mroot):
            #print("Yes")
            return True
            
        b = self.ino(root.right,mroot)
        
        return a or b
        
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        return self.ino(s,t)
        
