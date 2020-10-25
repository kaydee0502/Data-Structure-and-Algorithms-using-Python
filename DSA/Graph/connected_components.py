#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 07:52:27 2020

@author: kaydee
"""
from collections import defaultdict

class Graph:
    def __init__(self,n):
        self.gph = defaultdict(list)
        for i in range(1,n+1):
            self.gph[i] = []
            
        
        
    def addEdge(self,u,v):
        self.gph[u].append(v)
        self.gph[v].append(u)
        
    def printG(self):
        for i in self.gph:
            print(i,"->",end= " ")
            for j in self.gph[i]:
                print(j,end=" ")
            print()
            
    def dfst(self,s,vis):
        vis[s] = True
        #print(s,c)
        
        #print(s,end=" ")
        for i in self.gph[s]:
            
            if vis[i] == False:
                self.dfst(i,vis)
                    
                
                
    def cp(self,a):
        vis = [False]*(len(self.gph)+1)
        cc = 0
        for i in self.gph:
            if vis[i] == False:
                cc += 1
                self.dfst(i,vis)
                
        return cc
        
                
m,n = map(int,input().split())
g = Graph(m)
for j in range(n):
    a1,a2 = map(int,input().split())
    g.addEdge(a1,a2)

print(g.cp(1))
