# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 13:34:29 2020

@author: KayDee
"""

from collections import defaultdict


class Graph():
    
    def __init__(self):
        self.gph = defaultdict(list)
        self.next = None
        
    def addEdge(self, u, v, w=0):
        self.gph[u].append(v)
        #self.gph[v].append(u)
        
    def printGraph(self):
        graph = []
        for i in self.gph:
            for j in self.gph[i]:
                graph.append((i, j))
        return graph
    
    def printNeighbours(self, v):
        neig = []
        for i in self.gph[v]:
            neig.append(i)
        if neig:
            return neig
        else:
            return "No Padosi sed lyf"
        
    def BFS(self, start):
        if start not in self.gph:
            return "No node"
        queue = [start]
        visits = dict((x, False) for x in self.gph)
        visits[start] = True
        bfs = []
        while queue:

            bfs.append(queue[0])
            
            for i in self.gph[queue[0]]:
                if not visits[i]:
                    queue.append(i)
                    visits[i] = True

            
            
            queue.pop(0)
        return bfs
    def DFSUtil(self,s,visited,res):
        visited[s] = True
        res.append(s)
        for i in self.gph[s]:
            if not visited[i]:
                self.DFSUtil(i,visited,res)
        return res 
    def DFS(self,start):
        visited = dict((x,False) for x in self.gph) 
        res = self.DFSUtil(start,visited,[])
        return res
            
            
    
g = Graph()
#g.addEdge(5,3) 
g.addEdge(0, 1) 
g.addEdge(2,3) 
g.addEdge(3,4) 
#g.addEdge(2, 3) 
#g.addEdge(3, 3)
print(g.printGraph())
print(g.printNeighbours(0))
print(g.BFS(2))
print(g.DFS(2))

        