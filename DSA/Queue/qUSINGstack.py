# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 10:03:03 2020

@author: KayDee
"""

class QwStack():
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        self.top = None

    def controller(self,op):
        #print(op)
        if op[0] == '1':
            self.enqueue(int(op[1]))
        elif op[0] == '2':
            self.dequeue()
        else:
            print(self.top)
    

    def enqueue(self,data):
        if not self.stack1:
            self.top = data
        self.stack1.append(data)

    def dequeue(self):
        while self.stack1:
            val = self.stack1.pop()
            self.stack2.append(val)
        self.stack2.pop()
        while self.stack2:
            val = self.stack2.pop()
            self.enqueue(val)







 
q = QwStack()
for i in range(int(input())):
    query = input().split()
    q.controller(query)
    
