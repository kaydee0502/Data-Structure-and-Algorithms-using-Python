#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 09:32:00 2020

@author: kaydee
"""
from collections import defaultdict

class Graph:
    def __init__(self,V):
        self.V =  V+1
        self.gph = {}
        for i in range(self.V):
            self.gph[i] = []
        self.topo= []
        
    def addEdge(self,u,v):
        self.gph[u].append(v)
        #self.gph[v].append(u)
        
    def printG(self):
        for i in self.gph:
            print(i,"->",end= " ")
            for j in self.gph[i]:
                print(j,end=" ")
            print()
            
    def bfst(self,s,vis):
        #print("lol",s)
        q = [s]
        vis[s] = True
        while q:
            for i in self.gph[q[0]]:
                #print("lol",i,vis)
                if vis[i] == False:
                    #print(i)
                    q.append(i)
                    vis[i] = True
            
            print(q.pop(0),end=" ")
            
            #print(vis)
            
    def BFS(self,s):
        vis = [False]*(self.V)
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
        vis = [False]*(self.V)
        self.dfst(s,vis)
        
        for i in self.gph:
            if vis[i] == False:
                self.dfst(i,vis)
     
    def tlsutil(self,s,vis):
        vis[s] = True
        for i in self.gph[s]:
            if vis[i] == False:
                self.tlsutil(i, vis)
        self.topo.append(s)

            
    def TLS(self,posbs):
        self.topo = []
        vis = [False]*(self.V)
        for i in posbs:
            if posbs[i] == 1 and vis[i] == False:
                self.tlsutil(i,vis)
        return self.topo[::-1]
        
        
m,n = map(int,input().split())
g = Graph(m)
posbs = dict((x,1) for x in range(1,m+1))
for j in range(n):
    a1,a2 = map(int,input().split())
    posbs[a2] = 0
    g.addEdge(a1,a2)

print(*g.TLS(posbs))