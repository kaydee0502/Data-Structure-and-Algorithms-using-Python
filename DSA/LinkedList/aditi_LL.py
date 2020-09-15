# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 13:16:42 2020

@author: KayDee
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
   
        
class Linklist:
    def __init__ (self):
        self.head = None
        #self.tail = None
        
    def prepend(self,val):
        newnode = Node(val)
        if self.head:
            newnode.next = self.head
        else:
            self.tail = newnode
        self.head = newnode
        
    def append(self,val):
        newnode = Node(val)
        if not self.head:
            self.head = newnode
            return
        temp = self.head
        while temp.next != None:
            temp = temp.next
            
        temp.next = newnode
        
    def insert(self,index,value):
        newnode = Node(value)
        temp = self.head
        if index == 0 or not self.head:
            self.prepend(value)
            return
        for i in range(index-1):
            temp = temp.next
            
        newnode.next = temp.next
        temp.next = newnode
        
        print(temp.data)
    
    def delete(self,val):
        if not self.head:
            print("Nothing to delete")
            return
        temp = self.head
        
        while temp.next != None:
            if temp.next.data == val:
                break
            temp = temp.next
        else:
            print("Value not found")
            return
        
        val_del = temp.next
        temp.next = temp.next.next
        return
        
        
        
        
        
        
            
        
        
        
        
myll = Linklist()
myll.delete(18732)
myll.insert(0,15)
myll.prepend(8)
myll.prepend(10)
myll.append(12)
myll.append(100)



temp = myll.head
while temp:
    print(temp.data,"-->",end = "")
    temp = temp.next
print("None")

