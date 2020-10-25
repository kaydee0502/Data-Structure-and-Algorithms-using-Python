#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 21:32:24 2020

@author: kaydee
"""
from collections import deque
class Graph:
    def __init__(self,V):
        self.V = V
        self.g = {}
        for i in range(1,self.V+1):
            self.g[i] = []
            
    def ae(self,u,v):
        self.g[u].append(v)
        self.g[v].append(u)
        
        
    def calc(self):
        arr = [0]*self.V
        arr[0] = 2
        vis = [False]*self.V
        vis[0] = True
        Q = deque([1])
        s = 3
        level = []
        while Q:
            
            if len(Q)==len(level):
                for o in level:
                    arr[o-1] = s
                level = []
                if s%2==0:
                    s+=2
                else:
                    s*=2
            for x in self.g[Q[0]]:
                if vis[x-1] ==False:
                    vis[x-1] =True
                    Q.append(x)
                    level.append(x)
            Q.popleft()
        return arr
            
        
        
            
            
            
T = int(input())
while T:
    n = int(input())
    gr = Graph(n)
    for k in range(n-1):
        a,b = map(int,input().split())
        gr.ae(a,b)
    print(*gr.calc())
    
    
    T-=1 