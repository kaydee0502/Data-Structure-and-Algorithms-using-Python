'''

399. Evaluate Division
Medium

3398

274

Add to List

Share
You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

 

Example 1:

Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation: 
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
Example 2:

Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
Output: [3.75000,0.40000,5.00000,0.20000]
Example 3:

Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
Output: [0.50000,2.00000,-1.00000,-1.00000]
 

Constraints:

1 <= equations.length <= 20
equations[i].length == 2
1 <= Ai.length, Bi.length <= 5
values.length == equations.length
0.0 < values[i] <= 20.0
1 <= queries.length <= 20
queries[i].length == 2
1 <= Cj.length, Dj.length <= 5
Ai, Bi, Cj, Dj consist of lower case English letters and digits.

'''

from collections import defaultdict

class Solution:
    
    def __init__(self):
        self.g = defaultdict(list)
    
    
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        nodes  = set()
        
        
        def bfs(src,dst):
            
            if src == dst:
                return 1.0
            
            vis = {src}
            
            q = [[src,1.0]]
            
            ans = 1
            
            while q:
                cur = q.pop(0)
                
                if cur[0] == dst:
                    return cur[1]
                
               
                for v in self.g[cur[0]]:
                    
                    if v[0] not in vis:
                        vis.add(v[0])
                        q.append([v[0],cur[1]*v[1]])
                    
            return -1
                    
                
                
        
        
        for i,v in zip(equations,values):
            self.g[i[0]].append([i[1],v])
            self.g[i[1]].append([i[0],1/v])
            nodes.add(i[0])
            nodes.add(i[1])
            
            
        res = []
        for i,j in queries:
            if not i in nodes and not j in nodes:
               res.append(-1)
            
            else:
                a = bfs(i,j)
                res.append(a)
                
                
        return res
        
            
            
        
            
        
        
        