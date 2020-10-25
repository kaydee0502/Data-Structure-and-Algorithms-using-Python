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
        for i in range(1,n+1):
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
            
    def dijkstra(self,s,e):
        dist = [float("inf")]*(self.V+1)
        prev = {}
        for i in self.gph:
            prev[i] =None
        dist[s] = 0
        prior = pq()
        prior.put((dist[s],s))
        while not prior.empty():
            dis, u = prior.get()
            for v in self.gph[u]:
                if dist[v[0]] > dist[u] + v[1]:
                    dist[v[0]] = dist[u] + v[1]
                    prev[v[0]] = u
                    prior.put((dist[v[0]],v[0]))
                    
        if dist[e] == float("inf"):
            return -1
        else:
            return dist[e]
                    
                
            
            
        
            
        
   
                
        
        
                
m,n = map(int,input().split())
g = Graph(m)
for j in range(n):
    a1,a2,w = map(int,input().split())
    g.addEdge(a1,a2,w)
    
s,e = map(int,input().split())

print(g.dijkstra(s,e))