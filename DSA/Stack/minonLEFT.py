# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 18:05:04 2020

@author: KayDee
"""

class Stack():
    def __init__(self):
        self.res = []
        self.stck = []
        self.mini = []
        self.top = -1
    
    def push(self,v):
        
        #print(self.mini)
        if not self.mini:
            self.res.append(-1)
            self.mini.append(v)
        elif v > self.mini[-1]:
            self.res.append(self.mini[-1])
            self.mini.append(v)
        elif v < self.mini[-1]:
            if v < min(self.mini):
                self.res.append(-1)
            else:
                temp = self.mini[:]
                while v < temp[-1]:
                    temp.pop()
                self.res.append(temp[-1])
                #while?
            self.mini.append(v)
        #self.stck.append(v)
        self.top += 1
        
    def pop(self):
        self.top -= 1
        return self.stck.pop()
    def get(self):
        return self.res
    
    def peek(self):
        return self.stck[top]
        
        
T = int(input())
while T:
    myStack = Stack()
    dump = input()
    data = list(map(int,input().split()))
    for i in data:
        myStack.push(i)
        
    #print(myStack.stck)
    ans = myStack.get()
    print(*ans)
    T-=1