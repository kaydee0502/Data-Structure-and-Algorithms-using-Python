# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 17:07:54 2020

@author: KayDee
"""

class Node():
    def __init__(self,data):
        
            self.data = data
            self.next = None
           
            
class Stack():
    def __init__(self,size):
        self.base = None
        self.top = None
        self.length = -1
        self.size = size
        
    def push(self,val):
        if self.length == self.size-1:
            print("Stack Overflow")
            return
        addnode = Node(val)
        if self.base == None:
            self.base = addnode
            self.top = addnode
            self.length += 1
            return
        
        addnode.next = self.top
        self.top = addnode
        self.length += 1
    
    def pop(self):
        if self.length == -1:
            print("Stack Underflow")
            return
    
        if self.top.next == None:
            data = self.top.data
            self.base = None
            self.top = None
            return data
            
            
        data = self.top.data
        t = self.top.next
        self.top = t
        
        
        self.length -= 1
        return data
    def peek(self):
        return self.top.data
    def isEmpty(self):
        if self.top == None:
            return True
        return False
    def trav(self):
        temp = self.top
        while temp:
            print(temp.data)
            temp = temp.next
        
        
    
            
myS = Stack(5)
myS.push(4)
myS.push(2)
myS.push(5)
myS.pop()
myS.push(9)
s = myS.peek()
myS.push(4)
myS.push(2)
myS.push(5)
print("peek - ",s)
myS.trav()
        
            