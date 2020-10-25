# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 21:13:56 2020

@author: KayDee
"""

class Head_Tail():
    def __init__(self):
        self.head = None
        self.tail = None
    def traverse(self):
        lis = []
        #node = self.next
        
        temp = self.head
    
        while temp != None:
            print(temp.data,"--->",end=" ")
            lis.append(temp.data)
            temp = temp.next
            
        print("NULL")
        return lis
    def reverse(self):
        a = self.head
        self.tail =self.head
        b = a.next
        temp = b.next
        while temp:
            b.next = a
            a = b
            b = temp
            temp = temp.next
        b.next = a
        self.head.next = None
        self.head = b
            



class LinkedList():
    def __init__(self,data):
        
            self.data = data
            self.next = None
            self.length = 1
            
    
    def append(self,val):
        addNode = LinkedList(val)
        myLL.tail.next = addNode
        myLL.tail = addNode
        
        
    def prepend(self,val):
        addNode = LinkedList(val)
        addNode.next = myLL.head
        myLL.head = addNode
        
    def insert(self,index,val):
        addnode = LinkedList(val)
        if index == 0:
            self.prepend(val)
            return
        a = myLL.head
        for i in range(index-1):
            a = a.next
        b = a.next
        a.next = addnode
        addnode.next = b
    def remove(self,index):
        a = myLL.head
        for i in range(index-1):
            a = a.next
        delete = a.next
        b = delete.next
        a.next = b
        del delete
            
        
      
        
        
       
node = LinkedList(10)
myLL = Head_Tail()
myLL.head = node
myLL.tail = node
node.append(5)
node.append(6)
node.append(7)

node.prepend(1)

node.append(69)
node.insert(3,100)
node.prepend(11)
node.remove(4)
myLL.reverse()
myLL.traverse()