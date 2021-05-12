#User function Template for python3

class Solution:
    
    
    def __init__(self):
        self.G = []
   
         
    def kruskal(self,V):
        self.G.sort()
        parent = [x for x in range(V)]
        rank = [0] * (V)
        
        
        
        def find(x):
            if x == parent[x]:
                return x
                
            parent[x] = find(parent[x])
            return parent[x]
        
        def union(x,y):
            x = find(x)
            y = find(y)
            
            if x == y:
                return True
            
            if rank[x]<rank[y]:
                parent[x] = y
            elif rank[y]<rank[x]:
                parent[y] = x
            else:
                parent[x] = y
                rank[y] += 1
                
            return False
            
        c = 0
        span = []
        for w,u,v in self.G:
            
            if not union(u,v):
                span.append(f"{u} <--> {v} | {w}")
                #print(u,v,w)
                c+=w
                
        print(*span,sep="\n")
                
            
        return c
            
            
        
                
            
   
   
   
        
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        
        for u in range(V):
            for v,w in adj[u]:
                self.G.append([w,u,v])
                
        #print(self.G)
        return self.kruskal(V)
            
       

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        ob = Solution()
        
        print(ob.spanningTree(V,adj))
# } Driver Code Ends