#User function Template for python3
from collections import defaultdict
import heapq
class Solution:
    
    
    def __init__(self):
        self.G = defaultdict(list)
        
    def addE(self,u,v,w):
        self.G[u].append([w,v])
        #self.G[v].append([w,u])
        
    def prim(self,s,N):
        cost = 0
    
        q = [[0,s]]
        mst = [False] * (N+1)
        key = [float("inf")] * (N+1)
        key[s] = 0
        c = 0
        heapq.heapify(q)
    
        while c<N:
            
            w,u = heapq.heappop(q)
            #print(w,u,key)
            
            
            
            if mst[u] == True:
                continue
            mst[u] = True
            cost += w
            
            c+=1
    
            for w,v in self.G[u]:
                if mst[v] == False and w < key[v]:
                    key[v] = w
                    heapq.heappush(q,[w,v])
    
        return cost
        
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        
        for u in range(V):
            for v,w in adj[u]:
                self.addE(u,v,w)
                
        #print(self.G)
            
        cost = self.prim(0,V)
        return cost

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