#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 08:28:24 2020

@author: kaydee
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 07:52:27 2020

@author: kaydee
"""
from collections import defaultdict



class Graph:
    def __init__(self,n):
        self.V = n
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
            
    def bfst(self,s):
        
        vis=[False]*(self.V+1)
        cols = [None]*(self.V+1)
        q = [s]
        level= []
        vis[s] = True
        cols[s] = "Red"
        
        while q:
            for i in self.gph[q[0]]:
                
                if vis[i] == False:
                    #print(i)
                    q.append(i)
                    level.append(i)
                    vis[i] = True
                    cols[i] = "Red" if cols[q[0]] == "Blue" else "Blue"
                elif cols[i] == cols[q[0]] or i == q[0]:
                    return 0
                    
            
        
                    
                    
            
            q.pop(0)
        return 1
                   
            #print(vis)
            
    def BFS(self,s):
        vis = [False]*len(self.gph)
        self.bfst(s,vis)
        for j in self.gph:
            if vis[j] == False:
                self.bfst(j,vis)
    
   
                
        
        
                
m,n = map(int,input().split())
g = Graph(m)
for j in range(n):
    a1,a2 = map(int,input().split())
    g.addEdge(a1,a2)
print(g.bfst(1))