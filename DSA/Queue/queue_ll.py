# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 21:07:12 2020

@author: KayDee
"""

class Node():
    def __init__(self,data):
        
        self.data = data
        self.next = None
           
            
class Queue():
    def __init__(self,size):
        self.first = None
        self.last = None
        self.size = size
        self.length = -1
        
    def enqueue(self,val):
        addnode = Node(val)
        if self.last == None:
            self.first = addnode
            self.last = addnode
            self.length += 1
            return
        if self.length == self.size:
            print("Queue is full")
            return
        self.last.next = addnode
        self.last = addnode
        self.length += 1
        
    def dequeue(self):
        if self.first == None:
            print("Queue is empty")
            return
        if self.first.next == None:
            a = self.first.data
            self.first = None
            self.length -= 1
            return a
        active = self.first.data
        self.first = self.first.next
        self.length -= 1
        return active

    def peek(self):
        return self.last.data
    
    def printQ(self):
        temp = self.first
        while temp:
            print(temp.data,"-> ",end="")
            temp = temp.next
            
Q = Queue(5)
'''Q.enqueue(3)     
Q.enqueue(4)  
Q.enqueue(5)  
Q.enqueue(6) 
Q.enqueue(89)
Q.dequeue() 
Q.dequeue() 
Q.enqueue(85)
Q.dequeue()
Q.printQ()  ''' 