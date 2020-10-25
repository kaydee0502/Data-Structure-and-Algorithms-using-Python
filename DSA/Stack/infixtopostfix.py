# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 14:51:22 2020

@author: KayDee
"""

class Stack():
    def __init__(self,size):
        self.stack = ["("]
        self.top = 0
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





def expression(val):
    global ops
    final_expression = ""
    for i in val:
        print(i)
        print(myStack.stack)
        if i == '(':
            myStack.push(i)
        
            
        elif i in ops:
            
            if myStack.peek() == '(':
                myStack.push(i)
            elif ops[myStack.peek()] > ops[i]:
                o = myStack.pop()
                final_expression += o
                myStack.push(i)
            else:
                myStack.push(i)
                
                
        elif i == ')':
            while True:
                oo = myStack.pop()
                if oo == "(":
                    break
                final_expression += oo
                print(final_expression)    
        
                    
        else :
            final_expression += i
    return final_expression
            
            
print("lol")          
            
            
            
ops = {'-' : 0, '+' : 1, '*' : 2, '/' : 3, '^' : 4}        
myStack = Stack(100)        
exp = input()
exp = exp + ")"
res = expression(exp)
print("Result :",res)
