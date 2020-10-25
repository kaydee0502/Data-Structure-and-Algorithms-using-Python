#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 08:20:06 2020

@author: kaydee
"""
class Stack:
    def __init__(self):
        self.stack = []
        self.prec = {"^":3,"/":2,"*":2,"+":1,"-":1}
        self.postfix = ""
        
    def push(self,val):
        self.stack.append(val)
        
    def pop(self):
        return self.stack.pop()
    
    def peek(self):
        if self.stack:
            return self.stack[-1]
    
def convert(exp):
    stck = Stack()
    exp.append(")")
    stck.push("(")
    
    for i in range(len(exp)):
        if exp[i] in stck.prec.keys():
            if stck.peek() == "(" or stck.prec[stck.peek()] < stck.prec[exp[i]]:
                #print(stck.peek())
                stck.push(exp[i])
                
            else:
                while stck.peek() != "(" and stck.prec[stck.peek()] >= stck.prec[exp[i]]:
                    
                    stck.postfix += stck.pop()
                stck.push(exp[i])
        elif exp[i] =="(":
            stck.push(exp[i])
        elif exp[i] == ")":
            while stck.peek() != "(":
                    stck.postfix += stck.pop()
            stck.pop()
        else:
            stck.postfix += exp[i]
            
    
    return stck.postfix
                        
                        
                
                
            
        
        
        


exp = list(input("Enter the infix exp :"))
exp = [x for x in exp if x]




print(convert(exp))


