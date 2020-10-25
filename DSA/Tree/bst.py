# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 16:32:27 2020

@author: KayDee
"""

class Node():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        

class Tree():
    def __init__(self):
        self.root = None
        self.parent = None
        
        
        
    def insert(self,val):
        addnode = Node(val)
    
        if self.root == None:
            self.root = addnode
            return
        temp = self.root
        while temp:
            if temp.data == val:
                print("No duplicate allowed")
                return
            elif val < temp.data:
                if temp.left == None:
                    temp.left = addnode
                    return
                temp = temp.left
            elif val > temp.data:
                if temp.right == None:
                    temp.right = addnode
                    return
                temp = temp.right
    
    def lookup(self,val):
        temp = self.root
        while temp:
            if temp.data == val:
                print(val,"found in tree")
                return temp
            elif val < temp.data:
                temp = temp.left
            elif val > temp.data:
                temp = temp.right
        print(val, "not found")
    
    def remove(self,vald):
        if self.root.data == vald:
            print("cant remove root node node")
            return
        temp = self.root
        self.parent = None
        while temp:
            if temp.data == vald and temp.left == None and temp.right == None:
                if vald > self.parent.data:
                    self.parent.right = None
                    
                if vald < self.parent.data:
                    self.parent.left = None
                return
                    
            elif temp.data == vald and (temp.left == None or temp.right == None):
                if vald > self.parent.data:
                    if not temp.left:
                        self.parent.right = temp.right
                        return
                    else:
                        self.parent.right = temp.left
                        return
                if vald < self.parent.data:
                    if not temp.left:
                        self.parent.right = temp.right
                        return
                    else:
                        self.parent.right = temp.left
                        return
            elif temp.data == vald and not (temp.left == None and temp.right == None):
                delete = temp
                temp = temp.right
                while temp:
                    if temp.left == None:
                        break
                    temp = temp.left
                    
                    
                    
                if delete.right == temp:
                        #temp.right = None
                        temp.left = delete.left
                else:
                        temp.right = delete.right
                        temp.left = delete.left
                        
                        
                        
                if vald < self.parent.data:
                     self.parent.left = temp
                     return
                else:
                    self.parent.right = temp
                    return
                    
        
                
            elif vald < temp.data:
                self.parent = temp
                temp = temp.left
                
                
    
                
            elif vald > temp.data:
                self.parent = temp
                temp = temp.right
        print("remove val not found")
    
    def breadthFirstSearch(self):
        queue = []
        elements = []
        currentNode = self.root
        queue.append(currentNode)
        #elements.append(currentNode.data)
        while queue:
            currentNode = queue[0]
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)
            elements.append(currentNode.data)
            queue.pop(0)
        print(elements)
        return elements
                
    def breadthFirstSearchR(self,queue,elements):
    
        if not queue:
            return elements
        # currentNode = self.root
        # queue.append(currentNode)
        #elements.append(currentNode.data)
        
        currentNode = queue[0]
        if currentNode.left:
            queue.append(currentNode.left)
        if currentNode.right:
            queue.append(currentNode.right)
        elements.append(currentNode.data)
        queue.pop(0)
        print(elements)
        return self.breadthFirstSearchR(queue,elements) 
        
    def inOrderDFS(self):
        return inOrderTraverse(self.root,[])
    
    def preOrderDFS(self):
        return preOrderTraverse(self.root,[])
    
    def postOrderDFS(self):
        return postOrderTraverse(self.root,[])
        
                
        
        
def inOrderTraverse(root,dfs):
    if root.left:
        inOrderTraverse(root.left,dfs)
    dfs.append(root.data)
    if root.right:
        inOrderTraverse(root.right,dfs)
    return dfs

def preOrderTraverse(root,dfs):
    dfs.append(root.data)
    if root.left:
        preOrderTraverse(root.left,dfs)
    # dfs.append(root.data)
    if root.right:
        preOrderTraverse(root.right,dfs)
    return dfs
    
def postOrderTraverse(root,dfs):
    
    if root.left:
        postOrderTraverse(root.left,dfs)
    # dfs.append(root.data)
    if root.right:
        postOrderTraverse(root.right,dfs)
    dfs.append(root.data)
    return dfs     
    
            
                
                
                
tree = Tree()
tree.insert(9)
tree.insert(6)
tree.insert(12)
tree.insert(1)
tree.insert(8)
tree.insert(10)
tree.insert(14)
#tree.remove(6)
print(tree.inOrderDFS())
print(tree.preOrderDFS())
print(tree.postOrderDFS())
tree.breadthFirstSearch()
# print("lol",tree.breadthFirstSearchR([tree.root],[]))
# tree.insert(22)
# tree.insert(17)
# tree.insert(6)
# tree.insert(12)
# tree.insert(13)
# tree.lookup(404)
