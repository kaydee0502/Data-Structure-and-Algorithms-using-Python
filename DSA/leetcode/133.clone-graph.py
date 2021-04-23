#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    
   
                        
    
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        if not node:
            return
        
        chash = {node : Node(node.val)}
        
        
        q = [node]
        
        while q:
            c = q.pop(0)
            
            for i in c.neighbors:
                if i not in chash:
                    chash[i] = Node(i.val)
                    q.append(i)
                chash[c].neighbors.append(chash[i])
                
        
        return chash[node]
        
# @lc code=end

