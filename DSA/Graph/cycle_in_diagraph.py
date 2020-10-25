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
        self.gph = defaultdict(list)
        for i in range(1,n+1):
            self.gph[i] = []
            
        
        
    def addEdge(self,u,v):
        self.gph[u].append(v)
        #self.gph[v].append(u)
        
    def printG(self):
        for i in self.gph:
            print(i,"->",end= " ")
            for j in self.gph[i]:
                print(j,end=" ")
            print()
            
    def dfst(self,s,vis,rec):
        vis[s] = True
        rec[s] = True
        #print(s,c)
        
        #print(s,end=" ")
        for i in self.gph[s]:
            #print(s,i)
            if rec[i] == True:
                return 1
            
            if vis[i] == False:
                if self.dfst(i,vis,rec):
                    return 1
        rec[s] = False
        return 0
                    
                
                
    def cyc(self,a):
        vis = [False]*(len(self.gph)+1)
        rec = [False]*(len(self.gph)+1)
        for i in self.gph:
            if vis[i] == False:
                if self.dfst(i,vis,rec):
                    return 1
        return 0
                
        
        
                
m,n = map(int,input().split())
g = Graph(m)
for j in range(n):
    a1,a2 = map(int,input().split())
    g.addEdge(a1,a2)

print(g.cyc(1))
