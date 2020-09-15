# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 10:04:39 2020

@author: KayDee
"""

T = int(input())
for _ in range(T):
    n,a,b,c = list(map(int,input().split()))
    builds = [i for i in range(1,n-c+1)]
    builds+=[n-c+1]*c
    first = builds.copy()
    p1 = a-c
    p2 = b-c
    
    c1 = builds.pop()
    builds.insert(p1,c1)
    
    if p2 != 0:
        c2 = builds.pop()
        builds.insert((-p2),c2)
  
    if (a+b-c > n) or (a==1 and b==1) or (c>a or c>b):
        print("Case #{}: IMPOSSIBLE".format(_+1))
    else:
        print("Case #{}:".format(_+1),*builds)
        
    
            
   
    
   