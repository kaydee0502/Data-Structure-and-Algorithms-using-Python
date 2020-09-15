# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 09:10:35 2020

@author: KayDee
"""

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
        
        
        
class Stack:
    def __init__(self):
        self.stack = Linklist()
        
    def push(self,val):
        self.stack.prepend(val)
    
    def pop(self):
        if not self.stack.head:
            return
        self.stack.head = self.stack.head.next
        
    def peek(self):
        return self.stack.head.data
        
    
    
        
class Queue:
    def __init__(self):
        self.q = Linklist()
        
    def enqueue(self,val):
        self.q.append(val)
    
    def dequeue(self):
        if not self.q.head:
            return
        self.q.head = self.q.head.next
        
    def peek(self):
        return self.q.head.data
        
        
myStck = Stack()

myStck.push(8)
myStck.push(3)
myStck.push(2)
myStck.pop()
print(myStck.peek())
        
myQ = Queue()

myQ.enqueue(4)
myQ.enqueue(5)
myQ.enqueue(7)
myQ.enqueue(2)
myQ.dequeue()
print(myQ.peek())
        
        
        
        


