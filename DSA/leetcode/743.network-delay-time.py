#
# @lc app=leetcode id=743 lang=python3
#
# [743] Network Delay Time
#

# @lc code=start
import heapq
from collections import defaultdict

class Solution:
    
    def __init__(self):
        self.g = defaultdict(list)
    
    
    def addE(self,*args):
        #print(args)
        u,v,w = args
        
        self.g[u].append([w,v])
    
    
    def dij(self,g,n,k):
        dist = [float("inf")]*(n+1)
        
        dist[k] = 0
        
        q = [[dist[k],k]]
        heapq.heapify(q)
        
        #print(self.g)
        while q:
            _,u = heapq.heappop(q)
            #print(_,u)
            
            for w,v in self.g[u]:
               # print(w,v)
                if dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w
                    heapq.heappush(q,[dist[v],v])
                    
        return dist
            
            
    
    
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        for i in times:
            self.addE(*i)
        
        dists = self.dij(times,n,k)
        dists = dists[1:]
        
        if max(dists) == float("inf"):
            return -1
        
        else:
            return max(dists)
        
        
# @lc code=end

