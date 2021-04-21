#
# @lc app=leetcode id=297 lang=python3
#
# [297] Serialize and Deserialize Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        comp = ""
        if not root:
            return ""
        
        
        
        q = [root]
        comp += (str(root.val)+"|")
        
        while q:
            if q[0].left:
                q.append(q[0].left)
                comp+=(str(q[0].left.val)+"|")
            else:
                comp+="n|"
                
            if q[0].right:
                q.append(q[0].right)
                comp+=(str(q[0].right.val)+"|")
            else:
                comp+="n|"
                
            q.pop(0)
            
            
        return comp
                
            
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        
        if data == "":
            return None
        
        
        data = data.split("|")
        root = TreeNode(int(data[0]))
        
        i = 0
        q = [root]
        print(data)
        while q and i < len(data):
                
            curr = q[0]
            
            i+=1
            if i<len(data) and data[i] != "n":
                
                curr.left = TreeNode(int(data[i]))
                q.append(curr.left)
            i+=1
            if i<len(data) and data[i] != "n":
                curr.right= TreeNode(int(data[i]))
                q.append(curr.right)
                
            q.pop(0)
        return root
            
            
                
            
            
            
            
        
        
        
        
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end

