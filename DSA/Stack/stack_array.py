# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 17:08:19 2020

@author: KayDee
"""

class Stack():
    def __init__(self,size):
        self.stack = []
        self.top = -1
        self.size = size
        
    def push(self,elem):
        if self.top == self.size-1:
            print("Stack Overflow")
            return
        
        self.stack.append(elem)
        self.top += 1
        
    def pop(self):
        if self.top == -1:
            print("Stack Underflow")
            return
        popval = self.stack.pop()
        self.top -= 1
        return popval
        
    def peek(self):
        if self.top == -1:
            print("Stack is empty")
            return
        return self.stack[self.top]
    
  


myStack = Stack(5)
'''v1 = myStack.pop()
myStack.push(2)
#myStack.push(3)
myStack.pop()
#myStack.push(5)
#myStack.push(8)
r = myStack.peek()
myStack.push(2)
myStack.push(5)
print(myStack.stack)'''

    