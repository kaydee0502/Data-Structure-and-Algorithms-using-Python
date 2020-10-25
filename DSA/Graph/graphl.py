#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 15:56:53 2020

@author: kaydee
"""
from collections import defaultdict

class Graph:
    def __init__(self):
        self.gph = defaultdict(list)
        
    def addEdge(self,u,v):
        self.gph[u].append(v)
        self.gph[v].append(u)
        
    def printG(self):
        for i in self.gph:
            print(i,"->",end= " ")
            for j in self.gph[i]:
                print(j,end=" ")
            print()
            
    def bfst(self,s,vis):
        
        q = [s]
        vis[s] = True
        while q:
            for i in self.gph[q[0]]:
                if vis[i] == False:
                    #print(i)
                    q.append(i)
                    vis[i] = True
            
            print(q.pop(0),end=" ")
            
            #print(vis)
            
    def BFS(self,s):
        vis = [False]*len(self.gph)
        self.bfst(s,vis)
        for j in self.gph:
            if vis[j] == False:
                self.bfst(j,vis)
        pass
    def dfst(self,s,vis):
        vis[s] = True
        print(s,end=" ")
        for i in self.gph[s]:
            if vis[i] == False:
                self.dfst(i,vis)
        
        
        
    def DFS(self,s):
        vis = [False]*len(self.gph)
        self.dfst(s,vis)
        for i in self.gph:
            if vis[i] == False:
                self.dfst(i,vis)
        
            
        
            
g=Graph()
g.addEdge(0,1)
g.addEdge(2,3)
g.addEdge(2,4)
g.addEdge(4,3)
g.addEdge(4,5)
g.addEdge(5,3)
g.printG()
g.BFS(5)
print()
g.DFS(5)
        