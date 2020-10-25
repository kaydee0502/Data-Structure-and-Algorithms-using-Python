#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 08:24:54 2020

@author: kaydee
"""
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
from queue import PriorityQueue as pq



class Graph:
    def __init__(self,n):
        self.V = n
        self.gph = defaultdict(list)
        for i in range(n):
            self.gph[i] = []
            
        
        
    def addEdge(self,u,v,w):
        self.gph[u].append((v,w))
        #self.gph[v].append(u)
        
    def printG(self):
        for i in self.gph:
            print(i,"->",end= " ")
            for j in self.gph[i]:
                print(j,end=" ")
            print()
            
    def bellmanFord(self,s):
        dist = [float("inf")]*(self.V)
        prev = {}
        for i in self.gph:
            prev[i] =None
        dist[s] = 0
        for _ in range(self.V-1):
            
            for u in self.gph:
                if dist[u] != float("inf"):
                    for v in self.gph[u]:
                        #relax nodes
                        if dist[v[0]] > dist[u] + v[1]:
                            dist[v[0]] = dist[u] + v[1]
                            prev[v[0]] = u
                
        return dist
                        
                    
                    
                    

                
m,n = map(int,input().split())
g = Graph(m)
for j in range(n):
    a1,a2,w = map(int,input().split())
    g.addEdge(a1,a2,w)
    
s= int(input())

t = g.bellmanFord(s)
print(f"From node {s}")
print("node\t\tdistance")
for o in range(len(t)):
    print(f"{o}\t\t{t[o]}")