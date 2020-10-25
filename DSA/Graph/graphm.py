#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 10:05:36 2020

@author: kaydee
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 15:56:53 2020

@author: kaydee
"""
from collections import defaultdict

class Graph:
    def __init__(self,V):
        self.V = V
        self.gph = [[0 for x in range(V)] for z in range(V)]
        
        
    def addEdge(self,u,v):
        self.gph[u][v] = 1
        self.gph[v][u] = 1
        
    def printG(self):
        for i in self.gph:
            print(i)
        
        
        
            
    def BFS(self,s):
        vis = [False]*len(self.gph)
        q = [s]
        vis[q[0]] = True
        while q:
            
            for i in range(len(self.gph[q[0]])):
                if self.gph[q[0]][i] == 1 and vis[i] == False:
                    q.append(i)
                    vis[i] = True
                    
                    
            
            print(q.pop(0),end=" ")
            
            #print(vis)
    
            
    def dfst(self,s,vis):
        vis[s] = True
        print(s,end=" ")
        for i in range(self.V):
            #print(self.gph[s])
            if self.gph[s][i] == 1 and vis[i] == False:
                self.dfst(i,vis)
        
        
        
    def DFS(self,s):
        vis = [False]*len(self.gph)
        self.dfst(s,vis)
        
        
            
g=Graph(6)
g.addEdge(0,4)
g.addEdge(2,3)
g.addEdge(2,4)
g.addEdge(3,1)
g.addEdge(4,1)
g.addEdge(1,5)
g.printG()
g.BFS(0)
print()
g.DFS(0)
        