#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 10:15:13 2020

@author: kaydee
"""
from collections import defaultdict


import sys
sys.setrecursionlimit(100000)


class Graph:
    def __init__(self,n):
        self.gph = defaultdict(list)
        self.revg = defaultdict(list)
        for i in range(1,n+1):
            self.gph[i] = []
            self.revg[i] = []
            
            
            
        
        
    def addEdge(self,u,v):
        self.gph[u].append(v)
        self.revg[v].append(u)
        
    def printG(self):
        for i in self.gph:
            print(i,"->",end= " ")
            for j in self.gph[i]:
                print(j,end=" ")
            print()
            
    def dfst(self,s,vis,stack):
        vis[s] = True
        #print(s,c)
       
        #print(s,end=" ")
        for i in self.gph[s]:
            
            
            if vis[i] == False:
                
                self.dfst(i,vis,stack)
                
        #print("t",s)
        stack.append(s)
        return stack
                    
                
                
    def cp(self,a):
        vis = [False]*(len(self.gph)+1)
        stack = []
        for i in self.revg:
            if vis[i] == False:
                
                stack = self.dfst(i,vis,stack)
        return stack
    
    def revdfs(self,s,vis,comp):
        vis[s] = True
        comp.append(s)
        for i in self.revg[s]:
            if vis[i] == False:
                
                self.revdfs(i,vis,comp)
        return comp
                
                
    
    def scc(self,stack):
        sccs = []
        vis = [False]*(len(stack)+1)
        while stack:
            x = stack.pop()
            if vis[x] == False:
                sccs.append(self.revdfs(x,vis,[]))
                
        return sccs
                
        
     
                
        
        
                
m,n = map(int,input().split())
g = Graph(m)
for j in range(n):
    a1,a2 = map(int,input().split())
    g.addEdge(a1,a2)

preord = g.cp(1)
print(len(g.scc(preord)))

