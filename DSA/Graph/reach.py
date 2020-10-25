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
            
    def dfst(self,s,vis,c):
        vis[s] = True
        #print(s,c)
        
        #print(s,end=" ")
        for i in self.gph[s]:
            if i == c:
                return 1
            if vis[i] == False:
                if self.dfst(i,vis,c):
                    return 1
                
        return 0
                
    def cp(self,a,b):
        vis = [False]*(len(self.gph)+1)
        return self.dfst(a,vis,b)
        
                
m,n = map(int,input().split())
g = Graph(m)
for j in range(n):
    a1,a2 = map(int,input().split())
    g.addEdge(a1,a2)
c1,c2 = map(int,input().split())
print(g.cp(c1,c2))
