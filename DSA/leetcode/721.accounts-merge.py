#
# @lc app=leetcode id=721 lang=python3
#
# [721] Accounts Merge
#

# @lc code=start
from collections import defaultdict
class Solution:
    
    def __init__(self):
        self.g = defaultdict(list)
    
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        
        uniSet = {}
        rev = {}
        
        def find(x):
            if not x in uniSet:
                uniSet[x] = x
                
            if uniSet[x] != x:
                uniSet[x] = find(uniSet[x])
            return uniSet[x]
        
        
        def union(x,y):
            uniSet[find(x)] = find(y)
            
        for n,*em in accounts:
            
            if len(em) == 1:
                find(em[0])
            #print(n)
            for i,j in itertools.combinations(em,2):
                union(i,j)
                
            for i in em:
                if not i in rev:
                    rev[i] = n
                    
            
        grp = collections.defaultdict(list)
        
        for e in uniSet:
            grp[find(e)].append(e)
            
        #print(rev)
        return [[rev[parent]] + sorted(childs) for parent,childs in grp.items()]
            
# @lc code=end

